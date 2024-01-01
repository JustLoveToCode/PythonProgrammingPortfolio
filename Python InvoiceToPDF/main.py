import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoice/*.xlsx")
print(filepaths)
# The name of the filepath is as shown below
# ['Invoice\\10001-2023.1.18.xlsx', 'Invoice\\10002-2023.1.18.xlsx', 'Invoice\\10003-2023.1.18.xlsx']

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # This will take the filename only which is the 100001...
    # with stem it will extract only the filename itself and not the entire filepath
    filename = Path(filepath).stem
    # When it is a-b-c-d:
    # This will split the strings inside the array with ['a','b','c','d']
    # invoice_nr will get the first item of that list in the array and the
    # date will get the second item of that list in the array,
    # Automatically, Python will assign it for the variable
    invoice_nr, date = filename.split("-")

    pdf.set_font(family='Times', size=40, style="B")
    # the w will set the width which is the invisible width of the cell
    # the h will set the height which is the invisible height of the cell
    # ln=1 will create a break line so that it will move to the next line.
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family='Times', size=25, style="B")
    pdf.cell(w=50, h=8, txt=f"Date nr.{date}", ln=1)

    # Adding the header:
    # Heading need to be outside of the for loop since it is only Created Once:
    # For csv it will be read_csv():
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Getting the Label of the data
    columns = df.columns
    # Using the List Comprehension for Python
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)
    # This is the width of the cell and the height of the cell
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Note that the row mean it is reading the header in the horizontal manner
    # A B C D E, for index,row in df.iterrows() mean it is looping through the row
    # in A,B,C,D and E in the Horizontal manner:
    # Adding the rows to the table:
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        # This is the width of the cell and the height of the cell
        # The reason why the data is printed side by side because we did not assign the ln=1
        # At the end of the data, we add the code ln=1 so that the next database will be
        # created on the new row.
        # The data for the corresponding heading can have multiple data,
        # Hence, you will need to use the for loop itself
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Getting the total sum here using the .sum() method:
    total_sum = df["total_price"].sum()
    total_amount_purchased = df['amount_purchased'].sum()
    total_average_price = df['price_per_unit'].mean()
    pdf.set_font(family="Times", size=25, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_amount_purchased), border=1)
    pdf.cell(w=30, h=8, txt=str(total_average_price), border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum sentence:
    pdf.set_font(family='Times', size=10, style='B')
    # This will set the width w from the very left of the margin which is 30
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)

    # Add the Company name and logo:
    pdf.set_font(family='Times', size=25, style='B')
    # This will set the width w from the very left of the margin which is 50
    pdf.cell(w=50, h=8, txt=f"Pythonhub")
    # Importing the image and setting the wide of the image to be w=10
    pdf.image("python.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")
