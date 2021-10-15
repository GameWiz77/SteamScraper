"""" 
This is the SteamScraper Documentation
Any code referenced in this document will have a matching #comment in the main.py file.

The purpose of SteamScraper is to be able to easily go out on the the internet and scrape the prices of various items. In the case of this demo it is used to find the price of video games on the computer website Steam. This code is largely scalable and adaptable with only a few code changes, which will be described in this Documentation

// How to use - FOR THIS APPLICATION TO WORK, THE USER WILL NEED TO INSTALL 4 LIBARIES, BS4, BEAUTIFULSOUP4, PYSIMPLEGUI, AND GOOGLE BY MARIO VILAS

The end user will run the program, a UI will appear. The user than clicks the input box,types the name of a game (or other item if the code has been adapted), and a second UI element will appear showing the front picture of the game, the official name of the game, and its price or discounted price.

I recommended if the end user is not familiar with the names of game, that they visit https://store.steampowered.com/ to test the code

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

# Quit & - This section activates the main code, if the user inputs 'quit' or 'Open' the program will close.

# GOOGLE - This section of the code is very important as this section will be the one needed to be modified when changing what item is to be looked up. 
'for url in search(inputurl1 + 'steam', stop=1)' - This section combines the user input with a pre-determined key-word, in this case it combines the user input with 'steam', an online video game store, to look for that games specific page. That pages URL is then written to the 'tsm' variable. To change what type of items you want to look up, you would need to change the 'steam' key-word to something else, Home Depot, CMC Milling, Lowe's, etc. The stop segment specifies how many URLS the command will find, in this case it will only find one.

# BS4 Def - This section of the code recieves the URL from the # GOOGLE segment and parses any data from the website with the HTML code <img> and stores it in image1.png.

# BS4 Content - This section of the code takes the predefined 'tsm' variable, which hold the page URL, and runs it through Beautiful Soup. Beautiful Soup is an HTML data parser, here we tell it to look for two things, the game name (appHubAppName), and the game price (game_purchase_price price). This is important as to adapt this code to a differnt item type, one would have to find the HTML tags used by other sites. As this can easily be done I wont explain how to do it here. These two are then stripped of unnecessary information and text. 

^This code is seperated into two exceptions, if Beautiful Soup cannot find the default price of an item, it will fall into the next exception where it will try to find the discounted price, if it cannot find a discounted price, it will finally land on the print statement ('No game found'). 

"""
