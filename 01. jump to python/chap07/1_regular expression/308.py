import re
original_text = '''a1 aslkdfjsalkejfklasef
2b alksjfklsejfkls
c3 djfkslfeklanv
4d aslefkjaksldfkla
5e djsklfaneklnb
f6 dlfsneflksnf
'''
# p = re.compile('[0-9][a-z]')
p = re.compile('a1 [a-z]+\n2b', re.DOTALL)
m = p.match(original_text)
print(m)
