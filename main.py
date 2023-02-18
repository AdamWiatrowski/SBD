import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QTableWidgetItem, QLineEdit, QDialog, QFormLayout, QDialogButtonBox, QTextEdit, QToolBar, QAction


class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ekran logowania')
        self.setGeometry(100, 100, 300, 150)

        # Tworzenie interfejsu użytkownika
        self.username_label = QLabel('Nazwa użytkownika:', self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('Hasło:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Zaloguj', self)

        # Ustawianie layoutu
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Podłączanie akcji do przycisku logowania
        self.login_button.clicked.connect(self.login)

    def login(self):
        # Sprawdzanie poprawności danych logowania (tutaj zaimplementowane sztywno)
        if self.username_input.text() == 'admin' and self.password_input.text() == 'admin123':
            self.close()  # Zamykanie ekranu logowania
            self.menu_screen = MainWindow()
            self.menu_screen.show()  # Pokazywanie ekranu z menu
        else:
            self.password_input.setText('')  # Czyszczenie pola hasła

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

class ChorobyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkich pacjentów
        self.cur.execute('SELECT * FROM choroba')
        rows = self.cur.fetchall()

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
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

        # Zapytanie SQL o wszystkie pokoje
        self.cur.execute('SELECT * FROM pokoje')
        rows = self.cur.fetchall()

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
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

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
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

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
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

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
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

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
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

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Zabieg/Operacja')

class AddReceptaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utworzenie etykiet i pól tekstowych dla danych nowej recepty
        # LEKARZ
        lekarz_label = QLabel('Lekarz wystawiajacy:')
        self.lekarz_input = QLineEdit()

        pacjent_label = QLabel('Pacjent:')
        self.pacjent_input = QLineEdit()

        nazwa_label = QLabel('Nazwa:')
        self.nazwa_input = QLineEdit()

        data_label = QLabel('Data wydania:')
        self.data_input = QLineEdit()

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QVBoxLayout()

        layout.addWidget(lekarz_label)
        layout.addWidget(self.lekarz_input)

        layout.addWidget(pacjent_label)
        layout.addWidget(self.pacjent_input)

        layout.addWidget(nazwa_label)
        layout.addWidget(self.nazwa_input)

        layout.addWidget(data_label)
        layout.addWidget(self.data_input)

        layout.addWidget(dodaj_button)
        layout.addWidget(anuluj_button)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj nową receptę')

    def get_data(self):
        return self.lekarz_input.text(), self.pacjent_input.text(), self.nazwa_input.text(), self.data_input.text()

class ReceptyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkie recepty
        self.cur.execute('SELECT * FROM recepty')
        rows = self.cur.fetchall()

        # Uzyskanie etykiet kolumn tabeli z bazy danych
        labels = [description[0] for description in self.cur.description]

        # Tworzenie tabeli i wypełnienie jej danymi
        table = QTableWidget()
        table.setColumnCount(len(labels))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(labels)
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

        # Ustawienie tabeli jako centralnego widżetu okna
        self.setCentralWidget(table)

        # Ustawienie tytułu okna
        self.setWindowTitle('Recepta')

        # Tworzenie paska narzędzi z przyciskiem dodawania nowej recepty
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_recepta_action = QAction('Dodaj nową receptę', self)
        add_recepta_action.triggered.connect(self.show_add_recepta_dialog)

        toolbar.addAction(add_recepta_action)

    def show_add_recepta_dialog(self):
        dialog = AddReceptaDialog(self)
        if dialog.exec_():
            lekarz, pacjent, nazwa, data_wydania = dialog.get_data()

            # Dodaj nową receptę do bazy danych
            self.cur.execute('INSERT INTO recepty (lekarz_wystawiajacy, pacjent, lek, data_wystawienia) VALUES (?, ?, ?, ?)', (int(lekarz), int(pacjent), nazwa, data_wydania))
            self.conn.commit()
            print("hejka")
            # Odśwież widok tabeli
            self.refresh_table()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie recepty
        self.cur.execute('SELECT * FROM recepty')
        rows = self.cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())




