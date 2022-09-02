#!/usr/bin/env python3
"""
Regex-ing
"""
import logging
import re
from time import gmtime, strftime
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Method taht returns the log message obfuscated
    :type fields: List[str]
    :type redaction: str
    :type message: str
    :type separator: str
    :rtype: str
    """
    new_message = message
    for field in fields:
        new_message = re.sub(field + "=" + f"[^,{separator}]+",
                             " " + field + "=" + redaction, new_message)

    return new_message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        """
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.__fields, self.REDACTION, msg, self.SEPARATOR)