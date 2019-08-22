import re

def clean(html):
#    regex = re.compile(r".*<script.*(\{\{).*<\/script.*", re.MULTILINE)
#    s = re.sub(regex, "foo", html)
    if '<script' in html:
        return html.replace('{{', '{ {').replace('}}', '} }')
    else:
        return html