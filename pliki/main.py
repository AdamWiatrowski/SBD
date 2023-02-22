import sys
import sqlite3
import socket
from datetime import datetime

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QTableWidgetItem, QLineEdit, QDialog, QFormLayout, QDialogButtonBox, QTextEdit, QToolBar, QAction, \
    QDateEdit, QComboBox, QMessageBox, QSpinBox, QGridLayout, QCalendarWidget

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
class AddChorobaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        nazwa_label = QLabel('Nazwa:')
        self.nazwa_input = QLineEdit()

        objawy_label = QLabel('Objawy:')
        self.objawy_input = QLineEdit()

        rek_leki_label = QLabel('Rekomendowane leki:')
        self.rek_leki_input = QLineEdit()

        postepowanie_label = QLabel('Postepowanie:')
        self.postepowanie_input = QLineEdit()


        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QFormLayout()

        layout.addRow(nazwa_label, self.nazwa_input)
        layout.addRow(objawy_label, self.objawy_input)
        layout.addRow(rek_leki_label, self.rek_leki_input)
        layout.addRow(postepowanie_label, self.postepowanie_input)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(dodaj_button)
        buttons_layout.addWidget(anuluj_button)

        layout.addRow(buttons_layout)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj nowa chorobe')

    def get_data(self):
        return self.nazwa_input.text(), \
                self.objawy_input.text(), \
                self.rek_leki_input.text(), \
                self.postepowanie_input.text()

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

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_choroba_action = QAction('Dodaj nowa chorobe', self)
        add_choroba_action.triggered.connect(self.show_add_choroba_dialog)

        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_choroba = QAction('Szukaj', self)
        search_choroba.triggered.connect(self.search_choroba_final)

        toolbar.addAction(add_choroba_action)
        toolbar.addAction(search_choroba)
        toolbar.addWidget(self.szukaj_wpisz)


    def show_add_choroba_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddChorobaDialog(self)
            if dialog.exec_():
                nazwa, objawy, rekomendowane_leki, postepowanie = dialog.get_data()
                if(len(nazwa) == 0 or len(objawy) == 0):
                    error_box = QMessageBox()
                    error_box.setIcon(QMessageBox.Warning)
                    error_box.setWindowTitle("Błąd")
                    error_box.setText("Nazwa oraz Objawy nie moga byc puste.")
                    error_box.exec_()
                else:
                    self.conn = sqlite3.connect('szpital.db')
                    self.conn.set_trace_callback(log)

                    self.cur = self.conn.cursor()

                    # Dodaj nową receptę do bazy danych
                    self.cur.execute('INSERT INTO choroba (nazwa, objawy, rekomendowane_leki, postepowanie) VALUES (?, ?, ?, ?)', (nazwa, objawy, rekomendowane_leki, postepowanie))

                    # Odśwież widok tabeli
                    self.refresh_table()
                    self.conn.commit()
                    self.conn.close()

            # Zwalniamy:
            change_blocked()

    def search_choroba_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute(
            "SELECT * FROM choroba WHERE nazwa LIKE ? OR objawy LIKE ? OR rekomendowane_leki LIKE ? OR postepowanie LIKE ?",
            (search, search, search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

    def refresh_table(self):
        # Zapytanie SQL o wszystkie recepty
        self.cur.execute('SELECT * FROM choroba')
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

# POKOJE:
class AddPokojeWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.liczba_lozek = QSpinBox(self)
        self.liczba_lozek.setObjectName("Liczba lozek")
        self.liczba_lozek.setMinimum(0)
        self.liczba_lozek.setSingleStep(1)

        self.liczba_wolnych_lozek = QSpinBox(self)
        self.liczba_wolnych_lozek.setObjectName("Liczba wolnych lozek")
        self.liczba_wolnych_lozek.setMinimum(0)
        self.liczba_wolnych_lozek.setSingleStep(1)

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QFormLayout()
        layout.addRow("Liczba łóżek:", self.liczba_lozek)
        layout.addRow("Liczba wolnych łóżek:", self.liczba_wolnych_lozek)
        layout.addRow(dodaj_button, anuluj_button)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj nowy pokój')

    def get_data(self):
        return self.liczba_lozek.value(), self.liczba_wolnych_lozek.value()

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

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_pokoj_action = QAction('Dodaj nowy pokoj', self)
        add_pokoj_action.triggered.connect(self.show_add_pokoj_dialog)

        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)

        search_pokoj = QAction('Szukaj', self)
        search_pokoj.triggered.connect(self.search_pokoj_final)

        toolbar.addAction(add_pokoj_action)
        toolbar.addAction(search_pokoj)
        toolbar.addWidget(self.szukaj_wpisz)

    def show_add_pokoj_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddPokojeWindow(self)
            if dialog.exec_():
                liczba_lozek, liczba_wolnych_lozek = dialog.get_data()

                self.conn = sqlite3.connect('szpital.db')
                self.conn.set_trace_callback(log)

                self.cur = self.conn.cursor()

                # Dodaj nową receptę do bazy danych
                self.cur.execute('INSERT INTO pokoje (liczba_lozek, liczba_wolnych_lozek) VALUES (?, ?)', (int(liczba_lozek), int(liczba_wolnych_lozek)))

                # Odśwież widok tabeli
                self.refresh_table()
                self.conn.commit()
                self.conn.close()

            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie recepty
        self.cur.execute('SELECT * FROM pokoje')
        rows = self.cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

    def search_pokoj_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute(
            "SELECT * FROM POKOJE WHERE numer_pokoju LIKE ? OR liczba_lozek LIKE ? OR liczba_wolnych_lozek LIKE ?",
            (search, search, search))

        rows = cur.fetchall()

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

# PACJENCI:
class AddPacjentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utworzenie etykiet i pól dla danych nowego pacjenta
        imie_label = QLabel('Imię:')
        self.imie_input = QLineEdit()

        nazwisko_label = QLabel('Nazwisko:')
        self.nazwisko_input = QLineEdit()

        wiek_label = QLabel('Wiek:')
        self.wiek_input = QSpinBox()
        self.wiek_input.setMinimum(1)

        plec_label = QLabel('Płeć:')
        self.plec_input = QComboBox()
        self.plec_input.addItem('K')
        self.plec_input.addItem('M')

        waga_label = QLabel('Waga:')
        self.waga_input = QSpinBox()
        self.waga_input.setMinimum(1)

        wzrost_label = QLabel('Wzrost:')
        self.wzrost_input = QSpinBox()
        self.wzrost_input.setMinimum(1)

        data_label = QLabel('Data przyjęcia:')
        self.data_input = QDateEdit(calendarPopup=True)
        self.data_input.setDate(QDate.currentDate())
        self.data_input.setDisplayFormat('yyyy-MM-dd')

        pokoj_label = QLabel('Pokój:')
        self.pokoj_input = QComboBox()
        self.fill_pokoje()

        # tu moze byc wybor nadal;
        choroba_label = QLabel('Choroba:')
        self.choroba_input = QComboBox()
        self.fill_choroba()

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

    def fill_choroba(self):
        conn = sqlite3.connect('szpital.db')
        conn.set_trace_callback(log)
        cur = conn.cursor()

        # Zapytanie SQL o wszystkie pokoje, gdzie są wolne łóżka
        cur.execute('SELECT nazwa FROM choroba')

        choroby = cur.fetchall()
        choroby = [choroba[0] for choroba in choroby]

        # Ustawienie elementów QComboBox
        self.choroba_input.addItems(choroby)

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

    def accept(self):
        # Sprawdzenie, czy nazwisko i imię pacjenta zostały wprowadzone
        if not self.nazwisko_input.text() or not self.imie_input.text():
            QMessageBox.warning(self, 'Błąd', 'Nazwisko i imię pacjenta nie mogą być puste!')
            return

        super().accept()

    def get_data(self):
        return self.imie_input.text(), \
               self.nazwisko_input.text(), \
               self.wiek_input.text(), \
               self.plec_input.currentText(), \
               self.waga_input.text(), \
               self.wzrost_input.text(), \
               self.data_input.text(), \
               self.pokoj_input.currentText(), \
               self.choroba_input.currentText(), \
               self.lekarz_input.currentText().split(' - ')[0]
# todo + add aliases
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
        self.cur.execute('SELECT pacjenci.imie, pacjenci.nazwisko, pacjenci.wiek, pacjenci.plec, pacjenci.waga, pacjenci.wzrost, pacjenci.data_przyjecia, pacjenci.pokoj,pacjenci.choroba, lekarz.imie, lekarz. nazwisko FROM pacjenci JOIN lekarz on pacjenci.lekarz_prowadzacy = lekarz.id_l')
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

        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_pacjent = QAction('Szukaj', self)
        search_pacjent.triggered.connect(self.search_pacjent_final)


        toolbar.addAction(add_pacjent_action)
        toolbar.addAction(search_pacjent)
        toolbar.addWidget(self.szukaj_wpisz)

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
                    self.conn = sqlite3.connect('szpital.db')
                    self.conn.set_trace_callback(log)
                    self.cur = self.conn.cursor()
                    self.cur.execute(
                        'INSERT INTO pacjenci (imie, nazwisko, wiek, plec, waga, wzrost, data_przyjecia, pokoj, choroba, lekarz_prowadzacy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                        (imie, nazwisko, int(wiek), plec, int(waga), int(wzrost), data_przyjecia, int(pokoj), choroba,
                         int(lekarz_prowadzacy)))


                    self.cur.execute(
                        'UPDATE pokoje SET liczba_wolnych_lozek = liczba_wolnych_lozek - 1 WHERE numer_pokoju = ?',
                        (pokoj,))

                    # Odśwież widok tabeli
                    self.refresh_table()
                    self.conn.commit()
                    self.conn.close()
                except:
                    error_box = QMessageBox()
                    error_box.setIcon(QMessageBox.Warning)
                    error_box.setWindowTitle("Błąd")
                    error_box.setText("Niektóre pola są bledne! Wypełnij poprawnie pola.")
                    error_box.exec_()
            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkich pacjentów
        self.cur.execute('SELECT pacjenci.imie, pacjenci.nazwisko, pacjenci.wiek, pacjenci.plec, pacjenci.waga, pacjenci.wzrost, pacjenci.data_przyjecia, pacjenci.pokoj,pacjenci.choroba, lekarz.imie, lekarz. nazwisko FROM pacjenci JOIN lekarz on pacjenci.lekarz_prowadzacy = lekarz.id_l')
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

    def search_pacjent_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"


        cur.execute("SELECT pacjenci.imie, pacjenci.nazwisko, pacjenci.wiek, pacjenci.plec, pacjenci.waga, pacjenci.wzrost, pacjenci.data_przyjecia, pacjenci.pokoj,pacjenci.choroba, lekarz.imie, lekarz. nazwisko FROM pacjenci JOIN lekarz on pacjenci.lekarz_prowadzacy = lekarz.id_l WHERE pacjenci.imie LIKE ? OR pacjenci.nazwisko LIKE ? OR pacjenci.wiek LIKE ? OR pacjenci.plec LIKE ? OR pacjenci.waga LIKE ? OR pacjenci.wzrost LIKE ? OR pacjenci.data_przyjecia LIKE ? OR pacjenci.pokoj LIKE ? OR pacjenci.choroba LIKE ? OR lekarz.imie LIKE ? OR lekarz. nazwisko LIKE ?", (search, search, search, search, search, search, search, search, search, search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

# LEKARZE:
class AddLekarzWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Ustawienie tytułu i rozmiaru okna dialogowego
        self.setWindowTitle('Dodaj nowego lekarza')
        self.setFixedWidth(400)

        # Utworzenie widgetów do wprowadzania danych
        self.nazwisko_input = QLineEdit()
        self.nazwisko_input.setPlaceholderText('Nazwisko')

        self.imie_input = QLineEdit()
        self.imie_input.setPlaceholderText('Imię')

        self.plec_input = QComboBox()
        self.plec_input.addItem('K')
        self.plec_input.addItem('M')

        self.pozycja_input = QLineEdit()
        self.pozycja_input.setPlaceholderText('Pozycja')

        self.wiek_input = QSpinBox()
        self.wiek_input.setMinimum(0)
        self.wiek_input.setMaximum(150)

        self.pensja_input = QSpinBox()
        self.pensja_input.setSingleStep(500)
        self.pensja_input.setMinimum(0)
        self.pensja_input.setMaximum(50000)

        self.data_zatrudnienia_input = QDateEdit(calendarPopup=True)
        self.data_zatrudnienia_input.setDate(QDate.currentDate())
        self.data_zatrudnienia_input.setDisplayFormat('yyyy-MM-dd')

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        dodaj_button.clicked.connect(self.accept)

        anuluj_button = QPushButton('Anuluj')
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QVBoxLayout()

        form_layout = QGridLayout()
        form_layout.addWidget(QLabel('Nazwisko:'), 0, 0)
        form_layout.addWidget(self.nazwisko_input, 0, 1)
        form_layout.addWidget(QLabel('Imię:'), 1, 0)
        form_layout.addWidget(self.imie_input, 1, 1)
        form_layout.addWidget(QLabel('Plec:'), 2, 0)
        form_layout.addWidget(self.plec_input, 2, 1)
        form_layout.addWidget(QLabel('Pozycja:'), 3, 0)
        form_layout.addWidget(self.pozycja_input, 3, 1)
        form_layout.addWidget(QLabel('Wiek:'), 4, 0)
        form_layout.addWidget(self.wiek_input, 4, 1)
        form_layout.addWidget(QLabel('Pensja:'), 5, 0)
        form_layout.addWidget(self.pensja_input, 5, 1)
        form_layout.addWidget(QLabel('Data zatrudnienia:'), 6, 0)
        form_layout.addWidget(self.data_zatrudnienia_input, 6, 1)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(dodaj_button)
        buttons_layout.addWidget(anuluj_button)

        layout.addLayout(form_layout)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def accept(self):
        # Sprawdzenie, czy nazwisko i imię lekarza zostały wprowadzone
        if not self.nazwisko_input.text() or not self.imie_input.text():
            QMessageBox.warning(self, 'Błąd', 'Nazwisko i imię lekarza nie mogą być puste!')
            return

        super().accept()

    def get_data(self):
        # Pobranie wartości z kontrolek i zwrócenie ich jako krotka
        nazwisko = self.nazwisko_input.text()
        imie = self.imie_input.text()
        plec = self.plec_input.currentText()
        pozycja = self.pozycja_input.text()

        wiek = self.wiek_input.value()
        pensja = self.pensja_input.value()

        data_zatrudnienia = self.data_zatrudnienia_input.date().toString('yyyy-MM-dd')

        return nazwisko, imie, plec, wiek, data_zatrudnienia, pensja, pozycja

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

        # Tworzenie paska narzędzi z przyciskiem dodawania nowej recepty
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_lekarz_action = QAction('Dodaj nową receptę', self)
        add_lekarz_action.triggered.connect(self.show_add_lekarz_dialog)

        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_lekarz = QAction('Szukaj', self)
        search_lekarz.triggered.connect(self.search_lekarz_final)

        toolbar.addAction(add_lekarz_action)
        toolbar.addAction(search_lekarz)
        toolbar.addWidget(self.szukaj_wpisz)

    def show_add_lekarz_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddLekarzWindow(self)
            if dialog.exec_():
                nazwisko, imie, plec, wiek, data_zatrudnienia, pensja, pozycja = dialog.get_data()

                # Dodaj nowy zabieg/operację do bazy danych
                self.conn = sqlite3.connect('szpital.db')
                self.conn.set_trace_callback(log)
                self.cur = self.conn.cursor()

                self.cur.execute('INSERT INTO lekarz (nazwisko, imie, plec, wiek, data_zatrudnienia, pensja, pozycja) VALUES (?, ?, ?, ?, ?, ?, ?)', (nazwisko, imie, plec, wiek, data_zatrudnienia, pensja, pozycja))

                # Odśwież widok tabeli
                self.refresh_table()
                self.conn.commit()
                self.conn.close()

            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute(
            'SELECT * FROM lekarz')
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

    def search_lekarz_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute(
            "SELECT id_l, nazwisko, imie, wiek, plec, data_zatrudnienia, pensja, pozycja from lekarz WHERE imie LIKE ? OR nazwisko LIKE ? OR data_zatrudnienia LIKE ? OR pensja LIKE ? OR pozycja LIKE ?",
            (search, search, search, search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

# LEKI:

class AddLekiDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utworzenie pól formularza
        self.nazwa_leku_input = QLineEdit(self)
        self.na_chorobe_input = QComboBox(self)
        self.na_recepte_input = QComboBox(self)
        self.ile_razy_input = QSpinBox(self)
        self.przeciwskazania_input = QTextEdit(self)
        self.moze_wystapic_input = QTextEdit(self)

        # Wypełnienie pól wyboru
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT nazwa FROM choroba")
        rows = self.cur.fetchall()

        choroby = [row[0] for row in rows]

        self.conn.close()
        self.na_chorobe_input.addItems(choroby)

        self.na_recepte_input.addItems(['tak', 'nie'])

        # Ustawienie wartości domyślnych dla niektórych pól
        self.ile_razy_input.setMinimum(1)

        # Utworzenie przycisków
        dodaj_button = QPushButton('Dodaj')
        anuluj_button = QPushButton('Anuluj')

        # Podpięcie metod do przycisków
        dodaj_button.clicked.connect(self.accept)
        anuluj_button.clicked.connect(self.reject)

        # Utworzenie layoutu i dodanie do niego elementów
        layout = QFormLayout()
        layout.addRow(QLabel('Nazwa leku:'), self.nazwa_leku_input)
        layout.addRow(QLabel('Na chorobę:'), self.na_chorobe_input)
        layout.addRow(QLabel('Na receptę:'), self.na_recepte_input)
        layout.addRow(QLabel('Ile razy dziennie:'), self.ile_razy_input)
        layout.addRow(QLabel('Przeciwskazania:'), self.przeciwskazania_input)
        layout.addRow(QLabel('Może wystąpić:'), self.moze_wystapic_input)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(dodaj_button)
        buttons_layout.addWidget(anuluj_button)

        layout.addRow(buttons_layout)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj nowy lek')

    def accept(self):
        # Sprawdzenie, czy nazwisko i imię pacjenta zostały wprowadzone
        if not self.nazwa_leku_input.text():
            QMessageBox.warning(self, 'Błąd', 'Nazwa leku nie moze byc pusta!')
            return

        super().accept()

    def get_data(self):
        return self.nazwa_leku_input.text(), \
                self.na_chorobe_input.currentText(), \
                self.na_recepte_input.currentText(), \
                self.ile_razy_input.value(), \
                self.przeciwskazania_input.toPlainText(), \
                self.moze_wystapic_input.toPlainText()

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

        # Tworzenie paska narzędzi z przyciskiem dodawania nowej recepty
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_lek_action = QAction('Dodaj nowy lek', self)
        add_lek_action.triggered.connect(self.show_add_lek_dialog)



        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_lek = QAction('Szukaj', self)
        search_lek.triggered.connect(self.search_lek_final)

        toolbar.addAction(add_lek_action)
        toolbar.addAction(search_lek)
        toolbar.addWidget(self.szukaj_wpisz)

    def show_add_lek_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddLekiDialog(self)
            if dialog.exec_():
                nazwa, na_chorobe, na_recepte, ile_razy, przeciwskazania, może_wystąpić = dialog.get_data()

                # Dodaj nowy zabieg/operację do bazy danych
                self.conn = sqlite3.connect('szpital.db')
                self.conn.set_trace_callback(log)
                self.cur = self.conn.cursor()

                self.cur.execute('INSERT INTO leki (nazwa, na_chorobe, na_recepte, ile_razy, przeciwskazania, może_wystąpić) VALUES (?, ?, ?, ?, ?, ?)', (nazwa, na_chorobe, na_recepte, ile_razy, przeciwskazania, może_wystąpić))

                # Odśwież widok tabeli
                self.refresh_table()
                self.conn.commit()
                self.conn.close()

            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute(
            'SELECT * FROM leki')
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

    def search_lek_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute("SELECT * FROM leki WHERE nazwa LIKE ? OR na_chorobe LIKE ? OR na_recepte LIKE ? OR przeciwskazania LIKE ? OR może_wystąpić like ?", (search, search, search, search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

# LEKI W MAGAZYNIE:

class AddLekiMagazynDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Wypełnienie pól wyboru
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT nazwa FROM choroba")
        rows = self.cur.fetchall()

        self.choroby = [row[0] for row in rows]

        self.conn.close()


        self.nazwa_leku_label = QLabel('Nazwa leku:', self)
        self.nazwa_leku_input = QComboBox(self)
        self.nazwa_leku_input.addItems(self.choroby)

        self.ilosc_sztuk_label = QLabel('Ilość sztuk:', self)
        self.ilosc_sztuk_input = QSpinBox(self)
        self.ilosc_sztuk_input.setMinimum(1)

        self.dodaj_button = QPushButton('Dodaj')
        self.anuluj_button = QPushButton('Anuluj')

        self.dodaj_button.clicked.connect(self.accept)
        self.anuluj_button.clicked.connect(self.reject)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.dodaj_button)
        buttons_layout.addWidget(self.anuluj_button)

        layout = QVBoxLayout()
        layout.addWidget(self.nazwa_leku_label)
        layout.addWidget(self.nazwa_leku_input)
        layout.addWidget(self.ilosc_sztuk_label)
        layout.addWidget(self.ilosc_sztuk_input)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.setWindowTitle('Dodaj lek do magazynu')

    def get_data(self):
        return self.nazwa_leku_input.currentText(), self.ilosc_sztuk_input.value()

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

        # Tworzenie paska narzędzi z przyciskiem dodawania nowego zabiegu/operacji
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_leki_magazyn_action = QAction('Dodaj nowy zabieg/operację', self)
        add_leki_magazyn_action.triggered.connect(self.show_add_lek_magazyn_dialog)

        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_leki_magazyn = QAction('Szukaj', self)
        search_leki_magazyn.triggered.connect(self.search_leki_magazyn_final)

        toolbar.addAction(add_leki_magazyn_action)
        toolbar.addAction(search_leki_magazyn)
        toolbar.addWidget(self.szukaj_wpisz)

    def show_add_lek_magazyn_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddLekiMagazynDialog(self)
            if dialog.exec_():
                nazwa, ilosc_sztuk = dialog.get_data()

                # Dodaj nowy zabieg/operację do bazy danych
                self.conn = sqlite3.connect('szpital.db')
                self.conn.set_trace_callback(log)
                self.cur = self.conn.cursor()

                self.cur.execute('INSERT INTO leki_magazyn (nazwa, ilosc_sztuk) VALUES (?, ?)', (nazwa, ilosc_sztuk))

                # Odśwież widok tabeli
                self.refresh_table()
                self.conn.commit()
                self.conn.close()

            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute(
            'SELECT * FROM leki_magazyn')
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

    def search_leki_magazyn_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute("SELECT * FROM leki_magazyn WHERE nazwa LIKE ? OR ilosc_sztuk LIKE ? ", (search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

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
        self.sala_input = QSpinBox(self)
        self.sala_input.setMinimum(1)
        self.sala_input.setMaximum(30)

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
        layout.addWidget(self.sala_input)

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
        pacjent = self.pacjent_combo.currentText().split(':')[0].split(" ")[0]
        lekarz = self.lekarz_combo.currentText().split(':')[0].split(" ")[0]
        sala = self.sala_edit.text()
        rodzaj = self.rodzaj_combo.currentText()
        data = self.data_edit.date().toString('yyyy-MM-dd')
        return data, lekarz, sala, pacjent, rodzaj

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
        self.cur.execute('SELECT id_oz, data_wykonania, lekarz.imie as lekarz_imie, lekarz.nazwisko as lekarz_nazwisko, sala, pacjenci.imie as pacjent_imie, pacjenci.nazwisko as pacjent_nazwisko, rodzaj from zabiegoperacja join pacjenci on zabiegoperacja.pacjent = pacjenci.id_p join lekarz on zabiegoperacja.lekarz = lekarz.id_l')
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

        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_zabiegop = QAction('Szukaj', self)
        search_zabiegop.triggered.connect(self.search_zabiegoperacja_final)

        toolbar.addAction(search_zabiegop)
        toolbar.addAction(search_zabiegop)
        toolbar.addWidget(self.szukaj_wpisz)

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
                    self.conn = sqlite3.connect('szpital.db')
                    self.conn.set_trace_callback(log)
                    self.cur = self.conn.cursor()

                    self.cur.execute('INSERT INTO zabiegoperacja (data_wykonania, lekarz, sala, pacjent, rodzaj) VALUES (?, ?, ?, ?, ?)', (data_wykonania, int(lekarz), int(sala), int(pacjent), rodzaj))


                    # Odśwież widok tabeli
                    self.refresh_table()
                    self.conn.commit()
                    self.conn.close()

                except:
                    error_box = QMessageBox()
                    error_box.setIcon(QMessageBox.Warning)
                    error_box.setWindowTitle("Błąd")
                    error_box.setText("Niektóre pola są puste! Wypełnij wszystkie pola.")
                    error_box.exec_()

            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute('SELECT id_oz, data_wykonania, lekarz.imie as lekarz_imie, lekarz.nazwisko as lekarz_nazwisko, sala, pacjenci.imie as pacjent_imie, pacjenci.nazwisko as pacjent_nazwisko, rodzaj from zabiegoperacja join pacjenci on zabiegoperacja.pacjent = pacjenci.id_p join lekarz on zabiegoperacja.lekarz = lekarz.id_l')
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

    def search_zabiegoperacja_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute(
            "SELECT id_oz, data_wykonania, lekarz.imie as lekarz_imie, lekarz.nazwisko as lekarz_nazwisko, sala, pacjenci.imie as pacjent_imie, pacjenci.nazwisko as pacjent_nazwisko, rodzaj from zabiegoperacja join pacjenci on zabiegoperacja.pacjent = pacjenci.id_p join lekarz on zabiegoperacja.lekarz = lekarz.id_l WHERE data_wykonania LIKE ? OR lekarz.imie LIKE ? OR lekarz.nazwisko LIKE ? OR sala LIKE ? OR pacjenci.imie LIKE ? OR pacjenci.nazwisko LIKE ? OR rodzaj LIKE ?",
            (search, search, search, search, search, search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

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
        lekarz = self.lekarz_combo.currentText().split(':')[0].split(" ")[0]
        pacjent = self.pacjent_combo.currentText().split(':')[0].split(" ")[0]
        nazwa = self.nazwa_combo.currentText()

        # Formatowanie daty
        data = self.data_edit.date().toString('yyyy-MM-dd')
        return lekarz, pacjent, nazwa, data

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
        self.cur.execute('SELECT id_r, pacjenci.imie as pacjent_imie, pacjenci.nazwisko as pacjent_nazwisko, lekarz.imie as lekarz_imie, lekarz.nazwisko as lekarz_nazwisko, lek, data_wystawienia  FROM recepty JOIN lekarz on recepty.lekarz_wystawiajacy = lekarz.id_l JOIN pacjenci on recepty.pacjent = pacjenci.id_p')
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



        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_recepta = QAction('Szukaj', self)
        search_recepta.triggered.connect(self.search_recepta_final)

        toolbar.addAction(add_recepta_action)
        toolbar.addAction(search_recepta)
        toolbar.addWidget(self.szukaj_wpisz)

    def show_add_recepta_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()
            dialog = AddReceptaDialog(self)
            if dialog.exec_():
                lekarz, pacjent, nazwa, data_wydania = dialog.get_data()

                self.conn = sqlite3.connect('szpital.db')
                self.conn.set_trace_callback(log)

                self.cur = self.conn.cursor()

                # Dodaj nową receptę do bazy danych
                self.cur.execute('INSERT INTO recepty (lekarz_wystawiajacy, pacjent, lek, data_wystawienia) VALUES (?, ?, ?, ?)', (int(lekarz), int(pacjent), nazwa, data_wydania))

                # Odśwież widok tabeli
                self.refresh_table()
                self.conn.commit()
                self.conn.close()

            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie recepty
        self.cur.execute('SELECT id_r, pacjenci.imie as pacjent_imie, pacjenci.nazwisko as pacjent_nazwisko, lekarz.imie as lekarz_imie, lekarz.nazwisko as lekarz_nazwisko, lek, data_wystawienia  FROM recepty JOIN lekarz on recepty.lekarz_wystawiajacy = lekarz.id_l JOIN pacjenci on recepty.pacjent = pacjenci.id_p')
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


    def search_recepta_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute(
            "SELECT id_r, pacjenci.imie as pacjent_imie, pacjenci.nazwisko as pacjent_nazwisko, lekarz.imie as lekarz_imie, lekarz.nazwisko as lekarz_nazwisko, lek, data_wystawienia  FROM recepty JOIN lekarz on recepty.lekarz_wystawiajacy = lekarz.id_l JOIN pacjenci on recepty.pacjent = pacjenci.id_p WHERE pacjenci.imie LIKE ? OR pacjenci.nazwisko LIKE ? OR lekarz.imie LIKE ? OR lekarz.nazwisko LIKE ? OR lek LIKE ? OR data_wystawienia LIKE ?",
            (search, search, search, search, search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

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

        print(id_p)
        self.cur.execute("SELECT data_przyjecia FROM pacjenci WHERE id_p = ?", (id_p,))

        # Pobranie wyników zapytania
        result = self.cur.fetchone()

        print(result)
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
        pacjent = self.pacjent_combo.currentText().split(':')[0].split(" ")[0]
        lekarz = self.lekarz_combo.currentText().split(':')[0].split(" ")[0]
        data_wypisu = self.data_edit.date().toString('yyyy-MM-dd')
        data_przyjecia = self.get_przyjecie(pacjent)
        choroba = self.get_choroba(pacjent)

        print(pacjent, lekarz, data_przyjecia, data_wypisu, choroba)
        return pacjent, lekarz, data_przyjecia, data_wypisu, choroba

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
        self.cur.execute("""
            SELECT 
                id_w, 
                lekarz.imie, 
                lekarz.nazwisko, 
                pacjenci.imie, 
                pacjenci.nazwisko, 
                data_przyjęcia, 
                data_wypisu, 
                wypis.choroba 
            FROM 
                wypis 
            JOIN 
                lekarz 
                ON wypis.lekarz = lekarz.id_l 
            JOIN 
                pacjenci 
                ON wypis.pacjent = pacjenci.id_p
        """)

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



        self.szukaj_wpisz = QLineEdit()
        self.szukaj_wpisz.setMaximumWidth(100)


        search_wypis = QAction('Szukaj', self)
        search_wypis.triggered.connect(self.search_wypis_final)

        toolbar.addAction(add_wypis_action)
        toolbar.addAction(search_wypis)
        toolbar.addWidget(self.szukaj_wpisz)


    def show_add_wypis_dialog(self):
        if check_config():
            self.show_error()
        else:
            # Zajmujemy:
            change_blocked()

            dialog = AddWypis(self)
            if dialog.exec_():
                pacjent, lekarz, data_przyjęcia, data_wypisu, choroba = dialog.get_data()

                self.conn = sqlite3.connect('szpital.db')
                self.conn.set_trace_callback(log)
                self.cur = self.conn.cursor()

                # Dodaj nowy zabieg/operację do bazy danych
                self.cur.execute('INSERT INTO wypis (pacjent, lekarz, data_przyjęcia, data_wypisu, choroba) VALUES (?, ?, ?, ?, ?)', (int(pacjent), int(lekarz), data_przyjęcia, data_wypisu, choroba))
                self.cur.execute(
                    "UPDATE pokoje SET liczba_wolnych_lozek = liczba_wolnych_lozek + 1 WHERE numer_pokoju = (SELECT pokoj from pacjenci WHERE id_p = ?)",
                    (int(pacjent), ))
                self.cur.execute("DELETE FROM pacjenci WHERE id_p=?", (int(pacjent),))


                # Odśwież widok tabeli
                self.refresh_table()

                self.conn.commit()
                self.conn.close()
            # Zwalniamy:
            change_blocked()

    def refresh_table(self):
        # Zapytanie SQL o wszystkie zabiegi/operacje
        self.cur.execute("""
            SELECT 
                id_w, 
                lekarz.imie, 
                lekarz.nazwisko, 
                pacjenci.imie, 
                pacjenci.nazwisko, 
                data_przyjęcia, 
                data_wypisu, 
                wypis.choroba 
            FROM 
                wypis 
            JOIN 
                lekarz 
                ON wypis.lekarz = lekarz.id_l 
            JOIN 
                pacjenci 
                ON wypis.pacjent = pacjenci.id_p
        """)

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

    def search_wypis_final(self):
        conn = sqlite3.connect('szpital.db')
        cur = conn.cursor()
        word = self.szukaj_wpisz.text()
        search = "%" + word + "%"

        cur.execute("""SELECT id_w, lekarz.imie, lekarz.nazwisko, pacjenci.imie, pacjenci.nazwisko, data_przyjęcia, data_wypisu, wypis.choroba 
                       FROM wypis 
                       JOIN lekarz ON wypis.lekarz = lekarz.id_l 
                       JOIN pacjenci ON wypis.pacjent = pacjenci.id_p 
                       WHERE lekarz.imie LIKE ? 
                          OR lekarz.nazwisko LIKE ? 
                          OR pacjenci.imie LIKE ? 
                          OR pacjenci.nazwisko LIKE ? 
                          OR data_przyjęcia LIKE ? 
                          OR data_wypisu LIKE ? 
                          OR wypis.choroba LIKE ?""",
                    (search, search, search, search, search, search, search))

        rows = cur.fetchall()

        # Wyczyszczenie tabeli i wypełnienie jej danymi
        table = self.centralWidget()
        table.clearContents()
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

# make sure there is LoginScreen()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_screen = WypisWindow()
    login_screen.show()
    sys.exit(app.exec_())
