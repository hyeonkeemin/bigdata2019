import re

def hexrepl(match):
    'return the hex string for a decimal number'
    value = int(match.group())
    return hex(value)

p=re.compile(r'\d+')
print(p.sub(hexrepl, 'call 65490 for printing, 49152 for user code.'))