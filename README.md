I used seleniumbase to emulate the website and bs4 to parse the page source.

I ran into problems a few days ago where I use this exact code but was unable to bypass the cloudflare captcha.

The way I went about this was on accident. I had a VPN on which probably simulated a real user. 

The days before I tried using user-agents, setting the window full screen, language settings but nothing was working.

I also tried implementing proxies into the chromedriver but ran into proxy issues.

When I got pass the captcha issue, a obstacle arise where the html wasn't printing as it should.

I think it was because the website was heavily reliant on javascript which make it so that everything had to be loaded for my code to find certain div classes.

When it finally printed the html, it printed the html of the cloudflare html instead of the actual html.

I think the way I bypassed this was adding a sleep timer and letting the website load before grabbing the html.

I used the .click() to interact with the "Top Trader" button to load the js of those classes.

I used XPATH because there were multiple buttons with the same class name.

Changed the print to just the address along with the ranking.

Removed printing and only adding addresses to a csv file.

Using Pandas library to find the intersections of the wallets.

Done for now but I might revisit where I will have the win percentage next to each wallet.

I will probably do that after I finish wallet-tracking.py.

https://gmgn.ai/sol/address/54EiavhVatcFbcRHKm2swd6eB8reyib3kTkDGScoGjGK

I can input wallets and scrape the winrate data of off this website.

