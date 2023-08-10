from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  # pip  install pillow
import mysql.connector
from tkinter import messagebox
import os
from tkinter import filedialog


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        
        self.var_Depart=StringVar()
        self.var_Admission_no=StringVar()
        self.var_Year=StringVar()
        self.var_CTeacher=StringVar()
        self.var_Stu_Id=StringVar()
        self.var_Name=StringVar()
        self.var_class=StringVar()
        self.var_dob=StringVar()
        self.var_Gender=StringVar()
        self.var_Contact=StringVar()
        self.var_Address=StringVar()
        self.var_Email=StringVar()
        self.var_Fname=StringVar()
        self.var_Mname=StringVar()
      
        # 1st image
        img=Image.open(r"images\1st.jpg")
        img=img.resize((530,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        self.btn_1=Button(self.root,command=self.open_img,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=2,width=540,height=160)
        
        # 2st image
        img_2=Image.open(r"images\2nd.jpg")
        img_2=img_2.resize((530,160),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        self.btn_2=Button(self.root,command=self.open_img_1,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=540,y=2,width=540,height=160)
        
        # 3st image
        img_3=Image.open(r"images\3rd.jpg")
        img_3=img_3.resize((530,160),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        self.btn_3=Button(self.root,command=self.open_img_2,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=1080,y=2,width=540,height=160)
        
        # bg  
        img_4=Image.open(r"images\university.jpg")
        img_4=img_4.resize((1580,710),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)
        
        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
        
        
        lbl_title=Label(bg_lbl,text="STUDENT MANAGMENT SYSTEM",font=("time new roman",37,"bold"),fg="blue",bg="#FFD700")
        lbl_title.place(x=0,y=0,width=1530,height=60)
       
       
       ####---MANAGE FRAME--------################
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg='white')
        Manage_frame.place(x=15,y=65,width=1500,height=550)
        
        
        # laft frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("time new roman",12,"bold"),fg="green",bg="#f1e398")
        DataLeftFrame.place(x=6,y=7,width=650,height=540)
        
        img_5=Image.open(r"images\3rd.jpg")
        img_5=img_5.resize((700,120),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

               
        img_5=Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        img_5.place(x=0,y=0,width=700,height=150)    
        
        #CUrrent Cource Information    
        stu_info=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Cource Information",font=("time new roman",12,"bold"),fg="#CA0497",bg="white")
        stu_info.place(x=0,y=150,width=640,height=115)  
        
        #Labels
        lbl_dep=Label(stu_info,text="Department",font=("time new roman",12,"bold"),bg="white")   
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(stu_info,textvariable=self.var_Depart,font=("time new roman",12,"bold"),state="readonly")
        combo_dep["value"]=("Select Department","Science","Commerce","Humanity")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)  
        
        #cource  ## For some additional fiture.
        #Admission no.
        lbl_adm=Label(stu_info,font=("arial",11,"bold"),text="Admission no.",bg="white")
        lbl_adm.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        adm_entry=ttk.Entry(stu_info,textvariable=self.var_Admission_no,font=("arial",11,"bold"),width=22)
        adm_entry.grid(row=0,column=3,sticky=W,padx=2,pady=5)
        
        #class teacher
        lbl_teach=Label(stu_info,font=("arial",11,"bold"),text="Class Teacher",bg="white")
        lbl_teach.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        teach_entry=ttk.Entry(stu_info,textvariable=self.var_CTeacher,font=("arial",11,"bold"),width=22)
        teach_entry.grid(row=1,column=3,sticky=W,padx=2,pady=5)
        
        # Year  
        current_year=Label(stu_info,text="Year",font=("time new roman",14,"bold"),bg="white")   
        current_year.grid(row=1,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(stu_info,textvariable=self.var_Year,font=("time new roman",12,"bold"),state="readonly")
        combo_dep["value"]=("Select year","2020-2021","2021-2022","2022-2023","2023-2024")
        combo_dep.current(0)
        combo_dep.grid(row=1,column=1,padx=2,pady=10,sticky=W)  
        
        
        #Students class  Information    
        stu_class_info=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Presonal Detail",font=("time new roman",12,"bold"),fg="#CA0497",bg="white")
        stu_class_info.place(x=0,y=260,width=640,height=245) 
        
        # Labels entry
        # ID
        lbl_id=Label(stu_class_info,font=("arial",11,"bold"),text="Student ID",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        id_entry=ttk.Entry(stu_class_info,textvariable=self.var_Stu_Id,font=("arial",11,"bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=5)
        
        # Name
        lbl_class=Label(stu_class_info,font=("arial",11,"bold"),text="Name",bg="white")
        lbl_class.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        class_entry=ttk.Entry(stu_class_info,textvariable=self.var_Name,font=("arial",11,"bold"),width=22)
        class_entry.grid(row=1,column=1,sticky=W,padx=2,pady=5)
        
        # class
        lbl_class=Label(stu_class_info,font=("arial",11,"bold"),text="Class & sec.",bg="white")
        lbl_class.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        class_entry=ttk.Entry(stu_class_info,textvariable=self.var_class,font=("arial",11,"bold"),width=22)
        class_entry.grid(row=0,column=3,sticky=W,padx=2,pady=5)
        
        # Gender
        lbl_gender=Label(stu_class_info,font=("arial",11,"bold"),text="Gender",bg="white")
        lbl_gender.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        gender_entry=ttk.Combobox(stu_class_info,textvariable=self.var_Gender,font=("time new roman",12,"bold"),state="readonly")
        gender_entry["value"]=("Select Gender","Male","Female","Other")
        gender_entry.current(0)
        gender_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # Date of birth
        lbl_dob=Label(stu_class_info,font=("arial",11,"bold"),text="Date of Birth",bg="white")
        lbl_dob.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        dob_entry=ttk.Entry(stu_class_info,textvariable=self.var_dob,font=("arial",11,"bold"),width=22)
        dob_entry.grid(row=2,column=1,sticky=W,padx=2,pady=5)
        
         # Address
        lbl_add=Label(stu_class_info,font=("arial",11,"bold"),text="Address",bg="white")
        lbl_add.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        add_entry=ttk.Entry(stu_class_info,textvariable=self.var_Address,font=("arial",11,"bold"),width=22)
        add_entry.grid(row=3,column=1,sticky=W,padx=2,pady=10)
        
         #Phone number
        lbl_phone=Label(stu_class_info,font=("arial",11,"bold"),text="Contact no.",bg="white")
        lbl_phone.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        phone_entry=ttk.Entry(stu_class_info,textvariable=self.var_Contact,font=("arial",11,"bold"),width=22)
        phone_entry.grid(row=2,column=3,sticky=W,padx=2,pady=5)
        
        #Email
        lbl_mail=Label(stu_class_info,font=("arial",11,"bold"),text="Email Id",bg="white")
        lbl_mail.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        mail_entry=ttk.Entry(stu_class_info,textvariable=self.var_Email,font=("arial",11,"bold"),width=22)
        mail_entry.grid(row=3,column=3,sticky=W,padx=2,pady=5)
        
        #Father name
        lbl_fname=Label(stu_class_info,font=("arial",11,"bold"),text="Father's Name",bg="white")
        lbl_fname.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        fname_entey=ttk.Entry(stu_class_info,textvariable=self.var_Fname,font=("arial",11,"bold"),width=22)
        fname_entey.grid(row=4,column=1,sticky=W,padx=2,pady=5)
        
        #Mother name
        lbl_mname=Label(stu_class_info,font=("arial",11,"bold"),text="Mother's Name",bg="white")
        lbl_mname.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        mname_entry=ttk.Entry(stu_class_info,textvariable=self.var_Mname,font=("arial",11,"bold"),width=22)
        mname_entry.grid(row=4,column=3,sticky=W,padx=2,pady=5)
        
        # BUtton Frame
        # Save button
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=480,width=640,height=34)
        
        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)
        
        # update               
        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=17,bg="green",fg="white")
        btn_update.grid(row=0,column=1,padx=1)
        
        # Delete                
        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=17,bg="red",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)
        
        # reset                
        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="#05BA89",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)

        
      
        
        
                                                                                                                                                                                                                                                       
        # RIght frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("time new roman",12,"bold"),fg="green",bg="#f1e398")
        DataRightFrame.place(x=650,y=7,width=840,height=540)
        
        img_6=Image.open(r"images\university.jpg")
        img_6=img_6.resize((825,200),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)
        
        img_6=Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        img_6.place(x=0,y=0,width=825,height=200) 
        
        # Search frame
        searchFrame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("time new roman",12,"bold"),fg="green",bg="#f1e398")
        searchFrame.place(x=0,y=200,width=828,height=60)
        
        search_by=Label(searchFrame,font=("arial",11,"bold"),text="Search By",fg="red",bg="#00008B")
        search_by.grid(row=0,column=0,sticky=W,padx=2)
##=======search
        self.var_comb_search=StringVar()
        search_by_entry=ttk.Combobox(searchFrame,textvariable=self.var_comb_search,font=("time new roman",12,"bold"),state="readonly")
        search_by_entry["value"]=("Select Option","Stu_Id","Contact","Name","class")
        search_by_entry.current(0)
        search_by_entry.grid(row=0,column=1,padx=5,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(searchFrame,textvariable=self.var_search,font=("arial",11,"bold"),width=22)
        search_entry.grid(row=0,column=2,sticky=W,padx=5,pady=5)
        
        btn_search=Button(searchFrame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=15,bg="#728FCE",fg="white")
        btn_search.grid(row=0,column=3,padx=6,pady=0)
        
        btn_del=Button(searchFrame,text="Delete",command=self.fetch_data,font=("arial",11,"bold"),width=15,bg="#FFDAB9",fg="gray")
        btn_del.grid(row=0,column=4,padx=6,pady=0)
        
        #==============STUDENTS DATA AND SCROLL BAR==============
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=830,height=255)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Depart","Admission_no","Year","CTeacher","Stu_Id","Name","class","dob","Gender","Contact","Address","Email","Fname","Mname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Depart",text="Department")
        self.student_table.heading("Admission_no",text="Admission no.")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("CTeacher",text="Class Teacher")
        self.student_table.heading("Stu_Id",text="Student Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Fname",text="Father Name")
        self.student_table.heading("Mname",text="Mother Name")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("Depart",width=100)
        self.student_table.column("Admission_no",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("CTeacher",width=130)
        self.student_table.column("Stu_Id",width=100)
        self.student_table.column("Name",width=130)
        self.student_table.column("class",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Email",width=130)
        self.student_table.column("Fname",width=130)
        self.student_table.column("Mname",width=130)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

                                                                                                                                                                                                        
     #=============Data Base Management============
    def add_data(self):
        if(self.var_Stu_Id.get()=="" or self.var_Name.get()=="" or self.var_Admission_no.get()==""):
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                conn= mysql.connector.connect(host="localhost",user="root",database="mydata",password="2730",auth_plugin="mysql_native_password",buffered=True)
                cursor=conn.cursor()

                sql = "INSERT INTO student (Depart,Admission_no,Year,CTeacher,Stu_Id,Name,class,dob,Gender,Contact,Address,Email,Fname,Mname) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
                val=(self.var_Depart.get(),
                     self.var_Admission_no.get(),
                     self.var_Year.get(),
                     self.var_CTeacher.get(),
                     self.var_Stu_Id.get(),
                     self.var_Name.get(),
                     self.var_class.get(), 
                     self.var_dob.get(),
                     self.var_Gender.get(),
                     self.var_Contact.get(),
                     self.var_Address.get(),
                     self.var_Email.get(),
                     self.var_Fname.get(),
                     self.var_Mname.get(),
                     )
                cursor.execute(sql,val)




                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

        #====================fetch data=========================================
    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost",user="root",database="mydata",password="2730",auth_plugin="mysql_native_password",buffered=True)
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM  student")
        data=cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,value=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]
        self.var_Depart.set(data[0])
        self.var_Admission_no.set(data[1])
        self.var_Year.set(data[2])
        self.var_CTeacher.set(data[3])
        self.var_Stu_Id.set(data[4])
        self.var_Name.set(data[5])
        self.var_class.set(data[6])
        self.var_dob.set(data[7])
        self.var_Gender.set(data[8])
        self.var_Contact.set(data[9])
        self.var_Address.set(data[10])
        self.var_Email.set(data[11])
        self.var_Fname.set(data[12])
        self.var_Mname.set(data[13])

    ##================================UPDATE=============================
    def update_data(self):
        if(self.var_Stu_Id.get()=="" or self.var_Name.get()=="" or self.var_Admission_no.get()==""):
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                update=messagebox.askyesno("Upadte","Are you sure to update student data",parent=self.root)
                if update>0:
                    conn= mysql.connector.connect(host="localhost",user="root",database="mydata",password="2730",auth_plugin="mysql_native_password",buffered=True)
                    cursor=conn.cursor()
                    upd=("update student set Depart=%s,Admission_no=%s,Year=%s,CTeacher=%s,Name=%s,class=%s,dob=%s,Gender=%s,Contact=%s,Address=%s,Email=%s,Fname=%s,Mname=%s where Stu_Id=%s")
                    uval=(self.var_Depart.get(),
                          self.var_Admission_no.get(),
                          self.var_Year.get(),
                          self.var_CTeacher.get(),
                          self.var_Name.get(),
                          self.var_class.get(), 
                          self.var_dob.get(),
                          self.var_Gender.get(),
                          self.var_Contact.get(),
                          self.var_Address.get(),
                          self.var_Email.get(),
                          self.var_Fname.get(),
                          self.var_Mname.get(),
                          self.var_Stu_Id.get(),
                     )
                    cursor.execute(upd,uval)
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student Successfully update",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
####======================DELETE======================================
    def delete_data(self):
        if self.var_Stu_Id.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure delete this student",parent=self.root)
                if Delete>0:
                    conn= mysql.connector.connect(host="localhost",user="root",database="mydata",password="2730",auth_plugin="mysql_native_password",buffered=True)
                    cursor=conn.cursor()
                    sql="delete from student where Stu_Id=%s"
                    value=(self.var_Stu_Id.get(),)
                    cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Student has been deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

##==============RESET DATA+============================================
    def reset_data(self):
        self.var_Depart.set("Select Department")
        self.var_Admission_no.set("")
        self.var_Year.set("select Year")
        self.var_CTeacher.set("")
        self.var_Stu_Id.set("")
        self.var_Name.set("")
        self.var_class.set("")
        self.var_dob.set("")
        self.var_Gender.set("Select Gender")
        self.var_Contact.set("")
        self.var_Address.set("")
        self.var_Email.set("")
        self.var_Fname.set("")
        self.var_Mname.set("")
 
##===============search===========================
    def search_data(self):
        if self.var_comb_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn= mysql.connector.connect(host="localhost",user="root",database="mydata",password="2730",auth_plugin="mysql_native_password",buffered=True)
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM student WHERE "+str(self.var_comb_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                row=cursor.fetchall()
                
                if len(row)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in row:
                        self.student_table.insert("",END,values=i)
                        
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
#===========open image=======================
    def open_img(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open Image",filetype=(("JPG FIle","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img=Image.open(fln)
        img_browse=img.resize((540,160),Image.ANTIALIAS)
        self.photoimg_browse=ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)

    def open_img_1(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open Image",filetype=(("JPG FIle","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img_1=Image.open(fln)
        img_browse_1=img_1.resize((540,160),Image.ANTIALIAS)
        self.photoimg_browse_1=ImageTk.PhotoImage(img_browse_1)
        self.btn_2.config(image=self.photoimg_browse_1)

    def open_img_2(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open Image",filetype=(("JPG FIle","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img_2=Image.open(fln)
        img_browse_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photoimg_browse_2=ImageTk.PhotoImage(img_browse_2)
        self.btn_3.config(image=self.photoimg_browse_2)

     
        
          
    
        
                                                                                                                                                                                                                            
        

if __name__=="__main__":
    root=Tk()
    odj=student(root)
    
    root.mainloop()      





















