#Q1
i1 = int(input('science marks:'))
i2 = int(input('maths marks:'))
i3 = int(input('english marks:'))
i4 = int(input('urdu marks:'))
i5 = int(input('chemistry marks:'))

marks_obtained = (i1+i2+i3+i4+i5)
total_marks = 500

print("Total marks : ",total_marks)
print("Marks obtained :",marks_obtained)
print("Grade :",marks_obtained/total_marks*100)

#Q2
var = int(input("number :"))
if var%2 == 0:
    print(var, " is even number")
else:
    print(var,"is odd number")

#Q3
list = [9,8,5,9]
print("length of list is :",len(list))

#Q4
list = [7,8,9,5,4]
sum = 0
for i in list:
    sum += i
print(sum)

#Q5
list = [9,7,8,14,6]
min = 0
max = 0
for i in list:
    if i > min:
        min = i
print(min)

#Q6
a = [1,1,2,3,5,8,13,21,34,55,89]
for i in a:
    if i < 5:
        print(i)