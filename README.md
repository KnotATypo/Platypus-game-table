# Platypus game table

Program to display a machine's table from James Harland's Platypus Game in COSC1107.

## Running

It is recommended to create a Python virtual environment to run this project. Click here to [learn more.](https://docs.python.org/3/tutorial/venv.html)

Create and activate virtual environment:

---
### Unix or MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```
### Windows
```bash
python3 -m venv venv
venv\bin\activate.bat
```
---
Install requirements:
```bash
pip install -r requirements.txt
```
Run program:
```bash
python3 main.py
```
You will be prompted with `Insert machine string: `. The string is expected to be in the same format as: `platypus(169217875, [t(y,k,g,w,wa),t(g,k,y,p,gg),t(y,e,g,k,wa),t(g,e,y,k,gg),t(y,w,y,e,gg),t(g,w,y,p,wa),t(y,p,y,w,gg)]).`

Note that on some machines may need to use `python` instead of `python3`.