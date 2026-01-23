from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture("../Videos/people.mp4") # For Video

model = YOLO("../YoloWeights/yolov8m.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "potted plant", "bed",
              "dining table", "toilet", "tv monitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
mask = cv2.imread("mask.png")

limitsUp = [103, 161, 296, 161]
limitsDown = [529, 489, 735, 489]

totalUp = []
totalDown = []

# Track unique IDs
counted_ids = set()
total_people = []


while True:
    success, img = cap.read()
    if not success:
        break
    # results = model(img, stream=True)
    # Use built-in tracker
    imgRegion = cv2.bitwise_and(img, mask)
    imgGraphics = cv2.imread("graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (730, 260))
    results = model.track(imgRegion, persist=True, stream=True)

    cv2.line(img, (limitsUp[0], limitsUp[1]), (limitsUp[2], limitsUp[3]), (0,  0, 255), 5)
    cv2.line(img, (limitsDown[0], limitsDown[1]), (limitsDown[2], limitsDown[3]), (0, 0, 255), 5)

    for r in results:
        if r.boxes.id is None:
            continue

        boxes = r.boxes
        ids = r.boxes.id.cpu().numpy().astype(int)

        for box, track_id in zip(boxes, ids):
            # Bounding Box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = math.ceil((box.conf[0]*100))/100

            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == "person" and conf > 0.3:
                # Count only once per unique ID
                if track_id not in counted_ids:
                    counted_ids.add(track_id)
                    total_people.insert(track_id, total_people)

                # Draw Box
                cvzone.cornerRect(img, (x1, y1, w, h), l=6)

                cx, cy = (x1 + w/2, y1 + h/2)
                cv2.circle(img, (int(cx), int(cy)), 5, (255, 0, 255), cv2.FILLED)

                if limitsUp[0] < cx < limitsUp[2] and limitsUp[1] -15 < cy < limitsUp[1] + 15:
                    if totalUp.count(track_id) == 0:
                        totalUp.append(track_id)
                        cv2.line(img, (limitsUp[0], limitsUp[1]),(limitsUp[2], limitsUp[3]), (0, 255, 0), 5)

                if limitsDown[0] < cx < limitsDown[2] and limitsDown[1] - 15 < cy < limitsDown[1] + 15:
                    if totalDown.count(track_id) == 0:
                        totalDown.append(track_id)
                        cv2.line(img, (limitsDown[0], limitsDown[1]), (limitsDown[2], limitsDown[3]), (0, 255, 0), 5)

                # Label
                cvzone.putTextRect(
                    img,
                    f'{currentClass} | {conf} | Total: {len(total_people)}',
                    (max(0, x1), max(35, y1)),
                    scale=1.4,
                    thickness=2,
                    offset=5,
                    colorT=(255, 255, 255),  # white text
                    colorR=(0, 0, 255)  # red rectangle
                )

    # cvzone.putTextRect(img, f' Count: {len(totalCount)}', (50, 50))
    cv2.putText(img, str(len(totalUp)), (929, 345), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)
    # cvzone.putTextRect(img, f' Count: {len(totalCount)}', (50, 50))
    cv2.putText(img, str(len(totalDown)), (1179, 345), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)

    cv2.imshow("Image", img)
    # cv2.imshow("ImageRegion", imgRegion)
    cv2.waitKey(1) # plays right through
    # cv2.waitKey(0) # plays frame and must press key to go to next frame

print(len(total_people))

results = model("bg.png", show=True)
annotated = results[0].plot() # get the image with boxes drawn

# Label
cvzone.putTextRect(
    annotated,
    f'Total People Going Up: {len(totalUp)}',
    (max(0, 220), max(35, 150)),
     scale=1.4,
     thickness=2,
     offset=5,
     colorT=(255, 255, 255),  # white text
     colorR=(0, 0, 255)  # red rectangle
      )

# Label
cvzone.putTextRect(
    annotated,
    f'Total People Going Down: {len(totalDown)}',
    (max(0, 220), max(185, 300)),
     scale=1.4,
     thickness=2,
     offset=5,
     colorT=(255, 255, 255),  # white text
     colorR=(0, 0, 255)  # red rectangle
      )
cv2.imshow("Result", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()