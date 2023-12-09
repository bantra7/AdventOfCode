## AoC (Advent of code)

My solutions to [Advent of code](https://adventofcode.com/) puzzles.

For each day, you have 5 files:
* i.md - solution outputs of the day _(ex: 13.md)_
* i.txt - input of the day _(ex: 13.txt)_
* it.txt - test input of the day _(ex: 13t.md)_
* main_p1.py - script for part 1 
* main_p2.py - script for part 1

### Creating day folder

It works with [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html), a project generation templating module.


Run
```
# Install cookiecutter module
python -m pip install cookiecutter

# Generate for current day
python -m cookiecutter . -o 2023/ --no-input

# Generate for another day
python -m cookiecutter . -o 2023/
```

### Run script for solutions
Run
```
# For part 1
python main_p1.py

# For part 2
python main_p2.py
```