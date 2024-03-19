"""
pdf_editor.py

A simple script to edit the title of a PDF file.

This script provides functionality to modify the title of a PDF document and save the modified PDF to a new file.

Usage:
    python pdf_editor.py <input_pdf> <output_pdf> <new_title>

Example:
    python pdf_editor.py input.pdf output.pdf "New Title"

Dependencies:
    - PyPDF2 (https://pythonhosted.org/PyPDF2/)

Author:
    Xandra Campo

Date:
    March 19, 2024
"""
import sys

from PyPDF2 import PdfReader, PdfWriter


def edit_pdf_title(input_pdf, output_pdf, new_title):
    """
    Edits the title of a PDF file and saves the modified PDF to a new file.

    Parameters
    ----------
    input_pdf : str
        Path to the input PDF file.
    output_pdf : str
        Path to save the modified PDF file.
    new_title : str
        New title to set for the PDF document.

    Returns
    -------
    None

    Raises
    ------
    FileNotFoundError
        If the input PDF file does not exist.
    PermissionError
        If there is a permission issue while accessing the input or output files.
    PyPDF2.utils.PdfReadError
        If the input PDF file is invalid or corrupted.
    """

    with open(input_pdf, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        # Copy all pages from the input PDF to the output PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Add or modify the document information dictionary with the new title
        pdf_writer.add_metadata({'/Title': new_title})

        # Write the modified PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)


if __name__ == "__main__":
    """
    Main block to execute the script from the command line.

    Usage
    -----
    python pdf-editor.py <input_pdf> <output_pdf> <new_title>

    Arguments
    ---------
    input_pdf : str
        Path to the input PDF file.
    output_pdf : str
        Path to save the modified PDF file.
    new_title : str
        New title to set for the PDF document.

    Example
    -------
    python pdf-editor.py path-to-pdf-file-1.pdf path-to-pdf-file-2.pdf new-title
    """

    if len(sys.argv) != 4:
        print("Usage: python pdf-editor.py <input_pdf> <output_pdf> <new_title>")
        sys.exit(1)

    edit_pdf_title(input_pdf=sys.argv[1], output_pdf=sys.argv[2], new_title=sys.argv[3])
