import qrcode # type: ignore
import qrcode.image.svg # type: ignore


def generate_qrcode():
    
    data = input("Give me Text or URL : ").strip()
    qr_filename = input("What the name of the QR code (no extension): ").strip()
    option_type = int(input("What do you want \n 1: PNG '\n 2: JPG \n 3: SVG \n\n" ))
    
    match option_type:
        
        case 1:
            img_generate_qr(data, qr_filename, ".png")
        case 2:
            img_generate_qr(data, qr_filename, ".jpg")
        case 3:
            generate_svg(data, qr_filename)
        case _:
            print("invalid input")


def img_generate_qr(data, qr_filename, type):
    
    qr = qrcode.QRCode(
        version=None,  # auto-size
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    png_img = qr.make_image(fill_color="black", back_color="white")
    png_img.save(qr_filename + type)
    print(f"PNG QR saved as {qr_filename}{type}")
        
def generate_svg(data, qr_filename):
    
    factory = qrcode.image.svg.SvgImage
    svg_img = qrcode.make(data, image_factory = factory)
    svg_img.save(qr_filename + ".svg")
    print(f"SVG QR saved as {qr_filename}.svg")




generate_qrcode()   