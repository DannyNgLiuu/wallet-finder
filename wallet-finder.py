from seleniumbase import Driver
from bs4 import BeautifulSoup

driver = Driver(uc=True)

pair = "j72dun5ha5med1wdchyrkmwpg9urd75sctgu4ncohvdr"

url = "https://dexscreener.com/solana/" + pair

driver.uc_open_with_reconnect(url, reconnect_time=4)

driver.uc_gui_click_captcha()

driver.sleep(15)

page_html = driver.get_page_source()

#use bs4 to parse the html
soup = BeautifulSoup(page_html, 'html.parser')

#find all <div> elements with class "custom-1dwgrrr"
target_divs = soup.find_all('div', class_='custom-1dwgrrr')

if target_divs:
    for div in target_divs:
        a_tag = div.find('a', href=True) #finds the <a> tag with href attribute
        if a_tag:
            print(f"Link: {a_tag['href']}")
        else:
            print("No <a> tag with href found in this div.") #error catching
        print("-" * 80)
else:
    print("No <div> with class 'custom-1dwgrrr' found.") #error catching

driver.quit()
