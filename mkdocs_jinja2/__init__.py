__version__ = '0.1.0'

import mkdocs.config
from mkdocs.plugins import BasePlugin
from jinja2 import Environment
import datetime

import mkdocs_jinja2.cleaner

def filter_strftime(t, fmt):
    if type(t) is datetime.datetime:
        return t.strftime(fmt)
    else:
        return datetime.datetime.fromtimestamp(t).strftime(fmt)

class JinjaEnvironment(BasePlugin):

    def on_nav(self, nav, config, files):
        self.nav = nav

    def on_page_content(self, html, page, config, files):
        env = Environment()
        env.filters['strftime'] = filter_strftime

        return env.from_string(cleaner.clean(html)).render(
                config=config,
                nav=self.nav,
                files=files
                )

