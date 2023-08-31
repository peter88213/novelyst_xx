# novelyst_xx

Language pack for [novelyst](https://peter88213.github.io/novelyst/).

# How to install the language pack

1. Download the `novelyst_xx.zip` file.
2. Unpack it and move the `i18n` directory tree to your *novelyst* installation directory. This may be `~/.pywriter/novelyst`. 


# How to create/update the language pack

1. Check/edit the entries in the `tools/settings.py` file.
1. Make sure you have got a recent `messages.pot` file for each program.
2. Run the `tools/set_up.py` script to create or update the `xx.po` dictionaries.
3. Edit the `xx.po` dictionaries in the `programs` subfolders.
4. Run the `tools/build_release.py` script to create the zipfile for distribution.


## License

This is Open Source software, and *novelyt_xx* is licenced under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/novelyst_progress/blob/main/LICENSE) file.

