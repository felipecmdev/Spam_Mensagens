import random
import time
import pyautogui as py

time.sleep(5)

mensagens = ["oi", "salve", "idiota", "hora de virar heroi", "partiu", "ja ta pronto?", "caramba"]

for i in range (50):
    msg = random.choice(mensagens)  
    py.write(msg)
    py.press("enter")
    
    
    
