import torch
from ultralytics import YOLO

print("CUDA Available:", torch.cuda.is_available())
if torch.cuda.is_available():
   print("GPU Name:", torch.cuda.get_device_name(0))

   # Load the model
   model = YOLO("yolov8n.pt")  # Replace with your model file
   # Move model to GPU
   model.to('cuda')
   # Run inference on an image
   results = model.predict(source="image.jpg", device='cuda')

   # Train the model on GPU
   # model.train(data="coco.yaml", epochs=50, device='cuda')
   model.train(data="coco.yaml", epochs=50, device='cuda', amp=True)
   # Validate the model on GPU
   model.val(data="coco.yaml", device='cuda')


   # !yolo
   # task = detect
   # mode = train
   # model = yolov8l.pt
   # data =../ content / drive / MyDrive / Datasets / PlayingCards / data.yaml
   # epochs = 50
   # imgsz = 640