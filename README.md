# RarDec

v0.1a

## About
A Rar decompressor working in Bash command line
## How to use it 
On Bash Line Command:
- Go to the directory where your archive rar is it
- write the following command _(start with python or python3, depending on your version)_ and pass in argument the file that you want unpacked

```python3 RarDec.py your_file.rar``` 

And then all your file will be extracted 

## Note
- You needs to install rarfile module _(with ```pip install rarfile```)_ but i have implemented in the script the possility to install rarfile, just follow the instructions
- You can only unpacked just one file at a time (one file in argument)
- The script working only with file .rar (no support zip, but it's coming soon)
