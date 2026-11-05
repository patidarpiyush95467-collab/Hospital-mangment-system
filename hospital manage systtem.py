doctors = {}
petiants = {}
apoiments = {}
def doctor():
    try:

       def Add_doctor():
            try:
            
                doctor_id = int(input("enter docator id :"))
                if doctor_id in doctors:
                   print("doctor allrady exist")
                else:
                  
                       name =input("enter doctor name :")
                       sapelisation = input("enter ypur spelisation")
                       address = input("enter your address  :")
                       salry = int(input('enter yor selary :'))
                       doctors[doctor_id] ={
                           
                           "name" : name,
                           "spelisation": sapelisation,
                           "address" : address,
                           "salry" : salry,

                       }
                       print("doctor data is added")
            except(ValueError):
                print("enter vailed information")
       def update_doctor():
            try:
               doctor_id = int(input("enter doctor id"))
               if doctor_id in doctors:
                    print("update doctor data")
                    new_name = input("enter new name")
                    new_sapelisation = input("enter new spalisation :")
                    new_address = input("enter new address")
                    new_salry = int(input("enter new salry"))
                    doctors[doctor_id]={
                        "name" : new_name,
                        "spelisation": new_sapelisation,
                        "address": new_address,
                        "salry" : new_salry,

                          }
                    print("doctor data is update")
               else:
                   print("doctor id is not found")
            except(ValueError):
                print("enter vaild information")
       def delete_doctor():
           try:
               doctor_id = int(input("enter doctor id"))
               if doctor_id in doctors:
                   del doctors[doctor_id]
                   print("doctor data is deleted ")
               else:
                   print("doctor id is not found")
           except(ValueError):
               print("enter vaild information")
       def view_doctor():
           try:
            
                   if len(doctors) == 0:
                        print("doctor data is not found")
                   else:
                        doctor_id = int(input("enter doctor id"))
                        if doctor_id in doctors:
                            doctor_data = doctors[doctor_id]
                        
                            print(f"doctor id : {doctor_id}")
                            print(f"doctor name : {doctor_data['name']}")
                            print(f"Doctor Specialisation: {doctor_data['spelisation']}")
                            print(f"doctor address : {doctor_data['address']}")
                            print(f"doctor salry : {doctor_data['salry']}")
                        else:
                            print("doctor id is not found")
           except(ValueError):
               print("enter vaild information")
       while True:

            print("---Doctor data---")
            print("1 add doctor ")
            print("2 update doctor data")
            print("3 delete doctor data")
            print("4 view doctor data")
            print("5 exit")
            choise = int(input("enter your choise"))
            if choise == 1:
                Add_doctor()
            elif choise == 2:
                update_doctor()
            elif choise == 3:
                delete_doctor()
            elif choise == 4:
                view_doctor()
            elif choise == 5:
                print("doctor data exit")
                return
            else:
                print("enter vailed choise to check doctor data")

    except(ValueError):
        print("enter vailed information")

             

def petiant_data():
    try:


        def add_petiant():
            try:
                petiant_id =int(input("enter petant id"))
                if petiant_id in petiants:
                    print("petiant id is allrady exit")
                else:
                    
                        name = input("enter your name")
                        adhar_no = int(input("enter your adhar no."))
                        report = input("enter your report")
                        petiants[petiant_id] = {
                            "name" : name,
                            "adhar no" : adhar_no,
                            "report" : report,
                            
                        }
            except(ValueError):
                print("enter vailed information")
        def update_petiant():
            try:
                petiant_id = int(input("enter petiant id"))
                if petiant_id in petiants:
                    new_name = input("enter new name")
                    new_adhar_no = int(input("enter new adhar no"))
                    new_report = input("enter new report")
                    petiants[petiant_id] = {
                        "name" : new_name,
                        "adhar no." : new_adhar_no,
                        "report" : new_report,

                    }
                else:
                    print("enter corect petiant id")
            except (ValueError):
                print("enter velid information")
        def delete_petiant():
            try:
                petiant_id = int(input("enter petiant id"))
                if petiant_id in petiants:
                    del petiants[petiant_id]
                    print("petiant data was deleted")
                else:
                    print("enter curect petiant id ")
            except (ValueError):
                print("enter velied information")
        def view_petiant():
            try:
                if len(petiants) == 0:
                    print("petiant data is not found")
                else:
                    petiant_id = int(input("enter petiant id"))
                    petiant_data = petiants[petiant_id]
                    print(f"petiant id : {petiant_id}")
                    print(f"petiant name : {petiant_data["name"]}")
                    print(f"adhar no. : {petiant_data["adhar no"]}")
                    print(f"report : {petiant_data["report"]}")
            except (ValueError):
                print("enter velied information")



            try:
                petiant_id = int(input("enter petiant ID to update"))
                if petiant_id in petiants:
                    name = input("enter updated name")
                    address = input("enter updated address")
                    adhar_no = int(input("enter updated adhar no."))
                    report = input("enter updated report")
                    petiants[petiant_id] = {
                        "name" : name,
                        "address" : address,
                        "adhar no" : adhar_no,
                        "report" : report
                    }
                else:
                    print("petiant not found")
            except(ValueError):
                print("enter vailed information")
        while True:
                print("----petient data----")
                print("1 add petiant data")
                print("2 update petiant data")
                print("3 delete petiant data")
                print("4 view petiant data")
                print("5 exit")
                choise = int(input("enter your choise"))
                if choise == 1:
                    add_petiant()
                elif choise ==2:
                    update_petiant()
                elif choise ==3:
                    delete_petiant()
                elif choise == 4:
                    view_petiant()
                elif choise == 5:
                    print("petiwnt detailes was be exit")
                    return
                else:
                    print("invelied choise")
    except(ValueError):
        print("enter vailed information")
def apoiment_data():
    try: 
        def add_apoiment():
            try:
                apoiment_id = int(input("enter apoiment ID"))
                if apoiment_id in apoiments:
                    print("ID is allrady exit")
                else:
                    name = input("enter your name")
                    address = input("enter your address")
                    emaile_id = input("enter your emaile id")
                    apoiments[apoiment_id] = {
                        "name" : name,
                        "Address" : address,
                        "emaile ID" : emaile_id,
                    }

                    print("apoiment added sucessfuly")
            except ValueError:
                print("enter velied information")
        def delete_apoiment():
            try:
                apoiment_id = int(input("enter apoiment id"))
                if apoiment_id in apoiments:
                    del apoiments[apoiment_id]
                    print("your apoiment is deleted")
                else:
                    print("enter velied apoiment id")
            except ValueError:
                print("enter velid innformation")
        def upadete_apoiment():
            try:
                apoiment_id = int(input("enter apoiment Id"))
                if apoiment_id in apoiments:
                    new_name = input("enter new apoiment Id")
                    new_address = input("enter your address")
                    new_emaile_id = input("enter your emaile id")
                    apoiments[apoiment_id] = {
                        "name" : new_name,
                        "Address" : new_address,
                        "emaile ID" : new_emaile_id,
                    }
                else:
                    print("enter curect apoiment id")
            except ValueError:
                print("enter velied information")
        def view_apoiment():
            try:
                if len(apoiments )== 0:
                    print("enter velied apoiment id")
                else:
                    apoiment_id = int(input("enter velied apoiment id"))
                    apoiment_data = apoiments[apoiment_id]
                    print(f"apooiment id : {apoiment_id}")
                    print(f"name: {apoiment_data["name"]}")
                    print(f"address : {apoiment_data["Address"]}")
                    print(f"emaile id : {apoiment_data["emaile ID"]}")
            except ValueError:
                print("enter velied information")

        while True:
            print("----apoiment data----")
            print("1 add apoiment")
            print("2 delete apoiment")
            print("3 update apoiment")
            print("4 view apoiment")
            print("5 exit")

            choise = int(input("enter your choise"))
            if choise == 1:
                add_apoiment()
            elif choise == 2 :
                delete_apoiment()
            elif choise == 3:
                upadete_apoiment()
            elif choise == 4:
                view_apoiment()
            elif choise == 5:
                print("apoiment was exit")
                return
            else:
                print("enter velid choise")
    except ValueError:
        print("enter velid information")
def main():
    try:
        while True:
        
            print("1 doctor data")
            print("2 petiant data")
            print("3 apoiment data")
            print("4 exit")
            choise = int(input("enter your choise "))
            if choise == 1:
                doctor()
            elif choise == 2:
                petiant_data()
            elif choise == 3:
                apoiment_data()
            elif choise == 4:
                print("exit")
                return
            else:
                print("enter velid choise to check hospital data")
    except ValueError:
        print("enter velied informetion")
main()
