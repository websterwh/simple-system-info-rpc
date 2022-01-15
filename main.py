import os
from pypresence import Presence
import time
from os import system

os.system('cls')
client_id = input(str('Client ID> '))
RPC = Presence(client_id)
RPC.connect() 

os.system('title System Info RPC')
print('Running RPC')
while True: 
    cpu_per = round(psutil.cpu_percent(),1)
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    RPC.update(details="RAM: "+str(mem_per)+"%", state="CPU: "+str(cpu_per)+"%", large_image='pc')
    time.sleep(15)
