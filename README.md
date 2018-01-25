This mkdocs plugin allows the use of Jinja2 templates inside Markdown content.

It can be useful, for example, to enumerate pages or use the configuration or site navigation data structures from within content.

Templates should render to HTML.

## Example
```
{% for year in ['2018', '2017'] %}
  <h3>{{ year }}</h3>
  {% for page in pages|sort(attribute='url', reverse=True) %}
    {{ page.title }}
    <br />
  {% endfor %}
{% endfor %}
```




