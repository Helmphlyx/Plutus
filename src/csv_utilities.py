"""CSV Utilities."""
import csv
import logging

from typing import List, Dict

log = logging.getLogger(__name__)


def read_csv(filename: str):
    """Read CSV file and return header, data, and row count."""
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        # initialize values to return
        header = next(csv_reader)
        data = []
        row_count = 0

        for row in csv_reader:
            if row:  # if not an empty line
                data.append(row)
                row_count += 1

        return header, data, row_count


def write_csv(filename: str, csv_content: Dict, row_count):
    """Write dictionary content to CSV file."""
    with open(filename, "w") as csv_file:
        field_names = list(csv_content.keys())  # extract dict keys for csv header
        csv_writer = csv.DictWriter(
            csv_file, fieldnames=field_names, lineterminator="\n"
        )
        csv_writer.writeheader()
        for index in range(row_count):
            csv_writer.writerow({key: csv_content[key][index] for key in field_names})


def csv_to_dict(header: List[str], data: List[List[str]]):
    """Convert CSV data into equivalent dictionary."""
    csv_dict = {}

    # Set up headers as keys in dictionary
    for key in header:
        csv_dict[key] = []

    # Populate list values in dictionary
    for row in data:
        for index, value in enumerate(row):
            try:
                csv_dict[header[index]].append(str(value).strip())
            except IndexError as e:
                log.error(
                    "CSV Data does not have corresponding CSV Header. Check file..."
                )
                log.error(e)
                raise IndexError
    return csv_dict
