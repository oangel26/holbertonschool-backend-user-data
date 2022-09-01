#!/usr/bin/env python3
"""
Regex-ing
"""
import re
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
                             field + "=" + redaction, new_message)

    return new_message


if __name__ == "__main__":
    personal_info1 = f'name=egg;email=eggmin@eggsample.com;\
    password=eggcellent;date_of_birth=12/12/1986;'
    personal_info2 = """name=bob;email=bob@dylan.com;password=bobbycool;\
    date_of_birth=03/04/1993;"""

    fields = ["password", "date_of_birth"]
    messages = [personal_info1, personal_info2]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))
