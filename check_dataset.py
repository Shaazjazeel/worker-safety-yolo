import os
import cv2
import random

# Dataset paths
DATASET_PATH = "dataset/construction-site-safety/train"
IMAGES_PATH = os.path.join(DATASET_PATH, "images")
LABELS_PATH = os.path.join(DATASET_PATH, "labels")

# Class names (must match data.yaml)
CLASS_NAMES = [
    "Hardhat", "Mask", "NO-Hardhat", "NO-Mask",
    "NO-Safety Vest", "Person", "Safety Cone",
    "Safety Vest", "Machinery", "Vehicle"
]

# Pick random image
image_files = os.listdir(IMAGES_PATH)
img_name = random.choice(image_files)

img_path = os.path.join(IMAGES_PATH, img_name)
label_path = os.path.join(LABELS_PATH, img_name.replace(".jpg", ".txt").replace(".png", ".txt"))

image = cv2.imread(img_path)
h, w, _ = image.shape

# Draw bounding boxes
with open(label_path, "r") as f:
    for line in f:
        cls, x, y, bw, bh = map(float, line.split())
        cls = int(cls)

        x1 = int((x - bw / 2) * w)
        y1 = int((y - bh / 2) * h)
        x2 = int((x + bw / 2) * w)
        y2 = int((y + bh / 2) * h)

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, CLASS_NAMES[cls], (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow("Dataset Check", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
