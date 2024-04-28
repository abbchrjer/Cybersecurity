from PIL import Image
import numpy as np

def bitplanes(im):
    im = Image.open(im)
    data = np.array(im)
    out = []
    # create an image for each k bit plane
    for k in range(7,-1,-1):
    # extract kth bit (from 0 to 7)
        res = data // 2**k & 1
        out.append(res*255)
    # stack generated images
    b = np.hstack(out)
    return Image.fromarray(b)

bitplanes("CTF-uppgift/LagomSäkerBild.png").show()