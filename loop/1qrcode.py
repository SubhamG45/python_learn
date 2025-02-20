import qrcode
name=input("enter your name:")
image=qrcode.make(name)
type(image)
image.save(f"{name}.png")