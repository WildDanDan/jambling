import random
import pyautogui
import time

point_dict = dict[str, tuple[float, float]]

# Disable threshold for cursor instantly moving to its destination
pyautogui.MINIMUM_DURATION = 0.001
pyautogui.MINIMUM_SLEEP = 0.001
pyautogui.FAILSAFE = False

def bounded_random(a: float, b: float) -> float:
  """
  Generate a random float number within the range [a, b).

  Parameters:
  a (float): The lower bound of the range.
  b (float): The upper bound of the range.
  """
  return a + (b - a) * random.random()

def move(x1: float, y1: float) -> None:
  """
  Moves the mouse cursor to the specified coordinates with a slight random offset.

  Args:
    x1 (float): The x-coordinate of the target position.
    y1 (float): The y-coordinate of the target position.
  """

  pyautogui.moveTo(
    x1 + bounded_random(-2, 3),
    y1 + bounded_random(-2, 3),
    duration=bounded_random(0.07, 0.09),
    tween=pyautogui.easeOutQuad
  )

def click_at(p: tuple[float, float], right=False):
  """
  Moves the mouse cursor to the specified coordinates (with a slight random
  offset) and performs a click action.

  Args:
    x     (float): x-coordinate of the target location.
    y     (float): y-coordinate of the target location.
    right (float): Right click? (default: left)
  """

  x, y = p
  click = pyautogui.click
  if (right): click = pyautogui.rightClick

  move(x, y)
  time.sleep(0.09)

  click(duration=bounded_random(0.06, 0.08))
  time.sleep(0.09)

def ctrl_click(p: tuple[float, float]) -> None:
  pyautogui.keyDown("ctrlleft")
  click_at(p)
  pyautogui.keyUp("ctrlleft")
  