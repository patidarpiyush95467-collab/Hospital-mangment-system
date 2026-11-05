studants = {}
teachers ={}

def teacher():
    try:
        choise = int(input("enter your choisee"))
        for i in range(choise):
            teacher_id = int(input("enter teacher ID"))
            if teacher_id not in teachers:
                password = int(input("enter your teacher ID password"))
                name = input("ente your name")
                DOB = input("enter your DOB")
                Mobaile_no = int(input("enter your number"))
                profesion = input("enter your profesion")
                Emaile_ID = input("enter your emaile ID")
                salry = int(input("enter your salry"))
                teachers[teacher_id] = {
                   
                    "name": name,
                    "birth date": DOB,
                    "MObaile no": Mobaile_no,
                    "profesion" : profesion,
                    "email ID " : Emaile_ID,
                    "salry" : salry,
                    "password" : password,
                }  

            else:
                print("teacher ID allrady exist")
    except ValueError:
         print("enter vaild Input")        

def studant():
    try:
        teacher_id = int(input("enter teacher ID"))
        password =int(input("enter your password"))
        if teacher_id in teachers :
                if password == teachers[teacher_id]["password"]:
                   print("rady to add studant")
                   choise = int(input("enter your choise"))
                   for i in range(choise):
                       studant_id = int(input("enter yor studantID"))
                       if studant_id not in studants:
                           name = input("enter your name")
                           Age = int(input("enter your age"))
                           Address = input("enterr your address")
                           father_name = input("enter your father name")
                           class_name = input("enter your class name")
                           password = int(input("enterr studant ID password"))
                           studants[studant_id] = {
                                                        "name" : name,
                                                        "age" : Age,
                                                        "address" : Address,
                                                        "father name " : father_name,
                                                        "class" : class_name,
                                                        "password" : password,
                                                        
                                                   }
                       else:
                           print("studant ID allrady exit")
                else:
                   print("password was incorect")
        else:
            print("teacher ID was incorect")
    except ValueError:
        print("enterr valid input")


def teacher_dashboard():
    try:
        print("----teacher dashboard----")
        print("1 teacher profaile")
        print("2 change password")
        print("3 delete teacher profaile")
        print("4 update teacher profaile")
        print("5 exit")
        choise= int(input("enter  your coise"))
        if choise ==1:
            teacher_id = int(input("enter tracher id"))
            password = int(input("enter your password"))
            if teacher_id in teachers:
                if password == teachers[teacher_id]["password"]:
             
                    print("Login successful")
                    print("Name:", teachers[teacher_id]["name"])
                    print("DOB", teachers[teacher_id]["birth date"])
                    print("Mobile:", teachers[teacher_id]["MObaile no"])
                    print("Profession:", teachers[teacher_id]["profesion"])
                    print("Email:", teachers[teacher_id]["email ID "])
                    print("Salary:", teachers[teacher_id]["salry"])
                else:
                    print("password was incorrect")
            else:
                print("enterr valid teacher id")
        elif choise == 2:
            teacher_id = int(input("enter teacher id"))
            password = int(input("enter teacher id password"))
            if teacher_id in teachers:
                if password == teachers[teacher_id]["password"]:
                    new_password = int(input("enter your new password"))
                    teachers[teacher_id]["password"] = new_password
                    print("password saved succesfully")
                else:
                    print("passsword was incoreect")
            else:
                print("teacher id was incorect")
        elif choise == 3:
            teacher_id = int(input("enter your teacher Id"))
            password = int(input("enter your password"))
            if teacher_id in teachers :
                if password == teachers[teacher_id]["password"]:
                    del teachers[teacher_id]
                    print("teacher profaile was deleted")
                else:
                    print("passwor was incorrect")
            else:
                print("teacher ID was in corrrect")
        elif choise == 4:
            teacher_id = int(input("enter your teacher Id"))
            password = int(input("enter your password"))
            if teacher_id in teachers :
                if password == teachers[teacher_id]["password"]:
                                print("update teacher data")
                                print("1 update name")
                                print("2 update DOB")
                                print("3 update mobaile no.")
                                print("4 update profesion")
                                print("5 update emaile ID")
                                print("6 update salry")
                                print("7 exit")
                                choise = int(input("enterr your choice"))
                                if choise == 1:
                                    new_name = input("enter your new name")
                                    teachers[teacher_id]["name"]=new_name
                                    print("update was sucesssfully")
                                elif choise == 2:
                                    new_DOB = input("enter your new DOB")
                                    teachers[teacher_id]["birth date"]= new_DOB
                                    print("update was suceessfully")
                                elif choise == 3:
                                    new_mobile_no = int(input("enter your new mobile no."))
                                    teachers[teacher_id]["mobaile_no"] = new_mobile_no
                                    print("update was succesfully")
                                elif choise == 4:
                                    new_profesion = input("enter your new profesion")
                                    teachers[teacher_id]["profesion"] = new_profesion
                                    print("update was succesfully")
                                elif choise == 5:
                                    new_emaile_Id = input("enter your new emaile ID")
                                    teachers[teacher_id]["emaile_ID"] = new_emaile_Id
                                    print("update was sussesfully")
                                elif choise == 6:
                                    new_salry = int(input("enter your new salry"))
                                    teachers[teacher_id]["salry"]= new_salry
                                    print("update was succcessfully")
                                elif choise == 7:
                                    print("exist")
                                else:
                                    print("enter valid input")
        elif choise == 5:
            print("exit")
        else:
            print("enter valid input")
    except ValueError:
        print("enter valid input")

def main():
    while True:
        try:
            print("----welcome to school mangment system----")
            print("1 add teacher")
            print("2 add studant")
            print("3 teacher dashboard ")
            print("4 student dashboard")
            print("5 exit")
            choise = int(input("enter your choise"))
            if choise == 1:
                teacher()
            elif choise == 2:
                studant()
            elif choise == 3:
                teacher_dashboard()
            elif choise == 4:
                print(" this feature is under devlopment")
            elif choise ==5:
                print("exist")
                break
            else:
                print("enter vailed input")
        except ValueError:
            print("enter vaild input")
main()                               






                
