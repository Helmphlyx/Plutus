"""Statement Book."""
from typing import List, Tuple
from enums.general_header import GeneralHeader
from statement import Statement
from csv_utilities import csv_to_dict


class StatementBook:
    """StatementBook."""

    def __init__(self, statements: List[Statement], headers: Tuple[GeneralHeader] = None):
        """Init."""
        self.headers = headers or self.default_statement_book_enum_headers
        self.statement_book_headers = []
        self.statement_book_content = []
        self.statement_book, self.statement_book_row_count = self.process_statements(
            statements
        )

    def __repr__(self):
        """Representation of StatementBook."""
        return f"StatementBook({self.statement_book_content})"

    def __str__(self):
        """String of StatementBook."""
        statement_book_headers_fmt = " ".join(
            ["{:<18.18}".format(value) for value in self.statement_book_headers]
        )
        statement_str = statement_book_headers_fmt.format(*self.statement_book_headers)
        for statement_row in self.statement_book_content:
            statement_str += "\n"
            statement_str += " ".join(
                ["{:<18.18}".format(value) for value in statement_row]
            )
        return statement_str

    @property
    def default_statement_book_enum_headers(self):
        """Ordered tuple of statement book's enumerated headers."""
        return (
            GeneralHeader.ISSUER,
            GeneralHeader.TRANS_DATE,
            GeneralHeader.POSTED_DATE,
            GeneralHeader.DESCRIPTION,
            GeneralHeader.AMOUNT,
            GeneralHeader.CURRENCY,
            GeneralHeader.CATEGORY,
            GeneralHeader.UTILITY_VALUES,
            GeneralHeader.UTILITY_NUMBERS,
            GeneralHeader.MISC,
        )

    def process_statements(self, statements: List[Statement]):
        """Process statements data into singular dictionary."""
        statement_book_data = []

        # extract data from each statement
        for statement in statements:
            statement_data = self.statement_to_statement_book(statement=statement)
            statement_book_data.extend(statement_data)

        statement_book_headers_str = [
            header.value for header in self.headers
        ]

        # convert header and content to single dictionary
        self.statement_book_headers = statement_book_headers_str
        self.statement_book_content = statement_book_data
        return csv_to_dict(statement_book_headers_str, statement_book_data), len(
            statement_book_data
        )

    def statement_to_statement_book(self, statement: Statement):
        """Extracts statement data into statement book format."""
        statement_dict = statement.statement
        statement_data = []

        # Extract statement values as a list of row values
        for row in range(statement.row_count):

            # Extract statement values in order of statement book headers
            row_data = []
            for header in self.headers:
                datum = statement_dict.get(header, "")

                # Default values for certain headers.
                if not datum:
                    if header is GeneralHeader.POSTED_DATE:
                        datum = statement_dict.get(GeneralHeader.TRANS_DATE, "")
                    if header is GeneralHeader.TRANS_DATE:
                        datum = statement_dict.get(GeneralHeader.POSTED_DATE, "")
                    if header is GeneralHeader.CURRENCY:
                        datum = ["USD"] * statement.row_count

                if not datum:
                    row_data.append(datum)
                else:
                    row_data.append(datum[row])
            statement_data.append(row_data)

        return statement_data
