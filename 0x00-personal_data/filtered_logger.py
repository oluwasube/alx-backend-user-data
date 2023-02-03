#!/usr/bin/env python3
"""
Definition of filter_datum function that returns an obfuscated log message
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message with certain fields obfuscated.

    :param fields: a list of strings representing all fields to obfuscate
    :param redaction: representing what the field will obfuscate
    :param message: a string representing the log line
    :param separator:representing which character is separating
    all fields in the log line (message)
    :return: a string representing the log message with obfuscated fields

    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
