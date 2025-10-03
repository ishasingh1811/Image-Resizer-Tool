import os

def get_all_images(input_folder):
    """
    Ye function ek folder ke andar ke saare image files ka full path return karta hai.
    Sirf supported image formats (jpg, jpeg, png, bmp, gif) ko hi lega.
    """
    supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

    # List of file paths
    image_files = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)   # folder ke andar ke saare files padhega
        if f.lower().endswith(supported_formats)  # sirf supported extensions hi lega
    ]
    return image_files
