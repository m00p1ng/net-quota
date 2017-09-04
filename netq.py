#!/usr/bin/env python
import sys
import re
import time
import urllib.request

URL = 'http://pi.ku.ac.th'
DELAY = 10


def print_quota(quota):
    remain = float(quota.split()[0])
    unit = quota.split()[1]
    reset = '\033[0m'

    if remain > 5 and unit is 'GB':
        color = '\033[1;32m'
    elif remain > 1 and unit is 'GB':
        color = '\033[1;33m'
    else:
        color = '\033[1;31m'

    sys.stdout.write("\r{}Remain Quota {}{}".format(color, quota, reset))


def main():
    sys.stdout.write("From {}\n".format(URL))
    while 1:
        res = urllib.request.urlopen(URL)

        result = re.search(
            b"<span style='font-size: 20px'>(.*)</span>", res.read())

        if not result:
            sys.stdout.write("\rPlease Login!!!")
            break

        quota = result.group(1).decode("utf8")

        print_quota(quota)
        time.sleep(DELAY)
        sys.stdout.flush()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\nexit")
