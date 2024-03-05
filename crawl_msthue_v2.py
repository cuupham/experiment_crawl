from playwright.sync_api import sync_playwright
from settings import create_df

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    base_url = "https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/an-giang-93?page="
    name_company = []
    msthue = []
    nguoidaidien = []
    diachi = []

    for i in range(5):
        page.goto(f"{base_url}{i + 1}")
        name_company_elt = page.locator(
            "//html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/h3/a").all()
        msthue_elt = page.locator(
            "xpath=//html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/div/a").all()
        nguoidaidien_elt = page.locator(
            "xpath=//html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/div/em/a").all()
        diachi_elt = page.locator(
            "xpath=//html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/address").all()

        for i1, i2, i3, i4 in zip(name_company_elt, msthue_elt, nguoidaidien_elt, diachi_elt):
            name_company.append(i1.text_content())
            msthue.append(i2.text_content())
            nguoidaidien.append(i3.text_content())
            diachi.append(i4.text_content())

# Save to Excel
data_form = {
    "Company": name_company,
    "Ma so thue": msthue,
    "Nguoi dai dien": nguoidaidien,
    "Dia chi": diachi
}
name_file = "msthue_list"
create_df(data_form, name_file)
