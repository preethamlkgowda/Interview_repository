Consider adding a docstring or comment to explain the purpose of the script, e.g., 'This script generates a PDF file from a given text input.'
```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
Add a docstring to the function to describe its purpose, parameters, and return value. For example: 'Saves the given text to a PDF file. Parameters: text (str): The text to save. filename (str): The name of the output PDF file.'

Consider using a more descriptive variable name than 'c', such as 'pdf_canvas', to improve code readability.
def save_text_to_pdf(text, filename="output.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    The variable 'line_height' is hardcoded. Consider making it a parameter of the function to allow customization.
    x = 50
    Add a comment explaining the purpose of the 'if y < 50' condition, e.g., 'Check if there is enough space on the current page for the next line. If not, start a new page.'
    y = height - 50
    You might want to reset 'x' to its initial value when starting a new page, in case it is modified in the future.
    line_height = 15
    for line in text.splitlines():
        if y < 50:
            c.showPage()
            y = height - 50
        Consider making 'user_text' an input parameter or reading it from an external file to make the script more flexible and reusable.
        c.drawString(x, y, line)
        Add a comment to explain the purpose of this block, e.g., 'Example usage of the save_text_to_pdf function with sample text.'
        y -= line_height
    c.save()

user_text = """
Hello, this is a sample PDF.
You can type or paste your text here,
and it will be saved as a PDF.
"""
save_text_to_pdf(user_text, "sample_output.pdf")
```
