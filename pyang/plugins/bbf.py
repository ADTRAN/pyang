"""BBF usage guidelines plugin
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
    plugin.register_plugin(BBFPlugin())

class BBFPlugin(lint.LintPlugin):
    def __init__(self):
        lint.LintPlugin.__init__(self)
        self.namespace_prefixes = ['urn:broadband-forum-org:yang:']
        self.modulename_prefixes = ['bbf']
        self.max_line_len = 70

    def add_opts(self, optparser):
        optlist = [
            optparse.make_option("--bbf",
                                 dest="bbf",
                                 action="store_true",
                                 help="Validate the module(s) according to " \
                                 "IETF rules and BBF best practices."),
            ]
        optparser.add_options(optlist)

    def setup_ctx(self, ctx):
        if not ctx.opts.bbf:
            return
        self._setup_ctx(ctx)
