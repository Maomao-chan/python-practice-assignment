name=input("Enter your name : ")
math=int(input("Enter math marks: "))
eng=int(input("Enter English marks: "))
py=int(input("Enter Python marks: "))
print(f"Student name: {name}")
avg=(math+eng+py)/3
print(f"Average marks: {avg}")
def grade(avg):
    if avg>=80:
        return "A+"
    elif avg>=70:
        return "A"
    elif avg>=60:
        return "A-"
    elif avg>=50:
        return "B"
    elif avg>=40:
        return "C"
    else:
        return "F"
print(f"Final Grade: {grade(avg)}")