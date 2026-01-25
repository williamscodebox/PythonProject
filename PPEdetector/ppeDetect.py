from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture("../Videos/ppe-1-1.mp4")

model = YOLO("ppe.pt")

classNames = ['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'SUV', 'Safety Cone', 'Safety Vest', 'bus', 'dump truck', 'fire hydrant', 'machinery', 'mini-van', 'sedan', 'semi', 'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            # Confidence
            conf = math.ceil((box.conf[0]*100))/100
            print(conf)
            # Class Name
            cls = int(box.cls[0])
            cvzone.putTextRect(
                img,
                f'{classNames[cls]} {conf}',
                (max(0, x1), max(35, y1)),
                scale=1.5,
                thickness=2,
                colorT=(255, 255, 255),  # white text
                colorR=(0, 0, 255)  # red rectangle
            )

    cv2.imshow("Image", img)
    cv2.waitKey(1)


# results = model("Images/sb.jpg", show=True)
# annotated = results[0].plot() # get the image with boxes drawn
# cv2.imshow("Result", annotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()