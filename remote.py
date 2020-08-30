from gpiozero import Button


hotSwitch = Button(26)

while True:
  if hotSwitch.is_pressed:
    print('On')