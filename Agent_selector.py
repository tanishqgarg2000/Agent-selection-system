from tkinter import *
from tkinter import ttk
import pymysql


class agent_selctionprocess:
    
    def __init__(self):
        self.root=Tk()
        self.root.title("Agent Details.")
        self.root.geometry("1300x650+0+0")
        self.root.resizable(False,False)
        
         #______________ALL VARIABLE______________

        self.Role=StringVar()
        self.smode=StringVar()
       
        

        #______________Title_____________
        title=Label(self.root,text="Agent Selection Mode",font=("times new roman",25,"bold"),bg="white",fg="black",bd=8,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #______________MANAGE_FRAMES______________
        manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        manage_frame.place(x=20,y=70,width=450,height=560)
        
         
        m_title=Label(manage_frame,text="Enter details",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=5,pady=10,padx=110)
        
        
        lbl_role=Label(manage_frame,text="Role",font=("times new roman",15,"bold"))
        lbl_role.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        
        combo_role=ttk.Combobox(manage_frame,textvariable=self.Role,font=("times new roman",14),state='readonly')
        combo_role['values']=("Sales","Support","Spanish Speaker")
        combo_role.grid(row=3,column=1,pady=10,padx=10,sticky="w")

       
        lbl_smode=Label(manage_frame,text="Selection Mode",font=("times new roman",15,"bold"))
        lbl_smode.grid(row=7,column=0,pady=10,padx=10,sticky="w")
        
        combo_smode=ttk.Combobox(manage_frame,textvariable=self.smode,font=("times new roman",14),state='readonly')
        combo_smode['values']=("All Available","Least Busy","Random")
        combo_smode.grid(row=7,column=1,pady=10,padx=10,sticky="w")
        
        searchbtn=Button(manage_frame,text="Search",command=self.search_detail,font=("times new roman",15,"bold"),width=20).grid(row=9,column=1,padx=15,pady=5)
        
        
        
        #_________________DETAILS_FRAME_________________________
        
        detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        detail_frame.place(x=480,y=70,width=800,height=560)
        
        
        d_title=Label(detail_frame,text="Agent Details",font=("times new roman",20,"bold"))
        d_title.grid(row=0,columnspan=10,pady=10,padx=110)
        
        showallbtn=Button(detail_frame,text="Show All",command=self.fetch_data,width=10,pady=5).grid(row=0,column=50,padx=20,pady=10)
        
        
         
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
        presentedbtn=Button(detail_frame,text="Select Agent",command= self.present_func,width=10,pady=5).grid(row=0,column=15,padx=20,pady=10)
        selectallbtn=Button(detail_frame,text="Select All Agent",command= self.selectall_func,width=15,pady=5).grid(row=0,column=20,padx=20,pady=10)
        
        self.root.mainloop()
        
    #____________________ALL FUNCTION_______________
    
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
        
    def get_cursor(self,ev):
        cursor_row=self.agent_table.focus()
        contents=self.agent_table.item(cursor_row)
        row=contents['values']
        print(row)
        return row
    
    def present_func(self):
        e=Event
        row_data=self.get_cursor(e)
        if(row_data==""):
            messagebox.showerror("Error","Select Agent Data From Table!!!")
        else:
            messagebox.showinfo("Success","Agent Selected\n(Information of Agent is available in table)\nAgent ID="+str(row_data[0]))
            
            print(row_data)
            
    def selectall_func(self):
        messagebox.showinfo("Success","All Agent are selected.\n(Information is given in the table.)")
             
    
    
    def search_detail(self):
        if self.Role.get()=="" or self.smode.get()=="":
            messagebox.showerror("Error","All Field are required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="adm")
            cur=con.cursor()
            if(self.smode.get()=="All Available"):
                cur.execute("select * from agents where isavailable = 'Yes' AND role LIKE '%"+str(self.Role.get())+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.agent_table.delete(*self.agent_table.get_children())
                    for row in rows:
                        self.agent_table.insert('',END,values=row)
                    con.commit()
                con.close()
              
            elif(self.smode.get()=="Least Busy"):
                cur.execute("select * from agents where availsince=(select MAX(availsince) from agents) AND isavailable = 'Yes' AND role LIKE '%"+str(self.Role.get())+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.agent_table.delete(*self.agent_table.get_children())
                    for row in rows:
                        self.agent_table.insert('',END,values=row)
                    con.commit()
                con.close()
              
            elif(self.smode.get()=="Random"):
                cur.execute("select * from agents where isavailable = 'Yes' AND role LIKE '%"+str(self.Role.get())+"%' ORDER BY RAND() LIMIT 1")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.agent_table.delete(*self.agent_table.get_children())
                    for row in rows:
                        self.agent_table.insert('',END,values=row)
                    con.commit()
                con.close()