import PyPDF2
import os
from os import listdir
from os.path import isfile, join
from PyPDF2.utils import PdfReadError
from pathlib import Path

pdf_folder = r'e:\electric\pdfs\photos'
invalid_pdf_folder = r'e:\electric\pdfs\invalid'

all_files = [f for f in listdir(pdf_folder) if isfile(join(pdf_folder, f))]
print(all_files)


def is_valid(d_file):
    try:
        PyPDF2.PdfFileReader(open(d_file, "rb"))
    except (PdfReadError, OSError):
        return False
    else:
        return True


for file in all_files:
    if is_valid(os.path.join(pdf_folder, file)) is False:
        print(f'file: {os.path.join(pdf_folder, file)} is INVALID')
        Path(os.path.join(pdf_folder, file)).rename(os.path.join(invalid_pdf_folder, file))
    else:
        print(f'file: {os.path.join(pdf_folder, file)} is valid')
