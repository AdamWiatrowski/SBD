import sys
import sqlite3

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QAction, QToolBar, QVBoxLayout, \
    QPushButton, QLineEdit, QLabel, QDialog, QComboBox, QFormLayout, QDateEdit, QHBoxLayout


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

        pokoj_label = QLabel('Pokój:')
        self.pokoj_input = QComboBox()
        self.fill_pokoje()

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
        cur = conn.cursor()

        # Zapytanie SQL o wszystkie pokoje, gdzie są wolne łóżka
        cur.execute('SELECT numer_pokoju FROM pokoje WHERE liczba_wolnych_lozek > 0')
        pokoje = [str(pokoj[0]) for pokoj in cur.fetchall()]

        # Ustawienie elementów QComboBox
        self.pokoj_input.addItems(pokoje)

    def fill_lekarze(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
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

        # Tworzenie paska narzędzi z przyciskiem dodawania nowego pacjenta
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        add_pacjent_action = QAction('Dodaj nowego pacjenta', self)
        add_pacjent_action.triggered.connect(self.show_add_pacjent_dialog)

        toolbar.addAction(add_pacjent_action)

    def show_add_pacjent_dialog(self):
        dialog = AddPacjentDialog(self)
        if dialog.exec_():
            imie, nazwisko, wiek, plec, waga, wzrost, data_przyjecia, pokoj, choroba, lekarz_prowadzacy = dialog.get_data()
            # Dodaj nowego pacjenta do bazy danych
            self.cur.execute(
                'INSERT INTO pacjenci (imie, nazwisko, wiek, plec, waga, wzrost, data_przyjecia, pokoj, choroba, lekarz_prowadzacy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (imie, nazwisko, int(wiek), plec, int(waga), int(wzrost), data_przyjecia, int(pokoj), choroba, int(lekarz_prowadzacy)))
            self.conn.commit()

            # Zmniejsz liczbę wolnych łóżek w wybranym pokoju o 1
            self.cur.execute('UPDATE pokoje SET liczba_wolnych_lozek = liczba_wolnych_lozek - 1 WHERE numer_pokoju = ?',
                             (pokoj,))
            self.conn.commit()

            # Odśwież widok tabeli
            self.refresh_table()

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



app = QApplication(sys.argv)
window = PacjenciWindow()
window.show()
sys.exit(app.exec_())
