import pyautogui as pgLibreria
import webbrowser as ventanaWeb
import time as tiempo

# Abre WhatsApp Web con el número de teléfono especificado
ventanaWeb.open("https://web.whatsapp.com/send?phone=+525637198658")

# Tiempo de espera para que WhatsApp Web cargue completamente
tiempo.sleep(20)  # Aumenté el tiempo de espera para asegurar que la página cargue

# Enviar el mensaje automáticamente 30 veces
for x in range(30):
    # Espera un poco antes de escribir el mensaje para asegurarse de que el chat esté listo
    tiempo.sleep(2)
    pgLibreria.write("¿Ya tienes tu respuesta? >:v")  # Mensaje enviado
    pgLibreria.press('enter')  # Hace alusión al botón de enviar

