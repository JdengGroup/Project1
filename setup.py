
import cx_Oracle
import getpass

class Setup():
    def __init__(self):
        self.cursor=cur
        
    def setData(cur):
        cur.execute('''INSERT INTO people
        VALUES ('ID001','Takeshi',180,70,'black','black','Edmonton west','m','01-JAN-1991')''')
        
        cur.execute('''INSERT INTO people
        VALUES ('ID002','Mary',160,50,'blue','yellow','Edmonton east','f','15-APR-1991')''')
        
        cur.execute('''INSERT INTO people
        VALUES ('ID003','Robert',175,75,'brown','brown','Calgary','m','23-MAY-1970')''')
        
        cur.execute('''INSERT INTO people
        VALUES ('ID004','Yamashita',170,60,'black','black','Some random place','m','29-AUG-1960')''')
        
        cur.execute('''INSERT INTO people
        VALUES ('ID005','Michiko',167,63,'black','black','Some random island ','f','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO people
        VALUES ('ID006','Suzuki',167,63,'black','black','Some random island ','f','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO people
        VALUES ('ID007','Sue',165,55,'black','brown','Other places','f','30-DEC-1993')''')
        
        
        cur.execute('''INSERT INTO drive_licence
        VALUES ('LN001','ID001','A', NULL ,'30-SEP-1956','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO drive_licence
        VALUES ('LN002','ID002','A', NULL ,'30-SEP-1956','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO drive_licence
        VALUES ('LN003','ID003','A', NULL ,'30-SEP-1956','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO drive_licence
        VALUES ('LN004','ID004','A', NULL ,'30-SEP-1956','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO drive_licence
        VALUES ('LN005','ID005','N', NULL ,'30-SEP-1956','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO drive_licence
        VALUES ('LN006','ID006','A', NULL ,'30-SEP-1956','30-SEP-1956')''')
        
        cur.execute('''INSERT INTO drive_licence
        VALUES ('LN007','ID007','A', NULL ,'30-SEP-1956','30-SEP-1956')''')
        
        
        
        cur.execute('''INSERT INTO driving_condition
        VALUES (1,'lololol')''')
        
        cur.execute('''INSERT INTO driving_condition
        VALUES (2,'hahaha')''')
        cur.execute('''INSERT INTO driving_condition
        VALUES (3,'glasses')''')


        
        
        
        
        
        
        cur.execute('''INSERT INTO restriction
        VALUES ( 'LN001',1)''')
        cur.execute('''INSERT INTO restriction
        VALUES ( 'LN002',1)''')        
        cur.execute('''INSERT INTO restriction
        VALUES ( 'LN003',2)''')                
        cur.execute('''INSERT INTO restriction
        VALUES ( 'LN004',3)''')                
        cur.execute('''INSERT INTO restriction
        VALUES ( 'LN005',2)''')                
        cur.execute('''INSERT INTO restriction
        VALUES ( 'LN006',3)''')   
        cur.execute('''INSERT INTO restriction
        VALUES ( 'LN007',1)''') 

        
        cur.execute('''INSERT INTO vehicle_type
        VALUES (1,'suv')''')
        
        cur.execute('''INSERT INTO vehicle_type
        VALUES (2,'van')''')
        
        cur.execute('''INSERT INTO vehicle_type
        VALUES (3,'car')''')
        
        
        
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR001','maker1','M001',2000,'Red',1)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR002','maker2','M002',1994,'Red',2)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR003','maker3','M003',2012,'Blue',2)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR004','maker4','M004',2007,'Black',3)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR005','maker1','M004',2007,'Red',1)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR006','maker4','M004',2001,'Red',1)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR007','maker4','M004',2001,'Red',1)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR008','maker4','M004',2001,'Red',1)''')
        
        cur.execute('''INSERT INTO vehicle
        VALUES ('SR009','maker5','M005',2002,'Red',1)''')
        
        
        cur.execute('''INSERT INTO owner
        VALUES ('ID001','SR001','y')''')
        
        cur.execute('''INSERT INTO owner
        VALUES ('ID002','SR002','y')''')
        
        cur.execute('''INSERT INTO owner
        VALUES ('ID003','SR003','y')''')
        
        cur.execute('''INSERT INTO owner
        VALUES ('ID004','SR004','y')''')
        
        cur.execute('''INSERT INTO owner
        VALUES ('ID001','SR005','y')''')
        
        cur.execute('''INSERT INTO owner
        VALUES ('ID001','SR006','y')''')
        
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (0,'ID001','ID002','SR001','30-DEC-2012',20000)''')
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (1,'ID002','ID003','SR002','30-DEC-1993',500)''')
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (2,'ID003','ID002','SR003','30-DEC-2005',3000)''')
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (3,'ID004','ID002','SR004','30-DEC-2009',70000)''')
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (4,'ID005','ID002','SR005','30-DEC-2003',3000)''')
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (5,'ID006','ID002','SR006','30-DEC-2007',50000)''')
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (6,'ID007','ID002','SR007','30-DEC-2030',200100)''')
        
        cur.execute('''INSERT INTO auto_sale
        VALUES (7,'ID007','ID002','SR008','30-DEC-2007',20000)''')
        
        
        
        cur.execute('''INSERT INTO ticket_type
        VALUES ('parking',200)''')
        
        cur.execute('''INSERT INTO ticket_type
        VALUES ('eat',500)''')
        
        cur.execute('''INSERT INTO ticket_type
        VALUES ('random',500)''')
        
        cur.execute('''INSERT INTO ticket_type
        VALUES ('carry',500)''')
        
        cur.execute('''INSERT INTO ticket_type
        VALUES ('sleep',500)''')
        
        
        
        
        cur.execute('''INSERT INTO ticket
        VALUES (0,'ID001','SR001','ID002','parking','30-APR-2009','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (1,'ID002','SR002','ID003','parking','30-APR-2011','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (2,'ID003','SR003','ID002','parking','30-APR-2007','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (3,'ID004','SR004','ID002','parking','30-APR-2001','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (4,'ID005','SR005','ID002','random','30-APR-2003','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (5,'ID006','SR006','ID002','sleep','30-JAN-2014','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (6,'ID006','SR006','ID002','sleep','30-JAN-2014','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (7,'ID006','SR006','ID002','sleep','30-JAN-2014','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (8,'ID007','SR007','ID002','eat','30-JAN-2014','Edmonton','LOLZ')''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (9,'ID007','SR007','ID002','eat','30-JAN-2014','Edmonton','LOLZ') ''')
        
        cur.execute('''INSERT INTO ticket
        VALUES (10,'ID007','SR007','ID002','eat','30-JAN-2014','Edmonton','LOLZ') ''')
    def setTable(cur):

        print("Database population starting.")
        try:
            cur.execute("drop table owner")
            cur.execute("drop table auto_sale")
            cur.execute("drop table restriction")
            cur.execute("drop table driving_condition")
            cur.execute("drop table ticket")
            cur.execute("DROP TABLE ticket_type")
            cur.execute("DROP TABLE vehicle")
            cur.execute("DROP TABLE vehicle_type")
            cur.execute("DROP TABLE drive_licence")
            cur.execute("DROP TABLE people")
            cur.execute("DROP VIEW vehicle_history")
            curs.execute("DROP SEQUENCE transactionId")
        except cx_Oracle.DatabaseError as de:
            print("Did not drop all tables.")
        cur.execute("""CREATE TABLE  people (
        sin           CHAR(15),  
        name          VARCHAR(40),
        height        number(5,2),
        weight        number(5,2),
        eyecolor      VARCHAR (10),
        haircolor     VARCHAR(10),
        addr          VARCHAR2(50),
        gender        CHAR,
        birthday      DATE,
        PRIMARY KEY (sin),
        CHECK ( gender IN ('m', 'f') )
        )""")
        cur.execute("""CREATE TABLE drive_licence (
        licence_no      CHAR(15),
        sin             char(15),
        class           VARCHAR(10),
        photo           BLOB,
        issuing_date    DATE,
        expiring_date   DATE,
        PRIMARY KEY (licence_no),
        UNIQUE (sin),
        FOREIGN KEY (sin) REFERENCES people
            ON DELETE CASCADE
            )""")
        cur.execute("""CREATE TABLE driving_condition (
        c_id        INTEGER,
        description VARCHAR(1024),
        PRIMARY KEY (c_id)
        )""")
        cur.execute("""CREATE TABLE restriction(
        licence_no   CHAR(15),
        r_id         INTEGER,
        PRIMARY KEY (licence_no, r_id),
        FOREIGN KEY (licence_no) REFERENCES drive_licence,
        FOREIGN KEY (r_id) REFERENCES driving_condition
        )""")
        cur.execute("""CREATE TABLE vehicle_type (
        type_id       integer,
        type          CHAR(10),
        PRIMARY KEY (type_id)
        )""")
        cur.execute("""CREATE TABLE vehicle (
        serial_no    CHAR(15),
        maker        VARCHAR(20),	
        model        VARCHAR(20),
        year         number(4,0),
        color        VARCHAR(10),
        type_id      integer,
        PRIMARY KEY (serial_no),
        FOREIGN KEY (type_id) REFERENCES vehicle_type
        )""")
        cur.execute("""CREATE TABLE owner (
        owner_id          CHAR(15),
        vehicle_id        CHAR(15),
        is_primary_owner  CHAR(1),
        PRIMARY KEY (owner_id, vehicle_id),
        FOREIGN KEY (owner_id) REFERENCES people,
        FOREIGN KEY (vehicle_id) REFERENCES vehicle,
        CHECK ( is_primary_owner IN ('y', 'n'))
        )""")
        cur.execute("""CREATE TABLE auto_sale (
        transaction_id  int,
        seller_id   CHAR(15),
        buyer_id    CHAR(15),
        vehicle_id  CHAR(15),
        s_date      date,
        price       numeric(9,2),
        PRIMARY KEY (transaction_id),
        FOREIGN KEY (seller_id) REFERENCES people,
        FOREIGN KEY (buyer_id) REFERENCES people,
        FOREIGN KEY (vehicle_id) REFERENCES vehicle
        )""")
        cur.execute("""CREATE TABLE ticket_type (
        vtype     CHAR(10),
        fine      number(5,2),
        PRIMARY KEY (vtype)
        )""")
        cur.execute("""CREATE TABLE ticket (
        ticket_no     int,
        violator_no   CHAR(15),  
        vehicle_id    CHAR(15),
        office_no     CHAR(15),
        vtype        char(10),
        vdate        date,
        place        varchar(20),
        descriptions varchar(1024),
        PRIMARY KEY (ticket_no),
        FOREIGN KEY (vtype) REFERENCES ticket_type,
        FOREIGN KEY (violator_no) REFERENCES people ON DELETE CASCADE,
        FOREIGN KEY (vehicle_id)  REFERENCES vehicle,
        FOREIGN KEY (office_no) REFERENCES people ON DELETE CASCADE
        )""")    