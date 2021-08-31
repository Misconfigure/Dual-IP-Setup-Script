#!/usr/bin/env python3

import os, time


os.system('sudo apt install conntrack nload htop tcpdump -y')



os.system("clear")
server_ip1 = input('Please enter your main IP: ')
os.system("clear")
server_ip2 = input('Please enter your server\'s Failover IP: ')
os.system("clear")

os.system('iptables -t nat -D POSTROUTING 1')
os.system(f'iptables -A POSTROUTING -t nat -p tcp -j SNAT --to-source {server_ip1}')
os.system(f'iptables -A POSTROUTING -t nat -p udp -j SNAT --to-source {server_ip2}')
#this script was made by sgomgitsyo please dont take credit
print("This script was made by SG. The dual has now been setup (:")