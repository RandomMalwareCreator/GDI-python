import time
import win32gui
import win32api
import win32con
import win32ui

def main():
    # Obtém as dimensões da tela
    screen_width = win32api.GetSystemMetrics(0)  # Largura da tela
    screen_height = win32api.GetSystemMetrics(1)  # Altura da tela

    # Loop infinito para realizar a inversão
    while True:
        # Obtém o contexto de dispositivo (DC) da tela
        hdc = win32gui.GetDC(0)
        
        # Realiza o efeito de inversão utilizando PatBlt (PATINVERT)
        win32gui.PatBlt(hdc, 0, 0, screen_width, screen_height, win32con.PATINVERT)
        
        # Aguarda 100ms antes de realizar a próxima inversão
        time.sleep(0.1)
        
        # Libera o contexto de dispositivo (DC)
        win32gui.ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()
