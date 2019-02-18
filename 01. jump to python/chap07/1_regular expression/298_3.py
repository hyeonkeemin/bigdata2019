import re
original_text = '''a1 aslkdfjsalkejfklasef
2b alksjfklsejfkls
c3 djfkslfeklanv
4d aslefkjaksldfkla
5e djsklfaneklnb
f6 dlfsneflksnf
'''
p = re.compile('[a-zA-Z0-9][0-9]')
m = p.match(original_text)
print(m)
