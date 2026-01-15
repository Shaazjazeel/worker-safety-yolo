from ultralytics import YOLO
import cv2
import os

# Paths
MODEL_PATH = "best.pt"
INPUT_VIDEO = "videos/input.mp4"
OUTPUT_VIDEO = "outputs/output.mp4"

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

# Open input video
cap = cv2.VideoCapture(INPUT_VIDEO)
if not cap.isOpened():
    raise IOError("Cannot open input video")

# Video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

# Classes that indicate violation
VIOLATION_CLASSES = {"NO-Hardhat", "NO-Safety Vest", "NO-Mask"}

# Process video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO inference (increase conf for cleaner results)
    results = model(frame, conf=0.6)

    violation_detected = False

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if label in VIOLATION_CLASSES:
                color = (0, 0, 255)  # Red
                violation_detected = True
            else:
                color = (0, 255, 0)  # Green

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                frame,
                f"{label} {conf:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    # Display warning text if violation detected
    if violation_detected:
        cv2.putText(
            frame,
            "SAFETY VIOLATION DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.1,
            (0, 0, 255),
            3
        )

    out.write(frame)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processing complete.")
print("Output saved to:", OUTPUT_VIDEO)
