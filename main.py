import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem

class ChorobyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich pacjentów
        self.cur.execute('SELECT * FROM choroba')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Choroby')

class PokojeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich pacjentów
        self.cur.execute('SELECT * FROM pokoje')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Pokoje')

class PacjenciWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich pacjentów
        self.cur.execute('SELECT * FROM pacjenci')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Pacjenci')

class LekarzeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich lekarzy
        self.cur.execute('SELECT * FROM lekarz')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Lekarze')

class LekiWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich lekarzy
        self.cur.execute('SELECT * FROM leki')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Leki')

class LekiMagazynWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich lekarzy
        self.cur.execute('SELECT * FROM leki_magazyn')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Leki w magazynie')

class ZabiegoperacjaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich lekarzy
        self.cur.execute('SELECT * FROM zabiegoperacja')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Zabieg/Operacja')

class ReceptyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich lekarzy
        self.cur.execute('SELECT * FROM recepty')
        rows = self.cur.fetchall()

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(9)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Recepta')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tworzenie przycisków
        self.btn_pacjent = QPushButton('PACJENT')
        self.btn_lekarz = QPushButton('LEKARZ')
        self.btn_pokoj = QPushButton('POKOJE')
        self.btn_choroby = QPushButton('CHOROBY')
        self.btn_leki = QPushButton('LEKI')
        self.btn_leki_magazyn = QPushButton('LEKI W MAGAZYNIE')
        self.btn_zabiegoperacja = QPushButton('ZABIEG/OPERACJA')
        self.btn_recepty = QPushButton('RECEPTY')

        # Dodawanie przycisków do layoutu
        layout = QVBoxLayout()
        layout.addWidget(self.btn_pacjent)
        layout.addWidget(self.btn_lekarz)
        layout.addWidget(self.btn_pokoj)
        layout.addWidget(self.btn_choroby)
        layout.addWidget(self.btn_leki)
        layout.addWidget(self.btn_leki_magazyn)
        layout.addWidget(self.btn_zabiegoperacja)
        layout.addWidget(self.btn_recepty)

        # Tworzenie okna i ustawienie layoutu
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Przypisanie akcji
        self.btn_pacjent.clicked.connect(self.show_pacjenci)
        self.btn_lekarz.clicked.connect(self.show_lekarze)
        self.btn_pokoj.clicked.connect(self.show_pokoje)
        self.btn_choroby.clicked.connect(self.show_choroby)
        self.btn_leki.clicked.connect(self.show_leki)
        self.btn_leki_magazyn.clicked.connect(self.show_leki_magazyn)
        self.btn_zabiegoperacja.clicked.connect(self.show_zabiegoperacja)
        self.btn_recepty.clicked.connect(self.show_recepty)

    def show_pacjenci(self):
        # Tworzenie i wyświetlenie okna z danymi pacjentów
        pacjenci_window = PacjenciWindow(self)
        pacjenci_window.show()

    def show_lekarze(self):
        # Tworzenie i wyświetlenie okna z danymi lekarzy
        lekarze_window = LekarzeWindow(self)
        lekarze_window.show()

    def show_pokoje(self):
        # Tworzenie i wyświetlenie okna z danymi pokojami
        pokoj_window = PokojeWindow(self)
        pokoj_window.show()

    def show_choroby(self):
        # Tworzenie i wyświetlenie okna z danymi pokojami
        choroba_window = ChorobyWindow(self)
        choroba_window.show()

    def show_leki(self):
        # Tworzenie i wyświetlenie okna z danymi pokojami
        leki_window = LekiWindow(self)
        leki_window.show()

    def show_leki_magazyn(self):
        # Tworzenie i wyświetlenie okna z danymi pokojami
        lekiM_window = LekiMagazynWindow(self)
        lekiM_window.show()

    def show_zabiegoperacja(self):
        # Tworzenie i wyświetlenie okna z danymi pokojami
        zabiegoperacja_window = ZabiegoperacjaWindow(self)
        zabiegoperacja_window.show()

    def show_recepty(self):
        # Tworzenie i wyświetlenie okna z danymi pokojami
        recepty_window = ReceptyWindow(self)
        recepty_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())