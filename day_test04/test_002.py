import  random
result=0
for i in range(101):
    print(i)
    result=result+i
print(result)

for i in range(101):
    if i%2==0:
        print(i)
        result=result+i
print(result)

for i in range(2,101,2):
        print(i)
        result=result+i
print(result)

computer_number=random.randint(1,100)
while True:
    person_number = int(input("请输入一个数字："))
    if person_number > computer_number:
        print("猜大了")
    elif person_number < computer_number:
        print("猜小了")
    elif person_number == computer_number:
        print("猜对了")
        break


list_squre=[]
for i in range(1,4):
    list_squre.append(i**2)

list_squre2=[i**2  for i in range(1,4)  if i!=1]




