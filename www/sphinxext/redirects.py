"""
Parse .htaccess RewriteRules and output HTML <meta> redirects
"""

from __future__ import division, absolute_import, print_function

import re


def setup(app):
    app.connect('html-collect-pages', html_collect_pages)
    return {'version': '0.1'}


def html_collect_pages(app):
    pages = parse_htaccess('.htaccess')
    collection = [(page, dict(dst=dst), 'redirectpage.html') for page, dst in pages]
    app.info("Redirects from .htaccess:\n{}".format(
        "\n".join("    {} -> {}".format(page, dst) for page, dst in pages)))
    return collection


def parse_htaccess(filename):
    """
    Not a full htaccess parser, but deals with the relevant subset
    """
    with open(filename, 'r') as f:
        text = f.read()

    redirects = []

    for line in text.splitlines():
        line = line.strip()
        if line.startswith('#') or not line:
            continue

        m = re.match('^RewriteRule\s+(.+?)\s+(.+?)\s*(\[.+\])?\s*$', line)
        if m:
            src = m.group(1)
            dst = m.group(2)
            redirects.append((src, dst))
            continue

    # Convert redirects to pages
    pages = []

    for src, dst in redirects:
        src = src.lstrip('^').lstrip('(').rstrip(')')
        parts = src.split('|')

        for part in parts:
            name = part.strip().strip('/') + '/index'
            pages.append((name, dst))

    return pages
