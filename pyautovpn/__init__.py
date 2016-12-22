import os
import commands
import re

def setup(password, token):
    user = commands.getstatusoutput("whoami")[-1]

    keychain_pwd = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_pass | egrep '^password'")[-1]
    if (re.search('password\:', keychain_pwd) != None):
        os.system("security -q delete-generic-password -a {0} -s pyautovpn_pass".format(user))

    keychain_token = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_token | egrep '^password'")[-1]
    if (re.search('password\:', keychain_token) != None):
        os.system("security -q delete-generic-password -a {0} -s pyautovpn_token".format(user))

    os.system("security -q add-generic-password -a {0} -s pyautovpn_pass -w {1}".format(user, password))
    os.system("security -q add-generic-password -a {0} -s pyautovpn_token -w {1}".format(user, token))

    print("Password and token added successfully")
