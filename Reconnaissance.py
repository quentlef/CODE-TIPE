import cv2
import matplotlib.pyplot as plt

# Chemin de ta vidéo
video_path = r'E:\Medal\Clips\Arma 3\test.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    exit()

# Lire et afficher 1 seule frame pour test
ret, frame = cap.read()
if ret:
    # Convertir BGR -> RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Afficher avec matplotlib
    plt.imshow(frame_rgb)
    plt.axis('off')
    plt.show()
else:
    print("Erreur de lecture")

cap.release()

