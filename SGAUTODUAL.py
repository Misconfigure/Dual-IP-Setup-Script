U
    j��a�  �                   @   s~   d dl Z d dlZe �d� e �d� ed�Ze �d� ed�Ze �d� e �d� e �de� �� e �de� �� ed	� dS )
�    Nz0sudo apt install conntrack nload htop tcpdump -y�clearzPlease enter your main IP: z(Please enter your server's Failover IP: z iptables -t nat -D POSTROUTING 1z:iptables -A POSTROUTING -t nat -p tcp -j SNAT --to-source z:iptables -A POSTROUTING -t nat -p udp -j SNAT --to-source z:This script was made by SG. The dual has now been setup (:)�os�time�system�inputZ
server_ip1Z
server_ip2�print� r   r   �SGAUTODUAL.py�<module>   s   




