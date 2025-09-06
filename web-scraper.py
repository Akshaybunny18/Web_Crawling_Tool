import requests
from bs4 import BeautifulSoup
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)

def sif(x, url, visited, data, deep=0, maxdeep=8):
    if deep > maxdeep:  
        return
    if url in visited:
        return
    visited.add(url)

    try:
        print(f"(Bunny) Fetching SUB(URLS): {url}")
        code = requests.get(url, timeout=10, verify=False).text
    except requests.RequestException:
        return

    soup = BeautifulSoup(code, 'lxml')
    hi = soup.find_all(['link','a','base','img','area','iframe','frame','audio','video','script'])

    for u in hi:
        link = u.get('href') or u.get('src')  # link = url['href'] #akshay
        if not link:
            continue

        # Normalize relative links
        if link.startswith('/'):
            full_url = base_url + link
        else:
            full_url = link

        # Collect matching links
        if x == "all":
            data.add(full_url)
        elif link.lower().endswith(f'.{x}'):
            data.add(full_url)

        # Recurse only if it looks like a navigable page
        if full_url.startswith(base_url):
            sif(x, full_url, visited, data, deep+1, maxdeep)


# ---------------- Main ----------------
print("=== Bunny Web Surfer ===")
print("This script crawls a website and extracts links to files you specify (e.g., pdf, jpg).")
print("If you enter 'all', it will fetch all discovered links from the given website.")
print("Note: Recursion depth is limited to avoid infinite loops.\n")

x = input("Enter a file extension (like pdf, jpg, mp4) or 'all': ").strip().lower()
base_url = input("Enter the starting URL (e.g., https://example.com): ").strip()

data = set()
visited = set()
sif(x, base_url, visited, data)

with open("urls.txt", "w") as file:
    for link in data:
        file.write(link + '\n')

print(f"\nSurfing complete. Found {len(data)} links. Saved to urls.txt")
