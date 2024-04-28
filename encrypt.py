from PIL import Image
import numpy as np

# Convert cover image to gray-scale
cover = Image.open("RR.png").convert('L')

data_c = np.array(cover)

# Convert image to 1-bit pixel, black and white and resize to cover image
secret = Image.open("qr.png").convert('1')
secret = secret.resize(cover.size)

data_s = np.array(secret, dtype=np.uint8)

# Rewrite LSB
res = data_c & ~1 | data_s

new_img = Image.fromarray(res).convert("L")
new_img.save("CTF-uppgift/LagomSäkerBild.png")
new_img.show()