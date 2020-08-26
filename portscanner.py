import socket
import os 
import sys
os.system ("bash color.sh")
banner="""\033[0;32m

-------------------
       ###           
★Im T Gray Hat  ★
       ###
------------------

  _____   __   ____  ____   ____     ___  ____  
 / ___/  /  ] /    T|    \ |    \   /  _]|    \ 
(   \_  /  / Y  o  ||  _  Y|  _  Y /  [_ |  D  )
 \__  T/  /  |     ||  |  ||  |  |Y    _]|    / 
 /  \ /   \_ |  _  ||  |  ||  |  ||   [_ |    \ 
 \    \     ||  |  ||  |  ||  |  ||     T|  .  Y
  \___j\____jl__j__jl__j__jl__j__jl_____jl__j\_j
                                            
"""
def nmap():
  os.system("clear");
  print(banner);
  ip=input("please ip : ");
  os.system("nmap -sV "+ip)
  print("Nmap Start")
  input("")
  


nmap();
