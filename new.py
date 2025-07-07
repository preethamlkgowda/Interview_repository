from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def save_text_to_pdf(text, filename="output.pdf"):
    # Set up the PDF canvas
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Start from top margin
    x = 50
    y = height - 50
    line_height = 15

    # Split the input text into lines
    for line in text.splitlines():
        if y < 50:
            c.showPage()  # Start a new page if space runs out
            y = height - 50
        c.drawString(x, y, line)
        y -= line_height

    # Save the PDF file
    c.save()
    print(f"PDF saved as: {filename}")

# Example usage
user_text = """
Hello, this is a sample PDF.
You can type or paste your text here,
and it will be saved as a PDF.
"""
save_text_to_pdf(user_text, "sample_output.pdf")
