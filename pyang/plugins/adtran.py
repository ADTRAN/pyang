"""ADTRAN usage guidelines plugin
See RFC 6087
"""

import optparse
import sys

from pyang import plugin
from pyang import statements
from pyang import error
from pyang.error import err_add
from pyang.plugins import lint

def pyang_plugin_init():
    plugin.register_plugin(ADTRANPlugin())

class ADTRANPlugin(lint.LintPlugin):
    def __init__(self):
        lint.LintPlugin.__init__(self)
        self.namespace_prefixes = ['http://www.adtran.com/ns/yang/']
        self.modulename_prefixes = ['adtran']
        self.max_line_len = 70

    def add_opts(self, optparser):
        optlist = [
            optparse.make_option("--adtn",
                                 dest="adtn",
                                 action="store_true",
                                 help="Validate the module(s) according to " \
                                 "IETF rules and ADTRAN best practices."),
            ]
        optparser.add_options(optlist)

    def setup_ctx(self, ctx):
        if not ctx.opts.adtn:
            return
        self._setup_ctx(ctx)
