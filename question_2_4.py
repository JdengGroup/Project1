class stc():
    
    def trans(curs):
        def Date(Date):#input format DD-MM-YYYY, output DD-MM-YYYY where MMM is the first three charecters of a month in English
            date = Date.split('-')
            month_set = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
            date[1] = month_set[int(date[1])-1]
            return "'" + '-'.join(date) + "'"
        
        '''
        This component is used to complete an auto transaction. Your program shall allow the officer to enter all necessary information to complete this task, including, but not limiting to, the details about the seller, the buyer, the date, and the price. The component shall also remove the relevant information of the previous ownership.
        '''
        # auto_sale( transaction_id,seller_id, buyer_id, vehicle_id, s_date, price )
        values = []
        
        trans_exist = True
        while trans_exist == True:
            data =int( (input('---------Auto Transaction Detailed Information----------\n'
                            'Transaction Information: \n\ttransacstion_id --> ')))
            query = ("SELECT transaction_id FROM auto_sale")
            curs.execute(query)
           # print(data)
           # print(curs.fetchall()[1][0]==data)
            find_one=False
            for item in curs.fetchall():
                if item[0]==data:
                    find_one=True
                    break
                else:
                    find_one=False
            if find_one ==True:
                print("This trainsaction is existed. Please enter another number: ")
            else:
                trans_exist=False
                values.append(str(data))            
    
        
        seller_exist = False
        while seller_exist == False:
            data = (input('\tseller_id --------> '))
            query = ("SELECT sin FROM people")
            curs.execute(query)
            #print(data)
            #print(curs.fetchall()[0][0].strip())
            #print(data==curs.fetchall()[0][0].strip())
            
            for item in curs.fetchall():
                if item[0].strip()==data:
                    seller_exist=True
            if seller_exist ==False:
                print("This ID is not existed. Please enter again: ")        
            values.append("'"+data+"'")
            
        buyer_exist = False
        while buyer_exist == False:
            data = (input('\tbuyer_id ---------> '))
            query = ("SELECT people.sin FROM people")
            curs.execute(query)
            for item in curs.fetchall():
                if item[0].strip()==data:
                    buyer_exist=True
            if buyer_exist==False:
                print("This ID is not existed. Please enter again: ")
            values.append("'"+data+"'")
        v_exist = False
        while v_exist == False:
            data = (input('\tvehicle_id -------> '))
            query = ("SELECT vehicle.serial_no FROM vehicle")
            curs.execute(query)
            for item in curs.fetchall():
                if item[0].strip()==data:
                    v_exist=True
                    query = ("DELETE FROM owner WHERE owner.vehicle_id = '"+data+"'")
                    curs.execute(query)
                    vehicle_id = data
            if v_exist==False:
                print("This ID is not existed. Please enter again: ")   
            values.append("'"+data+"'")    
    
        values.append(Date(input('\ts_date -----------> ')))
        values.append(input('\tprice ------------> '))
        print(','.join(values))
        
        
        statement = "("+','.join(values)+")"
        query = ("INSERT INTO auto_sale VALUES"+ statement)
        curs.execute(query)
        query = ("INSERT INTO owner VALUES(" + owner_id + "," + vehicle_id + ", yes)")
        curs.execute(query)
        curs.commit()
    def vioRcd(curs):
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
        curs.commit()
        # print(statement)
    
    # Search Engine    
