all:
	python3 main.py

leaks:
	python3 main.py leaks
#https://github.com/LouisBrunner/valgrind-macos
env_leaks_mac:
	brew tap LouisBrunner/valgrind
	brew install --HEAD LouisBrunner/valgrind/valgrind

env:
	pip3 install termcolor

fclean:
	rm -rf errors.txt
