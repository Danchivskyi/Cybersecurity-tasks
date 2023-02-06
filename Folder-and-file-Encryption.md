# 1. Działanie programu:
- Key jest generowany przez funkcję hashlib.sha256 z przekazanego ciągu znaków 'secret_key'.
- Funkcje encrypt_file i decrypt_file szyfrują i deszyfrują pojedyncze pliki. Funkcje te korzystają z AES (Advanced Encryption Standard) jako szyfru blokowego.
- Funkcje encrypt_folder i decrypt_folder rekurencyjnie szyfrują i deszyfrują wszystkie pliki i foldery w folderze wejściowym i zapisują wynik do folderu wyjściowego.
- W kodzie jest również użyte Padding.pad do dopasowania długości danych wejściowych do wymaganej długości bloku AES.

# 2. Dokumentacja:
encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024)
Szyfruje pojedynczy plik.
Key: Klucz szyfrujący.
in_filename: Ścieżka do pliku wejściowego.
out_filename: Ścieżka do pliku wyjściowego. Domyślnie jest to in_filename + '.enc'.
chunksize: Rozmiar danych do wczytywania w jednej iteracji.

decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024)
Deszyfruje pojedynczy plik.
Key: Klucz deszyfrujący.
in_filename: Ścieżka do pliku wejściowego.
out_filename: Ścieżka do pliku wyjściowego. Domyślnie jest to in_filename bez '.enc'.
chunksize: Rozmiar danych do wczytywania w jednej iteracji.

encrypt_folder(key, in_folder, out_folder=None)
Szyfruje wszystkie pliki i foldery w folderze wejściowym i zapisuje wynik do folderu wyjściowego.
Key: Klucz szyfrujący.
in_folder: Ścieżka do folderu wejściowego.
out_folder: Ścieżka do folderu wyjściowego. Domyślnie jest to in_folder + '_encrypted'.

decrypt_folder(key, in_folder, out_folder=None)
Deszyfruje wszystkie pliki i foldery w folderze wejściowym i zapisuje wynik do folderu wyjściowego.
Key: Klucz deszyfrujący.
in_folder: Ścieżka do folderu wejściowego.
out_folder: Ścieżka do folderu wyjściowego. Domyślnie jest to in_folder bez '_encrypted'.