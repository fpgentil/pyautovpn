import click
import pyautovpn

@click.command()
@click.option('--password', help='Your LDAP password')
@click.option('--token_path', help='Local path of your QR code')
@click.option('--vpn_name', help='Service name of your VPN')
def setup(password, token_path, vpn_name):
    pyautovpn.setup(password, token_path, vpn_name)

if __name__ == '__main__':
    setup()
