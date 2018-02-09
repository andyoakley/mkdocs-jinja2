__version__ = '0.1.0'

from mkdocs.plugins import BasePlugin
from jinja2 import Environment
import datetime

def filter_strftime(t, fmt):
    if type(t) is datetime.datetime:
        return t.strftime(fmt)
    else:
        return datetime.datetime.fromtimestamp(t).strftime(fmt)

class JinjaEnvironment(BasePlugin):

    def on_page_content(self, html, page, config, site_navigation):
        env = Environment()
        env.filters['strftime'] = filter_strftime

        return env.from_string(html).render(
                config=config,
                site_navigation=site_navigation,
                pages=site_navigation.pages,
                )

