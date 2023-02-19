import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QDateEdit, \
    QTableWidgetItem, QApplication, QMainWindow, QTableWidget, QToolBar, QAction, QTimeEdit
from PyQt5.QtCore import Qt, QDate

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
        self.cur = self.conn.cursor()
        pacjenci = self.cur.execute('SELECT id_p, imie, nazwisko FROM pacjenci').fetchall()

        pacjenci = [f"{pacjent[0]} - {pacjent[1]} {pacjent[2]}" for pacjent in pacjenci]

        self.pacjent_combo.addItems(pacjenci)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def fill_lekarz(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
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

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
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
        dialog = AddZabiegoperacjaDialog(self)
        if dialog.exec_():
            data_wykonania, lekarz, sala, pacjent, rodzaj = dialog.get_data()

            try:
                # Dodaj nowy zabieg/operację do bazy danych
                self.cur.execute('INSERT INTO zabiegoperacja (data_wykonania, lekarz, sala, pacjent, rodzaj) VALUES (?, ?, ?, ?, ?)', (data_wykonania, int(lekarz), int(sala), int(pacjent), rodzaj))
            except:
                print("nie moze byc puste - musi byc liczba")
                # KOMUNIKAT
            else:
                self.conn.commit()
                # Odśwież widok tabeli
                self.refresh_table()

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


app = QApplication(sys.argv)
window = ZabiegoperacjaWindow()
window.show()
sys.exit(app.exec_())
