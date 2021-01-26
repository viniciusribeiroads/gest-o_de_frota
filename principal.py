from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from datetime import datetime

banco = sqlite3.connect('data_transportes.db')
cursor = banco.cursor()


def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == "transportes" and senha == "2021" :
        primeira_tela.close()
        segunda_tela.show()
        segunda_tela.pushButton_2.clicked.connect(lanc_comb)
        segunda_tela.pushButton_4.clicked.connect(lan_oleo)
        segunda_tela.pushButton_5.clicked.connect(listar_abast)
        segunda_tela.pushButton_3.clicked.connect(listar_oleo)
        segunda_tela.pushButton.clicked.connect(logout)
    else :
        primeira_tela.label_4.setText("Dados de login incorretos!")
    

def logout():
    segunda_tela.close()
    primeira_tela.show()

def lanc_comb():
    data = segunda_tela.dateEdit.date().toPyDate()
    data = data.strftime('%d/%m/%Y')
    placa = segunda_tela.lineEdit.text()
    km = segunda_tela.lineEdit_2.text()
    litros = segunda_tela.lineEdit_3.text()
    motorista = segunda_tela.lineEdit_4.text()
    setor = segunda_tela.comboBox.currentText()
    try:
        cursor.execute("INSERT INTO abastecimentos VALUES('"+str(data)+"','"+str(placa)+"', '"+str(km)+"', '"+str(litros)+"','"+motorista+"', '"+setor+"')")
        banco.commit() 
        segunda_tela.lineEdit.setText("")
        segunda_tela.lineEdit_2.setText("")
        segunda_tela.lineEdit_3.setText("")
        segunda_tela.lineEdit_4.setText("")
    except:
        QMessageBox.about(segunda_tela, 'ERRO', 'Erro ao inserir dados, favor verificar.')
    
def lan_oleo():
    data = segunda_tela.dateEdit_2.date().toPyDate()
    data = data.strftime('%d/%m/%Y')
    placa = segunda_tela.lineEdit_8.text()
    km = segunda_tela.lineEdit_7.text()
    responsavel = segunda_tela.lineEdit_6.text()
    try:
        cursor.execute("INSERT INTO troca_oleo VALUES('"+str(data)+"', '"+str(placa)+"', '"+str(km)+"', '"+str(responsavel)+"')")
        banco.commit()
        segunda_tela.lineEdit_8.setText("")
        segunda_tela.lineEdit_7.setText("")
        segunda_tela.lineEdit_6.setText("")
    except:
        QMessageBox.about(segunda_tela, 'ERRO', 'Erro ao inserir dados, favor verificar.')


def listar_abast():
    segunda_tela.close()
    listagem_abast.show()
    listagem_abast.pushButton.clicked.connect(load_data)
    listagem_abast.pushButton_2.clicked.connect(filtrar_data)

def filtrar_data():
    dataInicial =  listagem_abast.dateEdit.date().toPyDate()
    dataFinal = listagem_abast.dateEdit_2.date().toPyDate()
    banco = sqlite3.connect('data_transportes.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM abastecimentos WHERE data BETWEEN '01/01/2021' AND '01/03/2021'")
    dados_lidos = cursor.fetchall()
    listagem_abast.tableWidget.setRowCount(len(dados_lidos))
    listagem_abast.tableWidget.setColumnCount(6)
    banco.close()

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            listagem_abast.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def load_data():
    banco = sqlite3.connect('data_transportes.db')
    cursor = banco.cursor()
    cursor.execute("SELECT *  FROM abastecimentos")
    dados_lidos = cursor.fetchall()
    listagem_abast.tableWidget.setRowCount(len(dados_lidos))
    listagem_abast.tableWidget.setColumnCount(6)
    banco.close()

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            listagem_abast.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



def listar_oleo():
    segunda_tela.close()
    listagem_abast.show()
    listagem_abast.pushButton.clicked.connect(troca_oleo)


def troca_oleo():
    banco = sqlite3.connect('data_transportes.db')
    cursor = banco.cursor()
    cursor.execute("SELECT *  FROM troca_oleo")
    dados_lidos = cursor.fetchall()
    listagem_abast.tableWidget.setRowCount(len(dados_lidos))
    listagem_abast.tableWidget.setColumnCount(4)
    banco.close()

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            listagem_abast.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("telalogin.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
listagem_abast = uic.loadUi('listagem.ui')
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
segunda_tela.comboBox.addItems(["Obras","Saude","Educacao"])
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

primeira_tela.show()
app.exec()


""" 

data = str(input('Data:'))
placa = str(input('Placa do veiculo: '))
km = float(input('KM: '))
litros = float(input('Litragem: '))
motorista = str(input('Motorista: '))
 """