import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=120,
    border=8,
)

qr.add_data("")  # link para onde o QRCode irá direcionar

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="",  # nome da imagem que ficará no centro do QRCode
)

imagem.save("")  # nome do QRCode
