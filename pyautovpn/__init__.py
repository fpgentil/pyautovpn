import os
import commands
import re

def setup(password, token, vpn_name):
    user = commands.getstatusoutput("whoami")[-1]

    keychain_pwd = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_pass | egrep '^password'")[-1]
    if (re.search('password\:', keychain_pwd) != None):
        os.system("security -q delete-generic-password -a {0} -s pyautovpn_pass".format(user))

    keychain_token = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_token | egrep '^password'")[-1]
    if (re.search('password\:', keychain_token) != None):
        os.system("security -q delete-generic-password -a {0} -s pyautovpn_token".format(user))

    keychain_name = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_name | egrep '^password'")[-1]
    if (re.search('password\:', keychain_name) != None):
        os.system("security -q delete-generic-password -a {0} -s pyautovpn_name".format(user))

    os.system("security -q add-generic-password -a {0} -s pyautovpn_pass -w {1}".format(user, password))
    os.system("security -q add-generic-password -a {0} -s pyautovpn_token -w {1}".format(user, token))
    os.system("security -q add-generic-password -a {0} -s pyautovpn_name -w {1}".format(user, vpn_name))

    print("Password,token and VPN name were added/updated successfully")
