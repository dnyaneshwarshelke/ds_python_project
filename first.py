'''def reverse_str(input_str):
    rev=input_str.split('.')
    reversed_st=' '.join(rev[::-1])

    return reversed_st

result="i.like.this.programming.very.much"
print(reverse_str(result))
'''

'''input1='i.like.this.programming.very.much'
rev=input1.split('.')
revv='+'.join(rev[::-1])

print(revv)'''

inp='dnyanu  shelke'
emp_list=[]
cap=inp.split()
for i in cap:
    cap_word=i[0].upper()+ i[1:]
    emp_list.append(cap_word)

result=' '.join(emp_list)
print(str(result))
print(emp_list)
#print(cap_word)











