from umqtt.simple import MQTTClient
from machine import Pin, I2C
import machine
import ubinascii
import network
import time
from esp8266_i2c_lcd import I2cLcd

 
# CONNESSIONE WIFI
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('Connecting to network...')
  sta_if.active(True)
  sta_if.connect('Raspispot', 'raspberrypi')
  while not sta_if.isconnected():
    pass
print(sta_if.ifconfig())

    
CONFIG = {
     # TUTTI I DETTAGLI DEL CLIENT MQTT
     "MQTT_BROKER": "54.152.234.238",
     "USER": "licfekew",
     "PASSWORD": "77wmRx9hIbaw",
     "PORT": 13017,
     "TOPIC": b"test",
     # IDENTIFICATIVO UNIVOCO CHIP (ESP8266)
     "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}
 
# METODO PER VISUALIZZARE IL MESSAGGIO SUL DISPLAY
def onDisplay(topic, msg):
  i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
  #i2c.scan()
  lcd = I2cLcd(i2c,63, 2, 16)
  lcd.clear()
  lcd.putstr(msg.decode('ascii'))   
  time.sleep(5)
  lcd.clear()
 
 
def listen():
  # CREA UN' ISTANZA DEL CLIENT MQTT
  client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
  # CALLBACK PER I MESSAGGI VISUALIZZATI SUL DISPLAY
  client.set_callback(onDisplay)
  client.connect()
  #client.publish("test", "ESP8266 is Connected")
  client.subscribe(CONFIG['TOPIC'])
  print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))

  try:
      while True:
        msg = client.wait_msg()
        msg = (client.check_msg())
  finally:
    client.disconnect()

listen()

