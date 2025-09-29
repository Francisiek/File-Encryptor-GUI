### FEEDBACK

## KOD
- powinien być plik requirements.txt, który wywołuje się komendą pip freeze > requirements.txt
- a instaluje zależności komendą pip install -r requirements.txt
- lepiej zamiast nazywać zmienne ogólną nazwą i liczbą, lepiej je nazwać opisowo, tak że je czytasz i wiesz do czego służą - im mniej komentarzy wymaga kod tym lepiej, wtedy on mówi sam za siebie

## BŁĘDY
- gdy jest za krótki klucz to wywala błąd, że zły padding taki kod:
```
Exception in Tkinter callback
Traceback (most recent call last):
  File "/home/frannc/code/igor/File-Encryptor-GUI/venv/lib/python3.12/site-packages/cryptography/fernet.py", line 35, in __init__
    key = base64.urlsafe_b64decode(key)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/base64.py", line 134, in urlsafe_b64decode
    return b64decode(s)
           ^^^^^^^^^^^^
  File "/usr/lib/python3.12/base64.py", line 88, in b64decode
    return binascii.a2b_base64(s, strict_mode=validate)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
binascii.Error: Incorrect padding

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/lib/python3.12/tkinter/__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "/home/frannc/code/igor/File-Encryptor-GUI/main.py", line 100, in <lambda>
    encryption_btt = cls.Custom_Button("Encrypt", frame, lambda: fc.encrypt())
                                                                 ^^^^^^^^^^^^
  File "/home/frannc/code/igor/File-Encryptor-GUI/python_files/functions.py", line 121, in encrypt
    f = Fernet(key)
        ^^^^^^^^^^^
  File "/home/frannc/code/igor/File-Encryptor-GUI/venv/lib/python3.12/site-packages/cryptography/fernet.py", line 37, in __init__
    raise ValueError(
ValueError: Fernet key must be 32 url-safe base64-encoded bytes.
```
- gdy zapisuje plik zaszyfrowaną wiadomość i odszyfrowaną to dodaje na końcu nazwy pliku literę 't'

## main.py
- domyślnie działa tylko na windowsie bo w ścieżkach do plików jest \ a nie /
+ bardzo profesjonalnie, że kod masz podzielony na regiony
- zdecydowanie lepiej zamiast na regiony podzielić każdą stronę na klasę albo funckję, co powoduje odizolowanie przestrzeni każdej strony
## global_var.py
- nazwy zmiennych powinny być na tyle wymowne, że patrzysz i od razu wiesz do czego służą
## classes.py
+ ładnie zrobiłeś te customowe klasy, dobry zabieg

## UX
- jak wybiorę zadługi plik jako klucz to nie pojawia się komunikat błędu
- można wybrać ten sam plik jako klucz i dane do zaszyfrowania
- zamiast przycisku USE w szyfrowaniu dąłbym SAVE, bo to chodzi o zapisanie pliku, i przycisk do skopiowania do schowka, żeby nie trzeba było zapisywać
+ prosty, o to chodzi

Reszta bardzo fajnie. Podzielone klasy super, widać, że próbujesz uogólnić niektóre elementy, żeby pisać coś raz i potem używać wieloktronie.
Generalnie ładne nazwy zmiennych - nie bój się używać takich długich i wymownych, bo po to mamy IDE, żeby to za nas uzupełniało :)
