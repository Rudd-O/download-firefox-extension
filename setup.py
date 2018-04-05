#!/usr/bin/env python

from setuptools import setup
import os

dir = os.path.dirname(__file__)
path_to_main_file = os.path.join(dir, "bin/download-firefox-extension")
path_to_readme = os.path.join(dir, "README.md")
for line in open(path_to_main_file):
	if line.startswith('__version__'):
		version = line.split()[-1].strip("'").strip('"')
		break
else:
	raise ValueError, '"__version__" not found in ' + path_to_main_file
readme = open(path_to_readme).read(-1)

classifiers = [
'Development Status :: 3 - Alpha',
'Environment :: Console',
'Intended Audience :: End Users/Desktop',
'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
'Operating System :: POSIX :: Linux',
'Programming Language :: Python :: 2 :: Only',
'Programming Language :: Python :: 2.7',
]

setup(
	name='download-firefox-extension',
	version=version,
	description='A helper to download Firefox extensions without the browser',
	long_description = readme,
	author='Manuel Amador (Rudd-O)',
	author_email='rudd-o@rudd-o.com',
	license="GPLv2+",
	url='http://github.com/Rudd-O/download-firefox-extension',
	classifiers = classifiers,
	scripts=["bin/download-firefox-extension"],
	keywords="firefox downloader extensions",
	requires=["mechanize", "beautifulsoup4"],
	zip_safe=False,
)
