#!/usr/bin/env python

import random
import sys


def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 10
    for _ in range(n):
        for _ in range(n):
            c = random.choice(['0', '1'])
            sys.stdout.write(c)
        sys.stdout.write('\n')
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
