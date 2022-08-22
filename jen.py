# import json
# def func():
#     f=open("signup.text","r")
#     username=input("enter the username :")
#     list=[]
#     dic={}
#     d={}
#     s={}
#     a="Happiness is being alone with our own thoughts", username,"Jen"
#     s["description"]=a
#     dic["user"]=list
#     password=input("enter the password :")
#     if len(password)>=6:
#         if "@" in password or "#" in password or "$" in password:
#             confirm_password=input("enter the confirm password :")
#             print("strong password")
#             d["username"]=username
#             d["password"]=password
#             d["profile"]=s
#             list.append(d)
#             Date_of_Birth=input("enter the birth date :")
#             Hobbies=input("enter your hobbies :")
#             Gender=input("enter gender :")
#             s["Date_of_Birth"]= Date_of_Birth
#             s["Hobbies"]=Hobbies
#             s["Gender"] =Gender
#             with open("signup.text","w") as f:
#                 json.dump(dic,f,indent=8)
#                 f=open("signup.text","a")
#                 print("signup or login success")
#         else:
#             print("invalid")
#     else:
#         print("password should have special_chr")
#         func()
# print("login or signup")
# user=input("enter what you want :")
# if user=="signup":
#     func()
# elif user== "login":
#     func()  