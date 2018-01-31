import re


def fi_to_inches(s):
    s = re.sub('(feet|foot|ft)', "'",
               re.sub('(inch|inches|in)', '"',
                      s.replace(' ', '').lower()))
    if "'" in s:
        feet, i = s.split("'")
    else:
        feet = 0
        i = s
    if '"' in i:
        inches = i.split('"')[0]
    else:
        inches = 0

    return int(feet) * 12 + int(inches)


def inches_to_fi(i):
    feet = i // 12
    inches = i % 12

    f_str = str(feet) + "'"
    i_str = str(inches) + '"'

    if feet == 0:
        return i_str
    elif inches == 0:
        return f_str
    else:
        return f_str + i_str
