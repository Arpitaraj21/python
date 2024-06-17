import qrcode as qr

image = qr.make("https://github.com/Arpitaraj21/Resume/blob/main/Arpita-Raj-FlowCV%20(1).pdf")
image.save("myResume.png")