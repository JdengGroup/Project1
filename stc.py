import cx_Oracle
import getpass

user = input("Username [%s]:" % getpass.getuser())
if not user:
    user = getpass.getuser()

pw = getpass.getpass()

conString = ''+user+'/'+pw+'@gwynne.cs.ualberta.ca:1521/CRS'
con = cx_Oracle.connect(conString)

curs = con.cursor()

'''
table = input("Table Name ")
values = input("Input values splited by comma ")
insertStatment = 'insert into'+ table + 'values (' + values + ');'
'''
# Date handle function
def Date(Date):#input format DD-MM-YYYY, output DD-MMM-YYYY where MMM is the first three charecters of a month in English
    date = Date.split('-')
    month_set = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    date[1] = month_set[int(date[1])-1]
    return "'" + '-'.join(date) + "'"

# New Vehicle Registration
def NewVehicle():
    '''
    This component is used to register a new vehicle by an auto registration officer. By a new vehicle, we mean a vehicle that has not been registered in the database. The component shall allow an officer to enter the detailed information about the vehicle and personal information about its new owners, if it is not in the database. You may assume that all the information about vehicle types has been loaded in the initial database.
    '''
    # vehicle( serial_no, maker, model, year, color, type_id )
    values = []
    values.append("'"+input('---------New Vehicle Registration Detailed Information----------\n'
                        'Vehicle Information: \n\tserial_no --> ')+"'")
    values.append("'"+input('\tmaker ------> ')+"'")
    values.append("'"+input('\tmodel ------> ')+"'")
    values.append(input('\tyear -------> '))
    values.append("'"+input('\tcolor ------> ')+"'")
    values.append(input('\ttype_id ----> '))
    Statement = 'insert into vehicle values (' + ', '.join(values) + ');'
    #print(Statement)
    #owner(owner_id, vehicle_id, is_primary_owner)
    vehicle_id = values[0]
    values = []
    values.append("'"+input('Ownership Infomation: \n\towner\'s sin number ------> ')+"'")
    values.append(vehicle_id)
    values.append("'"+input('\tis primary owner? (y/n) -> ')+"'")
    Statement = 'insert into owner values(' + ', '.join(values) + ');'
    #print(Statement)
    #people( sin, name, height,weight,eyecolor, haircolor,addr,gender,birthday )
    values = []
    values.append("'"+input('Personal Information:\n\tsin -------------------> ')+"'")
    values.append("'"+input('\tname ------------------> ')+"'")
    values.append(input('\theight ----------------> '))
    values.append(input('\tweight ----------------> '))
    values.append("'"+input('\teyecolor --------------> ')+"'")
    values.append("'"+input('\thaircolor -------------> ')+"'")
    values.append("'"+input('\taddr ------------------> ')+"'")
    values.append("'"+input('\tgender ----------------> ')+"'")
    values.append(Date(input('\tbirthday (DD-MM-YYYY) -> ')))
    Statement = 'insert into people values(' + ', '.join(values) + ');'
    print(Statement)
    '''
    values.append(input('input  ------> '))
    values.append(input('input  ------> '))
    values.append(input('input  ------> '))
    values.append(input('input  ------> '))
    '''
    
# Auto Transaction
def Trans():
    '''
    This component is used to complete an auto transaction. Your program shall allow the officer to enter all necessary information to complete this task, including, but not limiting to, the details about the seller, the buyer, the date, and the price. The component shall also remove the relevant information of the previous ownership.
    '''
    # auto_sale( transaction_id,seller_id, buyer_id, vehicle_id, s_date, price )
    values = []
    
    trans_exist = True
    while trans_exist == True:
        data = ("'"+input('---------Auto Transaction Detailed Information----------\n'
                        'Transaction Information: \n\ttransacstion_id --> ')+"'")
        query = ("SELECT transaction_id FROM auto_sale")
        if data not in curs.execute(query):
            values.append(data)
            trans_exist = False
        else:
            print("This trainsaction is existed. Please enter another number: ")
    
    seller_exist = False
    while seller_exist == False:
        data = ("'"+input('\tseller_id --------> ')+"'")
        query = ("SELECT people.sin FROM people")
        if data in curs.execute(query):
            values.append(data)
            seller_exist = True
        else:
            print("This ID is not existed. Please enter again: ")        
    
    buyer_exist = False
    while buyer_exist == False:
        data = ("'"+input('\tbuyer_id ---------> ')+"'")
        query = ("SELECT people.sin FROM people")
        if data in curs.execute(query):
            values.append(data)
            buyer_exist = True
            owner_id = data
        else:
            print("This ID is not existed. Please enter again: ")

    v_exist = False
    while v_exist == False:
        data = ("'"+input('\tvehicle_id -------> ')+"'")
        query = ("SELECT vehicle.serial_no FROM vehicle")
        if data in curs.execute(query):
            values.append(data)
            v_exist = True
            query = ("DELETE FROM owner WHERE owner.vehicle_id = "+data)
            curs.execute(query)
            vehicle_id = data
        else:
            print("This ID is not existed. Please enter again: ")   

    values.append(input('\ts_date -----------> '))
    values.append(input('\tprice ------------> '))
    
    statement = "(' + ', '.join(values) + ')"
    query = ("INSERT INTO auto_sale VALUES"+ statement)
    curs.execute(query)
    query = ("INSERT INTO owner VALUES(" + owner_id + "," + vehicle_id + ", yes)")
    curs.execute(query)

    # print(statement)

# Driver Licence Registration
def DLReg():
    '''
    This component is used to record the information needed to issuing a drive licence, including the personal information and a picture for the driver. You may assume that all the image files are stored in a local disk system.
    '''

# Violation Record
def VioRcd():
    '''
    This component is used by a police officer to issue a traffic ticket and record the violation. You may assume that all the information about ticket_type has been loaded in the initial database.
    '''
    values = []
    
    t_exist = True
    while t_exist == True:
        data = ("'"+input('---------Violation Record Detailed Information----------\n'
                        'Ticket Information: \n\tticket number ----> ')+"'")
        query = ("SELECT ticket_no FROM ticket")
        if data not in curs.execute(query):
            values.append(data)
            t_exist = False
        else:
            print("This ticket number is existed. Please enter another number: ")    
    
    violator_exist = False
    while violator_exist == False:
        data = ("'"+input('\tviolator number --> ')+"'")
        query = ("SELECT people.sin FROM people")
        if data in curs.execute(query):
            values.append(data)
            violator_exist = True
        else:
            print("This ID is not existed. Please enter again: ") 

    v_exist = False
    while v_exist == False:
        data = (input('\tvehicle number ---> '))
        query = ("SELECT vehicle.serial_no FROM vehicle")
        if data in curs.execute(query):
            values.append(data)
            v_exist = True
        else:
            print("This number is not existed. Please enter again: ")       

    officer_exist = False
    while officer_exist == False:
        data = ("'"+input('\toffice number ----> ')+"'")
        query = ("SELECT registering_officer.id FROM registering_officer")
        if data in curs.execute(query):
            values.append(data)
            officer_exist = True
        else:
            print("This number is not existed. Please enter again: ")    
    
    type_exist = False
    while type_exist == False:
        data = ("'"+input('\tvtype ------------> ')+"'")
        query = ("SELECT ticket_type.vtype FROM ticket_type")
        if data in curs.execute(query):
            values.append(data)
            type_exist = True
        else:
            print("This type ID is not existed. Please enter again: ")    

    values.append("'"+input('\tdate ------------> ')+"'")
    values.append("'"+input('\tplace ------------> ')+"'")
    values.append("'"+input('\tdescriptions -----> ')+"'")
    
    statement = '(' + ', '.join(values) + ')'    
    query = ("INSERT INTO ticket VALUES" + statement)
    curs.execute(query)    
    
    # print(statement)

# Search Engine
def Search():
    '''
    This component is used to perform the following searches.
List the name, licence_no, addr, birthday, driving class, driving_condition, and the expiring_data of a driver by entering either a licence_no or a given name. It shall display all the entries if a duplicate name is given.
List all violation records received by a person if  the drive licence_nor or sin of a person  is entered.
Print out the vehicle_history, including the number of times that a vehicle has been changed hand, the average price, and the number of violations it has been involved by entering the vehicle's serial number.
'''
    
    
# Main Function
def main():
    appNum = input("\nChoose application number below\n\t1. New Vehicle Registration\n\t2. Auto Transaction\n\t3. Driver Licence Registration\n\t4. Violation Record\n\t5. Search Engine\n\n------> ")
    status = False
    while status==False:
        if appNum=='1':
            NewVehicle()
            break
        elif appNum=='2':
            Trans()
            break
        elif appNum=='3':
            DLReg()
            break
        elif appNum=='4':
            VioRcd()
            break
        elif appNum=='5':
            Search()
            break
        else:
            print("\n\nInvalid application number!")
            appNum = input('Choose application number again\n------> ')
    
main()
#print(Date(input()))