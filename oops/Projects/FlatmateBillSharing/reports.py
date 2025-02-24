import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amount
    and the period od the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pays = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pays = str(flatmate2.pays(bill, flatmate1))

        pdf = FPDF(orientation="P", unit='pt', format="A4")
        pdf.add_page()

        # add ICON
        pdf.image("files/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family="Times", size=18, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        #Insert Period label and Value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=100, h=40, txt=bill.period, border=0, ln=1)

        #Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size =12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate1_pays, border=0, ln=1)

        #Insert name and due amount of the 2nd flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate2_pays, border=0, ln=1)

        #change dir and generate PDF
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
