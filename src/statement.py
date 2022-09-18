"""Statement."""
from typing import Dict
from header_map import HeaderMap
from enums.general_header import GeneralHeader


class Statement:
    """Statement."""

    def __init__(self, statement_data: Dict, row_count: int, issuer: str):
        """Init."""
        self._issuer = issuer
        self.row_count = row_count
        self.statement: Dict = self.process_statement_data(statement_data)

    def __repr__(self):
        """Representation of Statement."""
        return f"Statement({self._issuer})"

    def __str__(self):
        """String of Statement."""
        statement_str = ""
        statement_headers = [(key, key.value) for key in self.statement]
        for header_tuple in statement_headers:
            statement_str += f"{header_tuple[1]}: {self.statement[header_tuple[0]]}\n"
        return statement_str

    def process_statement_data(self, statement_data: Dict):
        """Process statement data into generic format."""
        processed_statement = {}

        for header, data in statement_data.items():
            # map header equivalent generic header
            general_header = HeaderMap.header_map.get(header.lower())

            if not general_header:
                # default header for unmapped headers
                general_header = GeneralHeader.MISC

            data = self._preprocess_special_headers(general_header, header, data)

            # add data to dictionary key, if data exists we recompile the data
            if general_header not in processed_statement:
                processed_statement[general_header] = data
            else:
                current_data = processed_statement[general_header]
                new_data = [
                    current_datum + "\n" + datum
                    for current_datum, datum in zip(
                        current_data, data
                    )  # adds datum to present datum in new line
                ]
                processed_statement[general_header] = new_data
        else:
            # Add issuer data
            processed_statement[GeneralHeader.ISSUER] = [self._issuer] * self.row_count
        return processed_statement

    def _preprocess_special_headers(
        self, general_header: GeneralHeader, header: str, data
    ):
        """Preprocess data for special headers."""
        special_headers = {  # Set of special headers
            GeneralHeader.UTILITY_VALUES,
            GeneralHeader.UTILITY_NUMBERS,
            GeneralHeader.MISC,
        }

        # Reformat values for the listed special headers. They are compiled groupings of arbitrary headers.
        # As the source headers are arbitrary, we want to explicitly mention what they are in the value.
        if general_header in special_headers:
            return [f"{header}: {datum}" for datum in data]
        return data
