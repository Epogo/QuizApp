import tkinter as tk
from tkinter import *
import random
import sqlite3
import time
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

def signPage():
	login.destroy()
	global signpage #Sign page variable
	signpage = Tk()#Create interface
	signpage.title('Sign Up page for the quiz app')
	
	firstname=StringVar()
	username=StringVar()
	password=StringVar()
	
	signpage_can=Canvas(signpage,width=920,height=440,bg="#FCDE17")
	signpage_can.pack()
	
	signpage_frame=Frame(signpage_can,bg="#BCDA66")
	signpage_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
	
	heading=Label(signpage_frame,text="Sign Up page for the quiz app",fg="#CBF550",bg="#CDBA65")
	heading.config(font=('calibri 30'))
	heading.place(relx=0.2,rely=0.2)
	
	#Full name
	fullNlabel=Label(signpage_frame,text="Full Name",fg='white',bg='black')
	fullNlabel.place(relx=0.21,rely=0.4)
	fullN=Entry(signpage_frame,bg='white',fg='black',textvariable=firstname)
	fullN.config(width=42)
	fullN.place(relx=0.31,rely=0.4)
	
	#User name
	userLabel=Label(signpage_frame,text="Username",fg='white',bg='black')
	userLabel.place(relx=0.21,rely=0.5)
	user=Entry(signpage_frame,bg='white',fg='black',textvariable=username)
	user.config(width=42)
	user.place(relx=0.31,rely=0.5)
	
	#password
	passLabel=Label(signpage_frame,text="Password",fg='white',bg='black')
	passLabel.place(relx=0.215,rely=0.6)
	passw=Entry(signpage_frame,bg='white',fg='black',textvariable=password,show="*")
	passw.config(width=42)
	passw.place(relx=0.31,rely=0.6)
	
	def InsertUserToDataBase():
	
		fn=firstname.get()
		un=username.get()
		pw=password.get()
		
		if len(firstname.get())==0 and len(username.get())==0 and len(password.get())==0:
			error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
			error.place(relx=0.37,rely=0.7)
		
		elif len(username.get())==0 and len(password.get())==0:
			error = Label(text="Please Enter the username and password field",fg='black',bg='white')
			error.place(relx=0.37,rely=0.7)
		##More errors should be added.
		elif len(username.get())==0 and len(password.get())!=0:
			error = Label(text="Please Enter the username",fg='black',bg='white')
			error.place(relx=0.37,rely=0.7)
			
		elif len(username.get())!=0 and len(password.get())==0:
			error = Label(text="Please Enter the password",fg='black',bg='white')
			error.place(relx=0.37,rely=0.7)
		
		else:
			connection=sqlite3.connect('quiz.db')
			createDb=connection.cursor()
			createDb.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text)')
			createDb.execute("INSERT INTO userSignUp VALUES (?,?,?)",(fn,un,pw))
			connection.commit()
			createDb.execute('SELECT * FROM userSignUp')
			userdata=createDb.fetchall()
			print(userdata)
			connection.close()
			Logging()
	
	def Login():
		connection=sqlite3.connect('quiz.db')
		createDb=connection.cursor()
		connection.commit()
		createDb.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text)')
		createDb.execute('SELECT * FROM userSignUp')
		userdata=createDb.fetchall()
		Logging(userdata)
		
	signB=Button(signpage_frame,text='Sign Up',padx=5,pady=5,width=5,command=InsertUserToDataBase,bg="black",fg="white")
	signB.configure(width=15,height=1,activebackground="#B6C366",relief=FLAT)
	signB.place(relx=0.4,rely=0.8)
	
	signpage.mainloop()
	
def Logging():
	try:
		mainpage.destroy()#Destroy the main page if it has been opened.
	except:
		pass
	try:
		signpage.destroy()#Destroy the Sign-up page if it has been opened.
	except:
		pass
	connection=sqlite3.connect('quiz.db')
	createDb=connection.cursor()
	connection.commit()
	createDb.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text)')
	createDb.execute('SELECT * FROM userSignUp')
	userdata=createDb.fetchall()
	global login
	login=Tk()
	login.title('Quiz app logging')
	
	un=StringVar()
	pw=StringVar()
	
	login_canvas = Canvas(login,width=720,height=440,bg="#B64D4D")
	login_canvas.pack()

	login_frame=Frame(login_canvas,bg="orange")
	login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
	
	heading=Label(login_frame,text="Quiz app logging", fg="white",bg="orange")
	heading.config(font=('calibri 40'))
	heading.place(relx=0.2,rely=0.1)
	
	#USER NAME
	ulabel = Label(login_frame,text="Username",fg='white',bg='black')
	ulabel.place(relx=0.21,rely=0.4)
	uname = Entry(login_frame,bg='white',fg='black',textvariable = un)
	uname.config(width=42)
	uname.place(relx=0.31,rely=0.4)

    #PASSWORD
	plabel = Label(login_frame,text="Password",fg='white',bg='black')
	plabel.place(relx=0.215,rely=0.5)
	pas = Entry(login_frame,bg='white',fg='black',textvariable = pw,show="*")
	pas.config(width=42)
	pas.place(relx=0.31,rely=0.5)
	
	def checkLoggingData():
		for x,y,z in userdata:
			if y==uname.get() and z==pas.get():
				print(userdata)
				
				mainmenu(x)
				break
		else:
			error=Label(login_frame,text="Seems that the username or/and password are wrong",fg='black',bg='white')
			error.place(relx=0.37,rely=0.7)
			
	log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=checkLoggingData,fg="white",bg="black")
	log.configure(width=15,height=1,activebackground="#78C6E7",relief=FLAT)
	log.place(relx=0.4,rely=0.6)
	
	signup = Button(login_frame,text='Sign Up',padx=5,pady=5,width=5,command=signPage,fg="white",bg="black")
	signup.configure(width=15,height=1,activebackground="#78C6E7",relief=FLAT)
	signup.place(relx=0.4,rely=0.7)
	login.mainloop()

def mainmenu(firstname):
    login.destroy()
    global menu
    menu=Tk()
    menu.title('Quiz application menu')
	
    menu_canvas=Canvas(menu,width=720,height=440,bg="orange")
    menu_canvas.pack()
	
    menu_frame=Frame(menu_canvas,bg="#8BBBF4")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
	
    welcome = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="orange") 
    welcome.config(font=('Broadway 22'))
    welcome.place(relx=0.1,rely=0.02)
    
    firstname='Welcome '+ firstname
    l1 = Label(menu_frame,text=firstname,bg="black",font="calibri 18",fg="white")
    l1.place(relx=0.17,rely=0.15)
    
    level = Label(menu_frame,text='Select the desired Difficulty Level',bg="orange",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
	
    var = IntVar()
    easyR=Radiobutton(menu_frame, text ="Easy",bg="#CFBB4B",font="calibri 16",value=1, variable=var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR=Radiobutton(menu_frame, text ="Medium",bg="#A2AB4B",font="calibri 16", value=2, variable=var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR=Radiobutton(menu_frame, text ="Hard",bg="#C5DB4B",font="calibri 16", value=3, variable=var)
    hardR.place(relx=0.25,rely=0.6)
	
	
    def nav():
	
        x=var.get()
        print(x)
        if x==1:
            menu.destroy()
            easy()
        elif x==2:
            menu.destroy()
            medium()
        elif x==3:
            menu.destroy()
            hard()
        else:
            pass
            
    gamelaunch=Button(menu_frame,text="Launch Game",bg="black",fg="white",font="calibri 12",command=nav)
    gamelaunch.place(relx=0.25,rely=0.8)
    menu.mainloop()
    
def easy():

	global easy
	easy = Tk()
	easy.title('Quiz App for easy level')
	
	easy_canvas = Canvas(easy,width=720,height=440,bg="orange")
	easy_canvas.pack()
	
	easy_frame = Frame(easy_canvas,bg="#BCDC44")
	easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
	
	timer = Label(easy)
	timer.place(relx=0.8,rely=0.82,anchor=CENTER)
	
	def countDown():
		check=0
		for i in range(10,0,-1):
			if i==1:
				check=-1
			try:
				timer.configure(text=i)
				easy_frame.update()
				time.sleep(1)
			except:
				pass
		try:	
			timer.configure(text="Time has been over!")
		except:
			pass
		if check==-1:
			return (-1)
		else:
			return 0
	global score
	score = 0
		
	easyQ=[["What is the capital city of Japan?","Jerusalem","Tokyo","London","Paris"],
			   ["What is the longest river in the world?","Jordan","Nille","Amazonas","Rein"],
			   ["Which country is the most populated country in the world?","India","USA","Pakistan","China"]]
	answer=["Tokyo","Nille","China"]
	li=[0,1,2]
	x=random.choice(li[0:])
		
	ques=Label(easy_frame,text=easyQ[x][0],font="calibri 12",bg="orange")
	ques.place(relx=0.5,rely=0.2,anchor=CENTER)
		
	var=StringVar()
		
	a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="#BADA55")
	a.place(relx=0.5,rely=0.42,anchor=CENTER)

	b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="#BADA55")
	b.place(relx=0.5,rely=0.52,anchor=CENTER)

	c = Radiobutton(easy_frame,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="#BADA55")
	c.place(relx=0.5,rely=0.62,anchor=CENTER) 

	d = Radiobutton(easy_frame,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="#BADA55")
	d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
	li.remove(x)
    
		
	def display():
		
		if len(li)==0:
			try:
				easy.destroy()
				showGraph(score)
			except:
				pass
				
		if len(li)==1:
			nextQuestion.configure(text='End',command=calcscore)
				
		if li:
			x=random.choice(li[0:])
			ques.configure(text=easyQ[x][0])
				
			a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
			b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
			c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
			d.configure(text=easyQ[x][4],value=easyQ[x][4])
				
			li.remove(x)
			t=countDown()
			if t==-1:
				display()	
					
	def calcscore():
		global score
		if (var.get() in answer):
			score+=1
		display()
			
	submit = Button(easy_frame,command=calcscore,text="Submit", fg="white", bg="black")
	submit.place(relx=0.5,rely=0.82,anchor=CENTER)
		
	nextQuestion = Button(easy_frame,command=display,text="Next Question", fg="white", bg="black")
	nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
		
	y = countDown()
	if y == -1:
		display()
	easy.mainloop()
		
def medium():
    
	global medium
	medium = Tk()
	medium.title('Quiz App for Medium level')
    
	med_canvas = Canvas(medium,width=720,height=440,bg="#101357")
	med_canvas.pack()

	med_frame = Frame(med_canvas,bg="#A1A100")
	med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
	def countDown():
		check=0
		for i in range(10,0,-1):
			if i==1:
				check=-1
			try:
				timer.configure(text=i)
				med_frame.update()
				time.sleep(1)
			except:
				pass
		try:	
			timer.configure(text="Time has been over!")
		except:
			pass
		if check==-1:
			return (-1)
		else:
			return 0
        
	global score
	score = 0
    
	mediumQ = [
                [
                    "Which country is the biggest by matter of territory?",
                     "Israel",
                     "India",
                     "Canada",
                     "Turkey"
                ],
                [
                    "What is the biggest continent on planet earth?",
                    "Africa",
                    "South America",
                    "Asia",
                    "Europe"
                ],
                [
                    "Inside which country the Vatican is located?",
                    "France",
                    "Germany",
                    "England",
                    "Italy"
                ]
            ]
	answer =["Canada","Asia","Italy"]
        
	li = [0,1,2]
	x = random.choice(li[0:])
    
	ques = Label(med_frame,text =mediumQ[x][0],font="calibri 12",bg="#B26500")
	ques.place(relx=0.5,rely=0.2,anchor=CENTER)

	var = StringVar()
    
	a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="#A1A100")
	a.place(relx=0.5,rely=0.42,anchor=CENTER)

	b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="#A1A100")
	b.place(relx=0.5,rely=0.52,anchor=CENTER)

	c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="#A1A100")
	c.place(relx=0.5,rely=0.62,anchor=CENTER) 

	d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="#A1A100")
	d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
	li.remove(x)
    
	timer = Label(medium)
	timer.place(relx=0.8,rely=0.82,anchor=CENTER)
   
	def display():
        
		if len(li) == 0:
			try:
				medium.destroy()
				showGraph(score)
			except:
				pass
		if len(li) == 1:
			nextQuestion.configure(text='End',command=calcscore)    
		if li:
			x = random.choice(li[0:])
			ques.configure(text =mediumQ[x][0])
            
			a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
			b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
			c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
			d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
			li.remove(x)
			y = countDown()
			if y == -1:
				display()

	def calcscore():
		global score
		if (var.get() in answer):
			score+=1
		display()
    
	submit = Button(med_frame,command=calcscore,text="Submit", fg="white", bg="black")
	submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
	nextQuestion = Button(med_frame,command=display,text="Next", fg="white", bg="black")
	nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
	y = countDown()
	if y == -1:
		display()
	medium.mainloop()
				
def hard():
    
	global hard
	hard = Tk()
	hard.title('Quiz App for Hard level')
    
	hard_canvas = Canvas(hard,width=720,height=440,bg="#101357")
	hard_canvas.pack()

	hard_frame = Frame(hard_canvas,bg="#A1A100")
	hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

	timer = Label(hard)
	timer.place(relx=0.8,rely=0.82,anchor=CENTER)
	def countDown():
		check=0
		for i in range(10,0,-1):
			if i==1:
				check=-1
			try:
				timer.configure(text=i)
				hard_frame.update()
				time.sleep(1)
			except:
				pass
		try:	
			timer.configure(text="Time has been over!")
		except:
			pass
		if check==-1:
			return (-1)
		else:
			return 0
        
	global score
	score = 0
    
	hardQ = [
                [
                    "What is the approx. population of Israel??",
                     "9.5M",
                     "6.7M",
                     "12.9M",
                     "15.3M"
                ],
                [
                    "Which country gave ALASKA as a present to US?",
                    "Canada",
                    "Mexico",
                    "Russia",
                    "Japan"
                ],
                [
                    "Between which countries Lake constanz is located?",
                    "Swiss ang Germany",
                    "Germany and Austria",
                    "France and Spain",
                    "Sweden and Finland"
                ]
            ]
	answer = [
            "9.5M",
            "Russia",
            "Swiss ang Germany",
            ]
    
	li = [0,1,2]
	x = random.choice(li[0:])
    
	ques = Label(hard_frame,text =hardQ[x][0],font="calibri 12",bg="#B26500")
	ques.place(relx=0.5,rely=0.2,anchor=CENTER)

	var = StringVar()
    
	a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="#A1A100")
	a.place(relx=0.5,rely=0.42,anchor=CENTER)

	b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="#A1A100")
	b.place(relx=0.5,rely=0.52,anchor=CENTER)

	c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="#A1A100")
	c.place(relx=0.5,rely=0.62,anchor=CENTER) 

	d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="#A1A100")
	d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
	li.remove(x)

	def display():
        
		if len(li) == 0:
			try:
				hard.destroy()
				showGraph(score)
			except:
				pass
		if len(li) == 1:
			nextQuestion.configure(text='End',command=calcscore)    
		if li:
			x = random.choice(li[0:])
			ques.configure(text =hardQ[x][0])
            
			a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
			b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
			c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
			d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
			li.remove(x)
			y = countDown()
			if y == -1:
				display()

	def calcscore():
		global score
		if (var.get() in answer):
			score+=1
		display()
    
	submit = Button(hard_frame,command=calcscore,text="Submit", fg="white", bg="black")
	submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
	nextQuestion = Button(hard_frame,command=display,text="Next", fg="white", bg="black")
	nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
	y = countDown()
	if y == -1:
		display()
	hard.mainloop()
	
def showGraph(graph):
    showg=Tk()
    showg.title('Your Marks')
	
    score="The final score is:" + str(graph)+"/3"
    marklabel=Label(showg,text=score,fg="black",bg="white")
    marklabel.pack()
	
    def signUpPageCall():
        showg.destroy()
        launch()
	#Here you can choose which difficulty level will be implemented (Should be updated).
    def easylaunch():
        showg.destroy()
        easy()
	
    re=Button(text="Re-attempt",command=easylaunch,bg="black",fg="white")
    re.pack()
    
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained','Total Marks'
    sizes = [int(graph),3-int(graph)]
    explode = (0.1,0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
    canvas = FigureCanvasTkAgg(fig, master=showg)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    b23=Button(text="Sign Out",command=signUpPageCall,fg="white", bg="black")
    b23.pack()
    
    showg.mainloop()
	
def launch():
	global mainpage 
	mainpage = Tk()
	mainpage.title('Welcome to Geographical knowledge quiz App')
	canvas = Canvas(mainpage,width = 900,height = 600, bg = 'purple')
	canvas.grid(column = 0 , row = 1)
	img = PhotoImage(file="output-onlinepngtools.png")
	canvas.create_image(50,10,image=img,anchor=NW)

	button = Button(mainpage, text='Play Now',command = Logging,bg="red",fg="yellow") 
	button.configure(width = 102,height=4, activebackground = "#6BF5F5", relief = SUNKEN)
	button.grid(column = 0 , row = 2)

	mainpage.mainloop()
    
if __name__=='__main__':
    launch()