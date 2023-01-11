# sup

CLI mnemonic tool to search and remember commands. Creates a local file for storing the commands and also backs it up over git.

## Installation

To install it, use pip

```bash
pip install sup
```

## Usage

* adding commands to remember

```bash
sup --add tmux movew -r --description renumber tmux windows
```

* searching commands

```bash
sup --search renumber tmux windows
```
