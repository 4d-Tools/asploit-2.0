#python Sploits
####4d-team####

import os
import subprocess

os.system("clear");
os.system("toilet -f mono12 a-sploit 2.0");

print("1.Phishing Attack");
print("2.Option Coming Soon");
print("3.sql injection");
print("4.Credits");
print("5.Port Forwarding");
print("6.Exit");


choice = int(input("ENTER CHOICE :"));



if choice ==1:
  os.system("cd main && chmod +x phish.py && python2 phish.py");


if choice ==2:
  os.system("cd main")
  os.system("chmod +x spoofer.py")
  os.system("python2 spoofer.py");

if choice ==3:
   os.system("cd packages && chmod +x run.sh && bash run.sh");

 
if choice ==4:
 os.system("cd creds && chmod +x creds.sh && bash creds.sh");

if choice ==5:
 os.system("cd portfoward && chmod +x menu.py && python2 menu.py");

if choice ==6:
 exit();
