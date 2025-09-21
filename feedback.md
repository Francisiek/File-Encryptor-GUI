### FEEDBACK

## KOD
- powinien być plik requirements.txt, który wywołuje się komendą pip freeze > requirements.txt
- a instaluje zależności komendą pip install -r requirements.txt
- lepiej zamiast nazywać zmienne ogólną nazwą i liczbą, lepiej je nazwać opisowo, tak że je czytasz i wiesz do czego służą - im mniej komentarzy wymaga kod tym lepiej, wtedy on mówi sam za siebie
- 
## main.py
- domyślnie działa tylko na windowsie bo w ścieżkach do plików jest \ a nie /
+ bardzo profesjonalnie, że kod masz podzielony na regiony
- zdecydowanie lepiej zamiast na regiony podzielić każdą stronę na klasę albo funckję, co powoduje odizolowanie przestrzeni każdej strony
## global_var.py
- nazwy zmiennych powinny być na tyle wymowne, że patrzysz i od razu wiesz do czego służą


## UX
- jak wybiorę zadługi plik jako klucz to nie pojawia się komunikat błędu
- można wybrać ten sam plik jako klucz i dane do zaszyfrowania
- zamiast przycisku USE w szyfrowaniu dąłbym SAVE, bo to chodzi o zapisanie pliku, i przycisk do skopiowania do schowka, żeby nie trzeba było zapisywać
- 