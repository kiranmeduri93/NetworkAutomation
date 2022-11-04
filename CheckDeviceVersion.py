###############################################################################
#
# SIMPLE PYTHON SCRIPT TO READ CISCO INFORMATION
# Author: Sai Kiran Meduri - medurikiran.sk@gmail.com
# Description: This is a simple script that takes user input and display device version
# Userinput values - deviceIps, username and password
#
#
# Netmiko is a PYTHON module which establishes SSH connection to the network devices.
# To install Netmiko module and supporting libraries, please run below commands.
#apt-get update
#apt-get install python -y
#apt-get install python-pip -y
#pip install netmiko
#
###############################################################################

from netmiko import ConnectHandler
def checkdeviceversion(ip,username,password):
    ciscorouter = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': username,
    'password': password,
    'secret': 'cisco',
    }

    connect =ConnectHandler(**ciscorouter)
    output = connect.send_command('show version')
    #print(output)

    for line in output.split("\n"):
        if "Cisco IOS Software" in line:
            newline = '\n'
            print(f'Device Ip: {ip}{newline}Version: {line}{newline}')

deviceips=input("Please enter list of device separated by space  : ")
userlogin=input("Please enter login username : ")
userpassword=input("Please enter login password : " )


devicelist = deviceips.split()
for ip in devicelist:
    checkdeviceversion(ip,userlogin,userpassword)
