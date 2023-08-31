"""Build a novelyst language pack.

- Generate the language specific '*.mo' dictionaries for novelyst and its plugins.
- Create a zipfile for distribution.

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from shutil import copyfile
import msgfmt
import zipfile
from settings import *
import set_up


def main():
    print(f'Build a novelyst language pack for {languageName}.')

    # Check whether tranlsations are complete.
    if not set_up.main():
        print('PROGRAM ABORTED. Please complete translations.')
        return False

    # Create the target path.
    i18Path = f'../i18n/locale/{languageCode}/LC_MESSAGES'
    os.makedirs(i18Path, exist_ok=True)
    distPath = f'../novelyst_{languageCode}.zip'
    moFiles = []

    # Create binary message catalogs.
    for programName in os.listdir('../programs'):
        poPath = f'../programs/{programName}/{languageCode}.po'
        if programName == 'novelyst':
            moName = 'pywriter.mo'
        else:
            moName = f'{programName}.mo'
        moPath = f'{i18Path}/{moName}'
        print(f'Writing "{moPath}" ...')
        msgfmt.make(poPath, moPath)
        moFiles.append(moPath)

    # Create the release package.
    print(f'Writing "{distPath}" ...')
    with zipfile.ZipFile(distPath, 'w') as release:
        os.chdir('../i18n')
        for file in moFiles:
            release.write(file, compress_type=zipfile.ZIP_DEFLATED)

    print('Done.')
    return True


if __name__ == '__main__':
    main()
