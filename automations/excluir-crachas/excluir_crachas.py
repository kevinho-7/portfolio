from playwright.sync_api import sync_playwright
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



    input("enter pra sair")
    nav.close()