###############################################
##Port Forwarding Menu Linked With ASploit#####
###############################################

import os
import subprocess

os.system("clear");
os.system("toilet -f mono12 PORT FORWARDING MENU");

print("1.USE Serveo");
print("2.USE ngrok-built-in");
print("3.Exit");

choice = int(input("ENTER CHOICE :"));

if choice ==1:
 os.system("./run-serveo.sh");
                       
if choice ==2:
 os.system("./start.sh");
                          

if choice ==3:
 exit();
