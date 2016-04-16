python-links-from-link-header
#############################

This Python module contains only one function: ``extract``.

It extracts links and their relations from a Link Header Field [1]_ and
returns a dict where the keys are the relations and the values are the
links themselves.

.. [1] https://www.w3.org/wiki/LinkHeader and http://www.rfc-editor.org/rfc/rfc5988.txt

Installation
************

::

    pip install links-from-link-header

Usage
*****

::
    
    >>> import links_from_header

    >>> header = '<https://api.github.com/user/repos?page=1>; rel="first", <https://api.github.com/user/repos?page=9>; rel="prev", <https://api.github.com/user/repos?page=11>; rel="next", <https://api.github.com/user/repos?page=50>; rel="last"'

    >>> links_from_header.extract(header)
    {
        'first': 'https://api.github.com/user/repos?page=1',
        'prev': 'https://api.github.com/user/repos?page=9',
        'next': 'https://api.github.com/user/repos?page=11',
        'last': 'https://api.github.com/user/repos?page=50',
    }
