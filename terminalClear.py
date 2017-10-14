import os

def terminalClear():
	os.system('cls' if os.name == 'nt' else 'clear')