#Código para enviar mensajes a whatsapp

#importación de librerias
import pyautogui as pgLibreria, webbrowser as ventanaWeb, time as tiempo
#Donde se abrira el programa y a quien enviara el mensaje
ventanaWeb.open("https://web.whatsapp.com/send?phone=+525523703521")
#Tiempo de espera del programa para enviar los mensajes
tiempo.sleep(5)

#For de cuantas veces se embiara el código
for x in range(15):
    pgLibreria.write("El dominio total xd")#mensaje enviado
    pgLibreria.press('enter')#Hace alusión al boton de enviar
    pass