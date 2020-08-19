import os, platform

VERSION = '1.3.10'
BASE_URL = 'https://login.weixin.qq.com'
OS = platform.system() # Windows, Linux, Darwin
DIR = os.getcwd()
DEFAULT_QR = 'QR.png'
TIMEOUT = (10, 60)

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
