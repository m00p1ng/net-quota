import sys
import re
import time
import urllib.request

url = 'http://pi.ku.ac.th'
DELAY = 10


def print_quota(quota):
    remain = float(quota.split()[0])
    reset = '\033[0m'

    if remain > 5:
        color = '\033[1;32m'
    elif remain > 3:
        color = '\033[1;33m'
    else:
        color = '\033[1;31m'

    sys.stdout.write("\r{}Remain Quota {}{}".format(color, quota, reset))


def main():
    sys.stdout.write("From {}\n".format(url))
    while 1:
        res = urllib.request.urlopen(url)

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
    main()
