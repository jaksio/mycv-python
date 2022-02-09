# Projekt Sudoku GUI + solver

Sudoku GUI pozwala na grę w sudoku za pomocą klawiatury i myszki. Po uruchomieniu programu sudoku.py pole można wybrać za pomocą lewego przycisku myszy. Po podświetleniu obramówki pola na czerwono możliwe jest wpisanie dowolnej cyfry zgodnej z regułami sudoku. Można cofnąć każdą wpisaną przez użytkownika liczbę za pomocą klawisza backspace.

Sudoku solver przedstawia algorytm rozwiązujący losowe sudoku. Działanie tego algorytmu przedstawiono graficznie w pliku solver.py. Po uruchomieniu programu po naciśnięciu lewego przycisku myszy program rozpocznie rozwiązywanie sudoku.

Po pobraniu projekt można uruchomić instalując wymagane elementy. W folderze Sudoku-GUI-automatic-solver za pomocą komend.
>>> source .venv/bin/activate
>>> pip install .
>>> pip install -r ./requirements_dev.txt

Uruchomienie GUI 
>>> python3 src/sudokusolver/sudoku.py 

Uruchomienie algorytmu rozwiązującego:
>>> python3 src/sudokusolver/solver.py 

W projekcie wykonano testy za pomocą mypy, flake8, pytest.
Uruchomić je można w folderze głównym za pomocą:
>>> mypy src
>>> flake8 src
>>> pytest

