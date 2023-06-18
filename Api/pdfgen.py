from reportlab.pdfgen import canvas

def generate_pdf(file_path):
    # Create the canvas object
    c = canvas.Canvas(file_path)

    # Set the title of the document
    c.setTitle('Appointment')

    # Draw some text on the canvas
    c.drawString(100, 750, 'Welcome to ReportLab!')

    # Draw a line
    c.line(100, 740, 500, 740)

    # Save the canvas as a PDF file
    c.save()

# Call the function to generate the PDF
generate_pdf('output.pdf')



