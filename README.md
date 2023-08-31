# novelyst_xx

Language pack for [novelyst](https://peter88213.github.io/novelyst/).

---

## How to install the language pack

1. Download the `novelyst_xx.zip` file.
2. Unpack it and move the `i18n` directory tree to your *novelyst* installation directory. This may be `~/.pywriter/novelyst`. 

---

## How to create/update the language pack

1. Check/edit the entries in the `tools/settings.py` file.
1. Make sure you have got a recent `messages.pot` file for each program.
2. Run the `tools/set_up.py` script to create or update the `xx.po` message catalogs.
3. Edit the `xx.po` message catalogs in the `programs` subfolders.
4. Run the `tools/build_release.py` script to create the zipfile for distribution.


### Editing a message catalog

A "message catalog" is a dictionary for the program's messages and menu entries. The file name is `xx.po`.

Be sure to use a text editor that writes utf-8 encoded text. Otherwise, it may not work with non-ASCII characters used in your language.

The  `xx.po` dictionary is organized as a set of *message ID (msgid)* - *message string (msgstr)* pairs, where *msgid* means the English term, and *msgstr* means the translated term. This is an example for such a pair where the message string is still missing:

```
msgid "Cannot overwrite file"
msgstr ""
```

Just enter all missing message strings. 
- If a message ID contains placeholders like `{}`, be sure to put them also into the message string.  
- If a message ID starts with `!`, the message string must also start with `!`. 


### Advertising a new/updated language pack

You may want to put a posting in the [novelyst forum](https://github.com/peter88213/novelyst/discussions).

---

## License

This is Open Source software, and *novelyt_xx* is licenced under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/novelyst_progress/blob/main/LICENSE) file.

