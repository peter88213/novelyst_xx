"""Generate translation files for GNU gettext.

- Generate the language specific '*.mo' dictionaries for novelyst and its plugins.

Usage: 
build.py

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst_xx
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
from shutil import copyfile
import msgfmt

LANGUAGE_CODE = 'xx'

PROJECTS = (
    'pywriter',
    )


def main(version='unknown'):

    # Create binary message catalogs.
    for moName in PROJECTS:
        poPath = f'../i18n/{moName}.po'
        moPath = f'../i18n/locale/{LANGUAGE_CODE}/LC_MESSAGES/{moName}.mo'
        print(f'Writing "{moPath}" ...')
        msgfmt.make(poPath, moPath)

    # Create the release package.


if __name__ == '__main__':
    main()
