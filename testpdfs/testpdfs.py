# import the neccessary modules
import os, PyPDF2, re, tika, time
from tika import parser

# function to extract the individual pages from each pdf found
def split_pdf_pages(root_directory, extract_to_folder):
 # traverse down through the root directory to sub-directories
 for root, dirs, files in os.walk(root_directory):
  for filename in files:
   basename, extension = os.path.splitext(filename)
   # if a file is a pdf
   if extension == ".pdf":
    # create a reference to the full filename path
    fullpath = root + "\\" + basename + extension

    # open the pdf in read mode
    pdf_file_name = open(fullpath, "rb")
    opened_pdf = PyPDF2.PdfFileReader(pdf_file_name)

    # for each page in the pdf
    for i in range(0, opened_pdf.numPages):
      pageObj = pdfReader.getPage(i)
      pdfWriter.addPage(pageObj)

    # write the page to a new pdf


     output = PyPDF2.PdfFileWriter()
     output.addPage(opened_pdf.getPage(i))
     with open(extract_to_folder + "\\" + basename + "-{}.pdf".format(i+1), "wb") as output_pdf:
      output.write(output_pdf)
      pdf_file_name.close()

# function for renaming the single page pdfs based on text in the pdf
def rename_pdfs(extraced_pdf_folder, rename_folder):
 # traverse down through the root directory to sub-directories
 for root, dirs, files in os.walk(extraced_pdf_folder):
  for filename in files:
    print(filename)
   # basename, extension = os.path.splitext(filename)
   # # if a file is a pdf
   # if extension == ".pdf":
   #  # create a reference to the full filename path
   #  fullpath = root + "\\" + basename + extension

   #  raw = parser.from_file(fullpath)
   #  pdf_text = (raw['content'].encode('utf-8'))
    # print(pdf_text)
    # doc_ext = re.findall(r'[A-Z],\s\d\d\d\d|.\d',pdf_text)[-1]
    # os.rename(fullpath, rename_folder + "\\" + doc_ext + ".pdf")

# parameter variables
root_dir = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs"
extract_to = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs\extracted"
rename_to = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs\renamed"

# use the two functions
split_pdf_pages(root_dir, extract_to)
# rename_pdfs(extract_to, rename_to)