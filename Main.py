from tkinter import *
from tkinter import ttk
import tkinter as tk

from enum import Enum

from BankAccount import bankAccount_Class
from BankAccount import arbejdernesLandsbank_Class
from BankAccount import sparNordBank_Class
from BankAccount import sparNordBankFordelKunde_Class

class BankClass_ENUM(Enum):
    ALLE_BANKER = 0
    ARBEJDERNES_LANDSBANK = 1
    SPARNORD_BANK = 2
    SPARNORD_BANK_FORDELSKUNDE = 3


def updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen):
    listBankCustomers.delete(0, END)
    listCounter = 0
    if (BankClass_ENUM.ALLE_BANKER.value == global_Bank_Choosen.get()):
        for bankCustomer in bankCustomerList:
            listBankCustomers.insert(END, str(listCounter) + " : " + bankCustomer.printToGuiComponents())
            listCounter += 1

    if (BankClass_ENUM.ARBEJDERNES_LANDSBANK.value == global_Bank_Choosen.get()):
        for bankCustomer in bankCustomerList:
            className = bankCustomer.__class__.__name__
            if ("arbejdernesLandsbank_Class" == className):
                listBankCustomers.insert(END, str(listCounter) + " : " + bankCustomer.printToGuiComponents())
                listCounter += 1

    if (BankClass_ENUM.SPARNORD_BANK.value == global_Bank_Choosen.get()):
        for bankCustomer in bankCustomerList:
            className = bankCustomer.__class__.__name__
            if ("sparNordBank_Class" == className):
                listBankCustomers.insert(END, str(listCounter) + " : " + bankCustomer.printToGuiComponents())
            listCounter += 1

    if (BankClass_ENUM.SPARNORD_BANK_FORDELSKUNDE.value == global_Bank_Choosen.get()):
        for bankCustomer in bankCustomerList:
            className = bankCustomer.__class__.__name__
            if ("sparNordBankFordelKunde_Class" == className):
                listBankCustomers.insert(END, str(listCounter) + " : " + bankCustomer.printToGuiComponents())
            listCounter += 1

if __name__ == '__main__':
    def closeWindow():
        root.destroy()

    bankCustomerList = []
    bankCustomerTransactionsList = []
    root = tk.Tk()

    global_Bank_Choosen = IntVar()
    global_New_Bank_Customer_Choosen = IntVar()
    global_Customer_Choosen_Index = IntVar()

    global_Bank_Choosen.set(BankClass_ENUM.ALLE_BANKER.value)
    global_New_Bank_Customer_Choosen.set(BankClass_ENUM.ARBEJDERNES_LANDSBANK.value)
    global_Customer_Choosen_Index.set(-1)

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
    labelBankOverview = ttk.Label(tabBankOverview, text="Se Bank : ")
    labelBankOverview.grid(column=0, row=0, padx = 8, pady = 10, sticky="W")

    tkVar = StringVar(root)
    banks = {"Alle Banker",
             "Arbejdernes Landsbank",
             "SparNord Bank",
             "SparNord Bank Fordelskunde"}
    tkVar.set("Alle Banker") # Sæt default option

    def change_banks_dropdown(*args):
        global global_Bank_Choosen
        print(tkVar.get())
        if ("Alle Banker" == tkVar.get()):
            global_Bank_Choosen.set(BankClass_ENUM.ALLE_BANKER.value)
            labelBankCustomerText.set("Oversigt over Bank Kunder i Alle Banker")

        if ("Arbejdernes Landsbank" == tkVar.get()):
            global_Bank_Choosen.set(BankClass_ENUM.ARBEJDERNES_LANDSBANK.value)
            labelBankCustomerText.set("Oversigt over Bank Kunder i Arbejdernes Landsbank")

        if ("SparNord Bank" == tkVar.get()):
            global_Bank_Choosen.set(BankClass_ENUM.SPARNORD_BANK.value)
            labelBankCustomerText.set("Oversigt over Bank Kunder i SparNord Bank")

        if ("SparNord Bank Fordelskunde" == tkVar.get()):
            global_Bank_Choosen.set(BankClass_ENUM.SPARNORD_BANK_FORDELSKUNDE.value)
            labelBankCustomerText.set("Oversigt over Bank Kunder i SparNord Bank Fordelskunde")

        updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen)

    tkVar.trace('w', change_banks_dropdown)

    popupMenuWatchBankCustomers = OptionMenu(tabBankOverview, tkVar, *banks)
    popupMenuWatchBankCustomers.grid(row = 0, column = 1)

    tkVarNew = StringVar(root)
    banksNew = {"Arbejdernes Landsbank",
                "SparNord Bank",
                "SparNord Bank Fordelskunde"}
    tkVarNew.set("Arbejdernes Landsbank")  # Sæt default option

    global_New_Bank_Customer_Choosen.set(1)
    def change_newBankCustomer_dropdown(*args):
        global global_New_Bank_Customer_Choosen
        print(tkVar.get())
        if ("Arbejdernes Landsbank" == tkVarNew.get()):
            global_New_Bank_Customer_Choosen.set(BankClass_ENUM.ARBEJDERNES_LANDSBANK.value)

        if ("SparNord Bank" == tkVarNew.get()):
            global_New_Bank_Customer_Choosen.set(BankClass_ENUM.SPARNORD_BANK.value)

        if ("SparNord Bank Fordelskunde" == tkVarNew.get()):
            global_New_Bank_Customer_Choosen.set(BankClass_ENUM.SPARNORD_BANK_FORDELSKUNDE.value)

        updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen)

    tkVarNew.trace('w', change_newBankCustomer_dropdown)

    popupMenuNewBankCustomers = OptionMenu(tabBankOverview, tkVarNew, *banksNew)
    popupMenuNewBankCustomers.grid(row = 0, column = 2)

    labelNewBankCustomer = ttk.Label(tabBankOverview, text="Navn på ny Bank Kunde : ")
    labelNewBankCustomer.grid(column=0, row=1, padx=8, pady=10, sticky="W")

    # Her defineres en tekstboks, som vi kan skrive tekst ind i.
    txtboxNewBankCustomer = Entry(tabBankOverview, width=50)
    txtboxNewBankCustomer.grid(column = 1, row = 1)

    def saveNewBankCustomer():
        global global_New_Bank_Customer_Choosen
        bankAccountCustomerName =  txtboxNewBankCustomer.get()
        if (BankClass_ENUM.ARBEJDERNES_LANDSBANK == BankClass_ENUM(global_New_Bank_Customer_Choosen.get())):
            bankCustomerList.append(arbejdernesLandsbank_Class(name=bankAccountCustomerName))

        if (BankClass_ENUM.SPARNORD_BANK == BankClass_ENUM(global_New_Bank_Customer_Choosen.get())):
            bankCustomerList.append(sparNordBank_Class(name=bankAccountCustomerName))

        if (BankClass_ENUM.SPARNORD_BANK_FORDELSKUNDE == BankClass_ENUM(global_New_Bank_Customer_Choosen.get())):
            bankCustomerList.append(sparNordBankFordelKunde_Class(name=bankAccountCustomerName))

        updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen)
        txtboxNewBankCustomer.delete(0, END)


    def deleteBankCustomer():
        del bankCustomerList[global_Customer_Choosen_Index.get()]
        listCurrentBankCustomerTransactions.delete(0, END)
        updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen)
        global_Customer_Choosen_Index.set(-1)
        labelCurrentBankCustomerText.set("Ingen kunde valgt !!!")

    newBankCustomerButton = ttk.Button(tabBankOverview, text="Gem ny Bank Kunde",
                                       command = saveNewBankCustomer)
    newBankCustomerButton.grid(row = 2, column = 0, padx=8, pady=10)

    deleteCustomerButton = ttk.Button(tabBankOverview, text="Slet Bank Kunde",
                                       command = deleteBankCustomer)
    deleteCustomerButton.grid(row = 2, column = 1, padx=8, pady=10)

    labelBankCustomerText = StringVar()
    labelBankCustomerText.set("Oversigt over Bank Kunder i Alle Banker")

    labelBankCustomer = ttk.Label(tabBankOverview, textvariable=labelBankCustomerText)
    labelBankCustomer.grid(column=0, row=3, padx=8, pady=10, sticky="W")

    def ListBankCustomersSelect(evt):
        index = listBankCustomers.curselection()[0]
        value = listBankCustomers.get(index)
        global_Customer_Choosen_Index.set(index)
        labelCurrentBankCustomerText.set("Kunde med index %d er valgt" % (index))
        listCurrentBankCustomerTransactions.delete(0, END)
        bankCustomerTransactionsList = bankCustomerList[index].printBankAccountTransactionsGUI()
        for bankCustomerTransaction in bankCustomerTransactionsList:
            listCurrentBankCustomerTransactions.insert(END, bankCustomerTransaction)

        print('Du valgte item %d : "%s"' % (index, value))

    listBankCustomers = Listbox(tabBankOverview, width=80, selectmode="SINGLE",
                                name="listBankCustomers")
    listBankCustomers.grid(row=4, column=0, padx=8, pady=10)
    listBankCustomers.bind('<<ListboxSelect>>', ListBankCustomersSelect)

    closeButton1 = ttk.Button(tabBankOverview, text="Quit", command=closeWindow)
    closeButton1.grid(column=0, row=6, padx=8, pady=10, sticky="W")

    # Nu opretter vi kontroller til vores Tab : tabCustomerOverview

    labelCurrentBankCustomerText = StringVar()
    labelCurrentBankCustomerText.set("Ingen kunde valgt !!!")

    labelCurrentBankCustomer = ttk.Label(tabCustomerOverview, textvariable=labelCurrentBankCustomerText)
    labelCurrentBankCustomer.grid(column=0, row=0, padx=8, pady=10, sticky="W")

    listCurrentBankCustomerTransactions = Listbox(tabCustomerOverview, width=80, selectmode="SINGLE",
                                name="listCurrentBankCustomerTransactions")
    listCurrentBankCustomerTransactions.grid(row=1, column=0, padx=8, pady=10)

    def depositAmount():
        amount = float(txtboxBankCustomerTransactions.get())
        txtboxBankCustomerTransactions.delete(0, END)
        bankCustomerList[global_Customer_Choosen_Index.get()].deposit(amount)
        listCurrentBankCustomerTransactions.delete(0, END)
        bankCustomerTransactionsList = bankCustomerList[global_Customer_Choosen_Index.get()].printBankAccountTransactionsGUI()
        for bankCustomerTransaction in bankCustomerTransactionsList:
            listCurrentBankCustomerTransactions.insert(END, bankCustomerTransaction)
        updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen)

    def withdrawAmount():
        amount = float(txtboxBankCustomerTransactions.get())
        txtboxBankCustomerTransactions.delete(0, END)
        bankCustomerList[global_Customer_Choosen_Index.get()].withdraw(amount)
        listCurrentBankCustomerTransactions.delete(0, END)
        bankCustomerTransactionsList = bankCustomerList[global_Customer_Choosen_Index.get()].printBankAccountTransactionsGUI()
        for bankCustomerTransaction in bankCustomerTransactionsList:
            listCurrentBankCustomerTransactions.insert(END, bankCustomerTransaction)
        updateBankCustomersList(listBankCustomers, bankCustomerList, global_Bank_Choosen)

    bankCustomerDepositButton = ttk.Button(tabCustomerOverview, text="Indsæt beløb på konto",
                                       command=depositAmount)
    bankCustomerDepositButton.grid(row=2, column=0, padx=8, pady=10)

    bankCustomerWithdrawButton = ttk.Button(tabCustomerOverview, text="Hæv beløb på konto",
                                           command=withdrawAmount)
    bankCustomerWithdrawButton.grid(row=2, column=1, padx=8, pady=10)

    labelBankCustomerTransactions = ttk.Label(tabCustomerOverview, text="Indtast ønsket beløb : ")
    labelBankCustomerTransactions.grid(column=0, row=3, padx=8, pady=10, sticky="W")

    # Her defineres en tekstboks, som vi kan skrive tekst ind i.
    txtboxBankCustomerTransactions = Entry(tabCustomerOverview, width=50)
    txtboxBankCustomerTransactions.grid(column=1, row=3)

    closeButton2 = ttk.Button(tabCustomerOverview, text="Quit", command=closeWindow)
    closeButton2.grid(column=0, row=5, padx=8, pady=10, sticky="W")

    root.mainloop()