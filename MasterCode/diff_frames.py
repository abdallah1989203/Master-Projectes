# frame_difference_script.py

import cv2
import os
import glob

def calculate_frame_difference():
    base_path = "/data/substract/yolds"
    pattern = os.path.join(base_path, "00233_*", "images")

    # Liste der Ordner
    folders = glob.glob(pattern)

    for folder in folders:
        # Liste der Bilder 
        image_files = sorted([f for f in os.listdir(folder) if f.endswith('.PNG') or f.endswith('.png')])
        
        if not image_files:   
            continue

        # erste Bild
        prev_image_path = os.path.join(folder, image_files[0])
        prev_image = cv2.imread(prev_image_path)

        # Schleife durch die Bilder 
        for i in range(1, len(image_files)):
            current_image_path = os.path.join(folder, image_files[i])
            current_image = cv2.imread(current_image_path)

            #Differenz zwischen den Bildern 
            diff = cv2.absdiff(prev_image, current_image)

            # Speichern Sie das Differenzbild 
            output_image_path = os.path.join(folder, f"diff_{image_files[i]}")
            cv2.imwrite(output_image_path, diff)

            prev_image = current_image

if __name__ == "__main__":
    calculate_frame_difference()
