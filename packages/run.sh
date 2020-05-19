clear
cd sqlmap

echo "Which URL TYPE OR PASTE HERE"
read url 
echo  "starting the Normal db-s attack "
echo "note : you can access sqlmap also in projectroot/packages/sqlmap"
echo "note : consider using sqlmap directly if you want to run custom commands"
echo "note : starting attack"
python2 sqlmap.py -u $url --dbs


