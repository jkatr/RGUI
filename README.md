# RGUI for Sublime Text

Modification of randy3k's send code package for sublime text to add features for rgui connection on windows. 

See readme for the original [project](https://github.com/randy3k/SendCode).

Features

- Work with multiple RGUIs (connects to last active rgui).
- Send line (block) of code directly to rgui.
- Run selected code in rgui by sourcing a temp file.
- Run whole (unsaved) script by sourcing a temp file.
- Use clipboard to copy data from/to excel.

### Installation

Install manually by downloading the package copying to corresponding sublime folder. 

### Usage

Select a program using the command `SendCode: Choose Program` in command palette. The default program on macOS, windows and linux are Terminal, Cmder and tmux respectively. Each syntax binds to its own program. For instance, you could bind `R` to r files and `tmux` to python files.

### Default keybindings:

- <kbd>f4</kbd>

    Sets the working directory to current file path. 


- <kbd>f5</kbd>

    Creates a temp file containig the current script, which doesn't have to be saved. The temp file is then sourced in the rgui. 


- <kbd>f6</kbd>

    If text is selected creates a temp file containig the selection. The temp file is then sourced in the rgui. 

- <kbd>f7</kbd>

    If text is selected, it sends the text to the program selected. If no text is selected, then it sends the current line (or block, if found). Finally, it moves the cursor to the next line.

- <kbd>f12</kbd>

    Removes all R objects closes graphics devices.

- <>

### Troubleshooting


1. R Gui on Windows

   Make sure the corresponding R program is opened when you are sending the text.


### Custom Keybindings

It is fairly easy to create your own keybinds for commands which you frequently use. For example, the following keybinds execute changing working directory commands for R, Python and Julia.

```json
[
    {
        "keys": ["ctrl+shift+h"], "command": "send_code",
        "args": {"cmd": "setwd(\"$file_path\")"},
        "context": [
            { "key": "selector", "operator": "equal", "operand": "source.r" }
        ]
    },
    {
        "keys": ["ctrl+shift+h"], "command": "send_code",
        "args": {"cmd": "%cd \"$file_path\""},
        "context": [
            { "key": "selector", "operator": "equal", "operand": "source.python" }
        ]
    },
    {
        "keys": ["ctrl+shift+h"], "command": "send_code",
        "args": {"cmd": "cd(\"$file_path\")"},
        "context": [
            { "key": "selector", "operator": "equal", "operand": "source.julia" }
        ]
    }
]
```

SendCode expands following variables in the `cmd` field:

- `$file`, the full path to the file
- `$file_path`, the directory contains the file
- `$file_name`, the file name
- `$file_base_name`, the file name without extension
- `$file_extension`, the file extension
- `$folder`, the first folder of current window
- `$project_path`, the directory where sublime-project is stored
- `$current_folder`, the folder of the window which contains the current view
- `$selection`, the text selected, or the word under cursor
- `$line`, the current line number

It also supports placeholders for variables, details can be found in the [unofficial documentation](http://docs.sublimetext.info/en/latest/reference/build_systems/configuration.html#placeholders-for-variables).

```
${file_path:$folder}
```
This will emit the directory of current file if there is one, otherwise the first folder of the current window.

You also don't have to worry about escaping quotes and backslashes between quotes, SendCode will
handle them for you.

The `prog` argument determines which program to use

```json
[
    {
        "keys": ["ctrl+shift+enter"], "command": "send_code",
        "args": {"cmd": "\n", "prog": "tmux"}
    }
]
```

### User settings

A couple of settings can be found `Preferences: SendCode Settings`.
Project-wise settings could also be specified in `sublime-project` as

```js
{
    "settings": {
        "SendCode": {
            "prog": "terminus",
            "r" : {
                "bracketed_paste_mode": true
            }
        }
    }
}
```


