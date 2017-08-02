from tkinter import *
from MARsql import *

#class for initlize window
class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.columnconfigure( 0, weight = 10 )
    def initialize(self):
        self.grid()

####TILE
        #label first name
        Title_label = Label(self,text="MAR/TAR SHNC",width=10 ,fg="black",bg="white")
        Title_label.grid(column=0,row=0,columnspan=2,sticky='EW',pady = 10)
####first name
        #label first name
        fn_label = Label(self,text="First Name",anchor="w",width=10 ,fg="black",bg="white")
        fn_label.grid(column=0,row=1,columnspan=1,sticky='EW',pady = 10)

        #text entry first name
        self.first_name = StringVar()
        self.fn_entry = Entry(self,textvariable=self.first_name)
        self.fn_entry.grid(column=1,row=1,sticky='EW',pady = 10)
        self.fn_entry.bind(self.OnButtonClick)
####last name

        #label last name
        ln_label = Label(self,text="Last Name",anchor="w",fg="black",bg="white")
        ln_label.grid(column=0,row=2,columnspan=1,sticky='EW')

        #text entry last name
        self.last_name = StringVar()
        self.ln_entry = Entry(self,textvariable=self.last_name)
        self.ln_entry.grid(column=1,row=2,sticky='EW',pady = 10)
        self.ln_entry.bind(self.OnButtonClick)

####Month
        #label month
        month_label = Label(self,text="Month",anchor="w",fg="black",bg="white")
        month_label.grid(column=0,row=3,columnspan=1,sticky='EW')
        #text entry month
        self.month = StringVar()
        self.month_entry = Entry(self,textvariable=self.month)
        self.month_entry.grid(column=1,row=3,sticky='EW',pady = 10)
        self.month_entry.bind(self.OnButtonClick)
####Year
        #label year
        year_label = Label(self,text="Year",anchor="w",fg="black",bg="white")
        year_label.grid(column=0,row=4,columnspan=1,sticky='EW')
        #text entry year
        self.year = StringVar()
        self.year_entry = Entry(self,textvariable=self.year)
        self.year_entry.grid(column=1,row=4,sticky='EW',pady = 10)
        self.year_entry.bind(self.OnButtonClick)

        #####create year check to make sure it fits in 4 chars
####MD Name
        #label md
        md_label = Label(self,text="MD Name",anchor="w",fg="black",bg="white")
        md_label.grid(column=0,row=5,columnspan=1,sticky='EW')
        #text entry md
        self.md = StringVar()
        self.md_entry = Entry(self,textvariable=self.md)
        self.md_entry.grid(column=1,row=5,sticky='EW',pady = 10)
        self.md_entry.bind(self.OnButtonClick)
###################################################

##MEDS
        mar_label = Label(self,text="MAR",fg="black",bg="white")
        mar_label.grid(column=4,row=0,columnspan=2,sticky='EW')
###space for grid
        space_label = Label(self,text="",width=10 ,fg="black",bg="white")
        space_label.grid(column=3,row=0,sticky='EW',pady = 10)
##Med1
        #label med1
        med1_label = Label(self,text="Medication 1",anchor="w",width=10 ,fg="black",bg="white")
        med1_label.grid(column=4,row=1,columnspan=1,sticky='EW',pady = 10)
        #text entry med1
        self.med1 = StringVar()
        self.med1_entry = Entry(self,textvariable=self.med1)
        self.med1_entry.grid(column=5,row=1,sticky='EW',pady = 10,columnspan=9,padx = 10)
        self.med1_entry.bind(self.OnButtonClick)

        #label order date med1
        orderDate1_label = Label(self,text="Order Date",anchor="w",width=10 ,fg="black",bg="white")
        orderDate1_label.grid(column=4,row=2,sticky='EW',pady = 10)

        #entry order date med1
        self.orderDate1 = StringVar()
        self.orderDate1_entry = Entry(self,textvariable=self.orderDate1,width=12 )
        self.orderDate1_entry.grid(column=5,row=2,sticky='EW',pady = 10)
        self.orderDate1_entry.bind(self.OnButtonClick)

        #label dose med1
        dose1_label = Label(self,text="Dose",anchor="w",width=10 ,fg="black",bg="white")
        dose1_label.grid(column=6,row=2,sticky='EW',pady = 10)

        #entry dose med1
        self.dose1 = StringVar()
        self.dose1_entry = Entry(self,textvariable=self.dose1,width=12)
        self.dose1_entry.grid(column=7,row=2,sticky='EW',pady = 10)
        self.dose1_entry.bind(self.OnButtonClick)

        #label freq med1
        freq1_label = Label(self,text="Freq",anchor="w",width=10 ,fg="black",bg="white")
        freq1_label.grid(column=8,row=2,sticky='EW',pady = 10)

        #entry freq med1
        self.freq1 = StringVar()
        self.freq1_entry = Entry(self,textvariable=self.freq1,width=12)
        self.freq1_entry.grid(column=9,row=2,sticky='EW',pady = 10)
        self.freq1_entry.bind(self.OnButtonClick)

        #label route med1
        route1_label = Label(self,text="Route",anchor="w",width=10 ,fg="black",bg="white")
        route1_label.grid(column=10,row=2,sticky='EW',pady = 10)

        #entry route med1
        self.route1 = StringVar()
        self.route1_entry = Entry(self,textvariable=self.route1,width=12)
        self.route1_entry.grid(column=11,row=2,sticky='EW',pady = 10)
        self.route1_entry.bind(self.OnButtonClick)

        #label time med1
        time1_label = Label(self,text="Time",anchor="w",width=10 ,fg="black",bg="white")
        time1_label.grid(column=12,row=2,sticky='EW',pady = 10)

        #entry time med1
        self.time1 = StringVar()
        self.time1_entry = Entry(self,textvariable=self.time1,width=12)
        self.time1_entry.grid(column=13,row=2,sticky='EW',pady = 10)
        self.time1_entry.bind(self.OnButtonClick)
####################
        self.resizable(False,False)

#############################################3
#BUTTONS
#button click

        button = Button(self,text=u"SAVE",command=self.OnButtonClick)
        button.grid(column=1,row=6,pady = 20)
        print("Button")


        print_button = Button(self,text=u"PRINT",command=self.printButton)
        print_button.grid(column=3,row=6,pady = 20)
        print("Print")

    def OnButtonClick(self):
        #self.labelVariable.set( self.e1.get()+" (You clicked the button)" )
        print(self.first_name.get())
        print(self.last_name.get())
        print(self.month.get())
        print(self.year.get())
        print(self.md.get())
        print(self.med1.get())
        create_table()
        insert(self.first_name.get(),self.last_name.get(),self.month.get(),self.year.get(),self.md.get(),self.med1.get())
        print(retrieve("mike"))
    #def OnPressEnter(self,event):
        #self.labelVariable.set( self.e1.get()+" (You pressed ENTER)" )

    def printButton(self):
        #print(viewTable())
        print(retrieve("mike"))
if __name__ == "__main__":
    #initizle class, None for parent class
    app = simpleapp_tk(None)

    app.title('MAR/TAR')
    #loop to wait for clicks or actions
    app.mainloop()
