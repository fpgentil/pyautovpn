PyAutoVPN
=========

Automatic One-time Password VPN connector for OSX.
It will generate a password concatenating your `stored password` and `one time password`.

## Installation
* Install Pillow dependencies
```
$ brew install libtiff libjpeg webp little-cms2
```

* Install zbarlight
```
$ brew install zbarlight
```

If you have any issues like:
```
#include <zbar.h>
             ^
    1 error generated.
    error: command 'cc' failed with exit status 1
```

* Try this way
```
LDFLAGS=-L/usr/local/lib/ CPATH=/usr/local/include/ pip install zbarlight
```

* Clone the project (since it's not published yet)

```
$ git clone https://github.com/fpgentil/pyautovpn
$ cd pyautovpn
$ pip install .

```


## Usage

* Make sure you have a VPN setup in your OSX
* Grab your QR code for OTP

#### Setup
```
$ python pyautovpn_setup.py --help

Usage: pyautovpn_setup.py [OPTIONS]

Options:
  --password TEXT    Your LDAP password
  --token_path TEXT  Local path of your QR code
  --vpn_name TEXT    Service name of your VPN
  --help             Show this message and exit.
```

#### Connect
```
$ python pyautovpn_connect.py
```

## Contributing

1. Fork it ( https://github.com/fpgentil/pyautovpn/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
