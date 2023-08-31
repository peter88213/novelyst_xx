"""Copy novelyst plugin translation files to novelyst_xx."""
import glob
import os
from shutil import copyfile

ROOT_DIR = '../..'

os.chdir(ROOT_DIR)
for program in glob.iglob('novelyst*', recursive=False):
    potFile = f'{program}/i18n/messages.pot'
    if os.path.isfile(potFile):
        targetPath = f'novelyst_xx/programs/{program}'
        os.makedirs(targetPath, exist_ok=True)
        copyfile(potFile, f'{targetPath}/messages.pot')
        print(program)
print('Done.')
