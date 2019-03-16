# morsepy
**Piccolo progetto per Reti di Calcolatori.**

Progetto realizzato per la materia Reti di Calcolatori: sono stati utilizzati:
#- 2 moduli ESP8266 con protocollo Wi-Fi;
#- 1 schermo i2c_lcd (kit Arduino)
#- MQTT come protocollo di comunicazione.

Un modulo, collegato ad un bottone fisico, permette l'inserimento del messaggio in morse, che verrà codificato ed inviato al secondo modulo, 
che riceverà il messaggio, lo decodificherà e lo mostrerà sul display.

*Un click -> dot (.)*

*Pressione non troppo prolungata -> dash (-)*

*Pressione maggiore di 1,0s -> reset*

