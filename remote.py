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
      #googleForm.submitClockIn('Julio')
      print('clockIn')

    elif clockInOut.value is False:
      #googleForm.submitClockOut('Julio')
      print('clockOut')
