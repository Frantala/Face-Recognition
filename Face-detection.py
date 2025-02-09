import cv2

# Cargar el clasificador de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Abrir la cámara 
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Mostrar el cuadro
    cv2.imshow('Camera', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y destruir todas las ventanas
cap.release()
cv2.destroyAllWindows()
