from playwright.sync_api import sync_playwright
import funcs

with sync_playwright() as p:

    # abrir navegador
    nav = p.firefox.launch(headless=False)
    pag = nav.new_page()
    pag.goto("https://www.ucsexplorer.com.br/login/login.aspx")
    print("Abriu zé\n")

    pag.locator("#ContentPlaceHolder1_txtemail").wait_for()
    pag.locator("#ContentPlaceHolder1_txtemail").fill("suporte@santanna.g12.br")

    pag.locator("#ContentPlaceHolder1_txtsenha").wait_for()
    pag.locator("#ContentPlaceHolder1_txtsenha").fill(funcs.get_senha())






    input("enter pra sair")
    nav.close()