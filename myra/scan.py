from PIL import Image

class Scan:
    """A class to represent an individual myra scan."""

    def __init__(self, image_path:str):
        """Initializes the image scan class."""

        self.image_path = image_path
        self.rgb_count:dict[tuple,int] = self.__scan_image()


    def __scan_image(self) -> dict[tuple,int]:
        """ 
        A class to update the rgb count values of the scan.

        `rgba`: A tuple representive the rgb value of a pixel. Ex:(0, 250, 0, 0)
        """

        rgb_count:dict[tuple,int] = {}

        image = Image.open(self.image_path)

        self.image_size = image.size

        pixels = image.load()

        for x in range(image.size[0]):
            for y in range(image.size[1]):

                rgba:tuple[int] = pixels[x,y]

                rgb_count[rgba[:3]] = 1 + rgb_count.get(rgba[:3], 0)

        return rgb_count

    






    


    



