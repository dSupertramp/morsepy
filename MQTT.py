# Import delle Librerie
from dht import DHT11
import machine
import time
from umqtt.robust import MQTTClient as client 
import network
import socket
# Routine di Callback
def messageReceived(topic,msg):
    print(">-- Message",(topic,msg)) 
    if msg == b"True":
        relayPin.value(1)
    elif msg == b"False":
        relayPin.value(0)
def morse():
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
      return msg



sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect('D-Link_DAP-JB', 'leonida93')
  while not sta_if.isconnected():
    pass
# Inizializzazione topic
topic = b"test/string" 
# Inizializzazione client MQTT
myClient = client("umqtt_client","54.152.234.238") 
#myClient.set_callback(messageReceived)
print (">-- MQTT connection")
myClient.connect()
myClient.subscribe(topic)
#while (userPin.value() == 1): 
#    # Novit脿 dal broker MQTT?
#    print (">-- MQTT polling")
    #if wlan.isconnected():
        #myClient.check_msg() 
    #else:
     #   reset() 
    # Misurazione
 
    # Pubblica sul broker MQTT
message = b"" + morse()
myClient.publish(topic,message) 
# Give us some sleep
time.sleep(10) 
