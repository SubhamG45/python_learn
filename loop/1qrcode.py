import qrcode
name=input("enter your name:")
image=qrcode.make("htts://www.youtube.com")
type(image)
image.save(f"{name}.png")