from reportlab.pdfgen import canvas

def generate_pdf(file_path):
    # Create the canvas object
    c = canvas.Canvas(file_path)

    # Set the title of the document
    c.setTitle('My PDF')

    # Draw some text on the canvas
    c.drawString(100, 750, 'Welcome to ReportLab!')

    # Draw a line
    c.line(100, 740, 500, 740)

    # Save the canvas as a PDF file
    c.save()

# Call the function to generate the PDF
generate_pdf('output.pdf')



{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ1c2VyMSIsImV4cCI6MTY4NjMyMTgyOX0.jmuR5cbocG_oTVHs--qxz5uSZZKqo2aPYjq5AbFKV-k",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ1c2VyMSIsImV4cCI6MTY4NjQ5NDUwOX0.p7gcTvhjS4G-pRlEvhD0E63Jmv6YPS3js7-Rk2UxnKI"}