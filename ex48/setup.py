try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 48',
	'author': 'Craige McWhirter',
	'url': 'URL to get at it',
	'download_url': 'Where to download it.',
	'author_email': 'craige@mcwhirter.com.au',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48'
}

setup(**config)
