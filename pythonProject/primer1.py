import qrcode

qr = qrcode.QRCode()
qr.add_data('Какие-то данные или URL-адрес')
img = qr.make_image()
img.save("some_file.png")
qr.clear()
qr.add_data('Новые данные или URL-адрес')
other_img = qr.make_image()
other_img.save("new_some_file.png")
