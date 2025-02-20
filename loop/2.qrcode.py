import qrcode
name = "subhammm"
image=qrcode.make("https://www.deepboarding.edu.np")
type(image)
image.save(f"{name}.jpg")
