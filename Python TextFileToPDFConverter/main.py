from fpdf import FPDF
import glob
from pathlib import Path

# Creating the List of the text filepaths:
# This will retrieve the List of the Filepaths:
# ['files/file1.txt', 'files/file2.txt', 'files/file3.txt']
filepaths = glob.glob("files/*.txt")
# Create 1 PDF file, you are only creating 1 PDF file here
# This is created OUTSIDE of the for loop, and hence only 1 pdf file is created
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Going through each of the text files:
for filepath in filepaths:
    # Add the page to the PDF document for each text file
    pdf.add_page()

    # Getting the filename without the extension
    # and convert it to the title case(Eg. Cat)
    filename = Path(filepath).stem
    # This will convert the first letter to the Uppercase
    name = filename.capitalize()

    # Adding the name of the PDF:
    pdf.set_font(family='Times', size=30, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

    # Getting the content of the file
    with open(filepath, "r") as file:
        content = file.read()
    # Adding the text file Content to the pdf:
    pdf.set_font(family="Times", size=12)
    # 0 basically mean it will expand to the entire
    # width of the pdf browser
    # When you increased the height, the height between each
    # line will basically increased accordingly for the line height
    # txt is the argument which is the content of the value
    pdf.multi_cell(w=0, h=8, txt=content)

# Produce the pdf
# This is created OUTSIDE of the for loop, hence only 1 'Output.pdf' is created.
pdf.output('FinalOutput.pdf')
