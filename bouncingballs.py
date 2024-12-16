import win32gui
import win32con
import win32api
import random
import time

# Função para desenhar na tela sem uma janela visível
def draw_circle():
    # Inicializando variáveis de movimento
    x, y = 10, 10
    signX, signY = 1, 1
    incrementor = 10

    while True:
        # Obtendo o contexto de dispositivo (DC) para a tela inteira
        hdc = win32gui.GetDC(0)  # 0 refere-se à tela inteira

        # Movendo o círculo
        x += incrementor * signX
        y += incrementor * signY

        # Definindo as coordenadas para a elipse
        top_x, top_y = x, y
        bottom_x, bottom_y = x + 100, y + 100

        # Criando uma cor aleatória para o círculo
        brush = win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        win32gui.SelectObject(hdc, brush)

        # Desenhando a elipse (círculo) na tela
        win32gui.Ellipse(hdc, top_x, top_y, bottom_x, bottom_y)

        # Detecção de bordas para mover o círculo
        if y >= win32api.GetSystemMetrics(1):  # Altura da tela
            signY = -1  # Inverte o movimento no eixo Y
        if x >= win32api.GetSystemMetrics(0):  # Largura da tela
            signX = -1  # Inverte o movimento no eixo X
        if y <= 0:
            signY = 1  # Inverte o movimento no eixo Y
        if x <= 0:
            signX = 1  # Inverte o movimento no eixo X

        # Espera de 10 milissegundos antes de atualizar a tela
        time.sleep(0.01)

        # Limpeza do contexto de dispositivo (para evitar borrões de desenho)
        win32gui.DeleteObject(brush)
        win32gui.ReleaseDC(0, hdc)

# Chama a função para iniciar o movimento do círculo
draw_circle()
