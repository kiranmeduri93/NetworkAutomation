###############################################################################
#
# SIMPLE PYTHON SCRIPT TO CHANGE CONFIG AND COMPARE WITH PREVIOUS REVISION 
# Author: Sai Kiran Meduri - medurikiran.sk@gmail.com
# Description: This is a simple script that takes config file, Ip, username and password as a user input, 
# scp config file to cisco filesyatem, load the configurtaion into running config and 
# show the diff of previous config
#
# Netmiko is a PYTHON module which establishes SSH connection to the network devices.
# To install Netmiko module and supporting libraries, please run below commands.
#apt-get update
#apt-get install python -y
#apt-get install python-pip -y
#pip install netmiko

##dir nvram: -- > check files in the filesystem for CISCO IOS 7200 Router
##delete nvram:two.txt -- > delete file in the filesystem for CISCO IOS 7200 Router
###############################################################################

from netmiko import ConnectHandler, SCPConn

def scpfile(file):
    print('!!!!!!!!!! Enabling scopy !!!!!!!!!!')
    connect.send_config_set('ip scp server enable')
    scp_conn = SCPConn(connect)
    scp_conn.scp_transfer_file(file, 'nvram:two.txt')
    connect.send_config_set('no ip scp server enable')
    print('!!!!!!!!!! File copied !!!!!!!!!!')
    print('!!!!!!!!!! Disabled scopy !!!!!!!!!!')

def copyflash():
    configfile = 'copy nvram:two.txt running-config'
    output = connect.send_command_timing(configfile)
    if 'Destination filename' in output:
        output1 = connect.send_command_timing('\n')
        #print(output1)
    else:
        print("something wrong")

def precheck():
    precheckconfig = connect.send_command_timing("sh running-config")
    #print(precheckconfig)
    return precheckconfig.split("\n")

def postcheck():
    postcheckconfig = connect.send_command_timing("sh running-config")
    #print(postcheckconfig)
    return postcheckconfig.split("\n")

file= input("enter configuration filename ")
ip = input("enter device IP address ")
user = input("enter device username ")
paswrd = input("enter device password ")
try:
    connect = ConnectHandler(device_type='cisco_ios',ip= ip, username=user,password=paswrd)
    l1 = precheck()
    scpfile(file) 
    copyflash()
    l2 = postcheck()
    comparelist = set(l2) - set(l1)
    print("!!!!!!!!!! New config !!!!!!!!!!")
    print("\n")
    for element in comparelist:
        print(element)
    print("\n")
    print("!!!!!!!!!! New config !!!!!!!!!!")

except Exception as e:
    print("TEST FAILED")
    print(e)  
