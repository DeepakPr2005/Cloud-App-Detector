from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1320x505+211+280")
    
    ##### ================ Variables =====================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_IDProof=StringVar()
        self.var_IDNumber=StringVar()
        self.var_address=StringVar()
        
        
    ### =================== Title ======================
       
        lbl_title = Label(self.root,text="Add Customer Details", font=("Comic Sans MS",32,"bold"),bg="black",fg="gold", bd=0, relief= GROOVE)
        lbl_title.place(x=0,y=0,width=1500,height=55)
    
    ### =================  Logo  ========================    
        img2=Image.open(r"C:\Users\Admin\OneDrive\Pictures\Saved Pictures\Deepak-382126006.jpg")
        img2=img2.resize((90,55),Image.ANTIALIAS)
        
        self.photoimg2 =ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0,y=0,width=90,height=55)
    
  # ====================     Label     =================================
        labelframeleft = LabelFrame(self.root, bd=2, relief= RIDGE ,text="Customer Details", font=("times new roman",16,"bold"),padx=2)
        labelframeleft.place(x=4,y=57,width=357,height=448)    
            # padx is used for space between x and y axis
    
  # ====================     Label and Entry     =================================
     ####  Cust Ref 
        lbl_cust_ref = Label(labelframeleft,font=("arial",12,"bold"),text="Customer Ref",bd=1,padx= 2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
    
        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref,width=23,font=("arial",12,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)
        
     ####  Cust Name
        
        cname = Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name",bd=1,padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
    
        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=23,font=("arial",12,"bold"))
        txtcname.grid(row=1,column=1)
    ####   Mother Name 
        
        lblname = Label(labelframeleft,text="Mother",font=("arial",12,"bold"),bd=2,padx=2,pady=6)
        lblname.grid(row=2,column=0,sticky=W)
    
        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother,width=23,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        
    ####   Gender Combo box
        label_gender = Label(labelframeleft,text="Gender",font=("arial",12,"bold"),bd=1,padx=2,pady=4)
        label_gender.grid(row=3,column=0,sticky=W)
    
            # How to make a Combobox
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",13,"bold"),width=21,state="readonly")
           ###   State = "readonly" becaue it will not allow you to write in the box
       
        combo_gender["value"]=("               Select","M","F","O")
        combo_gender.current(0)
            ###  0 = index no from where to start
            
        combo_gender.grid(row=3,column=1)
        
    ####   Post Code
        lblPostCode = Label(labelframeleft,text="Post Code:",font=("arial",12,"bold"),bd=1,padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
    
        txtPostCode = ttk.Entry(labelframeleft,textvariable=self.var_post,width=23,font=("Arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)
    
    ####   Mobile Number
        lblMobile = Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),bd=1,padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
    
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=23,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)
        
     ####   Email
        lblEmail = Label(labelframeleft,text="Email",font=("arial",12,"bold"),bd=1,padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
    
        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_email,width=23,font=("arial",13,"bold"))
        enty_ref.grid(row=6,column=1)
    
    ####   Nationality
        lblNationality = Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),bd=1,padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
    
        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",13,"bold"),width=21,state="readonly")
        combo_nationality["value"]=(" ","American","British","Indian","Other")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        
        
    ####   ID Proof Type ComboBox
        lblIDProof = Label(labelframeleft,text="ID Type",font=("arial",12,"bold"),bd=1,padx=2,pady=6)
        lblIDProof.grid(row=8,column=0,sticky=W)
    
        combo_ID=ttk.Combobox(labelframeleft,textvariable=self.var_IDProof,font=("arial",13,"bold"),width=21,state="readonly")
        combo_ID["value"]=(" ","Adhaar Card","Driving Licence","Pan Card","Other")
        combo_ID.current(0)
        combo_ID.grid(row=8,column=1)
        
#      ####   ID Number 
        lblIDNumber = Label(labelframeleft,text="ID Number",font=("arial",12,"bold"),bd=1,padx=2,pady=6)
        lblIDNumber.grid(row=9,column=0,sticky=W)
    
        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_IDNumber,width=23,font=("arial",13,"bold"))
        enty_ref.grid(row=9,column=1)
        
    ####   Address
        lblAddress = Label(labelframeleft,text="Address",font=("arial",12,"bold"),bd=1,padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
    
        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_address,width=23,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)
    
#     ####  ======================  Buttons  ====================================
        # btn_frame=Frame(labelframeleft,bd=2,relief=RIGE)
        # btn_frame.place(x=0,y=370,width=348,height=35)  
        
#         btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("Comic Sans MS",11,"bold"),bd=1,width=9,bg="black",fg="gold")
#         btnAdd.grid(row=0,column=0,padx=1)
        
#         btnupdate=Button(btn_frame,text="Update",font=("Comic Sans MS",11,"bold"),bd=1,width=9,bg="black",fg="gold")
#         btnupdate.grid(row=0,column=1,padx=1)
        
#         btnDelete=Button(btn_frame,text="Delete",font=("Comic Sans MS",11,"bold"),bd=1,width=9,bg="black",fg="gold")
#         btnDelete.grid(row=0,column=2,padx=1)
        
        # btnReset=Button(btn_frame,text="Reset",font=("Comic Sans MS",11,"bold"),bd=1,width=9,bg="black",fg="gold")
        # btnReset.grid(row=0,column=3,padx=1)
        
          
    ####       Label Frame
        Table_Frame = LabelFrame(self.root,text="\t\tView Details and Search System", font=("times new roman",21,"bold"), bd=0, relief= RIDGE,padx=2)
        Table_Frame.place(x=415,y=65,width=860,height=490)  
        
        lblSearchBy=Label(Table_Frame,text="Search By:", font=("arial",12,"bold"), bd=2,bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)  
        
        combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),text="",width=27,state="readonly")
        combo_Search["value"]=(" ","Mobile No.","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)   
        
        txtSearch = ttk.Entry(Table_Frame,width=27,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
#      ###      Buttons
        btnSearch=Button(Table_Frame,text="Search",font=("arial",11,"bold"),width=12,bg="black",fg="gold")
        btnSearch.grid(row=0,column=3,padx=1)   
        
        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",11,"bold"),width=12,bg="black",fg="gold")
        btnShowAll.grid(row=0,column=4,padx=1)
     
     ####    Show Data Table  
        details_table=Frame(Table_Frame,bd=4,relief=RIDGE)
        details_table.place(x=0,y=50,width=880,height=345)
        
    ####        Scroll Bar
        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)   
                    ### Orient is of 2 types Horizontal and Vertical
                    
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)            
                    
        self.Cust_details_table=ttk.Treeview(details_table,column=("ref","Name","Mother","Gender","Post","Mobile","Email","Nationality","IDProof","IDNumber","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)          
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)
        
        ######### For columns in Customer Table
        
        self.Cust_details_table.heading("ref",text="Refer No.")
        self.Cust_details_table.heading("Name",text="Name",)
        self.Cust_details_table.heading("Mother",text="Mother Name")
        self.Cust_details_table.heading("Gender",text="Gender")
        self.Cust_details_table.heading("Post",text="PostalCode")
        self.Cust_details_table.heading("Mobile",text="Mobile Number")
        self.Cust_details_table.heading("Email",text="Email")
        self.Cust_details_table.heading("Nationality",text="Nationality")
        self.Cust_details_table.heading("IDProof",text="ID Proof")
        self.Cust_details_table.heading("IDNumber",text="ID Number")
        self.Cust_details_table.heading("Address",text="Address")
        
        #####      To Show Headings in the Table
        self.Cust_details_table["show"]="headings"
        
#                 ###        Column Names
        self.Cust_details_table.column("ref",width=100)
        self.Cust_details_table.column("Name",width=100)
        self.Cust_details_table.column("Mother",width=100)
        self.Cust_details_table.column("Gender",width=100)
        self.Cust_details_table.column("Post",width=100)
        self.Cust_details_table.column("Mobile",width=100)
        self.Cust_details_table.column("Email",width=100)
        self.Cust_details_table.column("Nationality",width=100)
        self.Cust_details_table.column("IDProof",width=100)
        self.Cust_details_table.column("IDNumber",width=100)
        self.Cust_details_table.column("Address",width=100)
        
        
             ###### To Pack the columns
#         self.Cust_details_table.pack(fill=BOTH,expand=1)
#         self.fetch_data()
        
        
#     def add_data(self):
#         if  self.var_mobile.get()=="" or self.var_mother.get()=="":
#             messagebox.showerror("Error","All Fields are requird",parent=self.root)
#         else:
#             conn=mysql.connector.connect(host="localhost",username="root",password="redhat",database="macdonaldss")
#             my_cursor=conn.cursor()
#             my_cursor.execute("insert into macdonald1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
#                                                                                         self.var_ref.get(),
#                                                                                         self.var_cust_name.get(),
#                                                                                         self.var_mother.get(),
#                                                                                         self.var_gender.get(),
#                                                                                         self.var_post.get(),
#                                                                                         self.var_mobile.get(),
#                                                                                         self.var_email.get(),
#                                                                                         self.var_nationality.get(),
#                                                                                         self.var_IDProof.get(),
#                                                                                         self.var_IDNumber.get(),
#                                                                                         self.var_address.get()
#                                                                                     ))
            ### %s = the no of columns in your table/database the no of %s you have to give

#             conn.commit()
#             self.fetch_data()
#             conn.close()
                
#             messagebox.showinfo("Successfull","Customer Has been Added",parent=self.root)
           
            
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="redhat",database="macdonaldss")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from macdonald1")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
#             conn.commit()
        conn.close()
                                  
if __name__ == "__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()