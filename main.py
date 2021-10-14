import requests
from bs4 import BeautifulSoup
from googlesearch import search
import PySimpleGUI as sg
from PIL import Image
from urllib.request import urlopen
import time


t = -1
imagelist = []
theme = 'DarkGray12'
inputlist = []
menu_def = [['File', ['Open', 'Save', 'Exit',]],
              ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
              ['Settings', ['Theme'],]]

sg.theme(theme)   
# All the stuff inside your window.
layout = [[sg.Text("""Welcome to Steam price checker - 
    Type the Game Title to begin or
    Press Quit to Quit""")],
            [sg.Text('Enter Game Title'), sg.InputText(do_not_clear=False, key='title')],
            [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel'), sg.Button('Previous')] ]

# Create the Window
window = sg.Window('Steam Price Checker', layout)

def endgrid():
  count = 0
  zount = ''
  tount = ''    
  while count < len(inputlist): ###########convert count to string and file open to 'count'
    tount = requests.get(imagelist[count])
    print(tount)
    file = open('zount.png', "wb")
    file.write(tount.content)
    file.close()
    Image.open("zount.png").save("zountz.png")
    endgrid = [[sg.Image('zountz.png')],]
    endlayout = sg.Window('Steam Price Checker', endgrid)
    event, values = endlayout.read()
    count = count + 1
    print('test')



while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Cancel':
    print(inputlist)
    print(imagelist)
    window.close()
    endgrid()
    break
  if event == 'Previous':
    inputurl1 = inputlist[t]
  if event == 'Ok':
    t = t + 1
    inputurl1 = (values['title'])
    inputlist.append(inputurl1)
  print(inputurl1)
  if inputurl1 != ("quit") and inputurl1 != ("Open"):
    for url in search(inputurl1 + 'steam', stop=1):
        inputurl = url
    tsm = inputurl;
    htmldata = urlopen(tsm)
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    for item in images:
      x = (item['src'])
      index = x.find("header.jpg")
      if index > 0:
        break
    response = requests.get(x)
    print(x)
    imagelist.append(x)

    file = open("image1.png", "wb")
    file.write(response.content)
    file.close()
    page = requests.get(tsm)
    soup = BeautifulSoup(page.content, "html.parser")
    try:
      try:
        gamearea = soup.find(id="game_area_purchase")
        gamename = soup.find(id="appHubAppName")
        gamecost = gamearea.find("div", class_="game_purchase_price price")
        gamenamewrite = gamename.find("div", class_="apphub_AppName")
        print(gamename.text, ":", gamecost.text.strip());
        Image.open("image1.png").save("sample1.png")
        
        layout2 = [ [sg.Text(gamename.text + ": " + gamecost.text.strip())],
                    [sg.Image("sample1.png")],
                    [sg.Button("Close", bind_return_key=True)]]
        window2 = sg.Window('Steam Price Checker', layout2,)
        event, values = window2.read()
        if event == sg.WIN_CLOSED or event == 'Close':
          window2.close()




      except AttributeError:
        gamearea = soup.find(id="game_area_purchase")
        gamename = soup.find(id="appHubAppName")
        gamecost = gamearea.find("div", class_="discount_final_price")
        gamenamewrite = gamename.find("div", class_="apphub_AppName")
        print(gamename.text, ":", gamecost.text.strip());
        window.close()
    except:
      print("No game found")


    def wpage():
      print(page.text)
  else:
    break

