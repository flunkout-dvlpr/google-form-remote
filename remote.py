from gpiozero import Button
import googleForm 

hotSwitch = Button(26)
clockInOut = Button(19)
julio = Button(16)
miguel = Button(20)
pedro = Button(21)

while True:
  if True:
    if clockInOut.value is True:
      if julio.is_pressed:
        print('Julio clockIn')
      if miguel.is_pressed:
        print('Miguel clockIn')
      if pedro.is_pressed:
        print('Pedro clockIn')
      print('idle')

    elif clockInOut.value is False:
      #googleForm.submitClockOut('Julio')
      if julio.is_pressed:
        print('Julio clockOut')
      if miguel.is_pressed:
        print('Miguel clockOut')
      if pedro.is_pressed:
        print('Pedro clockOut')
      print('idle')

