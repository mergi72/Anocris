from pynput.mouse import Button, Controller
import time


#cities = (( 965, 170), ( 965, 195), ( 965, 220), ( 965, 245))
cities = (( 965, 195), ( 965, 220), ( 965, 245))
icon_cities = (( 1470, 470))
mines = (( 435, 120), ( 535, 120), ( 640, 120), ( 895, 120))
abuttons= (( 1125, 585), ( 1125, 605), ( 745, 670), ( 745, 690))
mouse = Controller()


def move( poz):
    mouse.position = poz
   
    
def click():
    mouse.click( Button.left, 1)
    
    
def sec( s):
    time.sleep( s)
    
    
# ( 1380, 120)
mouse.position = ( 1380, 120)
sec( 1)
click()
for city in cities:
    for mine in mines:
        move( mine)
        click()
        sec( 1)
        for abutton in abuttons:
            move( abutton)
            click()
            sec( 1)
    mouse.position = icon_cities
    click()
    sec( 1)