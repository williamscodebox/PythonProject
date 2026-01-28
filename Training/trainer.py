import torch
from ultralytics import YOLO

print("CUDA Available:", torch.cuda.is_available())
if torch.cuda.is_available():
   print("GPU Name:", torch.cuda.get_device_name(0))

def main():
   # Load the model
   model = YOLO("yolov8m.pt")  # Replace with your model file
   # Move model to GPU
   # model.to('cuda')
   # Run inference on an image
   results = model.predict(source="bikes.jpg", device='cuda')

   # Train the model on GPU
   # model.train(data="coco.yaml", epochs=50, device='cuda')
   model.train(data="./PlayingCards/data.yaml", epochs=50, device='cuda', amp=True, workers=0, batch=20)
   # Validate the model on GPU
   model.val(data="./PlayingCards/data.yaml", device='cuda')


if __name__ == "__main__":
   main()

   # !yolo
   # task = detect
   # mode = train
   # model = yolov8l.pt
   # data =./PlayingCards/data.yaml
   # epochs = 50
   # imgsz = 640