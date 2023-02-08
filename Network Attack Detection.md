# 1. Jak to pracuje
Program tworzy gniazdo TCP/IP i wiąże je z określonym adresem i portem. Następnie nasłuchuje połączeń przychodzących. Gdy połączenie zostanie zaakceptowane, program odbiera dane w małych porcjach i przesyła je z powrotem do klienta. Jeśli nie ma żadnych danych otrzymanych od klienta, program zamyka połączenie.

# 2. Dokumentacja
Jest to podstawowy szablon dla programu w Pythonie, który wykrywa ataki sieciowe. Program tworzy gniazdo TCP/IP i wiąże je z określonym adresem i portem. Następnie nasłuchuje połączeń przychodzących i odbiera dane w małych porcjach, przesyłając je z powrotem do klienta. Jeśli nie ma żadnych danych otrzymanych od klienta, program zamyka połączenie.

Aby uruchomić program, zapisz kod w pliku z rozszerzeniem .py i uruchom następujące polecenie w terminalu lub wierszu polecenia:


```
python network_attack_detection.py
```