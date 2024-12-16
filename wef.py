import random
import time
import win32gui
import win32con
import win32api
import win32clipboard
from ctypes import windll

def ci(x, y, w, h):
    # Obter o contexto do dispositivo da tela
    hdc = win32gui.GetDC(0)
    # Criar uma região elíptica (máscara)
    hrgn = windll.gdi32.CreateEllipticRgn(x, y, w + x, h + y)
    # Selecionar a região na área de clip do hdc
    windll.gdi32.SelectClipRgn(hdc, hrgn)
    # Realizar o BitBlt (operar a cópia de pixels com a operação NOTSRCCOPY)
    windll.gdi32.BitBlt(hdc, x, y, w, h, hdc, x, y, win32con.NOTSRCCOPY)
    # Deletar o objeto de região (para liberar a memória)
    windll.gdi32.DeleteObject(hrgn)
    # Liberar o contexto de dispositivo
    win32gui.ReleaseDC(0, hdc)

def main():
    # Obter as dimensões da tela
    hwnd = win32gui.GetDesktopWindow()
    rect = win32gui.GetWindowRect(hwnd)
    w = rect[2] - rect[0] - 500  # Largura da tela menos um offset
    h = rect[3] - rect[1] - 500  # Altura da tela menos um offset

    while True:
        # Gerar coordenadas x e y aleatórias
        size = 1000
        x = random.randint(-size // 2, w + size // 2)
        y = random.randint(-size // 2, h + size // 2)

        # Criar círculos com tamanhos progressivamente maiores
        for i in range(0, size, 100):
            ci(x - i // 2, y - i // 2, i, i)
            time.sleep(0.025)  # Pausar por 25ms

if __name__ == "__main__":
    main()
