from setuptools import setup

setup(name='pyautovpn',
      version='0.1',
      description='Automatic One-time Password VPN connector for OSX',
      url='http://github.com/fpgenitl/pyautovpn',
      author='Felipe Gentil',
      author_email='cdigentil@gmail.com',
      license='MIT',
      packages=['pyautovpn'],
      install_requires=['pyotp','appscript'],
      zip_safe=False)
