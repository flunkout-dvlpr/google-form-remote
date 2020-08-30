from gpiozero import Button
import googleForm 

hotSwitch = Button(26)
clockInOut = Button(19)
julio = Button(16)
miguel = Button(20)
pedro = Button(21)

while hotSwitch.is_active == True:
  print('HotSwitch')
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


