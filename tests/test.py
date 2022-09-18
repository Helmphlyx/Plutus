import os.path

from csv_utilities import read_csv, write_csv, csv_to_dict
from statement import Statement
from statement_book import StatementBook
from datetime import date
from os import listdir

if __name__ == "__main__":
    print("Running unit tests for csv utilities...")

    print("Testing read_csv function in csv_utilities: ")
    cwd = os.getcwd()

    input_file_path = os.path.join(cwd, "unit_test/test_statement.CSV")
    header, data, row_count = read_csv(input_file_path)

    assert header == "Status,Date,Description,Debit,Credit".split(",")
    assert data == [
        "Cleared,08/05/2022,PRIDE STATION 63020119 E LONGMEADOW MA,25.13,".split(",")
    ]
    assert row_count == 1
    print("Unit test for read_csv function in csv_utilities passed.\n")

    print("Testing write_csv function in csv_utilities: ")
    output_file_name = f"statement_book_{date.today()}.csv"
    output_file_path = os.path.join(cwd, "unit_test", output_file_name)

    write_csv(output_file_path, csv_content={}, row_count=0)

    assert os.path.exists(output_file_path)
    print("Unit test for write_csv function in csv_utilities passed.\n")
