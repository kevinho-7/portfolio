from playwright.sync_api import sync_playwright
import time
from datetime import datetime
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

        #espera 1 seg  dps preenche o campo com o CPF
            time.sleep(2)
            pag.locator("#ctl00_MainContent_cbNome_Input").fill(cpf)

        # clica no CPF e da um scroll ate o final da pag 
            pag.locator(".rcbList").click()
            pag.wait_for_load_state("networkidle")
            time.sleep(2)
            pag.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # pega as datas de cadastro dos crachas nos perfis dos funcionarios
            pag.wait_for_selector("small.text-muted", timeout=10000)
            datas = pag.locator("small.text-muted").all_inner_texts()

        # exclui o cadastro do cracha do usuario 
            # converted_dates = f.convert_string_to_dates(datas)
            # limit_date = datetime.strptime("06/04/2025", "%d/%m/%Y").date()

            rows = pag.locator("table tbody tr:has(small.text-muted)")
            total = rows.count()

            for i in range(total):
                row = rows.nth(i)
                date = [datetime.strptime(s, "%d/%m/%Y").date() for s in row.locator("small.text.muted").all_inner_texts()]
                if date <= datetime.date(2025, 4, 6):
                    row.locator(".btn-group").wait_for()
                    row.locator(".btn-group").click()
                    break
                else:
                    print("tudo certo cria")
                    break
            break
            
        input("enter pra sair")
        nav.close()