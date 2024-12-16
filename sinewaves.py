import math
import win32api
import win32gui
import win32con
import time
import threading

# Obtém o tamanho da tela (largura e altura)
SW = win32api.GetSystemMetrics(0)
SH = win32api.GetSystemMetrics(1)

# Função que simula a animação do seno
def sines():
    # Obtém o "device context" (DC) da tela
    hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetDC(hwnd)

    angle = 0
    while True:
        # Loop para criar o efeito de movimento
        for i in range(0, SH):  # Limita o loop até a altura da tela
            # Calcula o valor da seno para o movimento
            a = int(math.sin(angle) * 20)
            
            # Realiza a cópia dos pixels (simulando o efeito)
            win32gui.BitBlt(hdc, 0, i, SW, 1, hdc, a, i, win32con.SRCCOPY)
            
            # Atualiza o ângulo para o próximo ponto da curva seno
            angle += math.pi / 40

        # Dá um pequeno tempo de espera para não sobrecarregar a CPU
        time.sleep(0.01)

    # Libera o DC depois que o loop terminar (isso na prática não será alcançado porque o loop é infinito)
    win32gui.ReleaseDC(hwnd, hdc)

# Função para iniciar o thread da animação
def start_thread():
    thread = threading.Thread(target=sines)
    thread.daemon = True  # Garante que o thread termine quando o programa principal finalizar
    thread.start()

if __name__ == "__main__":
    start_thread()

    # Mantém o programa rodando
    while True:
        time.sleep(1)  # Impede o programa de terminar imediatamente
