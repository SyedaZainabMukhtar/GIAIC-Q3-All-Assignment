# Requires 'qrcode' and 'pillow' libraries: pip install qrcode pillow
import qrcode

def qr_code_generator():
    data = input("Enter the data to encode in QR code: ")
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    print("QR code saved as qrcode.png")

if __name__ == "__main__":
    qr_code_generator()