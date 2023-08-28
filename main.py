import json
import random
import threading
import time
import websocket
from colorama import Fore, Style, init

init(convert=True)
lock = threading.Lock()
status = ['dnd', 'idle', 'online']
success = f"[{Fore.LIGHTGREEN_EX}+{Fore.WHITE}]"

def onliner(token, status):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    status = random.choice(status)
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"presence": {"status": status,"afk": False}},"s": None,"t": None}
    ws.send(json.dumps(auth))
    online = {"op":1,"d":"None"}
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps(online))

def run_onliner():
  print(f"\n{Fore.LIGHTCYAN_EX + Style.BRIGHT}Mass Discord Token Onliner | {Fore.WHITE}[{Fore.LIGHTGREEN_EX}ΡΗΛΝΤOΜ{Fore.WHITE}]\n")
  while True:
    for token in open("tokens.txt","r+").readlines():
      threading.Thread(target=lambda : onliner(token.replace("\n",""), status)).start()
      lock.acquire()
      print(f"{success} {token[:20]} is online!")
      lock.release()
    time.sleep(30)
run_onliner()
