from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas

"""
Trang Static
"""

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://books.toscrape.com/")
star_list = ("One", "Two", "Three", "Four", "Five")

title_tags = browser.find_elements(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li/article/h3/a")
titles = [
    tag.get_attribute("title") for tag in title_tags
]
# for tag in title_tags:
#     print(tag.get_attribute("title"))

price_tags = browser.find_elements(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li/article/div[2]/p[1]")
prices = [tag.text for tag in price_tags]
# for tag in price_tags:
#     print(tag.text)

stars_tags = browser.find_elements(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li/article/p")

# stars = [
#     [x for x in tag.get_attribute("class").split() if x != "star-rating"][0]
#     for tag in stars_tags
# ]
stars = []
for star in stars_tags:
    star_string = [x for x in star.get_attribute("class").split() if x != "star-rating"][0]
    stars.append(star_list.index(star_string) + 1)

# Tao dataframe
df = pandas.DataFrame({
    "title": titles,
    "prices": prices,
    "stars": stars
})

df.to_excel("output/books_test.xlsx", index=False)
