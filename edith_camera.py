import cv2

# function to open camera
def open_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not found")
        return

    print("Camera started. Press 'q' to close.")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("EDITH Camera", frame)

        # press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# function to take photo
def take_photo():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not found")
        return

    ret, frame = cap.read()

    if ret:
        cv2.imwrite("edith_photo.jpg", frame)
        print("Photo saved as edith_photo.jpg")

    cap.release()
