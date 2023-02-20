import sys
import sqlite3
import socket
from datetime import datetime

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QTableWidgetItem, QLineEdit, QDialog, QFormLayout, QDialogButtonBox, QTextEdit, QToolBar, QAction, \
    QDateEdit, QComboBox, QMessageBox

username = "admin"

def check_config():
    with open('config.txt','r+') as f:
        for line in f:
            if line.split('=')[0] == "blocked":
                return False if line.split('=')[1] == "false\n" else True

def change_blocked():
    with open('config.txt', 'r') as f:
        lines = f.readlines()

    with open('config.txt', 'w') as f:
        for line in lines:
            if 'blocked' in line:
                value = line.split('=')[1].strip()
                if value == 'true':
                    line = line.replace('true', 'false')
                else:
                    line = line.replace('false', 'true')
            f.write(line)
    f.close()

# Funkcja tworzaca logi programu:
def log(x):
    f = open("log.txt", "a")

    now = datetime.now()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    log = str(now)+" | "+username+" | "+s.getsockname()[0]+" | ("+x+")"

    f.write(log+"\n")

    s.close()
    f.close()

# LOGIN SCREEN:
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
        # Sprawdzanie poprawności danych logowania
        # self.username_input.text() == 'admin' and
        if self.password_input.text() == 'haslo':
            # Zdefiniowanie username

            global username
            username = self.username_input.text()

            self.close()  # Zamykanie ekranu logowania
            self.menu_screen = MainWindow()
            self.menu_screen.show()  # Pokazywanie ekranu z menu
        else:
            self.password_input.setText('')  # Czyszczenie pola hasła

# MAIN MENU:
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
        self.btn_wypis = QPushButton('WYPIS')


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
        layout.addWidget(self.btn_wypis)

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
        self.btn_wypis.clicked.connect(self.show_wypis)

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

    def show_wypis(self):
        # Tworzenie i wyświetlenie okna z danymi pokojami
        wypis_window = WypisWindow(self)
        wypis_window.show()

# CHOROBY:
class ChorobyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(900)
        self.setFixedHeight(300)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
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

# POKOJE:
class PokojeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(400)
        self.setFixedHeight(300)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
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

# PACJENCI:
class AddPacjentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utworzenie etykiet i pól tekstowych dla danych nowego pacjenta
        imie_label = QLabel('Imię:')
        self.imie_input = QLineEdit()

        nazwisko_label = QLabel('Nazwisko:')
        self.nazwisko_input = QLineEdit()

        wiek_label = QLabel('Wiek:')
        self.wiek_input = QLineEdit()

        plec_label = QLabel('Płeć:')
        self.plec_input = QComboBox()
        self.plec_input.addItem('K')
        self.plec_input.addItem('M')

        waga_label = QLabel('Waga:')
        self.waga_input = QLineEdit()

        wzrost_label = QLabel('Wzrost:')
        self.wzrost_input = QLineEdit()

        data_label = QLabel('Data przyjęcia:')
        self.data_input = QDateEdit(calendarPopup=True)
        self.data_input.setDate(QDate.currentDate())
        self.data_input.setDisplayFormat('yyyy-MM-dd')

        pokoj_label = QLabel('Pokój:')
        self.pokoj_input = QComboBox()
        self.fill_pokoje()

        # tu moze byc wybor nadal;
        choroba_label = QLabel('Choroba:')
        self.choroba_input = QLineEdit()

        lekarz_label = QLabel('Lekarz prowadzący:')
        self.lekarz_input = QComboBox()
        self.fill_lekarze()

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QFormLayout()

        layout.addRow(imie_label, self.imie_input)
        layout.addRow(nazwisko_label, self.nazwisko_input)
        layout.addRow(wiek_label, self.wiek_input)
        layout.addRow(plec_label, self.plec_input)
        layout.addRow(waga_label, self.waga_input)
        layout.addRow(wzrost_label, self.wzrost_input)
        layout.addRow(data_label, self.data_input)
        layout.addRow(pokoj_label, self.pokoj_input)
        layout.addRow(choroba_label, self.choroba_input)
        layout.addRow(lekarz_label, self.lekarz_input)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(dodaj_button)
        buttons_layout.addWidget(anuluj_button)

        layout.addRow(buttons_layout)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj nowego pacjenta')

    def fill_pokoje(self):
        conn = sqlite3.connect('szpital.db')
        conn.set_trace_callback(log)
        cur = conn.cursor()

        # Zapytanie SQL o wszystkie pokoje, gdzie są wolne łóżka
        cur.execute('SELECT numer_pokoju FROM pokoje WHERE liczba_wolnych_lozek > 0')
        pokoje = [str(pokoj[0]) for pokoj in cur.fetchall()]

        # Ustawienie elementów QComboBox
        self.pokoj_input.addItems(pokoje)

    def fill_lekarze(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        lekarze = self.cur.execute('SELECT id_l, imie, nazwisko FROM lekarz').fetchall()

        lekarze = [f"{lekarz[0]} - {lekarz[1]} {lekarz[2]}" for lekarz in lekarze]

        self.lekarz_input.addItems(lekarze)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def get_data(self):
        return self.imie_input.text(), \
               self.nazwisko_input.text(), \
               self.wiek_input.text(), \
               self.plec_input.currentText(), \
               self.waga_input.text(), \
               self.wzrost_input.text(), \
               self.data_input.text(), \
               self.pokoj_input.currentText(), \
               self.choroba_input.text(), \
               self.lekarz_input.currentText().split(' - ')[0]

class PacjenciWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(1200)
        self.setFixedHeight(400)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
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

        # Tworzenie paska narzędzi z przyciskiem dodawania nowego pacjenta
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_pacjent_action = QAction('Dodaj nowego pacjenta', self)
        add_pacjent_action.triggered.connect(self.show_add_pacjent_dialog)

        toolbar.addAction(add_pacjent_action)

    def show_add_pacjent_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()

            dialog = AddPacjentDialog(self)
            if dialog.exec_():
                imie, nazwisko, wiek, plec, waga, wzrost, data_przyjecia, pokoj, choroba, lekarz_prowadzacy = dialog.get_data()
                # Dodaj nowego pacjenta do bazy danych
                try:
                    self.cur.execute(
                        'INSERT INTO pacjenci (imie, nazwisko, wiek, plec, waga, wzrost, data_przyjecia, pokoj, choroba, lekarz_prowadzacy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                        (imie, nazwisko, int(wiek), plec, int(waga), int(wzrost), data_przyjecia, int(pokoj), choroba,
                         int(lekarz_prowadzacy)))
                except:
                    error_box = QMessageBox()
                    error_box.setIcon(QMessageBox.Warning)
                    error_box.setWindowTitle("Błąd")
                    error_box.setText("Niektóre pola są bledne! Wypełnij poprawnie pola.")
                    error_box.exec_()
                else:
                    self.conn.commit()
                    # Zmniejsz liczbę wolnych łóżek w wybranym pokoju o 1
                    self.cur.execute(
                        'UPDATE pokoje SET liczba_wolnych_lozek = liczba_wolnych_lozek - 1 WHERE numer_pokoju = ?',
                        (pokoj,))
                    self.conn.commit()
                    # Odśwież widok tabeli
                    self.refresh_table()
            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkich pacjentów
        self.cur.execute('SELECT * FROM pacjenci')
        rows = self.cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

    def show_error(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Warning)
        error_box.setWindowTitle("Błąd")
        error_box.setText("Baza aktualnie edytowana. Poczekaj...")
        error_box.exec_()

# LEKARZE:
class LekarzeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(900)
        self.setFixedHeight(400)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
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

# LEKI:
class LekiWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(800)
        self.setFixedHeight(500)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
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

# LEKI W MAGAZYNIE:
class LekiMagazynWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(300)
        self.setFixedHeight(500)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
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

# ZABIEG/OPERACJA:
class AddZabiegoperacjaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utworzenie etykiet i pól wyboru dla danych nowej zabiegu/operacji
        # PACJENT
        pacjent_label = QLabel('Pacjent:')
        self.pacjent_combo = QComboBox(self)
        self.fill_pacjenci()

        # LEKARZ
        lekarz_label = QLabel('Lekarz:')
        self.lekarz_combo = QComboBox(self)
        self.fill_lekarz()

        # INTEGER TO CHECK;
        sala_label = QLabel('Sala:')
        self.sala_edit = QLineEdit()

        rodzaj_label = QLabel('Rodzaj:')
        self.rodzaj_combo = QComboBox(self)
        self.rodzaj_combo.addItems(['planowany', 'nagły', 'pilny'])

        data_label = QLabel('Data:')
        self.data_edit = QDateEdit(calendarPopup=True)
        self.data_edit.setDate(QDate.currentDate())
        self.data_edit.setDisplayFormat('yyyy-MM-dd')

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QVBoxLayout()

        layout.addWidget(pacjent_label)
        layout.addWidget(self.pacjent_combo)

        layout.addWidget(lekarz_label)
        layout.addWidget(self.lekarz_combo)

        layout.addWidget(rodzaj_label)
        layout.addWidget(self.rodzaj_combo)

        layout.addWidget(sala_label)
        layout.addWidget(self.sala_edit)

        layout.addWidget(data_label)
        layout.addWidget(self.data_edit)

        layout.addWidget(dodaj_button)
        layout.addWidget(anuluj_button)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj nowy zabieg/operację')

    def fill_pacjenci(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        pacjenci = self.cur.execute('SELECT id_p, imie, nazwisko FROM pacjenci').fetchall()

        pacjenci = [f"{pacjent[0]} - {pacjent[1]} {pacjent[2]}" for pacjent in pacjenci]

        self.pacjent_combo.addItems(pacjenci)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def fill_lekarz(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        lekarze = self.cur.execute('SELECT id_l, imie, nazwisko FROM lekarz').fetchall()

        lekarze = [f"{lekarz[0]} - {lekarz[1]} {lekarz[2]}" for lekarz in lekarze]

        self.lekarz_combo.addItems(lekarze)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def get_data(self):
        # Pobranie wybranych danych z pól wyboru i pól edycyjnych
        pacjent = self.pacjent_combo.currentText().split(':')[0]
        lekarz = self.pacjent_combo.currentText().split(':')[0]
        sala = self.sala_edit.text()
        rodzaj = self.rodzaj_combo.currentText()
        data = self.data_edit.date().toString('yyyy-MM-dd')
        return data, lekarz[0], sala, pacjent[0], rodzaj

class ZabiegoperacjaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(700)
        self.setFixedHeight(200)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkie zabiegi/operacje
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

        # Tworzenie paska narzędzi z przyciskiem dodawania nowego zabiegu/operacji
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_zabieg_action = QAction('Dodaj nowy zabieg/operację', self)
        add_zabieg_action.triggered.connect(self.show_add_zabieg_dialog)

        toolbar.addAction(add_zabieg_action)

    def show_add_zabieg_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddZabiegoperacjaDialog(self)
            if dialog.exec_():
                data_wykonania, lekarz, sala, pacjent, rodzaj = dialog.get_data()

                try:
                    # Dodaj nowy zabieg/operację do bazy danych
                    self.cur.execute('INSERT INTO zabiegoperacja (data_wykonania, lekarz, sala, pacjent, rodzaj) VALUES (?, ?, ?, ?, ?)', (data_wykonania, int(lekarz), int(sala), int(pacjent), rodzaj))
                except:
                    error_box = QMessageBox()
                    error_box.setIcon(QMessageBox.Warning)
                    error_box.setWindowTitle("Błąd")
                    if(len(sala) > 0):
                        error_box.setText("Sala musi byc liczba!")
                    else:
                        error_box.setText("Niektóre pola są puste! Wypełnij wszystkie pola.")
                    error_box.exec_()
                else:
                    self.conn.commit()
                    # Odśwież widok tabeli
                    self.refresh_table()
            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute('SELECT * FROM zabiegoperacja')
        rows = self.cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

    def show_error(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Warning)
        error_box.setWindowTitle("Błąd")
        error_box.setText("Baza aktualnie edytowana. Poczekaj...")
        error_box.exec_()

# RECEPTA:
class AddReceptaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utworzenie etykiet i pól wyboru dla danych nowej recepty
        # LEKARZ
        lekarz_label = QLabel('Lekarz wystawiający:')
        self.lekarz_combo = QComboBox(self)
        self.fill_lekarze()

        pacjent_label = QLabel('Pacjent:')
        self.pacjent_combo = QComboBox(self)
        self.fill_pacjenci()

        nazwa_label = QLabel('Nazwa:')
        self.nazwa_combo = QComboBox(self)
        self.fill_leki()

        data_label = QLabel('Data wydania:')
        self.data_edit = QDateEdit(calendarPopup=True)
        self.data_edit.setDate(QDate.currentDate())
        self.data_edit.setDisplayFormat('yyyy-MM-dd')

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QVBoxLayout()

        layout.addWidget(lekarz_label)
        layout.addWidget(self.lekarz_combo)

        layout.addWidget(pacjent_label)
        layout.addWidget(self.pacjent_combo)

        layout.addWidget(nazwa_label)
        layout.addWidget(self.nazwa_combo)

        layout.addWidget(data_label)
        layout.addWidget(self.data_edit)

        layout.addWidget(dodaj_button)
        layout.addWidget(anuluj_button)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj nową receptę')

    def fill_lekarze(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        lekarze = self.cur.execute('SELECT id_l, imie, nazwisko FROM lekarz').fetchall()

        lekarze = [f"{lekarz[0]} - {lekarz[1]} {lekarz[2]}" for lekarz in lekarze]

        self.lekarz_combo.addItems(lekarze)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def fill_pacjenci(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        pacjenci = self.cur.execute('SELECT id_p, imie, nazwisko FROM pacjenci').fetchall()

        pacjenci = [f"{pacjent[0]} - {pacjent[1]} {pacjent[2]}" for pacjent in pacjenci]

        self.pacjent_combo.addItems(pacjenci)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def fill_leki(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        leki = self.cur.execute('SELECT nazwa FROM leki').fetchall()

        leki = [f"{lek[0]}" for lek in leki]

        self.nazwa_combo.addItems(leki)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def get_data(self):
        # Pobranie wybranych danych z pól wyboru i pola edycji daty
        lekarz = self.lekarz_combo.currentText().split(':')[0]
        pacjent = self.pacjent_combo.currentText().split(':')[0]
        nazwa = self.nazwa_combo.currentText()

        # Formatowanie daty
        data = self.data_edit.date().toString('yyyy-MM-dd')
        return lekarz[0], pacjent[0], nazwa, data

class ReceptyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(600)
        self.setFixedHeight(300)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
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
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddReceptaDialog(self)
            if dialog.exec_():
                lekarz, pacjent, nazwa, data_wydania = dialog.get_data()

                # Dodaj nową receptę do bazy danych
                self.cur.execute('INSERT INTO recepty (lekarz_wystawiajacy, pacjent, lek, data_wystawienia) VALUES (?, ?, ?, ?)', (int(lekarz), int(pacjent), nazwa, data_wydania))
                self.conn.commit()
                # Odśwież widok tabeli
                self.refresh_table()

            # Zwalniamy:
            change_blocked()

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

    def show_error(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Warning)
        error_box.setWindowTitle("Błąd")
        error_box.setText("Baza aktualnie edytowana. Poczekaj...")
        error_box.exec_()

# WYPIS:
class AddWypis(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utworzenie etykiet i pól wyboru dla danych nowej zabiegu/operacji
        # PACJENT
        pacjent_label = QLabel('Pacjent:')
        self.pacjent_combo = QComboBox(self)
        self.fill_pacjenci()

        # LEKARZ
        lekarz_label = QLabel('Lekarz:')
        self.lekarz_combo = QComboBox(self)
        self.fill_lekarz()

        data_label = QLabel('Data wypisu:')
        self.data_edit = QDateEdit(calendarPopup=True)
        self.data_edit.setDate(QDate.currentDate())
        self.data_edit.setDisplayFormat('yyyy-MM-dd')

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QVBoxLayout()

        layout.addWidget(pacjent_label)
        layout.addWidget(self.pacjent_combo)

        layout.addWidget(lekarz_label)
        layout.addWidget(self.lekarz_combo)

        layout.addWidget(data_label)
        layout.addWidget(self.data_edit)

        layout.addWidget(dodaj_button)
        layout.addWidget(anuluj_button)

        self.setLayout(layout)
        self.setWindowTitle('Wypisz pacjenta')

    def fill_pacjenci(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        pacjenci = self.cur.execute('SELECT id_p, imie, nazwisko FROM pacjenci').fetchall()

        pacjenci = [f"{pacjent[0]} - {pacjent[1]} {pacjent[2]}" for pacjent in pacjenci]

        self.pacjent_combo.addItems(pacjenci)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def fill_lekarz(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()
        lekarze = self.cur.execute('SELECT id_l, imie, nazwisko FROM lekarz').fetchall()

        lekarze = [f"{lekarz[0]} - {lekarz[1]} {lekarz[2]}" for lekarz in lekarze]

        self.lekarz_combo.addItems(lekarze)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def get_przyjecie(self, id_p):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT data_przyjecia FROM pacjenci WHERE id_p = ?", (id_p,))

        # Pobranie wyników zapytania
        result = self.cur.fetchone()

        return result[0]


    def get_choroba(self, id_p):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT choroba FROM pacjenci WHERE id_p = ?", (id_p,))

        # Pobranie wyników zapytania
        result = self.cur.fetchone()

        return result[0]

    def get_data(self):
        # Pobranie wybranych danych z pól wyboru i pól edycyjnych
        pacjent = self.pacjent_combo.currentText().split(':')[0]
        lekarz = self.lekarz_combo.currentText().split(':')[0]
        data_wypisu = self.data_edit.date().toString('yyyy-MM-dd')
        data_przyjecia = self.get_przyjecie(pacjent[0])
        choroba = self.get_choroba(pacjent[0])

        print(pacjent[0], lekarz[0], data_przyjecia, data_wypisu, choroba)
        return pacjent[0], lekarz[0], data_przyjecia, data_wypisu, choroba

class WypisWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(700)
        self.setFixedHeight(300)

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.conn.set_trace_callback(log)
        self.cur = self.conn.cursor()

        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute('SELECT * FROM wypis')
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
        self.setWindowTitle('Wypis')

        # Tworzenie paska narzędzi z przyciskiem dodawania nowego zabiegu/operacji
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_wypis_action = QAction('Dodaj nowy wypis', self)
        add_wypis_action.triggered.connect(self.show_add_wypis_dialog)
        toolbar.addAction(add_wypis_action)

    def show_add_wypis_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()

            dialog = AddWypis(self)
            if dialog.exec_():
                pacjent, lekarz, data_przyjęcia, data_wypisu, choroba = dialog.get_data()


                # Dodaj nowy zabieg/operację do bazy danych
                self.cur.execute('INSERT INTO wypis (pacjent, lekarz, data_przyjęcia, data_wypisu, choroba) VALUES (?, ?, ?, ?, ?)', (int(pacjent), int(lekarz), data_przyjęcia, data_wypisu, choroba))
                self.cur.execute("DELETE FROM pacjenci WHERE id_p=?", (int(pacjent),))
                self.conn.commit()

                # Odśwież widok tabeli
                self.refresh_table()
            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute('SELECT * FROM wypis')
        rows = self.cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

    def show_error(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Warning)
        error_box.setWindowTitle("Błąd")
        error_box.setText("Baza aktualnie edytowana. Poczekaj...")
        error_box.exec_()

# make sure there is LoginScreen()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
