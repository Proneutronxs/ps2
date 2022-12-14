from fpdf import FPDF

class modelPDF(FPDF):
    def header(self):
        self.set_font('Arial', '', 15)
        self.rect(x=10,y=14,w=190,h=19)
        self.image('static/business/img/Logo.png', x=10, y=17, w=10, h=6)
        self.text(x=21, y=22, txt= 'EMPRESA ZETONE')
        self.line(72,14,72,26)
        #self.set_font('Arial', 'B', 13)
        #self.text(x=82, y=20, txt= 'RECURSOS HUMANOS')
        #self.text(x=73.5, y=24, txt= '(DPTO. HIGIENE Y SEGURIDAD)')
        self.set_font('Arial', '', 10)
        self.text(x=146, y=17, txt= 'Tipo de Documento:')
        self.set_font('Arial', 'B', 10)
        self.text(x=180, y=25, txt= 'PLANILLA')
        self.line(10,26,200,26)
        self.set_font('Arial', '', 10)
        self.text(x=16, y=30, txt= 'Título de Documento:')
        #self.set_font('Arial', 'B', 13)
        #self.text(x=82, y=32, txt= 'CONTROL DE RONDAS')
        self.line(145,14,145,33)
        self.set_font('Arial', 'B', 10)
        self.text(x=146, y=32, txt= 'Código: ')
        #self.text(x=162, y=32, txt= 'PLGRH22')
        self.set_font('Times', 'I', 12)
        #self.text(x=12, y=37, txt= 'Fecha Desde: ')
        #self.text(x=60, y=37, txt= 'Hasta: ')
        self.text(x=146, y=37, txt= 'Establecimiento:')
        self.line(10,38,200,38)
        self.ln(30)

    def footer(self):
        self.set_font('Arial', 'B', 10)
        self.set_y(-21)
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'R')
        
        self.rect(x=10,y=274,w=190,h=15.5)
        self.text(x=18, y=278, txt= 'Preparó:')
        #self.text(x=16.5, y=284, txt= 'Tec. HSSE')
        self.line(40,274,40,289.5)
        self.text(x=45, y=278, txt= 'F. Emisión:')
        #self.text(x=45, y=284, txt= '27/10/2022')
        self.line(70,274,70,289.5)
        self.text(x=78.5, y=278, txt= 'Revisó:')
        #self.text(x=78, y=283, txt= 'Gerente')
        #self.text(x=72.5, y=287, txt= 'Administrativo')
        self.line(100,274,100,289.5)
        self.text(x=118, y=278, txt= 'Aprobó:')
        #self.text(x=108, y=284, txt= 'ENCARGADO RRHH')
        self.line(150,274,150,289.5)
        self.text(x=152.5, y=278, txt= 'Versión:')
        self.text(x=156.5, y=284, txt= '0.5')
        self.line(170,274,170,289.5)
        self.ln(250)