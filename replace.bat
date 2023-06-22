@echo off
set /p pdf=Enter the name of a PDF file with URLs to be replaced (without .pdf):
python replace.py %pdf%.pdf
echo:
echo URLs in the file %pdf%.pdf have been replaced.
echo:
pause

