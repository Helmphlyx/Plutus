import os.path

from csv_utilities import read_csv, write_csv, csv_to_dict
from enums.general_header import GeneralHeader
from statement import Statement
from statement_book import StatementBook
from datetime import date
from os import listdir

import openpyxl as px

# Directory Paths for Weekly Script
LANDING_DIRECTORY=r"C:\Users"
FINANCE_WORKBOOK=r"C:\Users"

def file_to_statement(file_name: str):
    """Read in csv file and create statement object."""
    header, data, row_count = read_csv(filename=file_name)
    try:
        csv_dict = csv_to_dict(header=header, data=data)
    except Exception as e:
        print(f"Bad file {file_name}")
    # Assumes file name is the statement issuer
    base_file_name = os.path.basename(file_name)
    issuer = os.path.splitext(base_file_name)[0]
    return Statement(csv_dict, row_count, issuer)


if __name__ == "__main__":
    # Landing file directory
    directory_path = LANDING_DIRECTORY
    directory_path = os.path.normpath(directory_path)

    # Read in file names for files in directory
    list_of_files = [
        os.path.join(directory_path, file_name) for file_name in listdir(directory_path)
    ]
    print(f"The following files were found in the given directory: {list_of_files}")

    # filter to csv files
    list_of_files = [file for file in list_of_files if ".csv" in file or ".CSV" in file]

    # Convert file contents into statement objects
    print(f"Converting found files into statements...")
    list_of_statements = [file_to_statement(file_name) for file_name in list_of_files]

    # Create statement book object out of all statement obhjects
    print("Creating statement book from statements...")
    headers = (
        GeneralHeader.ISSUER,
        GeneralHeader.TRANS_DATE,
        GeneralHeader.AMOUNT,
        GeneralHeader.DESCRIPTION,
        GeneralHeader.CATEGORY
    )
    statement_book = StatementBook(list_of_statements, headers)


    # TODO: take lines in statement object and place in excel
    # Write to existing workbook + sheet
    wb = px.load_workbook(FINANCE_WORKBOOK)
    ws = wb["Landing"]

    for row in statement_book.statement_book_content:
        print(row)
        ws.append(row)
    wb.save(FINANCE_WORKBOOK)
    wb.close()
