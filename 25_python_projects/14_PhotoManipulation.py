# Requires 'pillow' library: pip install pillow
from PIL import Image, ImageEnhance

def manipulate_image():
    # Assumes an image named 'input.jpg' in the same directory
    try:
        img = Image.open("input.jpg")
    except FileNotFoundError:
        print("Please provide an input.jpg file.")
        return
    
    # Adjust brightness
    brightness = ImageEnhance.Brightness(img).enhance(1.5)
    brightness.save("bright_image.jpg")
    
    # Adjust contrast
    contrast = ImageEnhance.Contrast(img).enhance(1.5)
    contrast.save("contrast_image.jpg")
    
    print("Images saved as bright_image.jpg and contrast_image.jpg")

if __name__ == "__main__":
    manipulate_image()