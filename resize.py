import cv2
import os
import numpy as np

# Define input and output directories
input_dir = 'images/DONE'
output_dir = 'images/prewedding'
thumb_dir = 'images/prewedding_thumb'

# Create output directories if they don't exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(thumb_dir, exist_ok=True)

# Process images in the input directory
for idx, filename in enumerate(os.listdir(input_dir), start=1):
    input_path = os.path.join(input_dir, filename)
    
    # Read the image
    image = cv2.imread(input_path)
    if image is None:
        continue  # Skip if the file is not a valid image

    # Save the resized image
    output_path = os.path.join(output_dir, f'image{idx}.jpg')
    cv2.imwrite(output_path, image)

    # Create and save the thumbnail
    thumb = cv2.resize(image, (400, 600))  # Resize to 400x600 for thumbnail
    thumb_path = os.path.join(thumb_dir, f'thumb{idx}.jpg')
    cv2.imwrite(thumb_path, thumb)