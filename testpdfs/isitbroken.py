import os, PyPDF2, re, tika, time
from tika import parser


def split_pdf_pages(root_directory, extract_to_folder):
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            basename, extension = os.path.splitext(filename)


            if extension == ".pdf":
                fullpath = root + "\\" + basename + extension
                pdfFileObj = open(fullpath, "rb")
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)




                for page in range(0, pdfReader.numPages+1):
                    pdfWriter = PyPDF2.PdfFileWriter()
                    print(page)
                    pageObj = pdfReader.getPage(page)

                    outputpdf = extract_to_folder + "\\" + basename + "-{}.pdf".format(page+1)
                    pdfWriter.addPage(pageObj)

                    with open(outputpdf, "wb") as f:

                        pdfWriter.write(f)
                        
                pdfFileObj.close()


root_dir = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs"
extract_to = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs\extracted"
rename_to = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs\renamed"

split_pdf_pages(root_dir, extract_to)