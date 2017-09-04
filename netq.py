#!/usr/bin/env python
import sys
import re
import time
import base64
import urllib.request

DATA = 'aHR0cDovL3BpLmt1LmFjLnRo'
URL = base64.b64decode(DATA).decode('utf8')
DELAY = 1

white = '\033[1;37m'
reset = '\033[0m'


def print_quota(quota):
    remain = float(quota.split()[0])
    unit = quota.split()[1].strip()

    if remain > 5 and unit == 'GB':
        color = '\033[1;32m'
    elif remain > 1 and unit == 'GB':
        color = '\033[1;33m'
    else:
        color = '\033[1;31m'

    sys.stdout.write("\r{}Remain Quota{}{} {}{}".format(
        white, reset, color, quota, reset))


def print_exceed(exceed_quota):
    color = '\033[1;31m'
    sys.stdout.write('\r{}Exceed {}{}'.format(color, exceed_quota, reset))


def main():
    sys.stdout.write("From {}\n".format(URL))
    while 1:
        res = urllib.request.urlopen(URL).read()

        pattern = b"<span style='font-size: 20px'>(.*)</span>"
        result = re.search(pattern, res)

        if result:
            quota = result.group(1).decode("utf8")
            print_quota(quota)
        else:
            pattern = b"<span style='color: red; font-size: 20px'>(.*)</span>"
            result = re.search(pattern, res)
            if result:
                exceed_quota = result.group(1).decode("utf8")
                print_exceed(exceed_quota)
            else:
                sys.stdout.write("\rPlease Login!!!\n")
                sys.exit()

        time.sleep(DELAY)
        sys.stdout.write('\033[2K\033[1G')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\nexit\n")
