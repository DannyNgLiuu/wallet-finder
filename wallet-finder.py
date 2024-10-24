from seleniumbase import Driver
from bs4 import BeautifulSoup
import time 

driver = Driver(uc=True)

pair = "j72dun5ha5med1wdchyrkmwpg9urd75sctgu4ncohvdr"

url = "https://dexscreener.com/solana/" + pair

driver.uc_open_with_reconnect(url, reconnect_time=30) #increased time to allow targeted js to load

driver.uc_gui_click_captcha()


driver.wait_for_element_visible("div.custom-zl2cr9")

button = driver.find_element(
        "xpath", "//*[@id='root']/div/main/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/button[2]"
)

driver.execute_script("arguments[0].scrollIntoView(true);", button)

button.click()

time.sleep(1)

page_html = driver.get_page_source()

#use bs4 to parse the html
soup = BeautifulSoup(page_html, 'html.parser')

#find all <div> elements with class "custom-1dwgrrr"
target_divs = soup.find_all('div', class_='custom-1dwgrrr')

counter = 1

if target_divs:
    for div in target_divs:
        a_tag = div.find('a', href=True)  #finds the <a> tag with href attribute
        if a_tag:
            full_link = a_tag['href']

            #get the part after "account/"
            if "account/" in full_link:
                account_info = full_link.split("account/")[-1]
                print(f"Rank #{counter}: {account_info}")

                counter += 1
            else:
                print("No 'account/' found in the link.")
        else:
            print("No <a> tag with href found in this div.")
else:
    print("No <div> with class 'custom-1dwgrrr' found.")
    
driver.quit()