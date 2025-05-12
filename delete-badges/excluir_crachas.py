from playwright.sync_api import sync_playwright
import csv
import os
import time
from rich.console import Console
from datetime import datetime, date

# função para ler os CPF's dos funcionarios
# function to read employees' CPFs
def get_funcionario():
    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, "funcionarios_santanna.csv")

    cpfs = []
    with open(csv_path, newline='', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for _, cpf in reader:
            cpfs.append(cpf)

    return cpfs

console = Console()
console.clear()

with sync_playwright() as p:

    # abrir navegador
    # open browser
    nav = p.firefox.launch(headless=False)
    pag = nav.new_page()
    pag.goto("https://www.ucsexplorer.com.br/login/login.aspx")
    print("Navegador aberto!\nBrowser opened!\n")

    # logar no UCS Explorer
    # log in to UCS Explorer
    pag.locator("#ContentPlaceHolder1_txtemail").wait_for()
    pag.locator("#ContentPlaceHolder1_txtemail").fill("suporte@santanna.g12.br")

    pag.locator("#ContentPlaceHolder1_txtsenha").wait_for()

    pag.locator("#ContentPlaceHolder1_cmdLogin").wait_for()
    pag.locator("#ContentPlaceHolder1_cmdLogin").click()

    # procurar usuario
    # search for user
    pag.locator("a[title='Usuário']").wait_for()
    pag.locator("a[title='Usuário']").click()

    user_not_exist = 0
    empty_profiles = 0

    for cpf in get_funcionario():

        # seleciona a nav
        # select the input box
        pag.locator("#ctl00_MainContent_cbNome_Input").wait_for()
        pag.locator("#ctl00_MainContent_cbNome_Input").click()

        # espera 1 seg  dps preenche o campo com o CPF
        # wait 1 second then fill the field with the CPF
        time.sleep(1)
        pag.locator("#ctl00_MainContent_cbNome_Input").fill(cpf)

        # clica no CPF e da um scroll ate o final da pag 
        # click on the CPF and scroll to the bottom of the page
        time.sleep(1)
        if pag.locator("div.rcbMoreResults span", has_text="Nada encontrado").count() > 0:
            print("Usuario não encontrado no sistema!\nUser not found in the system!\n")
            user_not_exist += 1
            continue
        else:
            time.sleep(1)
            pag.locator(".rcbList").click()
            pag.wait_for_load_state("networkidle")
            time.sleep(1)
            pag.evaluate("window.scrollTo(0, document.body.scrollHeight)")

            # pega as datas de cadastro dos crachas nos perfis dos funcionarios
            # get badge registration dates from the employee profiles
            if pag.locator("small.text-muted").count() == 0:
                print("não existe nenhum perfil de acesso cadastrado\nNo access profile registered\n")
                empty_profiles += 1
                time.sleep(1)
                pag.locator("#cmdSalvar").wait_for()
                pag.locator("#cmdSalvar").click()
                continue
            else:
                pag.wait_for_selector("small.text-muted", timeout=10000)
                datas = pag.locator("small.text-muted").all_inner_texts()

            # cria as linhas da tabela que tem descrito o tipo de perfil e a data que foi criada 
            # create table rows that describe the profile type and the date it was created
                rows = pag.locator("table tbody tr:has(small.text-muted)")
                total = rows.count()

            # define uma data limite para a condição de excluir os crachas
            # set a cutoff date for the badge deletion condition
                limit_date = date(2025, 4, 6)

            # percorre cada linha da tabela dos perfis e clica no "excluir" caso menor ou igual a data limite estipulada
            # go through each profile row and click "delete" if date is before or equal to the limit date
                for i in range(total):
                    row = rows.nth(i)
                    date_str = row.locator("small.text-muted").inner_html()
                    date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()

                    if date_obj <= limit_date:
                        row.locator(".btn-group").wait_for()
                        row.locator(".btn-group").click()
                        time.sleep(1)
                        row.locator("a[href='javascript:void(0);']:has-text('Excluir')").wait_for()
                        row.locator("a[href='javascript:void(0);']:has-text('Excluir')").click()
                    else:
                        continue

        # espera um tempo para clicar em "Salvar" e passar para o proximo usuario
        # wait a moment to click "Save" and move to the next user
        time.sleep(1)
        pag.locator("#cmdSalvar").wait_for()
        pag.locator("#cmdSalvar").click()

    print(f"{user_not_exist} funcionaios não existentes no sistema\n{user_not_exist} employees not found in the system\n")
    print(f"Foram encontrados {empty_profiles} perfis sem acessos cadastrados anteiormente!\n{empty_profiles} profiles found without previously registered access!\n")
    time.sleep(2)
    print("Até logo!\nGoodbye!\n")
    nav.close()