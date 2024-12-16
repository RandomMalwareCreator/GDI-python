import random
import time
import win32gui
import win32api
import win32con
import win32clipboard
import ctypes

# Função para obter a resolução da tela
def get_screen_size():
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

# Inicia o loop para fazer a manipulação da tela
while True:
    # Pega a resolução da tela
    screen_width, screen_height = get_screen_size()
    
    # Posições aleatórias para a área onde a operação será realizada
    x = random.randint(0, 222)
    y = random.randint(0, 222)
    
    # Pega o contexto de dispositivo (DC) da tela
    hdc = win32gui.GetDC(0)
    
    # Realiza a operação de BitBlt (copiar parte da tela para o DC)
    # Em C++ seria BitBlt(hdc, rand() % 222, rand() % 222, w, h, hdc, rand() % 222, rand() % 222, NOTSRCERASE);
    win32gui.BitBlt(hdc, x, y, screen_width, screen_height, hdc, random.randint(0, 222), random.randint(0, 222), win32con.SRCCOPY)

    # Aguarda 10 milissegundos (simula o Sleep)
    time.sleep(0.01)
    
    # Libera o contexto do dispositivo (DC)
    win32gui.ReleaseDC(0, hdc)
