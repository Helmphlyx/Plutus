"""HeaderMap"""
from enums.general_header import GeneralHeader


class HeaderMap:
    header_map = {
        "transaction date": GeneralHeader.TRANS_DATE,
        "post date": GeneralHeader.POSTED_DATE,
        "description": GeneralHeader.DESCRIPTION,
        "category": GeneralHeader.CATEGORY,
        "type": GeneralHeader.UTILITY_VALUES,
        "amount": GeneralHeader.AMOUNT,
        "memo": GeneralHeader.MISC,
        "posted date": GeneralHeader.POSTED_DATE,
        "reference number": GeneralHeader.UTILITY_NUMBERS,
        "payee": GeneralHeader.DESCRIPTION,
        "address": GeneralHeader.DESCRIPTION,
        "status": GeneralHeader.MISC,
        "date": GeneralHeader.TRANS_DATE,
        "debit": GeneralHeader.AMOUNT,
        "credit": GeneralHeader.AMOUNT,
        "aba num": GeneralHeader.UTILITY_NUMBERS,
        "currency": GeneralHeader.CURRENCY,
        "account num": GeneralHeader.UTILITY_NUMBERS,
        "account name": GeneralHeader.UTILITY_VALUES,
        "bai Code": GeneralHeader.UTILITY_NUMBERS,
        "serial num": GeneralHeader.UTILITY_NUMBERS,
        "ref num": GeneralHeader.UTILITY_NUMBERS,
        "trans. date": GeneralHeader.TRANS_DATE,
    }
