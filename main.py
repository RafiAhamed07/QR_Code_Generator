import qrcode as qr


def QRCODE(msg="Default Message", sas="default_filename"):
    q = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    q.add_data(msg)
    q.make(fit=True)

    img = q.make_image(fill_color=(0,0,0), back_color=(255,255,255))

    img.save(f"{sas}.png")


msg_input = input("Type your message:")
sas_input = input("Name you want to save the file:")  # saveas = sas


msg = msg_input if msg_input else "Default Message"
sas = sas_input if sas_input else "QR"

QRCODE(msg, sas)
