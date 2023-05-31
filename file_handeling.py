

## 1. WAP to print how many lines of data present in a given file??
#! with length function
'''
fo=open('tushar.txt','r')
x=len(fo.readlines())
print(x)
'''

## 1. WAP to print how many lines of data present in a given file??
#! with out length function
'''
fo=open('tushar.txt','r')
count=0
for i in fo.readlines():
    count+=1
print(count)
'''




## 2. WAP to print how many words of data present in a given file??
'''
fo=open('tushar.txt','r')
count=0
s1=fo.read().split()
for i in s1:
    count+=1
print(count)
'''




## 3. WAP to print how many charecters of data present in a given file??
'''
fo=open('tushar.txt','r')
count=0
s1=fo.read()
for i in s1:
    count+=1
print(count)
'''



## 4. WAP to print words which are having more than 5 charecters??
'''
fo=open('tushar.txt','r')
s1=fo.read().split()
for i in s1:
    if len(i)>5:
        print(i)
'''




## 5. WAP to print lines which are having more than 100 charecters??
'''
fo=open('tushar.txt','r')
s1=fo.readlines()
for i in s1:
    if len(i)>100:
        print(i)
'''



## 6. WAP to print word which are starting with 'ha'??
'''
fo=open('tushar.txt','r')
s1=fo.read().split()
for i in s1:
    # if i[:2].lower()=='ha':
    #     print(i)
    if i.lower().startswith('ha'):
        print(i)
'''




## 7. WAP to print most repeated word in a given file??
'''
fo=open('tushar.txt','r')
s1=fo.read().split()
d={}
for i in s1:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
mx=max(d.values())
for j in d:
    if d[j]==mx:
        print(j)
'''




## 8. WAP to print most unique word in a given file??
'''
fo=open('tushar.txt','r')
s1=fo.read().split()
d={}
for i in s1:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for j in d:
    if d[j]==1:
        print(j)
'''





## 9. WAP to print maximum length word in a given file??
'''
fo=open('tushar.txt','r')
s1=fo.read().split()
d={}
for i in s1:
    if i not in d:
        d[i]=len(i)
mx=max(d.values())
for j in d:
    if d[j]==mx:
        print(j)
'''

