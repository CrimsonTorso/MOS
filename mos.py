#!/usr/bin/env python3

import os, time, sys


def clear():
	responce = os.system("clear")

def welcome_banner():
	print('''
   ▄▄▄▄███▄▄▄▄    ▄██████▄     ▄████████ 
 ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███ 
 ███   ███   ███ ███    ███   ███    █▀  
 ███   ███   ███ ███    ███   ███        
 ███   ███   ███ ███    ███ ▀███████████ 
 ███   ███   ███ ███    ███          ███ 
 ███   ███   ███ ███    ███    ▄█    ███ 
  ▀█   ███   █▀   ▀██████▀   ▄████████▀  
                                       
	[+] The Mutli OpSec Installer
	[?] 	By CrimsonTorso
		''')

clear()
welcome_banner()
confirm = input("[-] Download all tools? [y/n]: ").lower()
if confirm == 'y':
	print("Starting...")
	time.sleep(2.5)
	responce = os.system("mkdir tools && cd tools && git clone https://github.com/cryptolok/GhostInTheNet && sudo apt-get install openvpn proxychains tor && wget https://tails.braingap.uk/tails/stable/tails-amd64-3.12.1/tails-amd64-3.12.1.img")
	time.sleep(1.5)
	print("[!] Done!")


#Created By CrimsonTorso
# <3
