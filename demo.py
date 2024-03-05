from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/an-giang-93?page=1")

    company_elt = page.locator("//h3/a[contains(@title, 'Tra cứu mã số thuế')]").all()
    #company_elt = page.locator("//html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/h3/a").all()




    print(company_elt)
