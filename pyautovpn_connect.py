import click
import pyautovpn

@click.command()
def connect():
    pyautovpn.connect()

if __name__ == '__main__':
    connect()
