"""Set up translations for the novelyst language pack.

- Generate the language specific '*.po' dictionaries for novelyst and its plugins.

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from settings import *
import translations


def main():
    print(f'Set up novelyst translation files for {languageName}.')

    translationsComplete = True
    for programName in os.listdir('../programs'):
        poPath = f'../programs/{programName}'
        if not translations.main(poPath, app=programName):
            translationsComplete = False
    return translationsComplete


if __name__ == '__main__':
    main()
