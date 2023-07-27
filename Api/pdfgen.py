from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from Api.models import Prescription
import ast,io

buffer=io.BytesIO()

def clean():
    buffer.close()

def wrap_text(canvas, text, max_width, x, y, line_height):
    words = text.split()
    lines = []
    current_line = []
    next_line=0

    for word in words:
        if canvas.stringWidth(' '.join(current_line + [word])) <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    for line in lines:
        canvas.drawString(x, y, line)
        y -= line_height
        next_line=y
    return next_line+line_height
        


def generate_pdf(name,date,address,dob,phone,doctor_name,clinic_name,clinic_addr,clinic_phone,prescription):
    next_line=30
    margin=100
    gap=50
    # Create the canvas object
    letter=(612.0,500.0)
    global buffer
    buffer=io.BytesIO()
    c = canvas.Canvas(buffer,letter)
    

    # Set the title of the document
    c.setTitle('Appointment')

    # Draw some text on the canvas

    c.setFont("Helvetica-Bold",20)
    c.drawString((letter[0]-c.stringWidth(clinic_name,"Helvetica-Bold",20))/2, letter[1]-next_line,clinic_name)
    next_line+=30

    #wrap text is used only in positions we want the string to be dynamicaally adjust according to length
    if(c.stringWidth(clinic_addr)>letter[0]):
        next_line=wrap_text(c,clinic_addr,letter[0],20,letter[1]-next_line,30)
        next_line=(letter[1]-next_line)
    else:
        c.drawString((letter[0]-c.stringWidth(clinic_addr,"Helvetica-Bold",20))/2, letter[1]-next_line, clinic_addr)
    next_line+=30
    c.drawString((letter[0]-c.stringWidth(clinic_phone,"Helvetica-Bold",20))/2, letter[1]-next_line, clinic_phone)
    next_line+=30
    # Draw a line
    c.setDash(3,2)
    c.line(0,letter[1]-next_line,letter[0],letter[1]-next_line)
    

    c.setFont("Helvetica-Bold",15)
    next_line+=30
    
    #first row
    c.drawString(margin-50, letter[1]-next_line, 'Name:')
    c.setFont("Helvetica",15)
    c.drawString(margin+gap,letter[1]-next_line,name)#for gap
    c.setFont("Helvetica-Bold",15)
    c.drawString(letter[0]-c.stringWidth("Date:","Helvetica-Bold",15)-margin*2, letter[1]-next_line, 'Date:')
    c.setFont("Helvetica",15)
    c.drawString(letter[0]-c.stringWidth("Date:","Helvetica-Bold",15)-margin*2+c.stringWidth("Date:") +gap, letter[1]-next_line, date)

    #second row
    next_line+=30
    c.setFont("Helvetica-Bold",15)
    c.drawString(margin-50, letter[1]-next_line, 'Phone:')
    c.setFont("Helvetica",15)
    c.drawString(margin+gap,letter[1]-next_line,phone)#for gap
    c.setFont("Helvetica-Bold",15)
    c.drawString(letter[0]-c.stringWidth("DOB:","Helvetica-Bold",15)-margin*2, letter[1]-next_line, 'DOB:')
    c.setFont("Helvetica",15)
    c.drawString(letter[0]-margin*2 +gap, letter[1]-next_line, dob)

    #third row
    next_line+=30
    c.setFont("Helvetica-Bold",15)
    c.drawString(margin-50, letter[1]-next_line, 'Address:')
    c.setFont("Helvetica",15)

    
    #wrap text is used only in positions we want the string to be dynamicaally adjust according to length
    next_line=wrap_text(c,address,300,margin+gap,letter[1]-next_line,30)
    
    next_line=(letter[1]-next_line)
    # c.drawString(margin+gap,letter[1]-next_line,address)#for gap

    # fourth row
    next_line+=30
    c.line(0,letter[1]-next_line,letter[0],letter[1]-next_line)

    # center prescription heading
    next_line+=30
    c.setFont("Helvetica-Bold",20)
    c.drawString((letter[0]-c.stringWidth("Prescription","Helvetica-Bold",20))/2, letter[1]-next_line, 'Prescription')
    next_line+=30
    c.setFont("Helvetica",15)

    c.drawString(100,letter[1]-next_line,"M E D I C I N E")
    c.drawString(letter[0]-200,letter[1]-next_line,"D O S A G E")

    next_line+=30
    c.setFont("Helvetica-Bold",15)
    pres=ast.literal_eval(prescription)
    for p in pres:
        p=p.split(" ")
        if(len(p)<2):
            c.drawString(100,letter[1]-next_line,p[0])
        elif(len(p)<3):
            c.drawString(100,letter[1]-next_line,p[0])
            c.drawString(letter[0]-200,letter[1]-next_line,p[1])
        elif(len(p)>2):
            c.drawString(20,letter[1]-next_line,p[0])
            c.drawString(100,letter[1]-next_line,p[1])
            c.drawString(letter[0]-200,letter[1]-next_line,p[2])
        next_line+=20 
    
    c.line(0,letter[1]-next_line,letter[0],letter[1]-next_line)
    next_line+=30
    c.drawString(20,letter[1]-next_line,"Written by:")
    c.setFont("Helvetica",15)
    c.drawString(120,letter[1]-next_line,doctor_name)#for gap
    

    
    c.save()
    buffer.seek(0)
    return buffer
    

