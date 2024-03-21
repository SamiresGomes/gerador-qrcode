import qrcode

link = 'https://github.com/SamiresGomes'

nome_arquivo = 'qr_code_site.png'

#criando um objeto qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(link)
qr.make(fit=True)

imagem = qr.make_image()

imagem.save(nome_arquivo)

