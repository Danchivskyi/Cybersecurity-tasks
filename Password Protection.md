# Ochrona haseł: Aplikacja do bezpiecznego przechowywania haseł

# Wstęp 
Powyższy kod jest implementacją prostego menedżera haseł w języku Python. Aplikacja pozwala użytkownikowi na tworzenie konta z nazwą użytkownika i hasłem, a następnie logowanie się na swoje konto za pomocą tej samej nazwy użytkownika i hasła. Hasła są przechowywane w plikach tekstowych jako skróty sha256.

# Wyjaśnienie kodu
- hash_password: funkcja przyjmuje hasło jako argument i zwraca jego skrót sha256.
- create_account: funkcja tworzy nowe konto z podaną nazwą użytkownika i hasłem. Hasło jest skrótem sha256 i jest zapisywane w pliku o nazwie {username}.txt.
- login: funkcja przyjmuje nazwę użytkownika i hasło i sprawdza, czy istnieje plik z taką nazwą i czy skrót hasła z tego pliku jest taki sam jak skrót hasła podanego przez użytkownika. Funkcja zwraca True lub False w zależności od tego, czy uwierzytelnienie się powiodło się lub nie.
- main: funkcja uruchamia główną logikę aplikacji, w tym tworzenie konta i logowanie.

Kod jest oparty na funkcjach biblioteki 'hashlib' i 'getpass', które są używane do hashowania haseł i pobierania haseł bez wyświetlania ich na ekranie. Funkcja 'open' jest używana do otwierania i zapisywania plików tekstowych, a funkcja 'FileNotFoundError' jest używana do obsługi sytuacji, w których nie znaleziono pliku dla podanej nazwy użytkownika.