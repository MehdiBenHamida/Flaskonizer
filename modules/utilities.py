"""
File: utilities.py
utilities class definition to major needed common feature
"""
import re


class Common:

    @staticmethod
    def to_snake_case(st):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', st.replace(" ", "")).lower()
