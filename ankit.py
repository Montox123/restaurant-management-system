from tkinter import *
import random
import time
import datetime






class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("2000x8000")
        frame = Frame(root,bg="gray")
        frame.pack(fill=BOTH,expand=True)
        Tops=Frame(root, width=1600,relief=SUNKEN)
        Tops.pack(side=TOP)

        f1=Frame(root,width=800,height=1000,relief=SUNKEN)
        f1.pack(side=LEFT)

        self.root.title("Restaurant Management System")
        localtime=time.asctime(time.localtime(time.time()))

        lblInfo= Label(Tops,font=('helvetica',50,'bold'),text="UNKNOWN RESTAURANT ",fg="Black",bd=10)
        lblInfo.grid(row=0,column=0)

        lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
        lblInfo.grid(row=0,column=0)
        
        photo = PhotoImage(file="RI.png")

        ankit_label = Label(image=photo)
        ankit_label.pack(fill=BOTH,expand=True)


        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.MOMO = IntVar()
        self.Chowmine = IntVar()
        self.Burger = IntVar()
        self.Sandwich = IntVar()
        self.EggRoll = IntVar()
        self.PaneerChilli = IntVar()
        self.PaneerButterMasala = IntVar()
        self.ButterNaan = IntVar()
        self.AaluBiryani = IntVar()
        self.TanduriRoti = IntVar()
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.Lassi= IntVar()
        self.ChocoLava = IntVar()
        self.ChickenChilli = IntVar()
        self.ChickenButterMasala = IntVar()
        self.Friedrice = IntVar()
        self.ChickenBiryani = IntVar()
        self.ChickenSchezwan = IntVar()
        self.total_Chinese = StringVar()
        self.total_VegMeal = StringVar()
        self.total_NonVegMeal = StringVar()
        self.total_DandD = StringVar()
        self.tax_Chi = StringVar()
        self.tax_Veg = StringVar()
        self.tax_NonVegMeal = StringVar()
        self.tax_DandD = StringVar()


        #===================================
        bg_color = "#996633"
        fg_color = "powder blue"
        lbl_color = 'white'
        #Title of App
        
        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = bg_color,fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

        #==================Chinese Frame=====================#
        F2 = LabelFrame(self.root,text = 'Chinese',bd = 15,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "MOMO")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.MOMO)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Face Cream
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Chowmine")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Chowmine)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Face Wash
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Burger")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Burger)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hair Spray
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sandwich")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Sandwich)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Body Lotion
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "EggRoll")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.EggRoll)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================VegMeal Frame=====================#
        F2 = LabelFrame(self.root,text = 'Veg Meal',bd = 15,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 280,y = 180,width = 325,height = 380)

        #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "PaneerChilli")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.PaneerChilli)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "PaneerButterMasala")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.PaneerButterMasala)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "ButterNaan")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ButterNaan)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "AaluBiryani")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.AaluBiryani)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "TanduriRoti")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.TanduriRoti)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================NonVegMeal Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Drinks and Desert',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 600,y = 180,width = 325,height = 380)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maza")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.maza)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Frooti")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.frooti)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Lassi")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Lassi)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "ChocoLava")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ChocoLava)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)
        
        F2 = LabelFrame(self.root,text = 'NonVegMeal',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 900,y = 180,width = 325,height = 380)
        
         #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "ChickenChilli")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ChickenChilli)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "ChickenButterMasala")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ChickenButterMasala)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Friedrice")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Friedrice)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "ChickenBiryani")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ChickenBiryani)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "ChickenSchezwan")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ChickenSchezwan)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 1210,y = 180,width = 350,height = 450)
        #===========
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 200)

        #===================
        Chim_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total chinese Item")
        Chim_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        Chim_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_Chinese)
        Chim_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Veg Item")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_VegMeal)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Non Veg Item")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_NonVegMeal)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)
  
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total DrinksAndDesert")
        oth_lbl.grid(row = 3,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_DandD)
        oth_en.grid(row = 3,column = 1,ipady = 2,ipadx = 5)

        #================
        Chimt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Chinese Tax")
        Chimt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        Chimt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_Chi)
        Chimt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "VegMeal Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_Veg)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "NonVegMeals Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_NonVegMeal)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "DrinksAndDesert")
        otht_lbl.grid(row = 3,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_DandD)
        otht_en.grid(row = 3,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

#Function to get total prices
    def total(self):
        #=================Total Chinese Prices
        self.total_Chinese_prices = (
            (self.MOMO.get() * 45)+
            (self.Chowmine.get() * 50)+
            (self.Burger.get() * 30)+
            (self.Sandwich.get() * 40)+
            (self.EggRoll.get() * 40)
        )
        self.total_Chinese.set("Rs. "+str(self.total_Chinese_prices))
        self.tax_Chi.set("Rs. "+str(round(self.total_Chinese_prices*0.05)))
        #====================Total VegMeal Prices
        self.total_VegMeal_prices = (
            (self.AaluBiryani.get()*60)+
            (self.ButterNaan.get() * 30)+
            (self.PaneerButterMasala.get() * 160)+
            (self.PaneerChilli.get() *140)+
            (self.TanduriRoti.get() * 15)

        )
        self.total_VegMeal.set("Rs. "+str(self.total_VegMeal_prices))
        self.tax_Veg.set("Rs. "+str(round(self.total_VegMeal_prices*0.02)))
        #======================Total NonVegMeal Prices
        self.total_NonVegMeal_prices = (

            (self.ChickenBiryani.get()*90)+
            (self.Friedrice.get() * 50)+
            (self.ChickenButterMasala.get() * 160)+
            (self.ChickenChilli.get() *140)+
            (self.ChickenSchezwan.get() * 180)

        )
        self.total_NonVegMeal.set("Rs. "+str(self.total_NonVegMeal_prices))
        self.tax_NonVegMeal.set("Rs. "+str(round(self.total_NonVegMeal_prices*0.02)))

        #====================Total DrinksandDesert Prices
        self.total_DrinksAndDesert_prices = (

            (self.maza.get() * 20)+
            (self.frooti.get() * 50)+
            (self.coke.get() * 60)+
            (self.Lassi.get() * 30)+
            (self.ChocoLava.get() * 50)
            
        )
        self.total_DandD.set("Rs. "+str(self.total_DrinksAndDesert_prices))
        self.tax_DandD.set("Rs. "+str(round(self.total_DrinksAndDesert_prices*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Unknown Restaurant\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\ndishes          Qty         Price")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.MOMO.get() != 0:
            self.txt.insert(END,f"\nMOMO            {self.MOMO.get()}               {self.MOMO.get() * 45}")
        if self.Chowmine.get() != 0:
            self.txt.insert(END,f"\nChowmine        {self.Chowmine.get()}           {self.Chowmine.get() * 50}")
        if self.Burger.get() != 0:
            self.txt.insert(END,f"\nBurger          {self.Burger.get()}             {self.Burger.get() * 30}")
        if self.Sandwich.get() != 0:
            self.txt.insert(END,f"\nSandwich        {self.Sandwich.get()}           {self.Sandwich.get() * 30}")
        if self.EggRoll.get() != 0 :
            self.txt.insert(END,f"\nEggRoll         {self.EggRoll.get()}            {self.EggRoll.get() * 40}")
        if self.AaluBiryani.get() != 0:
            self.txt.insert(END,f"\nAaluBiryani     {self.AaluBiryani.get()}        {self.AaluBiryani.get() * 60}")
        if self.ButterNaan.get() != 0:
            self.txt.insert(END,f"\nButter Naan     {self.ButterNaan.get()}         {self.ButterNaan.get() * 30}")
        if self.PaneerButterMasala.get() != 0:
            self.txt.insert(END,f"\nPaneerButterMasala {self.PaneerButterMasala.get()} {self.PaneerButterMasala.get() * 160}")
        if self.PaneerChilli.get() != 0:
            self.txt.insert(END,f"\nPaneerChilli     {self.PaneerChilli.get()}      {self.PaneerChilli.get() * 140}")
        if self.TanduriRoti.get() != 0:
            self.txt.insert(END,f"\nTanduriRoti      {self.TanduriRoti.get()}       {self.TanduriRoti.get() * 15}")
        if self.maza.get() != 0:
            self.txt.insert(END,f"\nMaza             {self.maza.get()}              {self.maza.get() * 20}")
        if self.frooti.get() != 0:
            self.txt.insert(END,f"\nFrooti           {self.frooti.get()}            {self.frooti.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\nCoke             {self.coke.get()}              {self.coke.get() * 60}")
        if self.Lassi.get() != 0:
            self.txt.insert(END,f"\nLassi            {self.Lassi.get()}             {self.Lassi.get() * 30}")
        if self.ChocoLava.get() != 0:
            self.txt.insert(END,f"\nChocoLava        {self.ChocoLava.get()}          {self.ChocoLava.get() * 50}")
        if self.ChickenBiryani.get() != 0:
            self.txt.insert(END,f"\nChickenBiryani   {self.ChickenBiryani.get()}     {self.ChickenBiryani.get() * 90}")
        if self.Friedrice.get() != 0:
            self.txt.insert(END,f"\nFriedrice        {self.Friedrice.get()}          {self.Friedrice.get() * 50}")
        if self.ChickenButterMasala.get() != 0:
            self.txt.insert(END,f"\nChickenButterMasala {self.ChickenButterMasala.get()} {self.ChickenButterMasala.get() * 160}")
        if self.ChickenChilli.get() != 0:
            self.txt.insert(END,f"\nChickenChilli     {self.ChickenChilli.get()}      {self.ChickenChilli.get() * 140}")
        if self.ChickenSchezwan.get() != 0:
            self.txt.insert(END,f"\nChickenSchezwan   {self.ChickenSchezwan.get()}    {self.ChickenSchezwan.get() * 180}")    
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : {self.total_Chinese_prices+self.total_VegMeal_prices+self.total_NonVegMeal_prices+self.total_DrinksAndDesert_prices+self.total_Chinese_prices * 0.05+self.total_VegMeal_prices * 0.02+self.total_NonVegMeal_prices *0.02+self.total_DrinksAndDesert_prices*.05}")


    #Function to exit
    def exit(self):
        self.root.destroy()

    #Function To Clear All Fields


        


root = Tk()
object = Bill_App(root)
root.mainloop()

import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url ='https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization':'OHPfFBluxrmX3E6wa2yTWjDLvsgQRISiY7nqb1UopCh89tJK0NzPwS2qiEd4KTLfFNtIMBveARl68Y9x',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route':'p',
        'numbers': number

    }


    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)
    return dic.get('return')



def btn_click():
    num=textNumber.get()
    msg=textMsg.get("1.0",END)   
    r= send_sms(num,msg)
    if r:
        showinfo("send success","successfully send")
    else:
        showerror("Error","something went wrong..")


root=Tk()
root.title("message sender")
root.geometry("1000x550")
font=("helvetica",22,"bold")
textNumber=Entry(root,font=font)
textNumber.pack(fill=X,pady=20)

textMsg=Text(root)
textMsg.pack(fill=X)
sendBtn=Button(root,text="SEND SMS",command=btn_click)
sendBtn.pack()

root.mainloop()


