from playwright.sync_api import sync_playwright
from settings import create_df

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://fptshop.com.vn/may-tinh-xach-tay")

    name_laptop_elt = page.locator("xpath=//html/body/div[2]/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/h3/a").all()
    name_laptop = [i.text_content() for i in name_laptop_elt]
    price_elt = page.locator(
        "//html/body/div[2]/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[1]").all()
    price = [i.text_content() for i in price_elt]

# Save Excel
df_form = {
    "laptop": name_laptop,
    "price": price
}
filename = "laptop_list"
create_df(df_form, filename)

