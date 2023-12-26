import qrcode as qr


def QRCODE(msg="Default Message", sas="default_filename", fill_color=(0, 0, 0), back_color=(255, 255, 255)):
    q = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    q.add_data(msg)
    q.make(fit=True)

    img = q.make_image(fill_color=fill_color, back_color=back_color)

    img.save(f"{sas}.png")


# Taking RGB input for fill color as a comma-separated string
fill_color_input = input("Enter fill color RGB values (comma-separated): ")
fill_color = tuple(map(int, fill_color_input.split(',')))

# Taking RGB input for back color as a comma-separated string
back_color_input = input("Enter back color RGB values (comma-separated): ")
back_color = tuple(map(int, back_color_input.split(',')))

msg_input = input("Type your message:")
sas_input = input("Name you want to save the file:")  # saveas = sas

msg = msg_input if msg_input else "Default Message"
sas = sas_input if sas_input else "QR"

QRCODE(msg, sas, fill_color, back_color)
