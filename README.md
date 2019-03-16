# morsepy
Progetto realizzato per la materia Reti di Calcolatori.

Comunicazione tra due moduli ESP8266 e uno schermo i2c_lcd (kit Arduino), basata su MQTT come protocollo di comunicazione.

Da una parte, un bottone fisico consente l'immissione della "stringa" in morse, che viene codificata attraverso lo script morse.py e verrà inviata all'altro modulo, che decodificherà il messaggio e lo mostrerà sul display.

Pressione rapida -> punto (.)
Pressione leggermente prolungata -> trattino (-)
Pressione > 1,00s -> reset
