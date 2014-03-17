from searchEngin  import SearchEngin 
from setup import Setup
from question_2_4 import stc
import cx_Oracle
import getpass

'''
table = input("Table Name ")
values = input("Input values splited by comma ")
insertStatment = 'insert into'+ table + 'values (' + values + ');'

'''

#Set up connections
def connect():
    user='xindong1'
    if not user:
        user=getpass.getuser()
    #pw = getpass.getpass()
    pw='j69pbxq9'
    conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
    global cur,connection
    connection = cx_Oracle.connect(conString)  
    cur=connection.cursor()    


# Date handle function
def Date(Date):#input format DD-MM-YYYY, output DD-MM-YYYY where MMM is the first three charecters of a month in English
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
    stc.trans(cur)
    '''
    This component is used to complete an auto transaction. Your program shall allow the officer to enter all necessary information to complete this task, including, but not limiting to, the details about the seller, the buyer, the date, and the price. The component shall also remove the relevant information of the previous ownership.
    '''

# Driver Licence Registration
def DLReg():
    '''
    This component is used to record the information needed to issuing a drive licence, including the personal information and a picture for the driver. You may assume that all the image files are stored in a local disk system.
    '''

# Violation Record
def VioRcd():
    stc.vioRcd(cur)
    '''
    This component is used by a police officer to issue a traffic ticket and record the violation. You may assume that all the information about ticket_type has been loaded in the initial database.
    '''

# Search Engine
def Search(cur):
    #searchEngin.test(cur)
    a=SearchEngin(cur)
    #a.set_name('Takeshi')
    search_type=input("Choose search type below\n        1.Driver's information\n        2.Driver's ticket record\n\n------>")
    if search_type =='1':
        a.get_driver_info()
    elif search_type == '2':
        a.get_violation_rec()
    
    '''
    This component is used to perform the following searches.
List the name, licence_no, addr, birthday, driving class, driving_condition, and the expiring_data of a driver by entering either a licence_no or a given name. It shall display all the entries if a duplicate name is given.
List all violation records received by a person if  the drive licence_nor or sin of a person  is entered.
Print out the vehicle_history, including the number of times that a vehicle has been changed hand, the average price, and the number of violations it has been involved by entering the vehicle's serial number.
'''
    
    
# Main Function
def main():
    connect()
    Setup.setTable(cur)
    Setup.setData(cur)
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
            Search(cur)
            break

        else:
            print("\n\nInvalid application number!")
            appNum = input('Choose application number again\n------> ')
    connection.commit()
    connection.close()
    
main()
#print(Date(input()))


