from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://fptshop.com.vn/may-tinh-xach-tay"
browser.get(url)

# Get element
namelaptop_elements = browser.find_elements(By.XPATH,
                                            "/html/body/div[2]/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/h3/a")
namelaptops = [
    name.get_attribute("title")
    for name in namelaptop_elements
]

price_elements = browser.find_elements(By.XPATH,
                                       "/html/body/div[2]/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[1]")
prices = [
    p.text for p in price_elements
]

# Create DataFrame and Export Excel
df = pandas.DataFrame({
    "laptop": namelaptops,
    "price": prices
})

df.to_excel("output/laptop_list.xlsx", index=False)
