from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
  
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# PDF PATH 
PDF_file = (r"C:\Users\barot\OneDrive\Desktop\courses\python courses\OCR\bhartiya\bnew.pdf")
 
  
# Store all the pages of the PDF in a variable 
pages = convert_from_path(PDF_file, 500) 
 
image_counter = 1
  
for page in pages: 
  
    # Open PDF and convert page 1 to page_1.jpg 
    # Open PDF and convert page 2 to page_2.jpg 
    filename = "page_"+str(image_counter)+".jpg"


    # Save the images
    page.save(filename, 'JPEG') 
    image_counter = image_counter + 1
  
 
filelimit = image_counter-1
  
# Output TXT file
outfile = (r"C:\Users\barot\OneDrive\Desktop\courses\python courses\OCR\bhartiya\new.txt")
 
f = open(outfile, "a") 
  
for i in range(1, filelimit + 1): 
  
    # convert page_1.jpg to txt and save 
    # convert page_2.jpg to txt and save
    filename = "page_"+str(i)+".jpg"
          
    # Recognize the text in image using pytesserct 
    # chnage lang='hin' to any other language to like to convert supported by pytesseract.
    text = str(((pytesseract.image_to_string(Image.open(filename),lang='hin')))) 
    text = text.replace('\n', '')     
    f.write(text) 
   
f.close() 
