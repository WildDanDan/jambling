import pyautogui
import keyboard
import os
import time
from kinematics import click_at
import math

# TURN OFF ITEM LABELS BEFORE RUNNING BOT

character_level = 90
net_gold_per_sale = 20_737
max_sales = (character_level * 10_000 // net_gold_per_sale) - 1
run_count = 8

# UNCOMMENT THE FOLLOWING 3 LINES TO CONTINUOUSLY PRINT YOUR CURSOR POSITION
# while True:
#   print(pyautogui.position())
#   time.sleep(1)

# Static UI element locations
config = {
  'rest_period': 1,
  'sell_count': max_sales,
  'hesitation': 0.07,
  'coords': {
    'sell_button': (952, 1110),
    'character_weapon_slot': (1390, 408),
    'vendor_weapon_position': (633, 820),
    'inventory_origin': (1360, 800),
    'close_vendor_btn': (1355, 1111), # close menu button
    'open_inventory_btn': (1151, 1297), # click inventory?
    'drop_gold_btn': (1500, 1114), # click gold drop icon
    'confirm_dialog_box': (1154, 860), # confirm gold drop
    'vendor_body': (1280, 569), # click vendor
    'trade_menu_option': (1274, 367), # click trade option
    'vendor_weapon_tab': (815, 200) # click tab
  }
}

def sell_weapon():
  click_at(config['coords']['sell_button'])
  
  # Click once to sell, once to select 'yes' on the confirmation dialogue
  (x, y) = config['coords']['character_weapon_slot']
  click_at((x, y))
  click_at((x, y+15))
  
def buy_weapon():
  click_at(config['coords']['vendor_weapon_position'], right=True)

def drop_gold():
  print('Dropping gold...')

  coordinates: dict[str, tuple[int, int]] = config['coords']

  click_at(coordinates['close_vendor_btn'])
  click_at(coordinates['open_inventory_btn'])
  click_at(coordinates['drop_gold_btn'])
  pyautogui.typewrite("9999999", interval=0.2)
  click_at(coordinates['confirm_dialog_box'])
  click_at(coordinates['close_vendor_btn'])
  click_at(coordinates['vendor_body'])
  click_at(coordinates['trade_menu_option'])
  click_at(coordinates['vendor_weapon_tab'])

def print_progress(run_progress: int):
    progress = math.ceil(100 * run_progress / config['sell_count'])
    print(f'{progress}%')

def abort(e):
  print("Aborting script!")
  os._exit(0)

keyboard.on_press_key('esc', abort)

print(f"Selling weapon {max_sales} times between gold drops...")

for current_run in range(run_count):
  print(f'Starting sell loop in {config["rest_period"]}s.')
  
  for sale_count in range(config['sell_count']):
    sell_weapon()
    buy_weapon()
    print_progress(sale_count)

  time.sleep(config["rest_period"])
  if (current_run != run_count - 1): drop_gold()
