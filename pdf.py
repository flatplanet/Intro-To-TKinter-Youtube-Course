# pip install PyPDF4

import PyPDF4

pdf = pyfpdf4.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Codemy.com!!!", align="C")
pdf.output("tutorial.pdf")