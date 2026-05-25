# utils.py

import re


def clean(text):

    text = re.sub(r'\\*\\*(.+?)\\*\\*', r'\\1', text)
    text = re.sub(r'\\*(.+?)\\*', r'\\1', text)
    text = re.sub(r'#+\\s', '', text)
    text = re.sub(r'\\n{3,}', '\\n\\n', text)

    return text.strip()