"""" 
This is the SteamScraper Documentation
Any code referenced in this document will have a matching #comment in the main.py file.

The purpose of SteamScraper is to be able to easily go out on the the internet and scrape the prices of various items. In the case of this demo it is used to find the price of video games on the computer website Steam. This code is largely scalable and adaptable with only a few code changes, which will be described in this Documentation

// #Libraries
This code segment denotes all of the libraries and outside code used.
This section also has the imports necessary to run.

// #Defenitions
This code segment is one of the most important sections as it holds all of the variables that will be used later on in the code.

imagelist[] -  Holds all of the URLS for the images that will be used.

theme - Holds the theme used by all of the GUI elements; This can be changed to any of the themes listed on the PySimpleGUI website. 

inputlist[] - Holds all of the user inputed text.

menu_def - This defines the layout of the menu. This is not used in this build.

sg.theme() - This sets the theme of GUI elements to 'theme'

layout - This defines the layout of the main GUI element. The various elements of the UI defined in here, with self explanatory names. 

window - This initializes the UI element defined by 'layout'

endgrid() - This defines a def to display end credits. This is not used in this build.

// #Main Loop
This code segment is the main loop of the program. This is only broken when the user presses cancel on the main GUI element or the window is closed to said element.

event, values - This waits for and records the event that is caused by the main GUI element.

# Close - This section, when it recieves a 'Cancel' event or when the window is closed, breaks the loop and prints the imageslist[] and inputlist[]

# Previous - This section takes the previous values or input from the user and uses that instead of a new string input

# Ok - This section takes the 'event, values' input and records it as 'inputurl1'. This section also adds the 'event, values' to inputlist[]

# Quit & - This 
