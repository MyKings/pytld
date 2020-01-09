#!/usr/bin/env python
# coding: utf-8
# author: MyKings

import os

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


__all__ = [
    'get_fld', 'get_hostname', 'get_full_domain'
]

domains_tlds = []

def get_fld(domain_or_url, strict=True):
    """

    :param domain_or_url:
    :param strict: country-code Priority
                   eg:
                     True: www.google.hk. - google.hk
                     False: www.google.hk. - www.google.hk
    :return:
    """
    result = ''
    if domain_or_url:
        domain = str(domain_or_url).lower()
        if domain.startswith('http'):
            result = _fld_by_url(domain, strict)
        else:
            result = _fld_by_domain(domain, strict)

    return result


def get_full_domain(url):
    """
    Through the url to get a complete domain name
    :param url:
    :return:
    """
    result = url
    if result.startswith('http'):
        result = urlparse.urlparse(url).netloc.split(':', 1)[0]
    return result


def get_hostname(domain_or_url):
    """

    :param domain_or_url:
    :return:
    """
    _tld_name = get_fld(domain_or_url)
    _full_domain_name = get_full_domain(domain_or_url)
    result = None
    if _tld_name and _full_domain_name:
        result = _full_domain_name.replace(_tld_name, '')
        if result.endswith('.'):
            result = result[:-1]

    return result


def _init_domains_zone():
    """
    initialization domains zone
    https://data.iana.org/TLD/tlds-alpha-by-domain.txt
    """
    root_path = os.path.dirname(os.path.realpath(__file__))
    global domains_tlds
    with open(os.path.join(root_path, 'effective_tld_names.dat.txt'), 'rb') as fp:
        for line in fp:
            if line.decode('utf-8').strip() and not line.decode('utf-8').startswith('//'):
                domains_tlds.append(line.strip())
        domains_tlds = set(domains_tlds)


def _fld_by_domain(domain, strict):
    """

    :param domain:
    :param strict:
    :return:
    """
    result = ''

    if domain.endswith('.'):
        domain = domain[:-1]

    domain_fragment = domain.split('.')

    if len(domain_fragment) == 2:
        first_block = domain_fragment[-1]
        second_block = domain_fragment[-2]
        third_block = None
    elif len(domain_fragment) >= 3:
        first_block = domain_fragment[-1]
        second_block = domain_fragment[-2]
        third_block = domain_fragment[-3]
    else:
        first_block = None
        second_block = None
        third_block = None

    ntld = '%s.%s' % (second_block, first_block)

    # www.google.com.hk -> .com.hk
    if ntld in domains_tlds:
        if third_block:
            result = '%s.%s' % (third_block, ntld)
        else:
            result = ntld
        return result

    # www.google.hk -> .hk
    if first_block in domains_tlds:
        result = '.%s' % first_block
        if strict:
            return '%s.%s' % (second_block, first_block)

    # www.google.hk -> .google.hk
    if second_block in domains_tlds:
        result = '%s%s' % (second_block, result)
    else:
        result = '%s.%s' % (second_block, first_block)

    # Google is the top-level domain
    # www.it.google.hk -> .it.google.hk
    if third_block and second_block in domains_tlds:
       result = '%s.%s' % (third_block, result)

    return result


def _fld_by_url(url, strict):
    """

    :param url:
    :return:
    """
    domain_name = urlparse.urlparse(url).netloc.split(":", 1)[0]
    return _fld_by_domain(domain_name, strict)

_init_domains_zone()
