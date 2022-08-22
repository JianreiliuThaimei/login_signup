import json,os
def my():
    user=(input("enter login or signup :  "))
    if user=="signup":
        user_name=input("enter the user_name :  ")
        password=input("enter the password :  ")
        p=len(password)
        numbers = "0123456789"
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_chr = "!@#$%^&*()-+"
        a,b,c,d=0,0,0,0
        i=0
        while i<len(password):
            if password[i] in numbers:
                a+=1
            if password[i] in lower_case:
                b+=1
            if password[i] in upper_case:
                c+=1
            if password[i] in special_chr:
                d+=1
            i=i+1
        if p>=6:
            if a>=1 and b>=1 and c>=1 and d>=1 :
                print("strong password")
            else:
                print("invilade")
        else:
            print("no")
        password1=((input("repassword1 the password :  ")))
        if password==password1 :
                print("your password is match")
                if(os.path.isfile('Userdetails.json')):
                    op=open("Userdetails.json","r")
                    a=json.load(op)
                    for i in a["user"]:
                        if i["username"]==user_name:
                            print("Already Exists")
                            dic={}
                            d={}
                            dic["username"]=user_name
                            dic["password"]=password1
                            # d["Description"]=input("enter description : ")
                            d["D.O.B"]=input("enter D.O.B : ")
                            # d["Gender"]=input("enter your gender : ")
                            # d["Hobbies"]=input("enter your hobbies : ")
                            dic["Profile"]=d
                            v=a["user"]
                            v.append(dic)
                            f=open("Userdetails.json","w+")
                            json.dump(e,f,indent=4)  
                            f.close()
                            print("Signup Succesfully")
                            break  
                else:
                                
                    dic={}
                    l=[]
                    d={}
                    d1={}
                    dic["username"]=user_name
                    dic["password"]=password1
                    # d["description"]=input("enter the description : ")
                    # d["D.O.B"]=input("enter your D.O.B : ")
                    # d["Gender"]=input("enter your gender : ")
                    # d["Hobbies"]=input("enter your hobbies : ")
                    dic["Profile"]=d
                    l.append(dic)
                    d1["user"]=l
                    file=open("Userdetails.json","w+")
                    json.dump(d1,file ,indent=4)
                    file.close()
                    print("Signup Succesfully")            
        else:
            print("wrong password")  
    elif user=="login":
        e=open("Userdetails.json","r")                 
        f=json.load(e)
        g=input("Enter your user name for login:")
        h=input("Enter your password for login:")
        for i in f["user"]:
            if g==i['username']:
                if h==i['password']:
                    print("Login successful")
                    print(i)
                    break
                else:
                    print("Check your username")
            else:
                print("Check your password")
    else:
        print("Your enter worng input ")       
my()