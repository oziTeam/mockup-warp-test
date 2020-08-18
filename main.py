from mockup_generator import Mockup3DGenerator
from data import ARTWORK_DATA, MOCKUP_DATA



if __name__ == "__main__":
    mockup = Mockup3DGenerator(mockup_data=MOCKUP_DATA, artwork_data=ARTWORK_DATA)
    print("----- STARTING -----")
    mockup.do_generate()
    print("----- DONE -----")
