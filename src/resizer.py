from PIL import Image
import os
from utils import get_all_images

# Input and Output folder
INPUT_FOLDER = "../images"
OUTPUT_FOLDER = "../output"

# Desired size (width, height)
SIZE = (300, 300)

# Make sure output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def resize_and_convert(image_path, output_folder, size, output_format="PNG"):
    try:
        img = Image.open(image_path)  # Open image
        img_resized = img.resize(size)  # Resize image
        filename = os.path.splitext(os.path.basename(image_path))[0]  # File name without extension
        save_path = os.path.join(output_folder, f"{filename}.{output_format.lower()}")
        img_resized.save(save_path, output_format)  # Save in new format
        print(f"✅ Saved: {save_path}")
    except Exception as e:
        print(f"❌ Error processing {image_path}: {e}")

if __name__ == "__main__":
    images = get_all_images(INPUT_FOLDER)
    for img_path in images:
        resize_and_convert(img_path, OUTPUT_FOLDER, SIZE, output_format="PNG")
