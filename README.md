# rgui for Sublime Text

Send code from Sublime Text to rgui on Windows. Adapted from randy3k's [SendCode](https://github.com/randy3k/SendCode) Sublime Package.

Features

- Work with multiple rgui's. Code will be sent to the last active rgui.
- Send code as text directly to the rgui console or source a temp file containing selected code (sourcig a temp file is helpful when repeatedly running selected parts of a R-script in the rgui).
- Send code from unsaved file (helpful for quick debugs).
- Work with clipboard within rgui (helpful for quick data transfers, e.g. from Excel)

### Installation


### Usage

Default keybindings:

- <kbd>f4</kbd>

    If text is selected, it sends the text to the program selected. If no text is selected, then it sends the current block (if found). Finally, it moves the cursor to the next line.

- <kbd>f5</kbd>

    Sources the whole (unsaved) script as a temp file. Equivalent to select all and <kbd>f6</kbd> (see below).

- <kbd>f6</kbd>

    Sources the selected text as a temp file. 

- <kbd>f7</kbd>

    If text is selected, sends the text the rgui. If no text is selected, then it sends the current line (or block). Finally, it moves the cursor to the next line.

### Troubleshooting


1. R Gui on Windows

   Make sure the corresponding R program is opened when you are sending the text.

