emp_no=input("Enter Employee Number: ")
name=input("Enter a employee Name: ")
phone_no=input("Enter a Phone Number: ")
city=input("Enter a City: ")
data={
    "emp_no":emp_no,
    "name":name,
    "phone_no":phone_no,
    "city":city 
}
emp_info=[]
for i in data:
    if i<=emp_no:
        emp_info.append(data)
print(data)
