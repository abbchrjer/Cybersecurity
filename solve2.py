from PIL import Image
import numpy as np

im = Image.open("CTF-uppgift/LagomSäkerBild.png")
data_s = np.array(im)
data_s = data_s & 1
new_img = Image.fromarray(data_s * np.uint(255))
new_img.show()