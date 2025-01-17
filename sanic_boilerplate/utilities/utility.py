"""Utility functions."""
import re
from datetime import date
from datetime import datetime
from typing import Text


def is_valid_url(url: Text):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    try:
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            return obj.__dict__()
    except (TypeError, AttributeError):
        return obj.__str__()


def isoformat_to_datetime(isoformat_string):
    return datetime.strptime(isoformat_string, "%Y-%m-%dT%H:%M:%S.%f")

