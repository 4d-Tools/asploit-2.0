####requirements######
echo "note : we are going to update the system repository + upgrade the system"
echo "note : we are also going to install some nessacary packages"
apt-get update
apt install -y python fish bash php figlet toilet cowsay 
#apt install -y python3 python3-pip curl fish bash php figlet toilet cowsay // Uncomment It If Its A Ubuntu Or Debian Based Installation
apt upgrade -y
 ###############
echo "Making NgRok Executable";
cd portfoward && chmod +x ngrok
echo "All Pacakage Installed successfully . A-Sploit2.0\n";
#################
echo "Installing Framework Requirements";
cd main/weevely && pip install -r requirements.txt
echo "Installation Is Done ! Thank You For Installating a-Sploit2.0";

