# ImgtoCsv
### Convert Tables from image format from pdf or any image format and save them as .csv
### it uses [Pytesseract](https://github.com/tesseract-ocr/tesseract/releases) and [poppler](https://github.com/oschwartz10612/poppler-windows/releases/) download them from the embedded link
### You can set /bin/ in poppler to path variable or give it as argument to path in main.py
```python
path=r"poppler-20.12.1\Library\bin"
```
### give the path of tesseract executable to
```python
pytesseract.pytesseract.tesseract_cmd = r'D:\tess\tesseract'
```

run by 
```python
python main.py --IPFILE "INPUT FILE CAN BE PDF OR ANY IMAGE FORMAT" --OPFILE "NAME OF OUTPUTFILE"
```
