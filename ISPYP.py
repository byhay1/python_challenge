#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:31:09 2019
App: I-Spy-P 
Use: Search IP within .txt documents, identify IPv4, 
allow user to find particular IP, get GeoID from IP, 
and RDAP/WhoIS from IP based on Queries  
@author: beehive
"""
#/home/beehive/Documents/I-Spy-P/data/list_of_ips.txt
#---------------------
import re
import urllib
import urllib.request
import json as js
import io
import ASCIIbanner
#import request as req

#-------------INTRO-------------#
ASCIIbanner.callbanner()
print("\n Welcome to I-Spy-P!\n\n",\
      "A prompt will ask you to upload a .txt file containing IPs\n",\
      "Once uploaded, I-Spy-P will find all IPs and ask you to specify an IP you would like to Spy on\n",\
      "Once a valid IP is passed you will be able to run queries against the IP to see if IP was in file, GeoIP info, etc.\n", \
      "\n Type 'help' after file & target IP have been added to find details on queries\n",\
      "\n HAVE FUN ^_^")
#-------------FUNCTIONS-------------#
# takes in user file path and finds all IPs and returns all IPs to an empty list for analysis
file = str(input("Please enter the file path ~ "))
iplist = []
def infile(file): 
    '''
    - Used to take file input, as path, from user
    and find IP address from the file
    - Ensure path is cast as string ex. str(input())
    - Can further enhance and make robust by doing
    a re.match on the file path input
    '''
    with open(file, 'rt') as file: 
        l = file.readline()
        for l in file:
            for txt in l.split():
                findip = re.match("[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", txt)
                if findip: 
                    iplist.append(txt)
                else: 
                    continue

# check ip for validity   
target_ip = input("Input Target IP ~ ")

while True:
    if re.match("[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", target_ip):
        print("IP Set!, to change type 'changeip'\n")
        break
    else:
        target_ip = input("Try Again (ex. ###.###.###.###) ~ ")

# defining the I-Spy-P Query Language (ISPQL)                  
# define Search Statement       
def search(target_ip):
    '''
    - Used to search text file based on user input parameter
    '''
    for ip in iplist:
        if ip == target_ip:
            print("\nFound IP")      
        else:
            continue
        
# define GeoIP Statement
def geo(target_ip):
    '''
    - Uses dbip open souce api to pull geoIP 
    location information. 
    - get, requests for api 
    - p_dbip, opens and reads url
    - js_dbip, loads as json
    - js_dbip_str & js_dbip_strf, both dump json 
    as a string for regex manipulation
    '''
    dbip_api = "http://api.db-ip.com/v2/free/" + target_ip + "/"
    get = urllib.request.Request(dbip_api)
    p_dbip = urllib.request.urlopen(get).read()
    js_dbip = js.loads(p_dbip)
    js_dbip_str = re.sub(r'({|"|}|,|\s)', ' ', js.dumps(js_dbip))
    js_dbip_strf = re.sub(r'(    |\t)', '\n', js_dbip_str)
    all_geo = js_dbip_strf.splitlines()
    for line in all_geo: 
        if re.match("  ipAddress", line): 
            continue
        else: 
            print(line)    
    
    # Use below is request module is allowed in environment
    #dbip_api = req.get("http://api.db-ip.com/v2/free/" + target_ip + "/")
    #if (dbip_api.status_code == dbip_api.codes.ok): 
    #    js_dbip = dbip_api.json
    #    print(re.sub(r'({|"|}|,|\s)', '',js_dbip))
    #else: 
    #    return dbip_api.raise_for_status()
    

# define RDAP Statement
def rdap(target_ip):
    '''
    - Uses rdap open souce api to pull geoIP 
    location information. 
    - get, requests for api 
    - p_rdap , opens and reads url
    - js_rdap , loads as json
    - js_rdap _str & js_rdap _strf, both dump json 
    as a string for regex manipulation
    '''
    rdap_api = "https://www.rdap.net/ip/" + target_ip
    get = urllib.request.Request(rdap_api)
    p_rdap = urllib.request.urlopen(get).read()
    js_rdap = js.loads(p_rdap)
    js_rdap_str = re.sub(r'({|"|}|,|[|]|\s)', ' ', js.dumps(js_rdap))
    js_rdap_strf = re.sub(r'(    |\t)', '\n', js_rdap_str)
    with io.open('rdap_' + target_ip + '.txt', 'w') as rdapsearch_file: 
        rdapsearch_file.write(js_rdap_strf) 
    print("rdap_" + target_ip + ".txt has been exported!" )

# define Changeip Statement
new_ip = target_ip  
def changeip(new_ip):
    '''
    - Used to change user set IP
    - Does a simple validation check of the new globally 
    set target_ip var based on regex.
    '''
    new_ip = input("Set new IP ~ ")
    while True:
        if re.match("[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", new_ip):
            print("IP Set!, to change type 'changeip'")
            break
        else:
            new_ip= input("Try Again (ex. ###.###.###.###) ~ ")
    global target_ip
    target_ip = new_ip
    return target_ip

# define Help Statement 
def helpme():
    print("Welcome to Help!\n", 
          "             | | \n \
             | |===( )   ////// \n \
             |_|   |||  | o o| \n \
                    ||| ( c  )                  ____ \n \
                     ||| \= /                  ||   \_ \n \
                      ||||||                   ||     | \n \
                      ||||||                ...||__/|-' \n \
                      ||||||             __|________|__ \n \
                        |||             |______________| \n \
                        |||             || ||      || || \n \
                        |||             || ||      || || \n \
------------------------|||-------------||-||------||-||------- \n \
                        |__>            || ||      || ||  ")
    print(" After >> type the 'Query-Command' (ex. $ >> help).\n",
          "Description is in [] (ex. [Shows all of the things...])\n", 
          "\n           * changeip [changes IP address target]\n \
          * exit [exits the application]\n \
          * geo [finds geo location details of target ip]\n \
          * helpme [shows all queries]\n \
          * rdap [gets RDAP/whoIS information and exports as .txt from target IP]\n \
          * search [checks to see if target IP is in .txt file]\n",
          "\n Type 'changeip' to start over, or 'exit' if you've had enough")
    
    
#Start App 
query = input("Start Query >> ")    
def startapp(query): 
    flag = 1
    while flag:
        if query == 'search': 
            call_func[query](target_ip)
            query = input(">> ") 
            startapp(query)
            break
        elif query == 'geo':
            call_func[query](target_ip)
            query = input(">> ") 
            startapp(query)
            break
        elif query == 'rdap':
            call_func[query](target_ip)
            query = input(">> ") 
            startapp(query)
            break
        elif query == 'changeip':
            call_func[query](new_ip)
            query = input(">> ") 
            startapp(query)
            break
        elif query == 'helpme':
            call_func[query]()
            query = input(">> ") 
            startapp(query)
            break
        elif query == 'exit':
            flag = 0
        else:
            query = input(">> ")
            continue
#-------------VARIABLES-------------#


#-------------NON_FUNCT-------------#
call_func = {'search':search, 'geo':geo, 'rdap':rdap, 'changeip':changeip, 'helpme':helpme}    

#-------------INITIATE-------------#
if __name__ == '__main__': 
    infile(file)
    #print(iplist)
    startapp(query)         
    
