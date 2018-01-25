__version__ = '0.1.0'

from mkdocs.plugins import BasePlugin
from jinja2 import Environment

class JinjaEnvironment(BasePlugin):

    def on_page_content(self, html, page, config, site_navigation):
        return Environment().from_string(html).render(
                config=config,
                site_navigation=site_navigation,
                pages=site_navigation.pages
                )

