all:
	python3 main.py

#https://github.com/LouisBrunner/valgrind-macos
env_leaks_mac:
	brew tap LouisBrunner/valgrind
	brew install --HEAD LouisBrunner/valgrind/valgrind

