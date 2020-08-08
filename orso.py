# Name:			orso.py v0.1
# Type:			OSINT Tool
# Author:		MrSaighnal
# date:			08/08/20
# official Repository:	https://github.com/MrSaighnal/ORSO/
# .______________________________________________.
# |					         |
# |  Don't use this script for illegal purposes  |
# |______________________________________________|


import requests
import re
import os
import sys
import socket
from bs4 import BeautifulSoup

# set the colors
# Python program to print 
# colored text and background 
class colors: 

    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[103m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'


def startup():
	os.system("clear")
	print(colors.bold, "        ___           ___           ___           ___     ")
	print("        /\  \         /\  \         /\  \         /\  \    ")
	print("       /::\  \       /::\  \       /::\  \       /::\  \   ")
	print("      /:/\:\  \     /:/\:\  \     /:/\ \  \     /:/\:\  \  ")
	print("     /:/  \:\  \   /::\~\:\  \   _\:\~\ \  \   /:/  \:\  \ ")
	print("    /:/__/ \:\__\ /:/\:\ \:\__\ /\ \:\ \ \__\ /:/__/ \:\__\ ")
	print("    \:\  \ /:/  / \/_|::\/:/  / \:\ \:\ \/__/ \:\  \ /:/  /")
	print("     \:\  /:/  /     |:|::/  /   \:\ \:\__\    \:\  /:/  / ")
	print("      \:\/:/  /      |:|\/__/     \:\/:/  /     \:\/:/  /  ")
	print("       \::/  /       |:|  |        \::/  /       \::/  /   ")
	print("        \/__/         \|__|         \/__/         \/__/    ")
	print("")
	print(colors.fg.lightred, colors.bold, "[-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-]")
	print(colors.fg.lightred, colors.bold, "[-+-]", colors.fg.lightgreen, " Osint Recognition Subdomain Obtainer v0.1 ",  colors.fg.lightred, "[-+-]")
	print(colors.fg.lightred, colors.bold, "[-+-]", colors.fg.lightgreen, "           Author:", colors.fg.lightblue, "Mr Saighnal            ",  colors.fg.lightred, "[-+-]")
	print(colors.fg.lightred, colors.bold, "[-+-]", colors.fg.lightgreen, "     Email:", colors.fg.lightblue, "mrsaighnal@protonmail.com     ",  colors.fg.lightred, "[-+-]")
	print(colors.fg.lightred, colors.bold, "[-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-]")
	print("")
	print(colors.fg.lightred, colors.bold, colors.bg.orange, "        DON'T USE THIS TOOL FOR ILLEGAL PURPOSE!        ")
	print("")
	print("")
	print(colors.reset, colors.fg.yellow, "usage: python3 orso.py DOMAIN (ex: python3 orso.py google.com)")
	print("")
	print("")
	print("")
	os.system("sleep 3")

def scrape_crt(DOMAIN):
	
	URL = 'https://crt.sh/?q=' + DOMAIN
	page = requests.get(URL)
	
	links = []
	clinks = []
	soup = BeautifulSoup(page.content, 'html.parser')
	
	#check if there is not result
	found = soup.findAll(text='None found')
	if len(found) == 1:
		#print("error")
		return 0
	else:
		#Scraping the  web page to remove the trash
		soup = soup.find_all('table')[1]
		soup = soup.find_all('table')[0]
		soup = soup.find_all('tr')
		
		#iterate all the lines
		for x in range(1, len(soup)):
			#print(soup[x], "------\n")
			link = soup[x].find_all('td')[4]
			#I make the object of BS4 to a string in a new var called "slink"	
			slink = []
			for x in link:
				slink.append(str(x))
			#if there are not multiple elements in my object
			if "<br/>" not in slink:
				link = link.get_text()
				links.append(link)
			else:
				slink.remove('<br/>')
				for y in slink:
					y = y.replace('<br/>','')
					links.append(y)
		
		#delete the empty elements
		noNullLinks = filter(None, links)
		
		#delete the *.
		noSpecialCharsLinks = [x.replace('*.','') for x in noNullLinks]
		
		#delete duplicates
		clinks = list(dict.fromkeys(noSpecialCharsLinks))
		
		return clinks







def main():
	startup()
	print(colors.fg.yellow, colors.bold, "[!]", colors.reset, "Looking for subdomains of: ", colors.bold, sys.argv[1])
	
	result = scrape_crt(sys.argv[1])
	if result == 0:
		print(colors.fg.lightred, colors.bold, "[-]", colors.reset, "No subdomain found	")
	else:
		#print(result)
		print(colors.fg.lightgreen, colors.bold, "[+]", colors.reset, "Found ", colors.bold, len(result), colors.reset, "subdomains")
		os.system("sleep 2")
		print("")
		for y in result:
			print(y)     #  for resolving	 the hostname =>  print(y, "|", socket.gethostbyname(y))

if __name__ == "__main__":
	main()





#print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')




