import os.path

from csv_utilities import read_csv, write_csv, csv_to_dict
from statement import Statement
from statement_book import StatementBook
from datetime import date
from os import listdir


def file_to_statement(file_name: str):
    """Read in csv file and create statement object."""
    header, data, row_count = read_csv(filename=file_name)
    csv_dict = csv_to_dict(header=header, data=data)

    # Assumes file name is the statement issuer
    base_file_name = os.path.basename(file_name)
    issuer = os.path.splitext(base_file_name)[0]
    return Statement(csv_dict, row_count, issuer)


if __name__ == "__main__":
    while True:
        directory_path = input(
            "Please provide the directory path, to the directory holding all statements that you'd like to be compiled: "
        )
        if os.path.isdir(directory_path):
            break
        print(f"Inputted directory path does not exist...")

    directory_path = os.path.normpath(directory_path)

    list_of_files = [
        os.path.join(directory_path, file_name) for file_name in listdir(directory_path)
    ]
    print(f"The following files were found in the given directory: {list_of_files}")

    print(f"Converting found files into statements...")
    list_of_statements = [file_to_statement(file_name) for file_name in list_of_files]
    print(list_of_statements[0])

    print("Creating statement book from statements...")
    statement_book = StatementBook(list_of_statements)
    print(f"Statement book created with values:\n{statement_book}")

    output_file_name = f"statement_book_{date.today()}.csv"
    print(f"Exporting statement book to as {output_file_name}...")
    write_csv(
        os.path.join(directory_path, output_file_name),
        statement_book.statement_book,
        statement_book.statement_book_row_count,
    )
