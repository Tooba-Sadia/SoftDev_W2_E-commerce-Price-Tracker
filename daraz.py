from playwright.sync_api import sync_playwright
import csv
import os

csv_name = 'daraz.csv'
if os.path.exists(csv_name):
    os.remove(csv_name) # Resetting the csv so that only top 10 is saved in csv

def add_to_csv(index, name, price):
    d_csv = {
    'index': index,
    'Product Name': name,
    'Price': price
}
    try:
        file_exists = os.path.exists(csv_name)
        is_empty = not file_exists or os.path.getsize(csv_name) == 0  # Check if file is empty

        with open('daraz.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['index', 'Product Name', 'Price'])

            if is_empty:
                writer.writeheader()  # Write header only if the file is empty

            writer.writerow(d_csv)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless = True,slow_mo=2000) #slow_mo has delay in ms so 2000ms mean 2s
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    #bcz Daraz has alot of pictures so its better not to load it all
    #so we will only load the dom content
    #dom content is the html structure of the page
    link = 'https://www.daraz.pk/#?'
    page.goto(link,wait_until='domcontentloaded')   
    try:
        #using id bcz id doesnt change often
        page.locator("input#q").click()
        page.locator("input#q").fill("laptop")
        page.locator("input#q").press("Enter", timeout=5000)
        page.screenshot(path="searched_laptop_results.png")
    except:
        print("Search box not found")  

    #using Classes to locate the title and prices
    titles = page.locator("div.RfADt")
    prices = page.locator("div.aBrP0")

    for i in range(10):
        title = titles.nth(i)
        price = prices.nth(i)

        add_to_csv(i+1, title.locator("a[title]").inner_text(), price.locator("span").inner_text())

        
print("Data written to daraz.csv successfully.")

