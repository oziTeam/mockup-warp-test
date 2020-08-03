import os
import time

import cv2
import numpy as np
from PIL import Image, ImageChops

from warp_image import thinplate as tps, contants


class Mockup3DGenerator:
    def __init__(self, mockup_data, artwork_data, colors="#333333"):
        self.mockup_data = mockup_data
        self.artwork_data = artwork_data
        self.colors = colors

    def do_generate(self):
        for side in self.mockup_data:
            start = time.time()
            main_side_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
            for part in side['parts']:
                artwork_image = Image.open(self.artwork_data[part['artwork_side']]).convert("RGBA")
                artwork_image = np.array(artwork_image)
                open_cv_artwork_image = cv2.cvtColor(artwork_image, cv2.COLOR_RGB2BGR)

                # warp_artwork_image_name = "{}{}{}".format(prefix_name, SPLIT_CHAR, part.get("name"))
                # print("Doing warp...")
                resized_img = cv2.resize(open_cv_artwork_image, contants.shape)

                if os.path.isfile(part['model_path']):
                    grid = np.load(part['model_path'], allow_pickle=True)

                    mapx, mapy = tps.tps_grid_to_remap(grid, contants.shape)
                    img = cv2.remap(resized_img, mapx, mapy, cv2.INTER_CUBIC)
                    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
                    warped = Image.fromarray(img).convert("RGBA")

                    cut_image = Image.open(part['cut_image_path']).convert("RGBA")
                    out = Image.composite(cut_image, warped, cut_image)

                    main_side_image = ImageChops.darker(out, main_side_image)
                    # main_side_image = main_side_image.resize(main_side_image.size, Image.ANTIALIAS)


                else:
                    print("Model for {} not found".format(side['side_name'] + " | " + part['name']))

            end = time.time()
            print('[{:.4f} s] Generate mockup for {} executed'.format((end - start), side['side_name']))

            main_side_image.show()
