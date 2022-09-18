# How to Run BTruong's Final Project

This project is meant to compile credit card, bank, and any transactional statements
across various issuers into a single composed `.csv` file.

To run this project, follow the following steps:

## Step 1. Prepare Directory of Statements

1. Log onto the WebPage platform for one of your credit card/bank issuers.
2. Download the transactional statement across your desired period as a `.csv` file.
   1. The file should be downloaded to a directory that only contains any statements `.csv` files that you wish to compile.
   2. The filename will be used as a label of the origin issuer. Because of this, it is recommended that you use the issuer's name as the file name.
      1. For example: A statement from Discover should be downloaded as `discover.csv`
   3. Repeat the above steps for all desired transactional statements.
   4. Record or Copy the path to the directory.
      1. For example: `some/path/to/all_statements/`

## Step 2. Run the program

1. Open Terminal
2. Ensure Python 3.7+ is installed.
3. Navigate to the directory of this final project.
4. Call the following to run the program
```console
python main.py
```
5. The terminal will prompt the user for the directory path:
```console
Please provide the directory path, to the directory holding all statements that you'd like to be compiled:
```
6. Enter directory path recorded/copied in Step 1.
7. Statement book will be outputted in the same directory.

# To run the provided example:
1. Open Terminal
2. Ensure Python 3.7+ is installed.
3. Navigate to the directory of this final project.
4. Call the following to run the program
```console
python main.py
```
5. The terminal will prompt the user for the directory path:
```console
Please provide the directory path, to the directory holding all statements that you'd like to be compiled:
```
6. Pass in the file path to `./test_files/statement/` i.e. `C:\Users\user\PycharmProjects\cs_521\btruong_final_project\test_files\statement`
7. Examine the outputted statement book in the `./test_files/statement/` directory, with filename `statement_book_{date}.csv`


# To Run Unit Tests:

1. Open Terminal
2. Ensure Python 3.7+ is installed.
3. Navigate to the directory of this final project.
4. Call the following to run the program
```console
python test.py
```