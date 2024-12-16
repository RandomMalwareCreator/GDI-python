import ctypes
import random
import time
from win32api import GetSystemMetrics
from win32gui import GetDC, ReleaseDC
from win32con import SRCCOPY, NOTSRCCOPY
from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard

# Função de BitBlt
def BitBlt(hdcDest, xDest, yDest, width, height, hdcSrc, xSrc, ySrc, rop):
    ctypes.windll.gdi32.BitBlt(hdcDest, xDest, yDest, width, height, hdcSrc, xSrc, ySrc, rop)

# Obtendo as dimensões da tela
w = GetSystemMetrics(0)  # Largura da tela
h = GetSystemMetrics(1)  # Altura da tela

while True:
    # Obtendo o contexto de dispositivo (DC)
    hdc = GetDC(0)  # 0 representa o DC da tela inteira

    # Gerando um valor aleatório para a posição X
    x = random.randint(0, w)
    
    # Fazendo o BitBlt (cópia de uma parte da tela para outra)
    BitBlt(hdc, x, 1, 10, h, hdc, x, 0, NOTSRCCOPY)

    # Atraso para simular o comportamento de "Sleep(2)" no C++
    time.sleep(0.002)  # Sleep em segundos, 0.002 segundos = 2 ms

    # Liberando o contexto de dispositivo
    ReleaseDC(0, hdc)
