nazwa_pliku = input("Podaj nazwę pliku (z rozszerzeniem): ").strip()

if nazwa_pliku.lower().endswith(('.xls', '.xlsx')):
    print(" To jest plik arkusza Excel.")
else:
    print(" To NIE jest plik arkusza Excel.")


# --- KOMENTARZ ---
# Metoda 'endswith()' jest wbudowaną metodą typu 'str' (łańcucha znaków) w Pythonie.
# Sprawdza, czy dany tekst (łańcuch) kończy się określonym ciągiem znaków.
#
# Składnia:
#   napis.endswith(suffix)
#   napis.endswith((suffix1, suffix2, ...))  # można podać kilka rozszerzeń naraz
#
# Zwraca:
#   True  → jeśli napis kończy się podanym sufiksem,
#   False → w przeciwnym razie.
#
# Przykład:
#   "raport.xlsx".endswith(".xlsx") → True
#   "dane.csv".endswith(".xlsx")   → False
#
# Najczęstsze rozszerzenia plików Excela to:
#   .xls  → starszy format (Excel 97–2003)
#   .xlsx → nowszy format (od Excel 2007 wzwyż)
