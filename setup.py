# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stltest']

package_data = \
{'': ['*']}

install_requires = \
['PyAutoGUI>=0.9.53,<0.10.0',
 'dash>=2.6.1,<3.0.0',
 'dataset>=1.5.2,<2.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'mimesis>=6.0.0,<7.0.0',
 'numpy>=1.23.1,<2.0.0',
 'plotly>=5.9.0,<6.0.0',
 'pytest>=7.1.2,<8.0.0',
 'scipy>=1.9.0,<2.0.0',
 'streamlit>=1.11.1,<2.0.0']

setup_kwargs = {
    'name': 'stltest',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'LasIonfuNans',
    'author_email': 'lasionfunans@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
