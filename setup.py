
from distutils.core import setup

setup(
    name='mkdocs-jinja2',
    version='0.1.0',
    author='Andy Oakley',
    author_email='ao@ao.vc',
    packages=['mkdocs_jinja2'],
    license='LICENSE.txt',
    description='Mkdocs plugin to support Jinja2 templates in content files.',
    install_requires=[
    ],

    entry_points={
        'mkdocs.plugins': [
            'jinja2 = mkdocs_jinja2:JinjaEnvironment',
        ]
    }
)

