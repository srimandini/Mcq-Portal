from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 
import pymysql
# print(dir(tkinter))
import mcq

win=Tk()
img=ImageTk.PhotoImage(Image.open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\A.png"))
label=Label(image=img)
label.pack()

#obj1=mcq.myQuiz()
#print(obj1.displayResult(self))
#print("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}") 

def Login():
	username= uid.get()
	password= pwd.get()
	print(username," ",password)
	conobj = pymysql.connect(host = 'localhost', user='root',password='',port=3306)
	curobj = conobj.cursor()
	curobj.execute('use BCA2021AB;')
	#curobj.execute('alter table INFO add (Mark int , Per_Mark varchar(7));')
	curobj.execute('select * from INFO;')
	test= f'select * from INFO where userid="{username}" and password="{password}";'
	curobj.execute(test)
	record=curobj.fetchall()
	# print(record)
	if len(record):
		messagebox.showinfo("logininfo","Welcome to Home Page")
		win.destroy()
		from mcq import myQuiz
		quiz = myQuiz()
		#myQuiz
	else:
		messagebox.showinfo("logininfo","Sorry!!! Try Again...Better luck Next Time")
def Reset():
	uid.delete (0,END)
	pwd.delete (0,END)
def newUser():
	win.destroy()
	
	win1 = Tk()
	img1=ImageTk.PhotoImage(Image.open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\A.png"))
	label1=Label(image=img1)
	label1.pack()

	def Submit():
		a=nuid.get()
		b=nphno.get()
		c=menu.get()
		d=var1.get()
		e=npwd.get()
		#print(a,"",b,"",c,"",d,"",e)

		conobj=pymysql.connect(host="localhost",user="root",password="",port=3306)
		curobj=conobj.cursor()
		#curobj.execute('create database BCA2021AB;')
		curobj.execute('use BCA2021AB;')
		#curobj.execute('create table INFO (userid varchar(20),phno bigint(10),dept varchar(20),gender varchar(6),password varchar(10));')
		r='insert into INFO (userid,phno,dept,gender,password) values("{userid}","{phno}","{dept}","{gender}","{password}");'
		r1=r.format(userid=a,phno=b,dept=c,gender=d,password=e)
		print(r1)
		curobj.execute(r1)
		conobj.commit()
		curobj.close()						
		conobj.close()

		win1.destroy()

	def Reset():
		nuid.delete (0,END)	
		nphno.delete (0,END)
		# menu.delete (0,END)
		menu.set(None)
		# var1.delete (0,END)
		var1.set(None)
		npwd.delete (0,END)
	win1.title("SignUp Page")
	win1.maxsize(700,700)
	win1.minsize(700,700)

	Label (win1,text="PLEASE SIGNUP HERE",font=('Bernard MT',20,),fg="White",bg="blue",relief=RAISED,width=30).place(x=110,y=50)

	Label (win1,text="Set User-ID :",font=('Bernard MT',15,),fg="black",bg="red",relief=RAISED,width=20).place(x=110,y=150)
	nuid = Entry(win1,font=('Bernard MT',15),bg="blue", fg="white")
	nuid .place(x=350,y=150)

	Label (win1,text="Enter phone number :",font=('Bernard MT',15,),fg="black",bg="red",relief=RAISED,width=20).place(x=110,y=220)
	nphno = Entry(win1,font=('Bernard MT',15),bg="blue", fg="white")
	nphno.place(x=350,y=220)

	Label (win1,text="Select Dept number :",font=('Bernard MT',15,),fg="black",bg="red",relief=RAISED,width=20).place(x=110,y=290)
	menu=StringVar()
	drop=OptionMenu(win1,menu,"BCA","BSc.ITm","BSc.CS")
	drop.place(x=450,y=290)

	Label (win1,text="Select Gender :",font=('Bernard MT',15,),fg="black",bg="red",relief=RAISED,width=20).place(x=110,y=360)
	var1=StringVar (win1,None)
	Radiobutton(win1,text="Male",variable=var1,value="M",font=('Bernard MT',15)).place(x=350,y=360)
	Radiobutton(win1,text="FeMale",variable=var1,value="F",font=('Bernard MT',15)).place(x=450,y=360)

	Label (win1,text="Enter Password :",font=('Bernard MT',15,),fg="black",bg="red",relief=RAISED,width=20).place(x=110,y=430)
	npwd = Entry(win1,font=('Bernard MT',15),bg="blue", fg="white",show="*")
	npwd.place(x=350,y=430)

	Button (win1,text="Submit",font=('Bernard MT',15),bg="green",fg="red",command=Submit).place(x=180,y=500)
	Button (win1,text="Reset",font=('Bernard MT',15),bg="red",fg="blue",command=Reset).place(x=430,y=500)

	win1.mainloop()
def Exit():
	win.destroy()

win.title("Home Page")
win.maxsize(700,700)
win.minsize(700,700)

Label (win,text="PLEASE LOGIN HERE",font=('Bernard MT',20,),fg="White",bg="blue",relief=RAISED,width=30,height=1).place(x=110,y=50)

Label (win,text="Enter User ID:",font=('Bernard MT',15,),fg="black",bg="red",relief=RAISED,width=20).place(x=110,y=150)
uid = Entry(win,font=('Bernard MT',15),bg="blue", fg="white")
uid .place(x=350,y=150)

Label (win,text="Enter Password:",font=('Bernard MT',15,),fg="black",bg="red",relief=RAISED,width=20).place(x=110,y=250)
pwd = Entry(win,font=('Bernard MT',15),bg="blue", fg="white", show="*")
pwd.place(x=350,y=250)

Button(win,text="Login", font=('Bernard MT',15), bg="crimson",fg="white", command=Login).place(x=150,y=300)
Button(win,text="Reset", font=('Bernard MT',15), bg="crimson",fg="white", command=Reset).place(x=250,y=300)
Button(win,text="Sign Up", font=('Bernard MT',15), bg="crimson",fg="white", command=newUser).place(x=355,y=300)
Button(win,text="Exit", font=('Bernard MT',15), bg="crimson",fg="white", command=Exit).place(x=480,y=300)

win.mainloop()