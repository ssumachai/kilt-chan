import os

from black import main

if __name__ == "__main__":
    # Formatting
    print("-- Formatting... --")
    try:
        print(main(["main.py", "cogs", "db", "utils", "service", "fetcher"]))
    except:
        pass

    print("-- Sorting imports... --")
    os.system("isort main.py cogs db utils service fetcher --profile black")

    # Validating
    print("-- Validating formatting. --")

    print("-- Checking formatting... --")
    os.system("pyright")

    print("-- Checking imports... --")
    os.system("isort -c main.py cogs db utils --profile black")

    print("Done!")
