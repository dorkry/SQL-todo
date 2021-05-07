# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('books.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS lista (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL, 
            title TEXT NOT NULL, 
            descr TEXT NOT NULL, 
            format TEXT NOT NULL)""") 

c.execute("""INSERT INTO lista VALUES 
        (1, 'Michelle F.', 'Ta druga', 'Carrie sporo poświęciła, by znaleźć się na szczycie. Teraz, kiedy ma czterdzieści lat, jest uznaną producentką telewizyjną, ma za męża odnoszącego sukcesy scenarzystę, a czas dzieli między dwa piękne domy. Odchodząc na urlop macierzyński, jest pełna obaw – nie wierzy, że uda jej się znaleźć godną następczynię, która będzie w stanie podołać jej dotychczasowym obowiązkom. Ale Emma jest inteligentna, zdeterminowana i drobiazgowa. Dokładnie taka, jak Carrie. A skrupulatność, z jaką Emma we wszystkim naśladuje swoją mentorkę, jest wręcz... przerażająca.', 'MOBI')""")
c.execute("""INSERT INTO lista VALUES 
        (2, 'Paris B.A.', 'Na skraju załamania', 'Kiedy człowiek może znaleźć się na tytułowym skraju załamania? Na przykład wtedy, gdy dręczą go ogromne wyrzuty sumienia. Zaniechanie jest gorsze od braku jakiegokolwiek działania, do czego przekonuje nas autorka książki. Kiedy Cass Anderson, bohaterka powieści, nie zatrzymała się nocą w lesie, aby sprawdzić, czy kobieta siedząca w zaparkowanym samochodzie nie potrzebuje pomocy, na dobre zaczął się jej koszmar. Szybko okazało się, że wspomniana osoba nie żyje.', 'EPUB')""")
c.execute("""INSERT INTO lista VALUES 
        (3, 'Delaney J.P.', 'Lokatorka', 'Emma już nie mieszka przy Folger Street 1, na jej miejsce wprowadza się Jane. Obie lokatorki, obecna i była, są do siebie bardzo podobne: kolor włosów, rysy twarzy, pragnienie rozpoczęcia wszystkiego od nowa. Ultranowoczesne mieszkanie wymaga dostosowania się do surowych reguł narzuconych przez właściciela, ale wydaje się idealne do porządkowania życiowego chaosu. Kobiety łączy coś jeszcze – enigmatyczna więź z właścicielem apartamentu. Jednak po pewnym czasie obok pożądania pojawia się niepewność i niepokój. Co różni Emmę i Jane? Emma już nie żyje, Jane jeszcze tak.', 'MOBI')""")
c.execute("""INSERT INTO lista VALUES
        (4, 'Mróz R.', 'Behawiorysta', 'Zamachowiec zajmuje przedszkole, grożąc że zabije wychowawców i dzieci. Policja jest bezsilna, a mężczyzna nie przedstawia żadnych żądań. Nikt nie wie, dlaczego wziął zakładników, ani co zamierza osiągnąć. Sytuację komplikuje fakt, że transmisja na żywo z przedszkola pojawia się w internecie.', 'PDF')""")
c.execute("""INSERT INTO lista VALUES
        (5, 'Mróz R.', 'Lot 202', 'Zwyczajna, piątkowa noc w Nowej Hucie. Kamery monitoringu u zbiegu dwóch ulic rejestrują młodego chłopaka o drugiej piętnaście. Nie ma go na nagraniu z przecznicy dalej… Sześć lat później, podkomisarz Agnieszka Oliwa odnajduje ciało chłopaka w Opolu. Wszystko wskazuje na to, że w wyjątkowo osobliwy sposób popełnił samobójstwo. Tymczasem z Okęcia startuje samolot z premierem na pokładzie. Zwykły lot do Toronto ma potrwać dziewięć godzin i trzydzieści pięć minut. Szybko okazuje się jednak, że najprawdopodobniej nigdy nie dotrze do celu… rozpoczyna się wyścig z czasem, a jedyną poszlaką jest chłopak, który niegdyś zaginął na krakowskich ulicach.', 'EPUB')""")

conn.commit()
c.close()