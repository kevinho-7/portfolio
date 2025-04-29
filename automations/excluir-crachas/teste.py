from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # navegador = p.chromium.launch(headless=False)  # headless=False = mostra o navegador
    navegador = p.firefox.launch(headless=False)  # headless=False = mostra o navegador
    pagina = navegador.new_page()
    pagina.goto('https://www.youtube.com')
    print("Navegador abriu certim, uai!")
    
    # agora não fecha automaticamente
    input("Pressione Enter pra fechar o navegador...")
    navegador.close()

