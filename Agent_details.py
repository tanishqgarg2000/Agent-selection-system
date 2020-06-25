from tkinter import *
from tkinter import ttk
import pymysql


class agent_data:
    
    def __init__(self):
        self.root=Tk()
        self.root.title("Agent Details.")
        self.root.geometry("1300x650+0+0")
        self.root.resizable(False,False)
        
        #______________ALL VARIABLE______________
        self.id=StringVar()
        self.name=StringVar()
        self.phno=StringVar()
        self.gender=StringVar()
        self.isavailable=StringVar()
        self.availsince=StringVar()
        self.role=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
         
         
         
        #______________Title_____________
        title=Label(self.root,text="Agent Record System",font=("times new roman",25,"bold"),bg="white",fg="black",bd=8,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #______________MANAGE_FRAMES______________
        manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        manage_frame.place(x=20,y=70,width=450,height=560)
        
         
        m_title=Label(manage_frame,text="Manage Record",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=5,pady=10,padx=110)
        
        
        
        lbl_id=Label(manage_frame,text="Agent ID.",font=("times new roman",15,"bold"))
        lbl_id.grid(row=1,column=0,pady=10,padx=10,sticky="w")
        
        txt_id=Entry(manage_frame,textvariable=self.id,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_id.grid(row=1,column=1,pady=10,padx=10,sticky="w")
        
        
        
        lbl_name=Label(manage_frame,text="Name",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")
        
        txt_name=Entry(manage_frame,textvariable=self.name,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=10,sticky="w")
        
        
        
        lbl_phno=Label(manage_frame,text="Phone No.",font=("times new roman",15,"bold"))
        lbl_phno.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        
        txt_phno=Entry(manage_frame,textvariable=self.phno,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_phno.grid(row=3,column=1,pady=10,padx=10,sticky="w")
        
        
        
        lbl_gender=Label(manage_frame,text="Gender",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=10,sticky="w")
        
        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender,font=("times new roman",14),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=10,sticky="w")

        
        
        lbl_isavail=Label(manage_frame,text="Is Available",font=("times new roman",15,"bold"))
        lbl_isavail.grid(row=5,column=0,pady=10,padx=10,sticky="w")
        
        combo_isavail=ttk.Combobox(manage_frame,textvariable=self.isavailable,font=("times new roman",14),state='readonly')
        combo_isavail['values']=("Yes","No")
        combo_isavail.grid(row=5,column=1,pady=10,padx=10,sticky="w")
        
        
        
        lbl_asince=Label(manage_frame,text="Available Since\n(In Hours)",font=("times new roman",15,"bold"))
        lbl_asince.grid(row=6,column=0,pady=10,padx=10,sticky="w")
        
        txt_asince=Entry(manage_frame,textvariable=self.availsince,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_asince.grid(row=6,column=1,pady=10,padx=10,sticky="w")
        
        
        
        lbl_role=Label(manage_frame,text="Role",font=("times new roman",15,"bold"))
        lbl_role.grid(row=7,column=0,pady=10,padx=10,sticky="w")
          
        combo_role=ttk.Combobox(manage_frame,textvariable=self.role,font=("times new roman",14),state='readonly')
        combo_role['values']=("Sales","Support","Spanish Speaker")
        combo_role.grid(row=7,column=1,pady=10,padx=10,sticky="w")

        
        #______________________Buttons___________________
        
        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=20,y=470,width=400)
        
        addbtn=Button(btn_frame,text="Add",width=10,command=self.add).grid(row=0,column=0,padx=15,pady=5)
        updatebtn=Button(btn_frame,text="Update",width=10,command=self.update).grid(row=0,column=1,padx=5,pady=5)
        deletebtn=Button(btn_frame,text="Delete",width=10,command=self.delete).grid(row=0,column=2,padx=5,pady=5)
        clearbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=5,pady=5)
        
        
        
        #_________________DETAILS_FRAME_________________________
        
        detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        detail_frame.place(x=480,y=70,width=800,height=560)
        
        lbl_search=Label(detail_frame,text="Search By",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
         
        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",12),state='readonly')
        combo_search['values']=("ID","Name")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")
        
        txt_search=Entry(detail_frame,textvariable=self.search_txt,font=("times new roman",13,"bold"),width=20,bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchbtn=Button(detail_frame,text="Search",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=20,pady=10)
        showallbtn=Button(detail_frame,text="Show All",command=self.fetch_data,width=10,pady=5).grid(row=0,column=4,padx=20,pady=10)
        
        
        
        #________________Table_Frame_________________________
        
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE)
        table_frame.place(x=15,y=60,width=760,height=400)
        
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.agent_table=ttk.Treeview(table_frame,columns=("id","name","phoneno","gender","isavailable","availsince","role"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.agent_table.xview)
        scroll_y.config(command=self.agent_table.yview)
        self.agent_table.heading("id",text="Agent ID")
        self.agent_table.heading("name",text="Name")
        self.agent_table.heading("phoneno",text="Phone No.")
        self.agent_table.heading("gender",text="Gender")
        self.agent_table.heading("isavailable",text="Is Available")
        self.agent_table.heading("availsince",text="Available Since")
        self.agent_table.heading("role",text="Role")
        self.agent_table['show']='headings'
        self.agent_table.column("id",width=150)
        self.agent_table.column("name",width=100)
        self.agent_table.column("gender",width=100)
        self.agent_table.column("phoneno",width=150)
        self.agent_table.column("isavailable",width=100)
        self.agent_table.column("availsince",width=100)
        self.agent_table.column("role",width=80)
        self.agent_table.pack(fill=BOTH,expand=1)
        
        self.agent_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
        #_______________Buttons___________________
        button_frame=Frame(detail_frame,bd=4,relief=RIDGE)
        button_frame.place(x=20,y=470,width=750)
        
        returnbtn=Button(button_frame,text="Return",width=30,font=("times new roman",14,"bold"),command=self.return_func).grid(row=0,column=0,padx=15,pady=5)
        exitbtn=Button(button_frame,text="Exit",width=30,font=("times new roman",14,"bold"),command=self.exit_func).grid(row=0,column=1,padx=5,pady=5)
        self.root.mainloop()
        
    
    #_________________ALL FUNCTION___________________    

    def exit_func(self):
        option=messagebox.askyesno("Exit","Do you really want to Exit?")
        if option!=0:
            self.root.destroy()
        else:
            return
        
        
    def return_func(self):
        option=messagebox.askyesno("Previous","Do you really want to go Back?")
        if option!=0:
            self.root.destroy()
            import firstpage
            firstpage.mainpage()
        else:
            return
        
        
        
    def add(self):
        if self.id.get()=="" or self.name.get()=="" or self.phno.get()=="" or self.gender.get()=="" or self.isavailable.get()=="" or self.availsince.get()=="" or self.role.get()=="":
            messagebox.showerror("Error","All Field are required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="adm")
            cur=con.cursor()
            cur.execute("insert into agents values(%s,%s,%s,%s,%s,%s,%s)",(self.id.get(),
                                                                           self.name.get(),
                                                                           self.phno.get(),
                                                                           self.gender.get(),
                                                                           self.isavailable.get(),
                                                                           self.availsince.get(),
                                                                           self.role.get()
                                                                           ))
                
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted.")
        
    
        
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="adm")
        cur=con.cursor()
        cur.execute("select * from agents")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.agent_table.delete(*self.agent_table.get_children())
            for row in rows:
                self.agent_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def clear(self):
        self.id.set("")
        self.name.set("")
        self.phno.set("")
        self.gender.set("")
        self.isavailable.set("")
        self.availsince.set("")
        self.role.set("")
        self.search_by.set("")
        self.search_txt.set("")
        
    
    def get_cursor(self,ev):
        cursor_row=self.agent_table.focus()
        contents=self.agent_table.item(cursor_row)
        row=contents['values']
        self.id.set(row[0])
        self.name.set(row[1])
        self.phno.set(row[2])
        self.gender.set(row[3])
        self.isavailable.set(row[4])
        self.availsince.set(row[5])
        self.role.set(row[6])
        
    def update(self):
        if self.id.get()=="" or self.name.get()=="" or self.phno.get()=="" or self.gender.get()=="" or self.isavailable.get()=="" or self.availsince.get()=="" or self.role.get()=="":
            messagebox.showerror("Error","All Field are required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="adm")
            cur=con.cursor()
            cur.execute("update agents set name=%s,phno=%s,gender=%s,isavailable=%s,availsince=%s,role=%s where id=%s",(self.name.get(),
                                                                                                                        self.phno.get(),
                                                                                                                        self.gender.get(),
                                                                                                                        self.isavailable.get(),
                                                                                                                        self.availsince.get(),
                                                                                                                        self.role.get(),
                                                                                                                        self.id.get()    
                                                                                                                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been updated.")
            
    def delete(self):
        option=messagebox.askyesno("Previous","Do you really want delete?")
        if option!=0:
             con=pymysql.connect(host="localhost",user="root",password="",database="adm")
             cur=con.cursor()
             cur.execute("delete from agents where id=%s",self.id.get())
             con.commit()
             con.close()
             self.fetch_data()
             self.clear()
        else:
            return
        
       
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="adm")
        cur=con.cursor()
        cur.execute("select * from agents where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.agent_table.delete(*self.agent_table.get_children())
            for row in rows:
                self.agent_table.insert('',END,values=row)
            con.commit()
        con.close()
      