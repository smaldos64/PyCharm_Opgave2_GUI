import abc # abc står her for Abstract Base Class

class bankAccount_Transactions():
    def __init__(self):
        self._balance = 0
        self._transactionAmount = 0

class bankAccount_Class(object):
    __metaclass__ = abc.ABCMeta
    # I Python er en funktion i en klasse med navnet __init en constructor
    def __init__(self, name, amount = 2000, printTransactions = False):
    # Da variablen __balance har 2 __ i starten af navnet, er det en privat
    # variabel for et objekt af klassen bankAccount_Class
        self._balance = amount
        self._name = name
        # Herunder laves der en liste. Denne liste skal indeholde alle vores
        # bank transaktioner for den pågælde kunde => det pågældende objekt.
        self._transactionList = []
        self._printTransactions = printTransactions

    @abc.abstractmethod
    # Alle klasser, der arver fra klassen bankAccount_Class, SKAL implementere
    # metoden deposit, da denne er erklæret som en abstract metode her i
    # klassen bankAccount_Class !!!
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount;
            self.updateBankAccountTransActions(self._balance, -1 * amount)
        else:
            print("Overtræk er ikke tilladt i min bank !!!")

    def updateBankAccountTransActions(self, balance, amount):
        try:
            bankAccount_Transactions_Object = bankAccount_Transactions()
            bankAccount_Transactions_Object._balance = balance
            bankAccount_Transactions_Object._transactionAmount = amount
            self._transactionList.append(bankAccount_Transactions_Object)
        except:
            print("Fejl her")

    # Her overrides metoden print for objekter af klassen bankAccount_Class
    # Altså Method Override !!!
    def __str__(self):
        return ("Indestående på %s konto er : %s kr" % (self._name, str("%.2f" % self._balance)))

    def __str__(self, bankName=""):
        if ("" == bankName):
            self.__str__()
        else:
            return ("Indestående på %s konto er : %s kr. %s er kunde i %s." % (self._name, str("%.2f" % self._balance), self._name, bankName))

    def printBankAccountTransactions(self):
        returnString = "\n"
        returnString += "Transaktioner for %s, der er kunde i %s" % (self._name, self._bankName)
        returnString += "\n"
        returnString += "Kontobevægelse Saldo "
        returnString += "\n"
        returnString += "--------------------"
        returnString += "\n"
        for bankTransAction in self._transactionList:
            returnString += str("%.2f" % bankTransAction._transactionAmount) + " " + str("%.2f" % bankTransAction._balance)
            returnString += "\n"
        returnString += "\n"

        print("")
        print("Transaktioner for %s, der er kunde i %s" % (self._name, self._bankName))

        # Modsat i f.eks. C# kan man få fat i en statisk variabel her _bankName, der
        # er defineret på en klasse ved brug af et objekt på klassen !!!
        print(" ")

        print("Kontobevægelse Saldo ")
        print("--------------------")
        for bankTransAction in self._transactionList:
            print(str("%.2f" % bankTransAction._transactionAmount), str("%.2f" % bankTransAction._balance))
        print("")

        return (returnString)

    def setPrintTransactions(self, printTransactions):
        self._printTransactions = printTransactions

    def printToGuiComponents(self):
        returnString = self._name + " med kontobeløb " + str("%.2f" % self._balance) + " er kunde i " + self.__class__.__name__
        return (returnString)

class arbejdernesLandsbank_Class(bankAccount_Class):
    # variablen BankName er defineret udenfor en metode (udenfor klassens
    # constructor (__init__)), så det er en statisk variabel for klassen,
    # som således er gældende for alle objekter af klassen
    # arbejdernesLandsbank_Class
    _bankName = "Arbejdernes Landsbank"

    def __init__(self, name, amount=500):
        # Når man bruger udtrykket : super() kalder man en metode i den klasse
        # man arver fra med samme navn. I tilfældet her kalder vi konstruktoren =>
        # __init__ i vores bankAccount_Class.
        super().__init__(name, amount)
        self.deposit(200)

    def deposit(self, amount):
        self._balance += amount
        self.updateBankAccountTransActions(self._balance, amount)

    def annualInterest(self):
        self._balance *= 1.1

    def __str__(self):
        printString = super().__str__(arbejdernesLandsbank_Class._bankName)
        if (True == self._printTransactions):
            printString += self.printBankAccountTransactions()
        return (printString)
        #return (super().__str__() + " . %s er kunde i %s." % (self._name, arbejdernesLandsbank_Class._bankName))
        #return (super().__str__(arbejdernesLandsbank_Class._bankName))

class sparNordBank_Class(bankAccount_Class):
    _bankName = "SparNord Bank"

    def __init__(self, name, amount=1500):
        super().__init__(name, amount)
        self.deposit(500)

    def deposit(self, amount):
        self._balance += amount + 10
        self.updateBankAccountTransActions(self._balance, amount + 10)

    def __str__(self):
        #return (super().__str__() + " . %s er kunde i %s." % (self._name, sparNordBank_Class._bankName))
        return (super().__str__(sparNordBank_Class._bankName))

class sparNordBankFordelKunde_Class(sparNordBank_Class):
    def __init__(self, name, amount=1500):
        super().__init__(name, amount)
        self.deposit(1000)

    def deposit(self, amount, interest = 0):
        _balanceBefore = self._balance
        self._balance *= (1 + interest / 100)
        self._balance += amount + 50
        self.updateBankAccountTransActions(self._balance, self._balance - _balanceBefore)

    # I Python kan man ikke som i f.eks. C# lave method Overload ved at have
    # forskellige metoder med samme navn men forskellige antal parametre.
    # Derfor må man bruge optionale parametre som vist i metoden Deposit herover.
    """
    def deposit(self, amount, interest):
        self._balance *= (1 + interest/100)
        self.deposit(amount)
    """

    def __str__(self):
        printString = super().__str__() + " Og du er fordels kunde !!!"
        if (True == self._printTransactions):
            printString += self.printBankAccountTransactions()
        return (printString)