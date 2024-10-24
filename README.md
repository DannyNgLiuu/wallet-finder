I used seleniumbase to emulate the website and bs4 to parse the page source.

I ran into problems a few days ago where I use this exact code but was unable to bypass the cloudflare captcha.

The way I went about this was on accident. I had a VPN on which probably simulated a real user. 

The days before I tried using user-agents, setting the window full screen, language settings but nothing was working.

I also tried implementing proxies into the chromedriver but ran into proxy issues.

When I got pass the captcha issue, a obstacle arise where the html wasn't printing as it should.

I think it was because the website was heavily reliant on javascript which make it so that everything had to be loaded for my code to find certain div classes.

When it finally printed the html, it printed the html of the cloudflare html instead of the actual html.

I think the way I bypassed this was adding a sleep timer and letting the website load before grabbing the html.
