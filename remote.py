from gpiozero import Button
import googleForm 

state = False
def toggle(state):
  print('Switch toggled')
  if state == False:
    state = True
  else:
    state = False

hotSwitch = Button(26)
clockInOut = Button(19)
julio = Button(16)
miguel = Button(20)
pedro = Button(21)
while True:
  if clockInOut.is_pressed:
    toggle(state)
  while hotSwitch.is_active == True:
    print('Current state', state)
# if clockInOut.is_active == True and julio.is_pressed:
#   print('Julio clockIn')
# if clockInOut.is_active == True and miguel.is_pressed:
#   print('Miguel clockIn')
# if clockInOut.is_active == True and pedro.is_pressed:
#   print('Pedro clockIn')

# if clockInOut.is_active == False and julio.is_pressed:
#   print('Julio clockIn')
# if clockInOut.is_active == False and miguel.is_pressed:
#   print('Miguel clockIn')
# if clockInOut.is_active == False and pedro.is_pressed:
#   print('Pedro clockIn')


