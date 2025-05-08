from playwright.sync_api import sync_playwright
import time
from datetime import datetime, date
import funcs as f

with sync_playwright() as p:

    # abrir navegador
        nav = p.firefox.launch(headless=False)
        pag = nav.new_page()
        pag.goto("https://www.ucsexplorer.com.br/login/login.aspx")
        print("Abriu zé\n")

    # logar no UCS Explorer
        pag.locator("#ContentPlaceHolder1_txtemail").wait_for()
        pag.locator("#ContentPlaceHolder1_txtemail").fill("suporte@santanna.g12.br")

        pag.locator("#ContentPlaceHolder1_txtsenha").wait_for()
        pag.locator("#ContentPlaceHolder1_txtsenha").fill(f.get_senha())

        pag.locator("#ContentPlaceHolder1_cmdLogin").wait_for()
        pag.locator("#ContentPlaceHolder1_cmdLogin").click()

    # procurar usuario
        pag.locator("a[title='Usuário']").wait_for()
        pag.locator("a[title='Usuário']").click()

        for cpf in f.get_funcionario():

        # seleciona a nav
            pag.locator("#ctl00_MainContent_cbNome_Input").wait_for()
            pag.locator("#ctl00_MainContent_cbNome_Input").click()

        #espera 2 seg  dps preenche o campo com o CPF
            time.sleep(2)
            pag.locator("#ctl00_MainContent_cbNome_Input").fill(cpf)

        # clica no CPF e da um scroll ate o final da pag 
            time.sleep(2)
            pag.locator(".rcbList").click()
            pag.wait_for_load_state("networkidle")
            time.sleep(2)
            pag.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # pega as datas de cadastro dos crachas nos perfis dos funcionarios
            pag.wait_for_selector("small.text-muted", timeout=10000)
            datas = pag.locator("small.text-muted").all_inner_texts()

        # cria as linhas da tabela que tem descrito o tipo de perfil e a data que foi criada 
            rows = pag.locator("table tbody tr:has(small.text-muted)")
            total = rows.count()

        # define uma data limite para a condição de excluir os crachas
            limit_date = date(2025, 4, 6)

        # percorre cada linha da tabela dos perfis e clica no "excluir" caso menor ou igual a data limite estipulada
            for i in range(total):
                row = rows.nth(i)
                date_str = row.locator("small.text-muted").inner_html()
                date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()

                if date_obj <= limit_date:
                    row.locator(".btn-group").wait_for()
                    row.locator(".btn-group").click()
                    time.sleep(1.5)
                    row.locator("a[href='javascript:void(0);']:has-text('Excluir')").wait_for()
                    row.locator("a[href='javascript:void(0);']:has-text('Excluir')").click()
                else:
                    continue
        
        # espera um tempo para clicar em "Salvar" e passar para o proximo usuario
            time.sleep(2)
            pag.locator("#cmdSalvar").wait_for()
            pag.locator("#cmdSalvar").click()
                    
        input("enter pra sair")
        nav.close()
