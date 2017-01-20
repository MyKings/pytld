# pytld

Refer to `http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1`. The top-level domain analysis of the URL or domain name.

## Installation

```bash
$ pip install pytld
```

## Usage example

It can be from the URL or domain name analysis top-level domain:

```python
from pytld import get_tld
from pytld import get_full_domain
from pytld import get_hostname


def test_get_tld():
    assert get_tld('team.develop.google.hk.', strict=False) == 'develop.google.hk'
    assert get_tld('team.develop.google.hk.') == 'google.hk'
    assert get_tld('google.hk.') == 'google.hk'
    assert get_tld('http://www.example.com:8080/admin.php/afaf?13123') == 'example.com'
    assert get_tld('www.google.com') == 'google.com'
    assert get_tld('mail.google.com.hk') == 'google.com.hk'
    assert get_tld('apps.google.com.hk.') == 'google.com.hk'
    assert get_tld('blog.google.hk.') == 'google.hk'


def test_get_full_domain():
    assert get_full_domain('http://www.example.com.cn:8080/admin.php/afaf?13123') == 'www.example.com.cn'


def test_get_hostname():
    assert get_hostname('http://www.example.com.cn:8080/admin.php/afaf?13123') == 'www'

```

## License

MPL 1.1/GPL 2.0/LGPL 2.1

## Support

For any issues contact me at the e-mail given in the `Author` section.

## Author

mykings <xsseroot@gmail.com>
