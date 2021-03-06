# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django import template


def addtoblock(parser, token):
    """
    This is just a sekizai addtoblock stub, for compatibility reasons
    """
    parser.parse(('endaddtoblock',))
    parser.delete_first_token()
    return StubNode()


class StubNode(template.Node):
    """
    This is just a sekizai addtoblock stub, for compatibility reasons
    """
    def render(self, context):
        return ''
