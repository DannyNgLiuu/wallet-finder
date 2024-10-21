from seleniumbase import Driver

driver = Driver(uc=True, headless=False)


driver.get("https://dexscreener.com/solana/6qvqkpe5jewtwssumyjkjhphoukw23d8xerlzk7oanqg")


driver.sleep(10)


driver.quit()
