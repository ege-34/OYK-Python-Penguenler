##QT5 ile Rasathaneden anlık verileri çekip tablo oluşturduk..##
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget,QTableWidgetItem, QVBoxLayout
import sys, requests
from PyQt5 import QtCore, QtGui, QtWidgets



class Window(QWidget):
    def __init__ (self):
        super().__init__()

        self.title = "Deprem Takip Tablosu"
        self.top = 100
        self.left = 100
        self.width = 860
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.windowIcon()
        

        earthquake_data = get_deprem_data()
        self.tablo_olustur(len(earthquake_data))
        self.insert_data(earthquake_data)
        self.colorize_siddet()
        
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
       
        self.show()
    
    def tablo_olustur(self, row_count):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(9)

        self.tableWidget.setItem(0,0, QTableWidgetItem("ID"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Tarih"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Saat"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Enlem(N)"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Boylam(E)"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Derinlik(Km)"))
        self.tableWidget.setItem(0,6 ,QTableWidgetItem("Siddet"))
        self.tableWidget.setItem (0,7, QTableWidgetItem("Yer"))
        self.tableWidget.setItem(0,8, QTableWidgetItem("Çözüm Niteliği"))


    def insert_data(self, data):
        for row_number, row_data in enumerate(data):    
            self.tableWidget.setItem(row_number+1, 0, QTableWidgetItem(str(row_data['id'])))
            self.tableWidget.setItem(row_number+1, 1, QTableWidgetItem(row_data['tarih']))                
            self.tableWidget.setItem(row_number+1, 2, QTableWidgetItem(row_data['saat']))                
            self.tableWidget.setItem(row_number+1, 3, QTableWidgetItem(row_data["enlem"]))
            self.tableWidget.setItem(row_number+1, 4, QTableWidgetItem(row_data["boylam"]))
            self.tableWidget.setItem(row_number+1, 5, QTableWidgetItem(row_data["derinlik"]))    
            self.tableWidget.setItem(row_number+1, 6, QTableWidgetItem(row_data["siddet"]))
            self.tableWidget.setItem(row_number+1, 7, QTableWidgetItem(row_data["yer"]))
            self.tableWidget.setItem(row_number+1, 8, QTableWidgetItem(row_data["tip"]))

    def colorize_siddet(self):
        # self.tableWidget.item(1,6).setBackground(QtGui.QColor(0xFF0000))
        for row_count in range(1, self.tableWidget.rowCount()):
                    row_item = self.tableWidget.item(row_count,6)
                    cell_value = row_item.text()
                    if float(cell_value) >= 2:
                        row_item.setBackground(QtGui.QColor(0xFF0000))



                        
def get_deprem_data():
    req = requests.get('https://deprem.odabas.xyz/api/data.php')
    return req.json()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())           


                    

            
        
            
        

