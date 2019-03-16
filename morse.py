import machine
import time
led = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(5, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
count = 0
msg = ""
while True:
  while not button.value():
    if count==0:
      toc2 = time.ticks_ms()
      tic = time.ticks_ms()
      count=1
    time.sleep_ms(1)
    led.value(1)
    if button.value():
      led.value(0)
      toc = time.ticks_ms()
      if len(msg) > 0:
        if (toc2-tic2) >400 and (toc2-tic2) <700:
          msg= msg + "2"
        else:
          if (toc2-tic2) >1000:
            msg=msg + "3"
      count=0
      if (toc - tic) < 200:
        msg = msg + "0"
      else:
        if (toc - tic) > 200 and (toc - tic) < 3000:
          msg = msg + "1"
        else:
          led2.value(1)
          time.sleep_ms(500)
          led2.value(0)
          time.sleep_ms(600)
          led2.value(1)
          time.sleep_ms(500)
          led2.value(0)
          time.sleep_ms(600)
          led2.value(1)
          time.sleep_ms(600)
          led2.value(0)
          msg=""
          break
      print (msg)
      tic2 = time.ticks_ms()
  if len(msg)>0 and (time.ticks_ms()-toc2)>3000:
    led.value(0)
    print("fine")
    break



