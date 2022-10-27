from fpdf import FPDF

#hoja_pdf = FPDF(orientation='P', unit='mm', format='A4')
#hoja_pdf.add_page()

#CUADRADOS
#hoja_pdf.rect(x=10,y=10,w=100,h=30)

#LINEAS
#hoja_pdf.line(10,50,10,50)

#hoja_pdf.output('name.pdf')
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('static/business/img/Logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(50)
        # Title
        self.cell(80, 10, 'EMPRESA ZETONE', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.image('static/business/img/Logo.png', 10, 284, 10)
        self.cell(50, 10, 'EMPRESA ZETONE', 1, 0, 'C')
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
for i in range(1, 41):
    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output('tuto2.pdf', 'F')