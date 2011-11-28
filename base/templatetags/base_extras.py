from django import template
from pprint import pprint
import re

register = template.Library()

@register.filter("tablecols")
def tablecols(arr, cols):
    """
        Convert a list into a list of lists of length "cols",
        to be used for easy list -> table conversion. Last row is padded 
        with Nones if necessary.
    """
    arr = list(arr)
    acc = []

    # pad with None
    if len(arr) % cols:
        arr.extend([None for i in range(cols - len(arr) % cols)])

    for i in xrange(0, len(arr), cols):
        acc.append(arr[i:i + cols])

    return acc

@register.filter("truncate_chars")
def truncate_chars(value, max_length):
    max_len = int(max_length)
    if len(value) > max_len:
        truncd_val = value[:max_len]
        return  truncd_val + "..."
    return value

@register.filter("embolden")
def embolden(string, phrase):
    if phrase:
        r = re.compile(r"%s" % phrase, re.IGNORECASE)
        return re.sub(r, "<b>%s</b>" % phrase, string)
    return string
