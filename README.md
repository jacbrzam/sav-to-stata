# sav-to-stata
Python script that transforms SPSS data files (.sav) into Stata data files (.dta).
Although Stata supports importing SPSS files, the value labels names get renamed to "labels1", "labels2", and so on.
I wrote this code so that the value labels retain their name.

## Usage
1. Run the script, a file selection window should open.
2. Select the SPSS .sav file.
3. The script should output a .dta file with the same name as the SPSS file (minus the sav extension).

## Troubleshooting
I wrote this code using the following packages and versions:
- pandas (2.2.1)
- pyreadstat (1.2.7)
- tkinter (8.6.13)
