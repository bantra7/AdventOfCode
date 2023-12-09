def main():
    with open('{{cookiecutter.daynumber}}.txt') as f:
        data = f.read().split('\n')


if __name__ == '__main__':
    main()
