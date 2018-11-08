from tkinter import *
from tkinter import ttk
import tkinter as tk

from BankAccount import bankAccount_Class
from BankAccount import arbejdernesLandsbank_Class
from BankAccount import sparNordBank_Class
from BankAccount import sparNordBankFordelKunde_Class


def updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen):
    listBankCustomers.delete(0, END)
    listCounter = 1
    if (0 == global_Bank_Choosen):
        for bankCustomer in bankCustomerList:
            bankAccountInfo = (str)(print(bankCustomer))
            listBankCustomers.insert(listCounter, bankCustomer.printToGuiComponents())

if __name__ == '__main__':
    bankCustomerList = []

    root = tk.Tk()

    global_Bank_Choosen = 0
    global_New_Bank_Customer_Choosen = 1

    root.title("Bank System")
    root.geometry("1024x768")

    # Nu opretter vi Tabs på vores side
    tabControl = ttk.Notebook(root)

    tabBankOverview = ttk.Frame(tabControl)
    tabControl.add(tabBankOverview, text="Bank Oversigt")

    tabCustomerOverview = ttk.Frame(tabControl)
    tabControl.add(tabCustomerOverview, text="Kunde Oversigt")

    tabTransactionsOverview = ttk.Frame(tabControl)
    tabControl.add(tabTransactionsOverview, text="Kunde Posteringer")

    tabControl.pack(expand=1, fill="both")

    # Nu opretter vi kontroller til vores Tab : tabBankOverview
    """
    labelFrame = ttk.LabelFrame(tabBankOverview, text="First Tab Widgets")
    labelFrame.grid(column = 0, row = 0, padx = 8, pady = 10)

    label = ttk.Label(labelFrame, text="Enter your Nanme : ")
    label.grid(column = 0, row = 0, sticky="W")
    """

    labelBankOverview = ttk.Label(tabBankOverview, text="Se Bank : ")
    labelBankOverview.grid(column=0, row=0, padx = 8, pady = 10, sticky="W")

    tkVar = StringVar(root)
    banks = {"Alle Banker",
             "Arbejdernes Landsbank",
             "SparNord Bank",
             "SparNord Bank Fordelskunde"}
    tkVar.set("Alle Banker") # Sæt default option

    def change_banks_dropdown(*args):
        print(tkVar.get())
        if ("Alle Banker" == tkVar.get()):
            global_Bank_Choosen = 0
            labelBankCustomerText.set("Oversigt over Bank Kunder i Alle Banker")
        if ("Arbejdernes Landsbank" == tkVar.get()):
            global_Bank_Choosen = 1
            labelBankCustomerText.set("Oversigt over Bank Kunder i Aejdernes Landsbank")
        if ("SparNord Bank" == tkVar.get()):
            global_Bank_Choosen = 2
            labelBankCustomerText.set("Oversigt over Bank Kunder i SparNord Bank")
        if ("SparNord Bank Fordelskunde" == tkVar.get()):
            global_Bank_Choosen = 3
            labelBankCustomerText.set("Oversigt over Bank Kunder i SparNord Bank Fordelskunde")

    tkVar.trace('w', change_banks_dropdown)

    popupMenuWatchBankCustomers = OptionMenu(tabBankOverview, tkVar, *banks)
    popupMenuWatchBankCustomers.grid(row = 0, column = 1)

    tkVarNew = StringVar(root)
    banksNew = {"Arbejdernes Landsbank",
                "SparNord Bank",
                "SparNord Bank Fordelskunde"}
    tkVarNew.set("Arbejdernes Landsbank")  # Sæt default option

    def change_newBankCustomer_dropdown(*args):
        print(tkVar.get())
        if ("Arbejdernes Landsbank" == tkVarNew.get()):
            global_New_Bank_Customer_Choosen = 1
        if ("SparNord Bank" == tkVarNew.get()):
            global_New_Bank_Customer_Choosen = 2
        if ("SparNord Bank Fordelskunde" == tkVarNew.get()):
            global_New_Bank_Customer_Choosen = 3

    tkVarNew.trace('w', change_newBankCustomer_dropdown)

    popupMenuNewBankCustomers = OptionMenu(tabBankOverview, tkVarNew, *banksNew)
    popupMenuNewBankCustomers.grid(row = 0, column = 2)

    labelNewBankCustomer = ttk.Label(tabBankOverview, text="Navn på nu Bank Kunde : ")
    labelNewBankCustomer.grid(column=0, row=1, padx=8, pady=10, sticky="W")

    txtboxNewBankCustomer = Entry(tabBankOverview, width=50)
    txtboxNewBankCustomer.grid(column = 1, row = 1)

    def saveNewBankCustomer():
        bankAccountCustomerName =  txtboxNewBankCustomer.get()
        if (1 == global_New_Bank_Customer_Choosen):
            bankCustomerList.append(arbejdernesLandsbank_Class(name=bankAccountCustomerName))
        if (2 == global_New_Bank_Customer_Choosen):
            bankCustomerList.append(sparNordBank_Class(name="Test"))
        if (3 == global_New_Bank_Customer_Choosen):
            bankCustomerList.append(sparNordBankFordelKunde_Class(name="Test"))
        updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen)
        txtboxNewBankCustomer.delete(0, END)

    newBankCustomerButton = ttk.Button(tabBankOverview, text="Gem ny Bank Kunde",
                                       command = saveNewBankCustomer)
    newBankCustomerButton.grid(row = 2, column = 0, padx=8, pady=10)

    labelBankCustomerText = StringVar()
    labelBankCustomerText.set("Oversigt over Bank Kunder i Alle Banker")

    labelBankCustomer = ttk.Label(tabBankOverview, textvariable=labelBankCustomerText)
    labelBankCustomer.grid(column=0, row=3, padx=8, pady=10, sticky="W")

    listBankCustomers = Listbox(tabBankOverview, width=50)
    listBankCustomers.grid(row=4, column=0, padx=8, pady=10)
    #listBankCustomers.pack();

    # Nu opretter vi kontroller til vores Tab : tabCustomerOverview

    label2 = ttk.Label(tabCustomerOverview, text="Label på Tab 2 !!!")
    label2.grid(column=0, row=0, padx=8, pady=10, sticky="W")

    label2_2 = ttk.Label(tabCustomerOverview, text="Label 2 på Tab 2 !!!")
    label2_2.grid(column=0, row=1, padx=8, pady=10, sticky="W")

    root.mainloop()