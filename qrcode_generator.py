import image
import qrcode
qr=qrcode.QRCode(
    version=20,
    box_size=4,
    border=1
)

data="https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color="white")
img.save("test.png")
