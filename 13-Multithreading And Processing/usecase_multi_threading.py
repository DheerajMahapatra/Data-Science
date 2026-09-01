'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.

'''


'''
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/

'''


import threading
import requests
from bs4 import BeautifulSoup


urls = [
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")
    
threads = []

for url in urls:
    thread = threading.Thread(target = fetch_content, args = (url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("All web pages fetched")



'''
import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        print(f"\nProcessing {url}")

        # Title
        print("Title:", soup.title.text)

        # Headings
        print("\nHeadings:")
        for h in soup.find_all(["h1","h2","h3"]):
            print(h.text.strip())

        # Links
        print("\nLinks:")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                print(href)

        # Tables
        tables = soup.find_all("table")
        print("\nTables found:", len(tables))

        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all(["td","th"])
                cols = [c.text.strip() for c in cols]
                print(cols)

    except Exception as e:
        print("Error:", e)

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nAll web pages fetched")



Most useful BeautifulSoup commands (cheat sheet)
| Task          | Code                        |
| ------------- | --------------------------- |
| Find element  | `soup.find()`               |
| Find all      | `soup.find_all()`           |
| By class      | `soup.find(class_="class")` |
| By id         | `soup.find(id="id")`        |
| Get text      | `.text`                     |
| Get attribute | `.get("href")`              |



Pro tip (real scraping projects)
    Tables ko direct pandas dataframe me convert kar sakte ho:

import pandas as pd

tables = pd.read_html(url)
print(tables[0])

'''