
import cx_Oracle
import getpass


class SearchEngin():
    def __init__(self,cur):
        self.name=None
        self.licence_no=None
        self.sin=None
        #user = input("Username [%s]: " % getpass.getuser())
        self.cursor=cur
        
    def set_name(self,name):
        self.name=name

    def set_licence_no(self,licence_no):
        self.licence_no=licence_no

    def set_sin(self,sin):
        self.sin=sin
    def get_driver_info(self):
        valid=False
        while valid==False:
            inputType=input("Choose search type below\n        1.Driver's name\n        2.Driver's licence number\n\n------> ")
            if inputType=='1' or inputType=='2':
                valid=True
            
            
        if inputType=='1':
            parameter=input('Please enter name\n\n------> ')
            self.cursor.execute('''
            SELECT p.name, d.licence_no, p.addr, p.birthday, d.class, dc.description, d.expiring_date
            FROM drive_licence d ,people p , driving_condition dc , restriction r
            WHERE p.sin=d.sin AND
                  d.licence_no=r.licence_no AND
                  r.r_id=dc.c_id AND
                  p.name='''+"'"+ str(parameter) +"'")                
        elif inputType=='2':
            parameter=input("Please enter driver's licence number\n\n------> ")
            self.cursor.execute('''
            SELECT p.name, d.licence_no, p.addr, p.birthday, d.class, dc.description, d.expiring_date
            FROM drive_licence d ,people p , driving_condition dc , restriction r
            WHERE p.sin=d.sin AND
                  d.licence_no=r.licence_no AND
                  r.r_id=dc.c_id AND
                  d.licence_no='''+"'"+ str(parameter) +"'")
    
        #row = self.cursor.fetchone()
        row = self.cursor.fetchone()
        while row:
            print(row)
            row = self.cursor.fetchone()
    def get_violation_rec(self):
        valid=False
        while valid==False:
            inputType=input("Choose search type below\n        1.Driver's SIN\n        2.Driver's licence number\n\n------> ")
            if inputType=='1' or inputType=='2':
                valid=True        
        
        
        
        if inputType=='1':
            parameter=input('Please enter SIN\n\n------> ')
            self.cursor.execute('''
            SELECT t.ticket_no, p.name, t.vehicle_id , t.office_no, t.vtype , t.vdate, t.place, t.descriptions, tt.fine
            FROM ticket t, people p , ticket_type tt,drive_licence d
            WHERE t.violator_no = p.sin AND
                  tt.vtype=t.vtype AND
                  p.SIN='''+"'"+ str(parameter) +"'")            
        elif inputType=='2':
            parameter=input("Please enter driver's licence number\n\n------> ")
            self.cursor.execute('''
                SELECT t.ticket_no, p.name, t.vehicle_id , t.office_no, t.vtype , t.vdate, t.place, t.descriptions, tt.fine
                FROM ticket t, people p , ticket_type tt , drive_licence d
                WHERE t.violator_no = p.sin AND
                      tt.vtype=t.vtype AND
                      d.sin=p.sin AND
                      
                      d.licence_no='''+"'"+ str(parameter) +"'")
        row = self.cursor.fetchone()
        while row:
            print(row)
            row = self.cursor.fetchone()
    #def get 
        

  
    
