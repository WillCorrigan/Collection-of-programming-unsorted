import os, PyPDF2, re, tika, time
from tika import parser

def split_pdf_pages(root_directory, extract_to_folder):
	for root, dirs, files in os.walk(root_directory):
		for filename in files:
			basename, extension = os.path.splitext(filename)
			
			if extension == ".pdf":
				fullpath = root + "\\" + basename + extension
				pdf_file_name = open(fullpath, "rb")
    			opened_pdf = PyPDF2.PdfFileReader(pdf_file_name)

    			for i in range(0, opened_pdf.numPages):
    				pageObj = pdfReader.getPage(i)
    				pdfWriter.addPage(pageObj)


    				foldername = extract_to_folder + "\\" + basename + "-{}.pdf".format(i+1)
    				output = open(foldername, "wb")
				    pdfWriter.write(output)
				    pdf_file_name.close()


root_dir = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs"
extract_to = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs\extracted"
rename_to = r"C:\Users\wcorr\OneDrive\Desktop\testpdfs\renamed"

split_pdf_pages(root_dir, extract_to)