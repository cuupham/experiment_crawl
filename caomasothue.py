from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/an-giang-93?page='
name_company_final = []
masothue_final = []
nguoidaidien_final = []
diachi_final = []

for i in range(5):
    browser.get(f"{url}{i+1}")

    # Get Elements
    nameCompany_e = browser.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/h3/a")
    masothue_e = browser.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/div/a")
    nguoidaidien_e = browser.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/div/em/a")
    diachi_e = browser.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/main/section/div/div[2]/div/address")

    # name_company = [name.text for name in nameCompany_e]
    # masothue = [ms.text for ms in masothue_e]
    # nguoidaidien = [ndd.text for ndd in nguoidaidien_e]
    # diachi = [dc.text for dc in diachi_e]
    
    # name_company_final += name_company
    # masothue_final += masothue
    # nguoidaidien_final += nguoidaidien
    # diachi_final += diachi

    for name, masothue, nguoidaidien, diachi in zip(nameCompany_e, masothue_e, nguoidaidien_e, diachi_e):
        name_company_final.append(name.text)
        masothue_final.append(masothue.text)
        nguoidaidien_final.append(nguoidaidien.text)
        diachi_final.append(diachi.text)

# Create DataFrame and export excel
df = pandas.DataFrame({
    "Company": name_company_final,
    "Ma so thue": masothue_final,
    "Nguoi dai dien": nguoidaidien_final,
    "Dia chi": diachi_final
})

df.to_excel("msthue_list.xlsx", index = False)
