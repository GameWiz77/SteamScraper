import requests
from bs4 import BeautifulSoup
from googlesearch import search
import PySimpleGUI as sg
from PIL import Image
from urllib.request import urlopen
import time


themelist = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey', 'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']

theme = 'DarkGray12'
layouttheme = [[sg.Listbox(values=themelist, enable_events=True, size=(30, 6), key='list')]]

menu_def = [['File', ['Open', 'Save', 'Exit',]],
              ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
              ['Settings', ['Theme'],]]

sg.theme(theme)   
# All the stuff inside your window.
layout = [  [sg.Menu(menu_def, key='menu')],
  [sg.Text("""Welcome to Steam price checker - 
    Type the Game Title to begin or
    Press Quit to Quit""")],
            [sg.Text('Enter Game Title'), sg.InputText(do_not_clear=False, key='title')],
            [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel'),] ]

# Create the Window
window = sg.Window('Steam Price Checker', layout)

def HenWindow():
  t = 0
  t = t + 1
  sg.theme(theme)
  layout[t] = [  [sg.Menu(menu_def, key='menu')],
  [sg.Text("""Welcome to Steam price checker - 
    Type the Game Title to begin or
    Press Quit to Quit""")],
            [sg.Text('Enter Game Title'), sg.InputText(do_not_clear=False, key='title')],
            [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel'),] ]
  window3 = sg.Window('Steam Price Checker', layout[t])
  event, values = window3.read() 

event, values = window.read()
while True:
  if event == 'Theme':
    window.close()
    windowtheme = sg.Window('Theme Browser', layouttheme)
    event, values = windowtheme.read()
    theme = (values['list'][0])
    HenWindow()
  if event == sg.WIN_CLOSED or event == 'Cancel':
    break
    window.close()
  if event in themelist:
    theme = (values['menu'])
    window.close()
    HenWindow()
    continue

  inputurl1 = (values['title'])
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

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()
    page = requests.get(tsm)
    soup = BeautifulSoup(page.content, "html.parser")
    try:
      try:
        results = soup.find(id="game_area_purchase")
        fesults = soup.find(id="appHubAppName")
        job_elements = results.find("div", class_="game_purchase_price price")
        cob_elements = fesults.find("div", class_="apphub_AppName")
        print(fesults.text, ":", job_elements.text.strip());
        Image.open("sample_image.png").save("sample1.png")
        
        layout2 = [ [sg.Text(fesults.text + ": " + job_elements.text.strip())],
                    [sg.Image("sample1.png")],
                    [sg.Button("Close", bind_return_key=True)]]
        window2 = sg.Window('Steam Price Checker', layout2,)
        event, values = window2.read()
        if event == sg.WIN_CLOSED or event == 'Close':
          window2.close()




      except AttributeError:
        result = soup.find(id="game_area_purchase")
        gesults = soup.find(id="appHubAppName")
        job_element = result.find("div", class_="discount_final_price")
        cob_elements = gesults.find("div", class_="apphub_AppName")
        print(gesults.text, ":", job_element.text.strip());
        window.close()
    except:
      print("No game found")


    def wpage():
      print(page.text)
  else:
    break

