## AoC (Advent of code)

My solutions to [Advent of code](https://adventofcode.com/) puzzles.

For each day, you have 5 files:
* **_i_**.md - solution outputs of the day
* **_i_**.txt - input of the day
* **_it_**.txt - test input of the day
* main_p1.py - script for part 1
* main_p2.py - script for part 1

### Creating day folder

It works with [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html), a project generation templating module.


Run
```
python -m pip install cookiecutter
python -m cookiecutter folder_day_template -o 2023/
```

### Run script for solutions
Run
```
# For part 1
python main_p1.py

# For part 2
python main_p2.py
```