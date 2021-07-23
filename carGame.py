from __future__ import print_function
import cv2 as cv
import argparse


def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    # -- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2),
                           0, 0, 360, (255, 0, 255), 4)
    cv.imshow('Capture - Face detection', frame)


parser = argparse.ArgumentParser(
    description='Code for Cascade Path.')
parser.add_argument('--face_cascade', help='Path to face cascade.',
                    default='C:\PythonVSCode\Car-Game\haarcascades\haarcascade_frontalface_alt.xml')
parser.add_argument(
    '--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade

face_cascade = cv.CascadeClassifier()


# Load the cascades needed (Make sure directories are correct)
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
camera_device = args.camera


# Read the video stream/Make sure device is available
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break
