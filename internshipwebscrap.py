import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ------------------------------
# Save JSON data
# ------------------------------
def save(final_data):
    json_object = json.dumps(final_data, indent=4, ensure_ascii=False)
    with open("data.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)

# ------------------------------
# Start Browser with Anti-Bot Bypass
# ------------------------------
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

# Pass your Chrome version
driver = uc.Chrome(options=options, version_main=138)

# ------------------------------
# Open GoDaddy URL
# ------------------------------
start_url = 'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club'
print("Opening GoDaddy...")
driver.get(start_url)

# Give extra time for anti-bot challenge
time.sleep(5)

try:
    # Wait for price element
    price1_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'domain-price')]"))
    )
    price1 = price1_element.text
    print("Price 1:", price1)

    # Get all prices found
    price_elements = driver.find_elements(By.XPATH, "//span[contains(@class,'domain-price')]")
    prices = [p.text for p in price_elements if p.text.strip() != ""]

    # Print all found prices
    for i, price in enumerate(prices, start=1):
        print(f"Price {i}:", price)

    # Save to JSON
    save({"prices": prices})

except TimeoutException:
    print("⚠ Could not find prices — access may be blocked or elements not loaded.")

finally:
    driver.quit()
