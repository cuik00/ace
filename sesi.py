try:
    from telethon import TelegramClient, sync, events
    from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
    from telethon.errors import SessionPasswordNeededError
except:
    print('telethon not installed\npip install telethon to solved')
from time import sleep
try:
    from colorama import *
    init(autoreset=True)
    hijau = Style.BRIGHT+Fore.GREEN
    merah = Style.BRIGHT+Fore.RED
    kuning = Style.BRIGHT+Fore.YELLOW
    magenta = Style.BRIGHT+Fore.MAGENTA
    putih = Style.BRIGHT+Fore.WHITE
    reset = Fore.RESET
except:
    print('colorama belum terinstall\npkg install colorama\ngunakan perintah diatas untuk menginstall colorama')
import json, re, sys, os
if not os.path.exists('session'):
    os.makedirs('session')
api_id = 1148490
api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'

def wd(nomor):
    try:
        phone_number = nomor
        client = TelegramClient('session/' + phone_number, api_id, api_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone_number)
                me = client.sign_in(phone_number, input(f'Enter Yout Code Code : '))
                print(f"Sesi Berhasil dibuat [{nomor}]")
                client.disconnect()
            except SessionPasswordNeededError:
                passw = input(Fore.RESET + 'Your 2fa Password : ')
                me = client.start(phone_number, passw)
                client.disconnect()
        else:
            print(f"[{hijau}+{reset}] [{nomor}] Sudah mempunyai sesi")
    except Exception as e:
        print(f'[{merah}-{reset}] {merah}{e}')
if os.name == 'nt':os.system('cls')
else:os.system('clear')
print("""
Digunakan untuk membuat sesi telegram
    """)
try:
    while True:
        nn = input("masukkan nomor: ")
        wd(nn)
except KeyboardInterrupt:
    print("\nKeluar..!!")
except IOError:
    print("tidak ada file akun.txt")