from tkinter import*
from tkinter import ttk

class Student:
  def __init__ (self,root):
    self.root=root
    self.root.title("Student Management System")
    self.root.geometry("1400x800+0+0")
    self.root.resizable(width=False,height=False)
    



  #---------Title------------

    title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Castellar",45),bg="Black",fg="Orange")
    title.pack(side=TOP,fill=X)

  
  #-----------Managing_Frame-----------------

    Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lavender")
    Manage_Frame.place(x=20,y=120,width=1360,height=670)

    m_title=Label(Manage_Frame,text="Manage Students",bg="lavender",fg="black", font=("times new roman",30,"bold"))
    m_title.grid(row=1,columnspan=8,pady=20)
    

    lbl_roll=Label(Manage_Frame,text="Roll No.",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_roll.grid(row=2,column=0,padx=20,pady=25,sticky="w")

    txt_Roll=Entry(Manage_Frame,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
    txt_Roll.grid(row=2,column=1,padx=20,pady=25,sticky="w")

    lbl_name=Label(Manage_Frame,text="Name",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_name.grid(row=2,column=2,padx=100,pady=25,sticky="w")

    txt_name=Entry(Manage_Frame,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
    txt_name.grid(row=2,column=3,padx=0,pady=25,sticky="w")

    lbl_gender=Label(Manage_Frame,text="Gender",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_gender.grid(row=4,column=0,padx=20,pady=25,sticky="w")

    combo_Gender=ttk.Combobox(Manage_Frame,font=("times new roman",18,"bold"))
    combo_Gender['values']=("male","female","other")
    combo_Gender.grid(row=4,column=1,padx=20,pady=25)

    lbl_Faculty=Label(Manage_Frame,text="Faculty",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_Faculty.grid(row=4,column=2,padx=100,pady=25,sticky="w")

    combo_Faculty=ttk.Combobox(Manage_Frame,font=("times new roman",18,"bold"))
    combo_Faculty['values']=("Bsc Hons Ethical hacking and Cybersecurity","Bsc Hons Computing","")
    combo_Faculty.grid(row=4,column=3,padx=0,pady=25)

    lbl_Email=Label(Manage_Frame,text="Email",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_Email.grid(row=5,column=0,padx=20,pady=25,sticky="w")

    txt_Email=Entry(Manage_Frame,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
    txt_Email.grid(row=5,column=1,padx=20,pady=25,sticky="w")

    lbl_Contact=Label(Manage_Frame,text="Contact",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_Contact.grid(row=5,column=2,padx=100,pady=25,sticky="w")

    txt_Contact=Entry(Manage_Frame,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
    txt_Contact.grid(row=5,column=3,padx=0,pady=25,sticky="w")

    lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_DOB.grid(row=6,column=0,padx=20,pady=25,sticky="w")

    txt_DOB=Entry(Manage_Frame,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
    txt_DOB.grid(row=6,column=1,padx=20,pady=25,sticky="w")

    lbl_Address=Label(Manage_Frame,text="Address",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lbl_Address.grid(row=6,column=2,padx=100,pady=25,sticky="w")

    txt_Address=Entry(Manage_Frame,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
    txt_Address.grid(row=6,column=3,padx=0,pady=25,sticky="w")

    lblSearch=Label(Manage_Frame,text="Search By",bg="lavender",fg="black", font=("times new roman",20,"bold"))
    lblSearch.grid(row=0,column=0,padx=00,pady=10,sticky="w")

    combo_Search=ttk.Combobox(Manage_Frame,width=10,font=("times new roman",18,"bold"))
    combo_Search['values']=("Roll","Name","Faculty")
    combo_Search.grid(row=0,column=1,padx=0,pady=10)


    txt_Search=Entry(Manage_Frame,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
    txt_Search.grid(row=0,column=2,padx=0,pady=10,sticky="w")

    Searchbtn=Button(Manage_Frame,text="Search",width=15).grid(row=0,column=3,padx=0,pady=10)
    Showallbtn=Button(Manage_Frame,text="Show All",width=15).grid(row=0,column=4,padx=0,pady=10)


    
    

  #-------Button_frame------

    btn_Frame=Frame(Manage_Frame,bd=6,relief=RIDGE,bg="black")
    btn_Frame.place(x=20,y=580,width=1300)

    Addbtn=Button(btn_Frame,text="Add",width=30).grid(row=0,column=0,padx=30,pady=10)

    Updatebtn=Button(btn_Frame,text="Update",width=30).grid(row=0,column=1,padx=40,pady=10)

    Deletebtn=Button(btn_Frame,text="Delete",width=30).grid(row=0,column=2,padx=40,pady=10)

    Clearbtn=Button(btn_Frame,text="Clear",width=30).grid(row=0,column=3,padx=40,pady=10)

  


root= Tk()
ob= Student(root)
root.mainloop()