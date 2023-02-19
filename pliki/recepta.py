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
        self.cur = self.conn.cursor()
        lekarze = self.cur.execute('SELECT id_l, imie, nazwisko FROM lekarz').fetchall()

        lekarze = [f"{lekarz[0]} - {lekarz[1]} {lekarz[2]}" for lekarz in lekarze]

        self.lekarz_combo.addItems(lekarze)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def fill_pacjenci(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()
        pacjenci = self.cur.execute('SELECT id_p, imie, nazwisko FROM pacjenci').fetchall()

        pacjenci = [f"{pacjent[0]} - {pacjent[1]} {pacjent[2]}" for pacjent in pacjenci]

        self.pacjent_combo.addItems(pacjenci)

        # Zamknięcie połączenia z bazą danych
        self.conn.close()

    def fill_leki(self):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
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