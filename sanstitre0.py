import cv2

# === 1. Charger la vidéo ===
cap = cv2.VideoCapture(r'E:\Medal\Clips\Arma 3\videoplayback.mp4')

# Vérifier si la vidéo est ouverte
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    exit()

# === 2. Obtenir les infos ===
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Résolution: {width}x{height}, FPS: {fps}")

'''
# === 3. Créer l'objet pour écrire la vidéo ===
# Codec : 'XVID' pour .avi ou 'mp4v' pour .mp4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(r'E:\Medal\Clips\Arma 3\test_modifie.mp4', fourcc, fps, (width, height))
'''

# === 4. Lire et modifier frame par frame ===
while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin de la vidéo.")
        break
    print(frame)
    # === Effet : convertir en niveaux de gris ===
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Remettre en 3 canaux pour pouvoir enregistrer
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # === 5. Ecrire la frame modifiée ===
    '''
    out.write(gray_bgr)
    '''
    # (Optionnel) afficher la frame en live
    cv2.imshow('Traitement', gray_bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === 6. Libérer les ressources ===
cap.release()
'''
out.release()
'''
cv2.destroyAllWindows()

print("✅ Vidéo modifiée enregistrée !")

