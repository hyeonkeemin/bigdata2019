import sys
args = sys.argv[1:]
for usernames in args:
    usernames_first = usernames[0]
    print('Hello, '+usernames_first.upper()+usernames[1:]+"!")