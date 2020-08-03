import os

import numpy as np
from PIL import Image, ImageChops
import cv2
from warp_image import thinplate as tps, contants

ARTWORK_DATA = {
    "Front": "/home/vantrong291/Pictures/photos/3-front.jpg",
    "Hood": "/home/vantrong291/Pictures/photos/3-hood.jpg",
    "Back": "/home/vantrong291/Pictures/photos/3-back.jpg"
}

MOCKUP_DATA = [
    {
        "side_name": "Back",
        "parts": [
            {
                "name": "back.left_sleeve",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.back.left_sleeve.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/back.left_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Back"
            },
            {
                "name": "back.left_sleeve",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.back.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/back.front_back-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Back"
            },
            {
                "name": "back.right_sleeve",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.back.right_sleeve.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/back.right_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Back"
            },
            {
                "name": "back.top_hood",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.back.top_hood.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/back.top_hood-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Hood"
            },
        ]
    },
    {
        "side_name": "Front",
        "artwork_path": "/home/vantrong291/Pictures/photos/3-front.jpg",
        "parts": [
            {
                "name": "front.left_sleeve",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.front.left_sleeve.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/front.left_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Front"
            },
            {
                "name": "front",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.front.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/front.front-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Front"
            },
            {
                "name": "front.right_sleeve",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.front.right_sleeve.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/front.right_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Front"
            },
            {
                "name": "front.bottom_hood",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.front.bottom_hood.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/front.bottom_hood-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Hood"

            },
            {
                "name": "front.top_hood",
                "model_path": "/home/vantrong291/ws/fb/mockup-generator/models/tshirt.front.top_hood.model.npy",
                "cut_image_path": "/home/vantrong291/ws/test/mockup/front.top_hood-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Hood"
            }
        ]
    }
]


class Mockup3DGenerator:
    def __init__(self, mockup_data, artwork_data, colors="#333333"):
        self.mockup_data = mockup_data
        self.artwork_data = artwork_data
        self.colors = colors

    def do_generate(self):
        for side in self.mockup_data:
            main_side_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
            for part in side['parts']:
                artwork_image = Image.open(self.artwork_data[part['artwork_side']]).convert("RGBA")
                artwork_image = np.array(artwork_image)
                open_cv_artwork_image = cv2.cvtColor(artwork_image, cv2.COLOR_RGB2BGR)

                # warp_artwork_image_name = "{}{}{}".format(prefix_name, SPLIT_CHAR, part.get("name"))
                print("Doing warp...")
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

            main_side_image.show()


if __name__ == "__main__":
    mockup = Mockup3DGenerator(mockup_data=MOCKUP_DATA, artwork_data=ARTWORK_DATA)
    mockup.do_generate()
