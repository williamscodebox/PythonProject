from ultralytics import YOLO
import cv2

model = YOLO("../YoloWeights/yolov8m.pt")
results = model("Images/sb.jpg", show=True)
annotated = results[0].plot() # get the image with boxes drawn
cv2.imshow("Result", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()