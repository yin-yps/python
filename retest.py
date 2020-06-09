#! /usr/bin/python3
import re

pattern = re.compile('apple')
result  = pattern.match('apple1')
print(result)
result1 = re.match('apple','apple1')
print(result1)

result2 = re.match('.?','apple')
if result2:
    print(result2.group())

result3 = re.match(r'\d','138')
print(result3)

result4 = re.match(r'\D','/')
print(result4)

result5 = re.match(r'11\S23','11(23  123')
print(result5)

result6 = re.match(r'11\s123','11 123')
print(result6)

result7 = re.match(r'\W',' ')
print(result7)

s=r'asd\nasd'
print(s)
result8 = re.match(r'asd\\nasd',s)
print(result8)

result = re.match(r'\d{11}','12312451123')
if result:
    print(result.group())
else:
    print('none')

email='18322@263.com'
email1='1as_23@163.com'
result = re.match(r'\w{3,20}@(?:163|126|qq|263)\.com$',email)
if result:
    print(result.group())
else:
    print('none')


word='hello'
result= re.match(r'\w+llo\b',word)
if result:
    print(result.group())
else:
    print('none')
