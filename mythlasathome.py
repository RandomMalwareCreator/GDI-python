import ctypes
import random
import time
import win32api
import win32con
import win32gui
import win32ui

# Função equivalente a GetSystemMetrics
def get_system_metrics(index):
    return ctypes.windll.user32.GetSystemMetrics(index)

# Função equivalente a Sleep (em milissegundos)
def sleep(ms):
    time.sleep(ms / 1000.0)

# Função principal que será executada pela thread
def thing6():
    while True:
        # Obter contexto de dispositivo para a tela
        hdc = win32gui.GetDC(0)
        hdc_mem = win32gui.CreateCompatibleDC(hdc)
        
        # Obter a resolução da tela
        sw = get_system_metrics(0)  # Largura da tela
        sh = get_system_metrics(1)  # Altura da tela
        
        # Criar uma bitmap compatível
        bm = win32gui.CreateCompatibleBitmap(hdc, sw, sh)
        win32gui.SelectObject(hdc_mem, bm)
        
        # Obter a posição da área de trabalho
        rect = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
        
        # Gerar pontos para o polígono
        inc3 = random.randint(0, 700)
        v = random.randint(0, 1)
        if v == 1:
            inc3 = -700
        inc3 += 1
        
        pt = [
            (rect[0] - inc3, rect[1] + inc3),
            (rect[2] - inc3, rect[1] - inc3),
            (rect[0] + inc3, rect[3] - inc3)
        ]
        
        # Realizar uma transferência de imagem usando um polígono
        win32gui.PlgBlt(hdc_mem, pt, hdc, rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1], 0, 0, 0)
        
        # Criar uma cor aleatória para o pincel
        brush = win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        win32gui.SelectObject(hdc, brush)
        
        # Copiar o conteúdo da memória para a tela
        win32gui.BitBlt(hdc, random.randint(0, 20), random.randint(0, 20), sw, sh, hdc_mem, random.randint(0, 20), random.randint(0, 20), 0x123456)
        
        # Limpeza dos objetos criados
        win32gui.DeleteObject(brush)
        win32gui.DeleteObject(hdc_mem)
        win32gui.DeleteObject(bm)
        win32gui.ReleaseDC(0, hdc)
        
        sleep(1)  # Atraso de 1 milissegundo

# Função para iniciar a execução da thread
def start_thread():
    import threading
    thread = threading.Thread(target=thing6)
    thread.daemon = True  # Para que a thread termine com o programa
    thread.start()
    thread.join()  # Manter o script em execução enquanto a thread está ativa

# Chamar a função para iniciar
if __name__ == "__main__":
    start_thread()
