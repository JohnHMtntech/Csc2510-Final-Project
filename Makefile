all: Blackjack

Blackjack:	graphics.py game.py card.py button.py
	python -m PyInstaller --onefile --name Blackjack --distpath . --add-data "assets/*.png;assets" -y --clean graphics.py game.py card.py button.py

get_librarys:
	python -m pip install pygame-ce
	python -m pip install pyinstaller

run:	graphics.py game.py card.py button.py
	Blackjack

clean:
ifeq ($(OS),Windows_NT)
	rmdir /s /q build
	del Blackjack.spec
	del Blackjack.exe
else
	rm -rf build
	rm Blackjack.spec
	rm Blackjack
endif