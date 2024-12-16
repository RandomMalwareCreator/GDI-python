import ctypes
import random
import time
from win32api import GetSystemMetrics
from win32con import SRCCOPY, SRCAND
from win32gui import GetDC, ReleaseDC, GetDesktopWindow
from win32con import HWND_DESKTOP

# Função para realizar o BitBlt
def bitblt(hdcDest, nXDest, nYDest, nWidth, nHeight, hdcSource, nXSrc, nYSrc, dwRop):
    gdi32 = ctypes.windll.gdi32
    return gdi32.BitBlt(hdcDest, nXDest, nYDest, nWidth, nHeight, hdcSource, nXSrc, nYSrc, dwRop)

# Obter as dimensões da tela
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

# Obter o contexto de dispositivo (DC) da tela
hdc = GetDC(HWND_DESKTOP)

# Loop infinito
try:
    while True:
        # Gerar coordenadas randômicas para a origem e destino
        x1 = random.randint(0, screen_width)
        y1 = random.randint(0, screen_height)
        x2 = random.randint(0, screen_width)
        y2 = random.randint(0, screen_height)
        
        # Realizar a operação BitBlt com a operação SRCAND
        bitblt(hdc, x1, y1, screen_width, screen_height, hdc, x2, y2, SRCAND)

        # Pausa de 10ms
        time.sleep(0.01)
except KeyboardInterrupt:
    # Liberar o contexto de dispositivo (DC) ao final
    ReleaseDC(HWND_DESKTOP, hdc)
    print("Programa encerrado.")
