import socket
import os 
import sys
os.system ("bash color.sh")
banner="""\033[0;32m"
▅▅▅▅▅▅▅▅▅▅▅
▅▅▅▅▅▅▅▅
▅▅▅▅▅▅
▅▅▅▅
◥◤
-------------------
       ###           
★Im T Gray Hat  ★
       ###
-------------------
◢◣ 
▅▅▅▅
▅▅▅▅▅▅
▅▅▅▅▅▅▅▅
▅▅▅▅▅▅▅▅▅▅▅   
"""
def nmap():
  os.system("clear");
  print(banner);
  ip=input("please ip : ");
  os.system("nmap -sV "+ip)
  print("Nmap Start")
  input("")
  


nmap();
