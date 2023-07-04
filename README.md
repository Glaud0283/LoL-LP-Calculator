# About The Project

### Disclamer
###### This project is **not any kind of official program provided by Riot Games**, it is a basic tool for only and only LP calculations. It does not have any background process, when you close the window it is totally terminated. **It is not  any kind of script or illegal program that gives competitive advantage.** Basically it does not have any affect to the game. 
###### The data given are approximate values calculated by simple math, not by using Riot's MMR system. So do not expect precise values.
###### **It is only a project so any of your issues are not my problem.** Don't be a dick.

### Why?
###### In competitive games like League of Legends, everyone tried to calculate how many wins they need to reach their dream rank, at least once. But it is not as easy as pie if you need a detailed result. This program calculates your Net LP gain and number of matches you need by collecting your account stats and basic algebra.

### Files
###### Project contains only 2 files, a python script and a compiled `.exe` file. Python script uses `PySimpleGUI` library to form a windows application, and process the data given, which will be explained below. Executable file is a compressed file with all libraries, images and files. 

### Using the app
###### Python script is published for educative purposes and open source. So if you only need the program, you do not need to download script, just install the `.exe` and run it.



# Structure
###### This project contains 2 main parts:

### LoL Calculations
###### This part of program calculates the necessary and final data for calculations and returns a `dictionary` object.
###### `calculate_lp()` function returns the required LP value according to the data given. First it calculate rank to rank and then tier to tier (to lp if the rank provided is higher than master)
###### `calculate_matches()` function returns a dictionary that contains LP required, your account's net LP gain (a value with respect to your winrate, LP gain and loss), required matches to reach to target and required matches if you would win all matches wihout loses.

### User Interface
###### This part of program creates a UI and fill it with results from previous part.
###### Errors are handled and the user is warned by a popup screen
###### All colors in UI are official League of Legends brand colors. (For more imformation: https://brand.riotgames.com/en-us/league-of-legends/color/)

