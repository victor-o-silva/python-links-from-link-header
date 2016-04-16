import re


def extract(link_header):
    """Extract links and their relations from a Link Header Field."""
    links = [l.strip() for l in link_header.split(',')]
    rels = {}
    pattern = r'<(?P<url>.*)>;\s*rel="(?P<rel>.*)"'
    for link in links:
        group_dict = re.match(pattern, link).groupdict()
        rels[group_dict['rel']] = group_dict['url']
    return rels
