import commands, re, pyotp, time
from appscript import app

def decode(file_path):
    from PIL import Image
    import zbarlight
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
    return zbarlight.scan_codes('qrcode', image)[0]

def setup(password, token_path, vpn_name):
    user = commands.getstatusoutput("whoami")[-1]

    keychain_pwd = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_pass | egrep '^password'")[-1]
    if (re.search('password\:', keychain_pwd) != None):
        commands.getstatusoutput("security -q delete-generic-password -a {0} -s pyautovpn_pass".format(user))
    commands.getstatusoutput("security -q add-generic-password -a {0} -s pyautovpn_pass -w {1}".format(user, re.escape(password)))

    decoded_token = decode(token_path)
    keychain_token = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_token | egrep '^password'")[-1]
    if (re.search('password\:', keychain_token) != None):
        commands.getstatusoutput("security -q delete-generic-password -a {0} -s pyautovpn_token".format(user))
    commands.getstatusoutput("security -q add-generic-password -a {0} -s pyautovpn_token -w {1}".format(user, re.escape(decoded_token)))

    keychain_name = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_name | egrep '^password'")[-1]
    if (re.search('password\:', keychain_name) != None):
        commands.getstatusoutput("security -q delete-generic-password -a {0} -s pyautovpn_name".format(user))
    commands.getstatusoutput("security -q add-generic-password -a {0} -s pyautovpn_name -w {1}".format(user, re.escape(vpn_name)))

    print("Password,token and VPN name were added/updated successfully")

def connect():
    password = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_pass | egrep '^password'")[-1]
    token = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_token | egrep '^password'")[-1]
    vpn_name = commands.getstatusoutput("security -q find-generic-password -gl pyautovpn_name | egrep '^password'")[-1]
    if (
    (re.search('password\:', password) == None) or
    (re.search('password\:', token) == None) or
    (re.search('password\:', vpn_name) == None)):
        print("Passowrd, token or VPN name not found, use setup() first.")
        return

    password = password.replace("password: ", "")[1:-1]
    token = token.replace("password: ", "")[1:-1]
    vpn_name = vpn_name.replace("password: ", "")[1:-1]

    already_connected = commands.getstatusoutput("scutil --nc status {0} | sed -n 1p".format(re.escape(vpn_name)))[-1]
    if (already_connected == 'Connected'):
        print("VPN already connected")
        return

    totp = pyotp.TOTP(token)
    current_token = totp.now()
    vpn_password = "{0}{1}".format(password, current_token)

    commands.getstatusoutput("scutil --nc start {0}".format(re.escape(vpn_name)))
    time.sleep(2)
    app('System Events').keystroke(re.escape(vpn_password))
    time.sleep(2)
    app('System Events').keystroke('\r')
