import sqlite3

# CZY POTRZEBNE?
# todo wypis; xd

def add_pacjenci():
    # połączenie z bazą danych
    conn = sqlite3.connect('szpital.db')

    # utworzenie tabeli 'pacjenci'
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS pacjenci
                 (id_p INTEGER PRIMARY KEY AUTOINCREMENT, imie TEXT NOT NULL, nazwisko TEXT NOT NULL, wiek INTEGER NOT NULL, plec TEXT NOT NULL CHECK(plec in ('K', 'M')), waga INTEGER NOT NULL, wzrost INTEGER NOT NULL, data_przyjecia DATE DEFAULT (datetime('now','localtime')) NOT NULL, pokoj INTEGER NOT NULL, choroba TEXT NOT NULL, lekarz_prowadzacy INTEGER NOT NULL)''')

    # dodanie danych do tabeli 'pacjenci'
    dane_pacjentow = [
        (1, 'Anna', 'Wtorek', 54, 'K', 64, 167, '2023-02-02', 3, 'wąglik', 1),
        (2, 'Jerzy', 'Koala', 33, 'M', 89, 193, '2023-01-01', 6, 'dżuma', 2),
        (3, 'Jakub', 'Zimny', 21, 'M', 72, 168, '2022-12-20', 6, 'dżuma', 3),
        (4, 'Ewa', 'Nowak', 67, 'K', 70, 159, '2022-12-29', 1, 'cholera', 1),
        (5, 'Beata', 'Sobota', 55, 'K', 59, 159, '2023-01-28', 1, 'cholera', 5),
        (6, 'Halina', 'Zimna', 54, 'K', 68, 164, '2023-01-28', 3, 'wąglik', 6),
        (7, 'Patryk', 'Orka', 63, 'M', 95, 183, '2023-02-16', 2, 'ospa prawdziwa', 7),
        (8, 'Tobiasz', 'Kot', 72, 'M', 113, 180, '2023-02-07', 1, 'cholera', 8),
        (9, 'Izabela', 'Flet', 37, 'K', 74, 172, '2023-01-29', 3, 'wąglik', 9),
        (10, 'Julia', 'Kozacka', 29, 'K', 59, 155, '2023-01-18', 5, 'dżuma', 3),
        (11, 'Adam', 'Norek', 37, 'M', 85, 183, '2023-01-23', 2, 'ospa prawdziwa', 10),
        (12, 'Marek', 'Rak', 44, 'M', 122, 186, '2023-01-31', 7, 'dur brzuszny', 5),
        (13, 'Alan', 'Trup', 49, 'M', 99, 180, '2023-02-07', 8, 'dur brzuszny', 12),
        (14, 'Ilona', 'Palec', 50, 'K', 73, 177, '2022-12-19', 2, 'ospa prawdziwa', 13),
        (15, 'Laura', 'Rodan', 20, 'K', 58, 162, '2023-01-15', 5, 'dżuma', 3)
    ]

    for pacjent in dane_pacjentow:
        c.execute(
            "INSERT INTO pacjenci (id_p, imie, nazwisko, wiek, plec, waga, wzrost, data_przyjecia, pokoj, choroba, lekarz_prowadzacy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            pacjent)

    conn.commit()
    conn.close()

def add_pokoje():
    # połączenie z bazą danych
    conn = sqlite3.connect('szpital.db')

    # utworzenie tabeli 'pokoje'
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS pokoje
                 (numer_pokoju INTEGER PRIMARY KEY AUTOINCREMENT, liczba_lozek INTEGER NOT NULL, liczba_wolnych_lozek INTEGER)''')

    # dodanie danych do tabeli 'pokoje'
    dane_pokojow = [
        (1, 3, 1),
        (2, 3, 0),
        (3, 3, 0),
        (4, 2, 2),
        (5, 2, 1),
        (6, 2, 1),
        (7, 1, 0),
        (8, 1, 0),
        (9, 1, 1),
        (10, 4, 4)
    ]

    for pokoj in dane_pokojow:
        c.execute(
            "INSERT INTO pokoje (numer_pokoju, liczba_lozek, liczba_wolnych_lozek) VALUES (?, ?, ?)",
            pokoj)

    conn.commit()
    conn.close()

def add_choroba():
    # Połączenie z bazą danych
    conn = sqlite3.connect('szpital.db')
    c = conn.cursor()

    # Utworzenie tabeli
    c.execute('''CREATE TABLE choroba
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nazwa TEXT NOT NULL,
                 objawy TEXT NOT NULL,
                 rekomendowane_leki TEXT,
                 postepowanie TEXT)''')

    # Dane chorób
    dane_choroba = [
        ("wąglik", "brak sił, nudności, plamy na nogach i rękach", "apap, cirus", "zimne okłady, kąpiele w zimnej wodzie, krwioterapia"),
        ("dżuma", "zaczerwieniona skóra, senność, ból głowy", "otrivin, fenistil", "odpoczynek, ciepły okład zaczerwienionych miejsc"),
        ("cholera", "wysoka gorączka, ból zębów", "panadol, ketamina", "rozgrzanie ciała, płukanie jamy ustnej"),
        ("dur brzuszny", "plamy na brzuchu, nudności", "krople żołądkowe, kodeina", "ogrzanie podbrzusza, picie gorących napojów ziołowych"),
        ("ospa prawdziwa", "wysypka, swędząca skóra, gorączka", "maść końska, ibuprom", "stosowanie maści na wypryskach, odpoczynek"),
        ("zapalenie mózgu", "ból głowy, zawroty głowy, trudność widzenia", "coronal, brainik", "odpoczynek, masaż głowy"),
        ("zawał serca", "ucisk klatki piersiowej, ciężki oddech, niskie tętno", "acard, rutinoscorbin", "kroplówka, bajpasy")
    ]

    # Wstawienie danych do tabeli
    for choroba in dane_choroba:
        c.execute('''INSERT INTO choroba (nazwa, objawy, rekomendowane_leki, postepowanie)
                     VALUES (?, ?, ?, ?)''', choroba)

    # Zatwierdzenie zmian i zamknięcie połączenia z bazą danych
    conn.commit()
    conn.close()

def add_leki():
    conn = sqlite3.connect('szpital.db')
    c = conn.cursor()

    # Tworzenie tabeli leki
    c.execute('''CREATE TABLE leki
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT NOT NULL,
                na_chorobe TEXT NOT NULL,
                na_recepte TEXT NOT NULL CHECK(na_recepte in ('tak', 'nie')),
                ile_razy INTEGER NOT NULL,
                przeciwskazania TEXT,
                może_wystąpić TEXT)''')

    # Dodanie danych do tabeli
    leki = [(1, 'apap', 'wąglik', 'nie', 6, 'cukrzyca', 'ból głowy'),
            (2, 'acard', 'zawał serca', 'tak', 3, 'wada wzroku', 'ból zębów'),
            (3, 'cirus', 'wąglik', 'tak', 1, 'wada wzroku', 'senność'),
            (4, 'otrivin', 'dżuma', 'tak', 2, 'nadciśnienie', 'nudności'),
            (5, 'fenistil', 'dżuma', 'nie', 2, 'choroby sercowe', 'gorączka'),
            (6, 'panadol', 'cholera', 'nie', 3, 'nadciśnienie', 'nudności'),
            (7, 'ketamina', 'cholera', 'tak', 1, 'nadciśnienie', 'wysypka, ból nóg'),
            (8, 'rutinoscorbin', 'zawał serca', 'tak', 1, 'cukrzyca', 'gorączka'),
            (9, 'coronal', 'zapalenie mózgu', 'tak', 9, 'wada wzroku', 'zaczerwienie skóry'),
            (10, 'brainik', 'zapalenie mózgu', 'tak', 2, 'choroby sercowe', 'nudności'),
            (11, 'ibuprom', 'ospa prawdziwa', 'nie', 3, 'cukrzyca', 'senność'),
            (12, 'krople żołądkowe', 'dur brzuszny', 'nie', 2, 'niestrawność laktozy', 'zawroty głowy'),
            (13, 'maść końska', 'ospa prawdziwa', 'nie', 6, 'cukrzyca', 'zaczerwienie skóry'),
            (14, 'kodeina', 'dur brzuszny', 'tak', 2, 'choroby sercowe', 'senność')]

    c.executemany('INSERT INTO leki VALUES (?, ?, ?, ?, ?, ?, ?)', leki)
    conn.commit()
    conn.close()

def add_leki_magazyn():
    conn = sqlite3.connect('szpital.db')
    c = conn.cursor()
    # Tworzenie tabeli leki_magazyn
    c.execute('''CREATE TABLE leki_magazyn
                (nazwa TEXT PRIMARY KEY,
                ilosc_sztuk INTEGER NOT NULL)''')
    # Dodanie danych do tabeli
    leki_magazyn = [('apap', 10), ('acard', 17), ('cirus', 8), ('otrivin', 2),
              ('fenistil', 9), ('panadol', 27), ('ketamina', 43), ('rutinoscorbin', 1),
              ('coronal', 20), ('brainik', 8), ('ibuprom', 11), ('krople żołądkowe', 15),
              ('maść końska', 10), ('kodeina', 15)]
    c.executemany('INSERT INTO leki_magazyn VALUES (?, ?)', leki_magazyn)
    conn.commit()
    conn.close()

def add_lekarz():
    conn = sqlite3.connect('szpital.db')
    c = conn.cursor()
    # Tworzenie tabeli lekarz
    c.execute('''CREATE TABLE lekarz
                (id_l INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwisko TEXT NOT NULL,
                imie TEXT NOT NULL,
                wiek INTEGER NOT NULL,
                plec TEXT NOT NULL CHECK(plec in ('K', 'M')),
                data_zatrudnienia DATE DEFAULT (datetime('now','localtime')) NOT NULL,
                pensja INTEGER NOT NULL,
                pozycja TEXT)''')
    # Dodanie danych do tabeli
    lekarze = [(1, 'Nowicki', 'Adrian', 45, 'M', '2000-05-05', 14000, 'Pediatra'),
              (2, 'Rzepa', 'Olga', 45, 'K', '1999-11-13', 12500, 'Chirurg'),
              (3, 'Liske', 'Izabela', 32, 'K', '2022-12-15', 9000, 'Urolog'),
              (4, 'Rabarbar', 'Ewa', 59, 'K', '1989-11-02', 20000, 'Chirurg'),
              (5, 'Smuda', 'Adam', 41, 'M', '2017-02-01', 13250, 'Stomatolog'),
              (6, 'Ogon', 'Laura', 39, 'K', '2015-04-08', 12500, 'Okulista'),
              (7, 'Lis', 'Marek', 42, 'M', '2019-07-29', 12000, 'Chirurg'),
              (8, 'Wnuk', 'Beata', 37, 'K', '2018-10-20', 10000, 'Pediatra'),
              (9, 'Emeryt', 'Patryk', 48, 'M', '2006-02-01', 12000, 'Onkolog'),
              (10, 'Azor', 'Alina', 61, 'K', '1990-05-17', 17500, 'Anastazjolog'),
              (11, 'Koza', 'Tobiasz', 29, 'M', '2020-11-21', 8000, 'Asystent medyczny'),
              (12, 'Lipa', 'Robert', 56, 'M', '1990-05-17', 20000, 'Chirurg'),
              (13, 'Gola', 'Julia', 37, 'K', '2008-09-11', 11000, 'Onkolog')]
    c.executemany('INSERT INTO lekarz VALUES (?, ?, ?, ?, ?, ?, ?, ?)', lekarze)
    conn.commit()
    conn.close()

def add_zabiegoperacja():
    # połączenie z bazą danych
    conn = sqlite3.connect('szpital.db')
    # utworzenie tabeli 'zabiegoperacja'
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS zabiegoperacja
                 (id_oz INTEGER PRIMARY KEY AUTOINCREMENT, data_wykonania DATE NOT NULL, lekarz INTEGER NOT NULL, sala INTEGER NOT NULL, pacjent INTEGER NOT NULL, rodzaj TEXT NOT NULL)''')

    # dodanie danych do tabeli 'zabiegoperacja'
    dane_zabiegoperacja = [
        (1, '2022-12-29', 3, 2, 3, 'planowany'),
        (2, '2023-01-24', 10, 1, 11, 'nagły'),
        (3, '2023-01-24', 3, 5, 15, 'pilny'),
        (4, '2022-12-31', 1, 1, 4, 'nagły'),
        (5, '2023-02-07', 6, 3, 6, 'planowany')
    ]

    for oz in dane_zabiegoperacja:
        c.execute(
            "INSERT INTO zabiegoperacja (id_oz, data_wykonania, lekarz, sala, pacjent, rodzaj) VALUES (?, ?, ?, ?, ?, ?)",
            oz)

    conn.commit()
    conn.close()

def add_recepty():
    # połączenie z bazą danych
    conn = sqlite3.connect('szpital.db')

    # utworzenie tabeli 'recepty'
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS recepty
                 (id_r INTEGER PRIMARY KEY AUTOINCREMENT, lekarz_wystawiajacy INTEGER NOT NULL, pacjent INTEGER NOT NULL, lek TEXT NOT NULL, data_wystawienia DATE DEFAULT (datetime('now','localtime')) NOT NULL)''')

    # dodanie danych do tabeli 'recepty'
    dane_recept = [
        (1, 3, 3, 'otrivin', '2023-01-15'),
        (2, 4, 1, 'cirus', '2023-01-27'),
        (3, 3, 15, 'otrivin', '2023-02-02'),
        (4, 5, 12, 'kodeina', '2023-02-02'),
        (5, 9, 9, 'cirus', '2023-02-04')
    ]

    for recepta in dane_recept:
        c.execute(
            "INSERT INTO recepty (id_r, lekarz_wystawiajacy, pacjent, lek, data_wystawienia) VALUES (?, ?, ?, ?, ?)",
            recepta)

    conn.commit()
    conn.close()

add_pacjenci()
add_pokoje()
add_choroba()
add_leki()
add_leki_magazyn()
add_lekarz()
add_zabiegoperacja()
add_recepty()
