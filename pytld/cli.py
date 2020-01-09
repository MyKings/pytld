#!/usr/bin/env python
# coding: utf-8
# author: MyKings

import sys

from pytld import get_fld


def main():
    if len(sys.argv) >= 2:
        url_or_domain = sys.argv[1]
    else:
        url_or_domain = 'http://www.example.com'

    print(get_fld(url_or_domain))

if __name__ == '__main__':
    main()
