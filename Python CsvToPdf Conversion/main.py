from fpdf import FPDF
import pandas as pd

# The Orientation can be L which is LandScape or P which is Portrait
pdf = FPDF(orientation="P", unit="mm", format="A4")
# Do not allow the page break into the next page, by default it will be set to True
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")




# This will create an index that is starting from 0,
# The row will be the data inside the table.
# iterrows() Iterate over the DataFrame rows
for index, row in df.iterrows():
    # This will add the page for every iteration of the variables

    pdf.add_page()
    # Set the header:
    pdf.set_font(family="Times", style="B", size=24)
    # This is the rgb color
    pdf.set_text_color(100, 100, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    # x1 and y1 will be the starting point of the line.
    # x2 and y2 will be the ending point of the line.
    # There will be a point difference between the 2 coordinates
    # and this will basically create a line between the 2 coordinates
    # This will be in millimeter or mm as defined above
    # (20,298,10) where 20 and 298 is the y coordinate and the
    # line will be 10mm apart from each other, this will iterate through
    # the y which is the start of the y coordinate will be 20.
    # This will basically repeat every 10 step, which is 20,30,40,50
    # for the row itself for the i value.
    # Hence, you will get (10,20,200,20) and (10,30,200,30) and
    # (10,40,200,40) and (10,50,200,50) and so on.
    # The start and the end of the x is actually fixed, only the y
    # coordinate that is going downward for the horizontal line is
    # always changing.

    # Using the for loop to create multiple
    # horizontal lines downward the page.
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # This will add line break 265mm within that same pdf page:
    # Setting the footer:
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    # The for loop at the initial will stop there and now the second for loop
    # will iterate across the first variable, the second variable and so on.
    # range(2) will output 2 times, and range(3) will output 3 times altogether

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # This will add line break 265mm  within that same pdf page:
        # Setting the footer
        pdf.ln(278)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        # The for loop at the initial will stop there and now the second for loop
        # will iterate across the first variable, the second variable and so on.
        # range(2) will output 2 times, and range(3) will output 3 times altogether

        # Using the for loop to create multiple
        # horizontal lines downward the page.
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

# This is the output of the pdf file which is called output1.pdf
pdf.output("output1.pdf")
