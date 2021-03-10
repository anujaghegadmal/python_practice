employee=[
    {
        "name":"abc",
        "email":"abc@gmail.com",
        "phone_number":"8546123798",
        "city":"Mumbai"
    },
    {
        "name":"pqr",
        "email":"pqr@gmail.com",
        "phone_number":"5796841236",
        "city":"Pune"
    },
        {
        "name":"bvc",
        "email":"bvc@gmail.com",
        "phone_number":"6547821395",
        "city":"Pune"
    },
    {
        "name":"qwe",
        "email":"qwe@gmail.com",
        "phone_number":"3798854612",
        "city":"Nashik"
    },
    {
        "name":"iop",
        "email":"iop@gmail.com",
        "phone_number":"1597536485",
        "city":"Sangli"
    },
    {
        "name":"fgh",
        "email":"fgh@gmail.com",
        "phone_number":"4521637896",
        "city":"Mumbai"
    },
    {
        "name":"xcf",
        "email":"xcf@gmail.com",
        "phone_number":"3524169875",
        "city":"Nashik"
    },
    {
        "name":"mjh",
        "email":"mjh@gmail.com",
        "phone_number":"5987463214",
        "city":"Kolhapur"
    }
]
filter_list=[]
filter_city=input("Enter a city: ")
for i in employee:
    if i["city"]==filter_city:
       filter_list.append(i)

if len(filter_list)>0:
    print(filter_list)
else:
    print("City not found")
