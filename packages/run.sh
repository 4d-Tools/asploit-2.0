cowsay 'SQLMAP For ASPLOIT2.0';
cd sqlmap

echo "Which URL To Do Attack :";
read url 
echo  "starting the Normal db-s attack "
echo "note : you can access sqlmap also in projectroot/packages/sqlmap"
echo "note : consider using sqlmap directly if you want to run custom commands"
echo "note : starting attack"
python2 sqlmap.py -u $url --dbs


