import cv2
import os

def calculate_frame_difference(video_path, output_path):
    # VideoCapture-Objekt erstellen
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Video kann nicht geöffnet werden.")
        return

    #Video-Informationen abrufen
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    #VideoWriter-Objekt erstellen
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    ret, prev_frame = cap.read()
    if not ret:
        print("Fehler beim Lesen des ersten Frames.")
        return

    while True:
        ret, current_frame = cap.read()
        if not ret:
            break  #Ende des Videos 

        # Differenz zwischen den Frames berechnen
        diff = cv2.absdiff(prev_frame, current_frame)

        # Differenzbild ins Video schreiben
        out.write(diff)

        prev_frame = current_frame

    # Ressourcen freigeben
    cap.release()
    out.release()

if __name__ == "__main__":
    input_video_path = "/data/Bat.mp4"  # Ersetzen Sie dies durch den Pfad zu Ihrem Eingabevideo
    output_video_path = "/data/substract/vid.mp4"  # Ersetzen Sie dies durch den gewünschten Ausgabepfad
    calculate_frame_difference(input_video_path, output_video_path)
