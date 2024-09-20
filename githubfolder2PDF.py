import os
from fpdf import FPDF

def add_file_to_pdf(pdf, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"File: {file_path}\n\n")  # Add file name as a header
        for line in file:
            safe_line = line.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, safe_line)
        pdf.multi_cell(0, 10, "\n\n")  # Add some space after each file's content

def convert_directory_to_single_pdf(directory, output_pdf_path):
    pdf = FPDF()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py')):  # Add more file types if needed
                file_path = os.path.join(root, file)
                add_file_to_pdf(pdf, file_path)
                print(f"Added {file_path} to the PDF")
    
    pdf.output(output_pdf_path)

if __name__ == "__main__":
    code_base_directory = r"C:\Users\cinco\Desktop\Quant-Tools" # Replace with the path to your code base
    output_pdf = r'C:\Users\cinco\Desktop\quanttoolsReadme.pdf'  # Path to save the final PDF
    convert_directory_to_single_pdf(code_base_directory, output_pdf)
