from pathlib import Path
x = Path(".")
for i in x.iterdir():
    if i.is_file() and i.name == "hujjat.py":# "activate_the_latin_language_system.txt":
        print(i)