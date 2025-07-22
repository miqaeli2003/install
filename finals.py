#pirveli

import sqlite3
#listis sia
shopping_cart = [["pear", 1], ["orange", 1], ["apple", 2], ["tomatoes", 2], ["yoghurt", 3]]

reversed_cart = []
for i in range(len(shopping_cart) - 1, -1, -1):
    reversed_cart.append(shopping_cart[i])

conn = sqlite3.connect("shopping.db")
cursor = conn.cursor()

# aq vqmni xelit tablicebs database is tvis
cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        quantity INTEGER
    )
""")

cursor.execute("DELETE FROM purchases")

# monacemebis chasma reversirebis ciklisgan
for item in reversed_cart:
    cursor.execute("INSERT INTO purchases (item_name, quantity) VALUES (?, ?)", (item[0], item[1]))

conn.commit()
conn.close()

print("reversirebuli listi damatebulia database shi:")
for item in reversed_cart:
    print(item)

#meore

from pymongo import MongoClient

#mongodb
client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant"]
menu_collection = db["menu"]

menu = {
    "soda": 1.70,
    "fries": 2.99,
    "burger": 1.99,
    "shake": 3.5,
    "cookie": 2.4,
    "chicken strips": 3.9
}

menu_collection.delete_many({})  
for item, price in menu.items():
    menu_collection.insert_one({"item": item, "price": price})


def make_order():
    order = []

    menu_items = {doc["item"]: doc["price"] for doc in menu_collection.find()}

    print("Available menu items:")
    for item in menu_items:
        print("-", item)

    while True:
        item_name = input("What can I get for you? ").strip().lower()

        if item_name not in menu_items:
            print("I'm sorry, we don't serve that. Try again.")
            continue

        try:
            quantity = int(input(f"How many {item_name}s would you like? "))
            if quantity <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        order.append([item_name, quantity])

        more = input("Would you like to add more items? (yes/no): ").strip().lower()
        if more == "no":
            break

    print("\nYour order:")
    for item in order:
        print(f"{item[0].capitalize()} x {item[1]}")

    return order


make_order()


#mesame

import numpy as np
array1 = np.random.randint(1, 101, size=50)
array2 = np.random.randint(1, 101, size=50)


sum_array = array1 + array2
diff_array = array1 - array2
prod_array = array1 * array2
div_array = array1 / array2

combined = np.concatenate((array1, array2))
combined = combined.reshape((1, 1, 1, 1, 100))
combined = combined.reshape((1,1,1,1,1,1,1,1,2,50))

print("jami:\n", sum_array)
print("sxvaoba:\n", diff_array)
print("namravli:\n", prod_array)
print("gayofa:\n", div_array)
print("grdaqmnili masivi (10D) shi:", combined.shape)
print(combined.flatten())


#desing 
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 912)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 480, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditproduct = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditproduct.setGeometry(QtCore.QRect(280, 190, 621, 131))
        self.lineEditproduct.setObjectName("lineEditproduct")
        self.lineEditprice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditprice.setGeometry(QtCore.QRect(280, 470, 621, 131))
        self.lineEditprice.setObjectName("lineEditprice")
        self.pushButtonPriceChange = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPriceChange.setGeometry(QtCore.QRect(170, 690, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonPriceChange.setFont(font)
        self.pushButtonPriceChange.setObjectName("pushButtonPriceChange")
        self.pushButtonPriceDecrease = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPriceDecrease.setGeometry(QtCore.QRect(690, 690, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonPriceDecrease.setFont(font)
        self.pushButtonPriceDecrease.setObjectName("pushButtonPriceDecrease")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PRODUCT"))
        self.label_2.setText(_translate("MainWindow", "PRICE"))
        self.pushButtonPriceChange.setText(_translate("MainWindow", "change the price"))
        self.pushButtonPriceDecrease.setText(_translate("MainWindow", "Decrease the price"))