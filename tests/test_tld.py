#!/usr/bin/env python
# coding: utf-8

from pytld import get_full_domain
from pytld import get_hostname
from pytld import get_fld


# tld
assert get_fld('team.develop.google.hk.', strict=False) == 'develop.google.hk'
assert get_fld('team.develop.google.hk.') == 'google.hk'
assert get_fld('google.hk.') == 'google.hk'
assert get_fld('http://www.example.com:8080/admin.php/afaf?13123') == 'example.com'
assert get_fld('www.google.com') == 'google.com'
assert get_fld('mail.google.com.hk') == 'google.com.hk'
assert get_fld('apps.google.com.hk.') == 'google.com.hk'
assert get_fld('blog.google.hk.') == 'google.hk'

assert get_fld("*.test.com.cn") == "test.com.cn"

assert get_full_domain('http://www.example.com.cn:8080/admin.php/afaf?13123') == 'www.example.com.cn'
assert get_hostname('http://www.example.com.cn:8080/admin.php/afaf?13123') == 'www'
