import tkinter as tk
from tkinter import ttk


def profileWin(root):

	root1 = tk.Frame(root, bg= '#111c14')
	root1.grid()
	#define the label
	tk.Label(root1, text='CREATE PROFILE', font=("Arial", 30), bg='#111c14', fg='#76c2cc').grid(column=0, row=0, sticky='W', padx=75, pady=10)
	#define font


	#entry for name
	tk.Label(root1, text='Name:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)
	name = tk.StringVar()
	name_entered = ttk.Entry(root1, font=("Arial, 15"), textvariable=name)
	name_entered.grid(column=0, row=1, sticky=tk.W, padx=210, pady=10)


	#entry for reg No
	tk.Label(root1, text='Registration Number:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)
	regNo = tk.StringVar()
	regNumber = ttk.Entry(root1, font=("Arial, 15"), textvariable=regNo)
	regNumber.grid(column=0, row=2, sticky=tk.W, padx=210, pady=10)


	#entry for phone No
	tk.Label(root1, text='Phone Number:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)
	phoneNo = tk.StringVar()
	phoneNumber = ttk.Entry(root1, font=("Arial, 15"), textvariable=phoneNo)
	phoneNumber.grid(column=0, row=3, sticky=tk.W, padx=210, pady=10)

	#checkbox for gender
	tk.Label(root1, text='Sex:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=4, sticky=tk.W, padx=10, pady=10)
	genVar = tk.IntVar()
	male = tk.Radiobutton(root1, text="Male", variable=genVar, font=("Arial", 10), value=1, bg='#111c14', fg='#76c2cc')
	male.grid(column=0, row=4, sticky=tk.W, padx=210, pady=10, columnspan=2)

	female = tk.Radiobutton(root1, text="Female", variable=genVar, font=("Arial", 10), value=2, bg='#111c14', fg='#76c2cc')
	female.grid(column=0, row=4, sticky=tk.W, padx=310, pady=10, columnspan=2)

	def logg():
		try:
			name1 = name.get()
			regNo1 = regNo.get()
			phoneNo1 = int(phoneNo.get())
			gender1 = int(genVar.get())

			print(name1)
			print(regNo1)
			print(phoneNo1)

			if gender1 == 1:
				print("Male")
			elif gender1 == 2:
				print("Female")

		except(ValueError):
			print("Please Input Correct Values")


	#add finger print button
	addFinger = tk.Button(root1, text='Continue', command= lambda: [changepage(), logg()], bg='red', fg='white')
	addFinger.grid(column=0, row=5, sticky=tk.W, padx=230, pady=30)

	#focus the mouse on name 
	name_entered.focus()

def success(root):
	root3 = tk.Frame(root, bg= '#111c14')
	root3.grid()

	tk.Label(root3, text='Profile Created Successfully', font=("Arial", 30), bg='#111c14', fg='#76c2cc').grid(column=0, row=0, sticky='NSWE', pady=100)

	def exit():
		root.destroy()
 	
	close = tk.Button(root3, text='Close', font=("Arial", 10), bg='red', fg='white', command=exit)
	close.grid(column=0, row=1, sticky=tk.W, padx=230, pady=50)

def fingerWindow(root):
	root2 = tk.Frame(root, bg= '#111c14')
	root2.grid()

	tk.Label(root2, text='Insert Your Fingerprints', font=("Arial", 30), bg='#111c14', fg='#76c2cc').grid(column=0, row=0, sticky=tk.W, padx=50, pady=20)



	def run_progress(run=6000):
		progressBar = ttk.Progressbar(root2, orient='horizontal', length=400, mode='determinate')
		progressBar.grid(column=0, row=3, sticky=tk.W, padx = 50, pady=10)
		progressBar.start()
		root2.after(run, progressBar.stop)
		root2.after(6100, progressBar.destroy)
		b2.configure(state='normal')

	def run_progress1(run=6000):
		progressBar = ttk.Progressbar(root2, orient='horizontal', length=400, mode='determinate')
		progressBar.grid(column=0, row=3, sticky=tk.W, padx = 50, pady=10)
		progressBar.start()
		root2.after(run, progressBar.stop)
		root2.after(6100, progressBar.destroy)
		b3.configure(state='normal')


	#creating a frame and buttons
	b1 = tk.Button(root2, text='Place your Finger', font=("Arial", 10), bg='#111c14', fg='white', command=run_progress)
	b1.grid(column=0, row=2, sticky=tk.W, padx=35, pady=20)
	f1 = tk.Frame(root2, width=80, height=100, bg='#9dd4d1')
	f1.grid(column=0, row=1, sticky=tk.W, padx=50)

	b2 = tk.Button(root2, text='Re-Place your Finger', font=("Arial", 10), bg='#111c14', fg='white', command=run_progress1, state="disabled")
	b2.grid(column=0, row=2, sticky=tk.W, padx=165, pady=20)
	f2 = tk.Frame(root2, width=80, height=100, bg='#9dd4d1')
	f2.grid(column=0, row=1, sticky=tk.W, padx=200)

	b3 = tk.Button(root2, text='Place your Finger Again', font=("Arial", 10), bg='#111c14', fg='white', command=run_progress, state="disabled")
	b3.grid(column=0, row=2, sticky=tk.W, padx=315, pady=20)
	f3 = tk.Frame(root2, width=80, height=100, bg='#9dd4d1')
	f3.grid(column=0, row=1, sticky=tk.W, padx=350)


	#add finger print button
	fingerdone = tk.Button(root2, text='Done', command=changepage, font=('Arial', 10), bg='red', fg='white')
	fingerdone.grid(column=0, row=4, sticky=tk.W, padx=230, pady=15)


def changepage():
	global pagenum, root
	for widget in root.winfo_children():
		widget.destroy()
	if pagenum == 1:
		fingerWindow(root)
		pagenum = 2
	else:
		success(root)
		pagenum = 3
#creating a window
pagenum = 1
root = tk.Tk()
root['bg'] = '#111c14'
root.title("Enroll Student")
root.geometry("500x350")
root.resizable(False, False)
profileWin(root)


#call the function
root.mainloop()


