######################################
# 2019.10.18
# Created by SungMin-Kang
# -----------
# Last modified date
# Version 1.0
######################################

# import packages
import PyPDF2
import re
import os
import sys
import subprocess
from PyPDF2 import PdfFileMerger

# 경로지정
path = "./pdf"
file_list = os.listdir(path)
   
merger = PdfFileMerger()

for pdf in file_list:
    merger.append("./pdf/" + pdf)

try:
    if not os.path.exists('./output'):
        os.makedirs('./output')
except OSError:
    print('Error:')

merger.write("./output/merge_result.pdf")
merger.close()