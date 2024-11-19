

import qrcode
from PIL import Image

def generate_qr_code(data: str, filename: str) -> None:
    
    # Create a QR Code object with specific configurations
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code. Higher numbers = larger codes.
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
        box_size=10,  # Size of each QR code box in pixels
        border=4,  # The border size (minimum is 4 for QR Codes)
    )
    
    # Add data to the QR Code object
    qr.add_data(data)
    qr.make(fit=True)  # Automatically adjusts the size to fit the data
    
    # Create an image object from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code as an image file
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    # Input from the user
    print("Welcome to the QR Code Generator!")
    text_to_encode = input("Enter the text or URL to encode: ")
    output_filename = input("Enter the output file name (e.g., 'my_qr.png'): ")

    # Ensure the filename has the correct extension
    if not output_filename.endswith(".png"):
        output_filename += ".png"
    
    # Generate the QR code
    try:
        generate_qr_code(text_to_encode, output_filename)
        print("QR Code generation successful!")
    except Exception as e:
        print(f"An error occurred: {e}")