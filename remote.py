from gpiozero import Button


hotSwitch = Button()

while True:
  if hotSwitch.is_pressed:
    print('On')