from fpdf import FPDF


class rondinPDF(FPDF):
    def header(self):
        self.set_font('Arial', '', 15)
        self.rect(x=10,y=14,w=190,h=70)
        self.image('App/vikosur/vikosur.png', x=30, y=17, w=40, h=15)
        self.rect(x=97,y=14,w=15,h=15)
        ##BAJO EL LOGO
        self.set_font('Arial', 'B', 30)   
        self.text(x=100, y=25, txt= 'X')
        self.line(10,54,200,54)
        self.set_font('Arial', 'B', 8)
        self.text(x=26, y=38, txt= 'CHAMBÍ AGUANTA DAVID ELISEO') 
        self.set_font('Arial', '', 8)
        self.text(x=26, y=42, txt= 'CEL: 2984-779569')
        self.text(x=26, y=46, txt= 'EMAIL: vikodav@hotmail.com')
        self.text(x=26, y=50, txt= 'CERVANTES')
        ##DIRIGIDO
        self.set_font('Arial', '', 8)
        self.text(x=26, y=60, txt= 'Señor/es:')
        self.text(x=35, y=78, txt= 'IVA: - ')
        self.text(x=35, y=82, txt= 'Condiciones de pago: EFECTIVO / CONTADO')
        self.set_font('Arial', '', 8)
        self.text(x=26, y=72, txt= 'C.U.I.T.: ')
        ## DERECHA LOGO
        self.set_font('Arial', '', 6)
        self.text(x=123, y=16, txt= 'Comprobante no válido como Factura - Pendiente de Autorización')
        self.set_font('Arial', 'B', 13)
        self.text(x=123, y=26, txt= 'PRESUPUESTO / COTIZACIÓN')
        self.set_font('Arial', '', 8)
        self.text(x=123, y=49, txt= 'C.U.I.T.: N° 20-18872644-6')
        self.text(x=123, y=53, txt= 'INICIO DE ACTIVIDADES: 01/11/2019')   
        self.line(10,74,200,74)
        self.line(103,44,103,84)#DIVISIÓN VERTICAL
        self.set_font('Arial', '', 8)
        self.text(x=110, y=60, txt= '* Instalación y Mantenimiento')
        self.text(x=155, y=60, txt= '* Carga de Gas')
        self.text(x=110, y=65, txt= '* Aire Acondicionado / Heladeras')
        self.text(x=155, y=65, txt= '* Heladeras')
        self.text(x=110, y=70, txt= '* Calderas y Calefacción Central')
        self.text(x=155, y=70, txt= '* Instrumentos de Laboratorio') 
        #self.line(120,74,120,84)#DIVISIÓN VERTICAL
        self.set_font('Arial', 'B', 8)
        #self.text(x=130, y=80, txt= 'Presupuesto válido por 5 días')
        ##RECTANCULO DE ITEMS
        self.rect(x=10,y=88,w=190,h=170)
        self.set_font('Arial', 'B', 10)
        self.text(x=12, y=92, txt= 'CANT.')
        self.text(x=88, y=92, txt= 'DESCRIPCIÓN')
        self.text(x=154, y=92, txt= 'P.UNIT.')
        self.text(x=174, y=92, txt= 'IMPORTE')
        self.line(10,94,200,94)
        self.line(25,88,25,258)
        self.line(150,88,150,258)
        self.line(170,88,170,258)
        self.ln(83)

    def footer(self):
        self.set_font('Arial', 'B', 10)
        self.set_y(-18)
        self.cell(28, 5, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'R')
        self.rect(x=10,y=267,w=190,h=25)
        self.line(170,273,200,273)
        self.line(40,267,40,292)
        self.text(x=180, y=272, txt= 'TOTAL')
        self.line(170,267,170,292)
        self.ln(250)