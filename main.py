from tkinter import*
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox 

class Hospital:
	def __init__(self,root):
		self.root = root
		self.width = self.root.winfo_screenwidth()
		self.height = self.root.winfo_screenheight()
		self.root.geometry(str(self.width)+"x"+str(self.height)+"+0+0")
		self.root.overrideredirect(True)
		self.root.config(bg="white")
		
		self.nameVar = StringVar()
		self.emailVar = StringVar()
		self.passwordVar = StringVar()
		self.dobVar = StringVar()
		self.passionVar = StringVar()
		
		self.nameVar.set("")
		self.emailVar.set("")
		self.passwordVar.set("")
		self.dobVar.set("")
		self.passionVar.set("")
		
		
		self.image1 = Image.open("Doctor.jpg")
		self.image2 = Image.open("Patient.jpg")
		self.image3 = Image.open("Bg.jpg")
		self.image4 = Image.open("Home.jpg")
		self.image5 = Image.open("Setting.jpg")
		self.image6 = Image.open("Profile.jpg")
		
		self.resize_image1 = self.image1.resize((400, 400))
		self.resize_image2 = self.image2.resize((400, 400))
		self.resize_image3 = self.image3.resize((self.width, 1100))
		self.resize_image4 = self.image4.resize((100, 100))
		self.resize_image5 = self.image5.resize((100, 100))
		self.resize_image6 = self.image6.resize((100, 100))
		
		self.img1 = ImageTk.PhotoImage(self.resize_image1)
		self.img2 = ImageTk.PhotoImage(self.resize_image2)
		self.img3 = ImageTk.PhotoImage(self.resize_image3)
		self.img4 = ImageTk.PhotoImage(self.resize_image4)
		self.img5 = ImageTk.PhotoImage(self.resize_image5)
		self.img6 = ImageTk.PhotoImage(self.resize_image6)

		home = Button(self.root,image=self.img4,bd=0,command=self.main)
		home.place(x=self.width/2-50,y=self.height-125,width=100,height=100)
		setting = Button(self.root,image=self.img5,bd=0,command=self.setting)
		setting.place(x=800,y=self.height-125,width=100,height=100)
		profile = Button(self.root,image=self.img6,bd=0,command=self.profile)
		profile.place(x=200,y=self.height-125,width=100,height=100)
		
		self.main()
	def main(self):
		self.bgFrame = Frame(self.root,bg="white")
		self.bgFrame.place(x=0,y=0,width=self.width,height=self.height-150)
		
		self.navbar = Label(self.bgFrame,text="Hospital Management System",font=("Arial" ,12, "bold", "italic"),bg="#4fbab9",fg="white")
		self.navbar.place(x=0,y=0,width=self.width,height=150)
		
		self.doctorbtn = Button(self.bgFrame,image=self.img1,bd=0,bg="white",command=self.doctor)
		self.doctorbtn.place(x=self.width/3-300,y=350,width=400,height=400)
		self.doclabel = Label(self.bgFrame,text="Doctor",bg="white",fg="gray",font=("Arial",13,"bold"))
		self.doclabel.place(x=140,y=800)
		
		self.patientbtn = Button(self.bgFrame,image=self.img2,bd=0,bg="white",command=self.patient)
		self.patientbtn.place(x=self.width/3+250,y=350,width=400,height=400)
		self.patlabel = Label(self.bgFrame,text="Patient",bg="white",fg="gray",font=("Arial",13,"bold"))
		self.patlabel.place(x=700,y=800)
		
		self.labelbg = Label(self.bgFrame,bd=0,image=self.img3)
		self.labelbg.place(x=0,y=880)
		
		self.signupbtn = Button(self.bgFrame,text="SignUp",font=("Arial",5),bd=0,bg="#4fbab9",fg="gray15",command=self.SignUp)
		self.signupbtn.place(x=self.width/2-100,y=1800,width=200,height=70)
		
	def doctor(self):
		self.bgFrame = Frame(self.root,bg="white")
		self.bgFrame.place(x=0,y=0,width=self.width,height=self.height-150)
		
		self.navbar = Label(self.bgFrame,text="Doctor Login",font=("Arial" ,12, "bold", "italic"),bg="#4fbab9",fg="white")
		self.navbar.place(x=0,y=0,width=self.width,height=150)
		
	def patient(self):
		self.bgFrame = Frame(self.root,bg="white")
		self.bgFrame.place(x=0,y=0,width=self.width,height=self.height-150)
		
		self.navbar = Label(self.bgFrame,text="Patient Login",font=("Arial" ,12, "bold", "italic"),bg="#4fbab9",fg="white")
		self.navbar.place(x=0,y=0,width=self.width,height=150)
		
		
	def setting(self):
		self.bgFrame = Frame(self.root,bg="white")
		self.bgFrame.place(x=0,y=0,width=self.width,height=self.height-150)
		
		self.navbar = Label(self.bgFrame,text="Change Setting",font=("Arial" ,12, "bold", "italic"),bg="#4fbab9",fg="white")
		self.navbar.place(x=0,y=0,width=self.width,height=150)
		pass
	def profile(self):
		self.bgFrame = Frame(self.root,bg="white")
		self.bgFrame.place(x=0,y=0,width=self.width,height=self.height-150)
		
		self.navbar = Label(self.bgFrame,text="Your Profile",font=("Arial" ,12, "bold", "italic"),bg="#4fbab9",fg="white")
		self.navbar.place(x=0,y=0,width=self.width,height=150)
		
		self.profilebtn = Button(self.bgFrame,text="Add profile",fg="#4fbab9",bg="white",command=self.change_profile_photo)
		self.profilebtn.place(x=50,y=200,width=400,height=400)
		
		self.lab1 = Label(self.bgFrame,text="Name :- "+self.nameVar.get().title(),bg="white",fg="#4fbab9")
		self.lab1.place(x=500,y=270)
		
		self.lab2 = Label(self.bgFrame,text="Date of Birth :- "+self.dobVar.get(),bg="white",fg="#4fbab9")
		self.lab2.place(x=500,y=370)
		
		self.lab3 = Label(self.bgFrame,text="Passion :- "+self.passionVar.get().title(),bg="white",fg="#4fbab9")
		self.lab3.place(x=500,y=470)
		
		self.lab4 = Label(self.bgFrame,text="Email :- "+self.emailVar.get(),bg="white",fg="#4fbab9")
		self.lab4.place(x=100,y=700)
		
		
		
		
		
	def change_profile_photo(self):
		try:
			image = self.openimgdirectory()
			img = Image.open(image)
			img = img.resize((400, 400))
			img = ImageTk.PhotoImage(img)
			self.profilebtn.config(image=img)
			self.profilebtn.image=img
		except:
			pass
		
	def openimgdirectory(self):
		try:
			filename = filedialog.askopenfilename(title ="profile")
			return filename
			
		except:
			pass
	def SignUp(self):
		self.bgFrame = Frame(self.root,bg="white")
		self.bgFrame.place(x=0,y=0,width=self.width,height=self.height-150)
		
		self.navbar = Label(self.bgFrame,text="SignUp Page",font=("Arial" ,12, "bold", "italic"),bg="#4fbab9",fg="white")
		self.navbar.place(x=0,y=0,width=self.width,height=150)
		
		self.label = Label(self.bgFrame,bg="white",fg="#4fbab9",text=" Enter Your Info",font=("Arial",13,"bold","underline"))
		self.label.place(x=self.width/2-250,y=200)
		
		self.namelabel = Label(self.bgFrame,bg="white",text="Full Name :- ",font=("Arial",7))
		self.namelabel.place(x=50,y=400)
		self.nameentry = Entry(self.bgFrame,textvariable=self.nameVar,bd=0,bg="#4fbab9",fg="white",font=("Arial",5))
		self.nameentry.place(x=350,y=400,width=500,height=50)
		
		self.doblabel = Label(self.bgFrame,bg="white",text="Date of Birth :- ",font=("Arial",7))
		self.doblabel.place(x=50,y=500)
		self.dobentry = Entry(self.bgFrame,textvariable=self.dobVar,bd=0,bg="#4fbab9",fg="white",font=("Arial",5))
		self.dobentry.place(x=350,y=500,width=500,height=50)
		
		self.emaillabel = Label(self.bgFrame,bg="white",text="Enter Email :- ",font=("Arial",7))
		self.emaillabel.place(x=50,y=600)
		self.emailentry = Entry(self.bgFrame,textvariable=self.emailVar,bd=0,bg="#4fbab9",fg="white",font=("Arial",5))
		self.emailentry.place(x=350,y=600,width=500,height=50)
		
		self.passwordlabel = Label(self.bgFrame,bg="white",text="Create Password :- ",font=("Arial",7))
		self.passwordlabel.place(x=50,y=700)
		self.passwordentry = Entry(self.bgFrame,textvariable=self.passwordVar,bd=0,bg="#4fbab9",fg="white",font=("Arial",5))
		self.passwordentry.place(x=450,y=700,width=500,height=50)
		
		self.passionlabel = Label(self.bgFrame,bg="white",text="Enter Your Passion :- ",font=("Arial",7))
		self.passionlabel.place(x=50,y=800)
		self.passionentry = Entry(self.bgFrame,textvariable=self.passionVar,bd=0,bg="#4fbab9",fg="white",font=("Arial",5))
		self.passionentry.place(x=450,y=800,width=500,height=50)
		
		self.enterbtn = Button(self.bgFrame,text="Done",fg="#4fbab9",bg="white",command=self.message)
		self.enterbtn.place(x=self.width/2-100,y=1000,width=200,height=70)
		
	def message(self):
		if (self.nameVar.get()!="" and self.emailVar.get()!="" and self.passwordVar.get()!="" and self.passionVar.get()!="" and self.dobVar.get()!=""):
			messagebox.showinfo("showinfo", "SignUp Successfully") 
		else:
			messagebox.showwarning("showwarning","All entry must required") 

  
		pass
		
root = Tk()
obj = Hospital(root)
root.mainloop()