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

    def get_przyjecie(self, id_p):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT data_przyjecia FROM pacjenci WHERE id_p = ?", (id_p,))

        # Pobranie wyników zapytania
        result = self.cur.fetchone()

        return result[0]


    def get_choroba(self, id_p):
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
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

        # Połączenie z bazą danych
        self.conn = sqlite3.connect('szpital.db')
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
        dialog = AddWypis(self)
        if dialog.exec_():
            pacjent, lekarz, data_przyjęcia, data_wypisu, choroba = dialog.get_data()


            # Dodaj nowy zabieg/operację do bazy danych
            self.cur.execute('INSERT INTO wypis (pacjent, lekarz, data_przyjęcia, data_wypisu, choroba) VALUES (?, ?, ?, ?, ?)', (int(pacjent), int(lekarz), data_przyjęcia, data_wypisu, choroba))
            self.cur.execute("DELETE FROM pacjenci WHERE id_p=?", (int(pacjent),))
            self.conn.commit()
            # Odśwież widok tabeli
            self.refresh_table()

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