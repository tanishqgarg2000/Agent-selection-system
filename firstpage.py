from tkinter import *
from PIL import ImageTk
class mainpage:
    
    def __init__(self):
        self.root=Tk()
        self.root.title("Agent Selector")
        self.root.geometry("1200x600+100+50")
        self.root.resizable(False,False)
        
        
        #______________BG_IMAGE_____________
        self.bg=ImageTk.PhotoImage(file="C:/Users/DELL/Agent Selector/images/background.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #_____________TITLE____________________
        title=Label(self.root,text="AGENT SELECTOR",font=("times new roman",40,"bold"),bg="white",fg="black",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        #_____________USER_IMAGE________________
        self.user=ImageTk.PhotoImage(file="C:/Users/DELL/Agent Selector/images/user.jpg")
        self.userlbl=Label(image=self.user).grid(pady=150,padx=460)
        
        #____________BUTTONS____________________
        self.btn_details=Button(text="Agent Details",width=20,font=("times new roman",14,"bold"),bg="white",fg="black",command=self.agent_details).place(x=150,y=480)
        self.btn_selection=Button(text="Agent selecton Mode",width=20,font=("times new roman",14,"bold"),bg="white",fg="black",command=self.agent_selec).place(x=470,y=480)
        self.btn_exit=Button(text="Exit.",width=20,font=("times new roman",14,"bold"),bg="white",fg="black",command=self.exit_func).place(x=790,y=480)
    
        self.root.mainloop()
        self.root.destroy()
        
        
    #________________ALL FUNCTIONS_________________________
        
    def exit_func(self):
        option=messagebox.askyesno("Exit","Do you really want to Exit?")
        if option!=0:
            self.root.destroy()
        else:
            return
    
    def agent_details(self):
        self.root.destroy()
        import Agent_details
        Agent_details.agent_data()
        
        
    def agent_selec(self):
        self.root.destroy()
        import Agent_selector
        Agent_selector.agent_selctionprocess()
    
        
mainpage()