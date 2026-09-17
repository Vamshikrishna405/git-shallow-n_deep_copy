print('Regex also known as regular expression')
import re as r
text='my mobile number is 123456789'
res = r.search(r"\d+",text)
print(res)
print(res.group())
res1 = r.findall(r"\d+",text)
print(res1)
res2=r.sub(r"\d","#",text)
print(res2)
num = 'my password is 1 2 3 4'
print(r.findall(r"\d+",num))


