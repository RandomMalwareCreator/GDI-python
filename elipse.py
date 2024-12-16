import random
import time
import win32gui
import win32api
import win32con
import win32ui

def random_color():
    # Gera uma cor aleatória no formato RGB
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def draw_random_pie():
    # Obtém o HDC da tela
    hdc = win32gui.GetDC(0)

    # Obtém as dimensões da tela
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    # Cria uma cor aleatória
    color = random_color()
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))

    # Seleciona o pincel (brush)
    win32gui.SelectObject(hdc, brush)

    # Desenha um "pie" (parte de elipse) com coordenadas aleatórias
    x1 = random.randint(0, screen_width)
    y1 = random.randint(0, screen_height)
    x2 = random.randint(0, screen_width)
    y2 = random.randint(0, screen_height)
    x3 = random.randint(0, screen_width)
    y3 = random.randint(0, screen_height)
    x4 = random.randint(0, screen_width)
    y4 = random.randint(0, screen_height)

    # Desenha o "pie"
    win32gui.Pie(hdc, x1, y1, x2, y2, x3, y3, x4, y4)

    # Libera os recursos
    win32gui.DeleteObject(brush)
    win32gui.ReleaseDC(0, hdc)

def main():
    while True:
        draw_random_pie()
        time.sleep(0.01)  # Pausa de 10 milissegundos

if __name__ == "__main__":
    main()
