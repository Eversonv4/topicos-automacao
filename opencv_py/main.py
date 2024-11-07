# python -m venv venv
# pip freeze > requirements.txt
import cv2 as opencv
import matplotlib.pyplot as plt


# ---------- OpenCV ----------------

imagem_original = opencv.imread('ursinho.jpg')

# converter de BGR para RGB
imagem_rgb = opencv.cvtColor(imagem_original, opencv.COLOR_BGR2RGB)

# aplicar filtro de cinza
imagem_cinza = opencv.cvtColor(imagem_original, opencv.COLOR_BGR2GRAY)

# aplicar filtro de blur
imagem_desfocada = opencv.GaussianBlur(imagem_rgb, (15, 15), 0)

# detecção de bordas
imagem_bordas = opencv.Canny(imagem_cinza, 100, 200)

# achar e aplicar contornos na sua imagem
contornos, _ = opencv.findContours(imagem_bordas, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
imagem_contornos = imagem_rgb.copy()
opencv.drawContours(imagem_contornos, contornos, -1, (255, 0, 0), 2)

# --------- end Opencv ------------


# ------- Matplotlib --------------

# criando grid para mostrar as imagens
plt.figure(figsize=(12, 6))

# a imagem original
plt.subplot(2, 3, 1)
plt.imshow(imagem_rgb)
plt.title("Original")
plt.axis("off")

# a imagem com tons de cinza
plt.subplot(2, 3, 2)
plt.imshow(imagem_cinza, cmap='gray')
plt.title("Tons de Cinza")
plt.axis("off")

# filtro de desfoque
plt.subplot(2, 3, 3)
plt.imshow(imagem_desfocada)
plt.title("Desfoque")
plt.axis("off")

# detecção de bordas
plt.subplot(2, 3, 4)
plt.imshow(imagem_bordas, cmap='gray')
plt.title("Bordas (Canny)")
plt.axis("off")

# mostrar contornos
plt.subplot(2, 3, 5)
plt.imshow(imagem_contornos)
plt.title("Contornos")
plt.axis("off")

# mostrar tudo
plt.tight_layout()
plt.show()

# --------- end Matplotlib ------------