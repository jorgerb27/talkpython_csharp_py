from colorama import Fore
import httpx
import bs4

def main():
    print(f"using httpx: {httpx.__version__}")

    get_titles()

def get_html(n: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {n} ...",flush=True )
    url = f'https://talkpython.fm/{n}'

    resp = httpx.get(url, follow_redirects=True)  # Ensure redirects are followed

    final_url = str(resp.url)  # Final URL after all redirects
    resp2 = httpx.get(final_url)

    return resp2.text

def get_title_from_html(n: int, html: str) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {n} ...", flush=True)

    soup = bs4.BeautifulSoup(html, "html.parser")
    header = soup.select_one('title')
    if not header:
        return "MISSING"

    return header.text.strip()

def get_titles():
    for n in range(220, 230):
        html = get_html(n)
        title = get_title_from_html(n,html)
        print(Fore.GREEN + f"{n}: {title}", flush=True)


if __name__ == '__main__':
    main()