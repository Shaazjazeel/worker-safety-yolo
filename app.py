import os
import cv2
from flask import Flask, render_template, request, Response
from ultralytics import YOLO

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
model = YOLO("best.pt")

# Violation classes
VIOLATION_CLASSES = {"NO-Hardhat", "NO-Mask", "NO-Safety Vest"}


@app.route("/", methods=["GET", "POST"])
def index():
    input_video = None

    if request.method == "POST":
        if "video" not in request.files:
            return render_template("index.html", input_video=None)

        video = request.files["video"]
        if video.filename == "":
            return render_template("index.html", input_video=None)

        input_path = os.path.join(UPLOAD_FOLDER, video.filename)
        video.save(input_path)

        input_video = video.filename

    return render_template("index.html", input_video=input_video)


def process_frames(input_path):
    cap = cv2.VideoCapture(input_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # YOLO inference
        results = model(frame, conf=0.5, iou=0.6)

        annotated = frame.copy()
        violation_found = False

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Auto-like color per class (deterministic)
                base_color = (
                    (37 * cls_id) % 255,
                    (17 * cls_id) % 255,
                    (29 * cls_id) % 255
                )

                # Make violations RED
                if label in VIOLATION_CLASSES:
                    color = (0, 0, 255)  # RED
                    violation_found = True
                else:
                    color = base_color

                # Draw box + label
                cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 2)
                cv2.putText(
                    annotated,
                    label,
                    (x1, max(20, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    color,
                    2
                )

        # 🔥 Blinking alert text if violation found
        # Blink every 10 frames (you can change this)
        if violation_found and (frame_count // 10) % 2 == 0:
            cv2.putText(
                annotated,
                "VIOLATION DETECTED",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 0, 255),
                3
            )

        ok, jpeg = cv2.imencode(".jpg", annotated)
        if not ok:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + jpeg.tobytes()
            + b"\r\n"
        )

    cap.release()


@app.route("/video_feed/<filename>")
def video_feed(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    return Response(process_frames(input_path), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

