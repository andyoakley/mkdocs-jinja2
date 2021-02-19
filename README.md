# mkdocs-jinja2

This mkdocs plugin allows the use of [Jinja2 templates](https://jinja2docs.readthedocs.io/) inside Markdown content.

It can be useful, for example, to enumerate pages or use the configuration or site navigation data structures from within content.

Templates should render to HTML.

## Example

```jinja2
{% for year in ['2018', '2017'] %}
  <h3>{{ year }}</h3>
  {% for page in pages|sort(attribute='url', reverse=True) %}
    {{ page.title }}
    <br />
  {% endfor %}
{% endfor %}
```
