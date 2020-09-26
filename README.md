# ikimaru
An OSINT CLI tool desgined to fast track IP Reputation and Geo-locaton look up for Security Analysts.

# Pre-requeriments of Linux

* Python3 ```bash sudo apt install python3 ```
* Pip3 ```bash sudo apt install python3-pip ```

If you don't use Debian or Ubuntu, search for their respective platforms (like yum and pacman)

# Setup
This tool is compactible with:
* Any Linux Operating System (Debian, Ubuntu, CentOS)
* Termux

# Linux Setup
```bash
git clone https://github.com/SrJam/ikimaru.git
cd ikimaru
chmod +x ikimaru.py
sudo apt install python3-pip
pip3 install -r requirements.txt
```
# Termux Setup 

[Link about python and pip on Termux](https://wiki.termux.com/wiki/Python) that comes with the pkg python

```bash
git clone https://github.com/SrJam/ikimaru.git
cd ikimaru
chmod +x ikimaru.py
pip3 install -r requirements.txt
```
# Sample Syntax Linux and Termux
```bash
root@kali:~/ikimaru# python3 ikimaru.py 138.121.128.19

	 ▀		  ▀▀
	▄█     ▄█   ▄█▄  ▄█    ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████ ███    █▄  
	███    ███ ▄███▀ ███  ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ ███    ███ 
	███▌   ███▐██▀   ███▌ ███   ███   ███   ███    ███   ███    ███ ███    ███ 
	███▌  ▄█████▀    ███▌ ███   ███   ███   ███    ███  ▄███▄▄▄▄██▀ ███    ███ 
	███▌ ▀▀█████▄    ███▌ ███   ███   ███ ▀███████████ ▀▀███▀▀▀▀▀   ███    ███ 
	███    ███▐██▄   ███  ███   ███   ███   ███    ███ ▀███████████ ███    ███ 
	███    ███ ▀███▄ ███  ███   ███   ███   ███    ███   ███    ███ ███    ███ 
	█▀     ███   ▀█▀ █▀    ▀█   ███   █▀    ███    █▀    ███    ███ ████████▀  
		▀                                             ███    ███                       


[*] Running Geo-location Check Against 138.121.128.19

Country: Brazil
Region: Piaui
City: Teresina
Organization: Itech Telecom
ISP: Itech Telecom

[*] Geo-IP Lookup Complete!!!


[*] Running Reputation Check Against 138.121.128.19

Domain: "redeitechtelecom.com.br"
Hostname: []
Usage Type: "Fixed Line ISP"
Confidence of Abuse: 100
Number Times of Reported: 982
Last Reported: "2020-08-21T16:43:12+00:00"
Whitelisted: false

The IP Address 138.121.128.19 Is Malicious and well known for SSH Bruteforce Attacks

[*] IP Reputation Look up Complete!!!
```