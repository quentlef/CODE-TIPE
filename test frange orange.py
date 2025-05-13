import cv2

image_path = r'D:\Etudes Quentin\MP Jean Bart\TIPE\fringe.jpg'

image = cv2.imread(image_path)
'''
for i in range(len(image)):
    for j in range(len(image[i])):
        somme = 0
        if i>1 and j > 1 and i < len(image)-1 and j < len(image[2])-1 :
            for l in range(-1,2):
                for k in range(-1,2):
                    somme = somme + int(image[i+l][j+k][1])
            
            moyenne = somme/9
            print(moyenne)
            if image[i][j][2] < 175 and moyenne < 175:
                image[i][j] = [0,0,0]
        else:
            if image[i][j][2] < 150:
                image[i][j] = [0,0,0]
        
'''        

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Remettre en 3 canaux pour pouvoir enregistrer
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

for i in range(len(gray_bgr)):
    for j in range(len(gray_bgr[i])):
        if i>1 and j > 1 and i < len(image)-1 and j < len(image[2])-1 :
            for l in range(-1,2):
                for k in range(-1,2):
                    if int(gray_bgr[i][j][2]) < int(gray_bgr[i+l][j+k][2]) - 5:
                        gray_bgr[i][j] = [0,0,0]


cv2.imshow('Traitement', gray_bgr)
cv2.waitKey(0) 

cv2.destroyAllWindows()

print("✅ Vidéo modifiée enregistrée !")
