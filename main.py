from mockup_generator import Mockup3DGenerator

ARTWORK_DATA = {
    "Front": "./sample_data/artworks/3-front.jpg",
    "Hood": "./sample_data/artworks/3-hood.jpg",
    "Back": "./sample_data/artworks/3-back.jpg"
}

MOCKUP_DATA = [
    {
        "side_name": "Back",
        "parts": [
            {
                "name": "back.left_sleeve",
                "model_path": "./sample_data//models/tshirt.back.left_sleeve.model.npy",
                "cut_image_path": "./sample_data/cut_images/back.left_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Back"
            },
            {
                "name": "back.left_sleeve",
                "model_path": "./sample_data//models/tshirt.back.model.npy",
                "cut_image_path": "./sample_data/cut_images/back.front_back-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Back"
            },
            {
                "name": "back.right_sleeve",
                "model_path": "./sample_data//models/tshirt.back.right_sleeve.model.npy",
                "cut_image_path": "./sample_data/cut_images/back.right_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Back"
            },
            {
                "name": "back.top_hood",
                "model_path": "./sample_data//models/tshirt.back.top_hood.model.npy",
                "cut_image_path": "./sample_data/cut_images/back.top_hood-cut.png",
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
                "model_path": "./sample_data//models/tshirt.front.left_sleeve.model.npy",
                "cut_image_path": "./sample_data/cut_images/front.left_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Front"
            },
            {
                "name": "front",
                "model_path": "./sample_data//models/tshirt.front.model.npy",
                "cut_image_path": "./sample_data/cut_images/front.front-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Front"
            },
            {
                "name": "front.right_sleeve",
                "model_path": "./sample_data//models/tshirt.front.right_sleeve.model.npy",
                "cut_image_path": "./sample_data/cut_images/front.right_sleeve-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Front"
            },
            {
                "name": "front.bottom_hood",
                "model_path": "./sample_data//models/tshirt.front.bottom_hood.model.npy",
                "cut_image_path": "./sample_data/cut_images/front.bottom_hood-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Hood"

            },
            {
                "name": "front.top_hood",
                "model_path": "./sample_data//models/tshirt.front.top_hood.model.npy",
                "cut_image_path": "./sample_data/cut_images/front.top_hood-cut.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Hood"
            }
        ]
    }
]


if __name__ == "__main__":
    mockup = Mockup3DGenerator(mockup_data=MOCKUP_DATA, artwork_data=ARTWORK_DATA)
    print("----- STARTING -----")
    mockup.do_generate()
    print("----- DONE -----")
