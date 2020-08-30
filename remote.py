from gpiozero import Button
import googleForm 

hotSwitch = Button(26)
clockInOut = Buton(19)
julio = Buton(16)
miguel = Buton(20)
pedro = Buton(21)

while True:
  if True:
    if clockInOut.value is True:
      #googleForm.submitClockIn('Julio')
      print('clockIn')

    elif clockInOut.value is False:
      #googleForm.submitClockOut('Julio')
      print('clockOut')
