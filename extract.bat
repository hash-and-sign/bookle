@echo off
set /p pdf=Enter the name of a PDF file to extract URLs from (without .pdf):
python extract.py %pdf%.pdf
echo:
echo A sorted, unique list of URLs has been stored in urls.txt.
echo:
pause

