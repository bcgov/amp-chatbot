#!/bin/bash

# Dependencies:
#   1. gitbash
#   2. Global installations of Python
set -e

PWD=$(pwd)
INI=~/.cdw

# change to root of script directory
cd "${0%/*}"

# setup.env can specify dependency Paths or can be empty
source ./setup.env
# PYTHON_BIN=${CDW_PY_VERSION:-"python"}
PYTHON_BIN=$CDW_PY_VERSION

type -P "$PYTHON_BIN" &>/dev/null || PYTHON_BIN='/c/Program Files/Python/Python312/python.exe'
type -P "$PYTHON_BIN" &>/dev/null || PYTHON_BIN='/c/Program Files/Python/Python312/python.exe'

# Create the Python3 virtual environment
"$PYTHON_BIN" -m venv --system-site-packages  ./env || "$PYTHON_BIN" -m virtualenv --system-site-packages  ./env

BINDIR="env/bin"
SUBDIR="bin"
# Windows virtual environments use Scripts vs. bin directory
if [[ -n "$WINDIR" ]]; then
    BINDIR="env/Scripts"
    SUBDIR="Scripts"
fi

# on Windows the python file was overwriting the .exe (seemed to add the .exe by default)
if [[ -n "$WINDIR" ]]; then
    mv "$BINDIR/python.exe" "$BINDIR/python.exe.bkp"

cat <<EOT | tee "$BINDIR/python"
#!/bin/bash

if [ \$# -eq 0 ]; then
    "\${0%/*}/python.exe" -i
else
    "\${0%/*}/python.exe" "\$@"
fi
EOT

    mv "$BINDIR/python.exe.bkp" "$BINDIR/python.exe"
fi


# Setup the Python dependencies
$BINDIR/python -m pip install --upgrade pip
$BINDIR/python -m pip install -r requirements.txt

if ! [ -d ".git" ]
then
    # Setup the workspace as a git repository if it was not cloned
    git init --initial-branch=main .
fi

if ! [ -d ".vscode" ]
then
# Setup the vscode workspace if necessary
mkdir -p ".vscode"
cat <<EOT | tee .vscode/settings.json
{
    "python.pythonPath": "env/$SUBDIR/python",
    "python.languageServer": "Pylance",
    "pylint.interpreter": ["./env/$SUBDIR/python"],
    "pylint.path": ["pylint"],
    "pylint.args": ["--rcfile=./setup.cfg"],
    "pylint.ignorePatterns": ["*/env/Lib/*"]
}
EOT
fi

ls "$INI" &>/dev/null || touch "$INI"

cd "$PWD"
