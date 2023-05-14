from PIL import Image
import time

class Myra:
    """Overall class to manage image scans."""

    def __init__(self):
        """
        Initalize the Myra image scan class.
        """

    def scan(self, image_path:str) -> dict[tuple,int]:
      """
      Scans every pixel and counts the occurance of each color in the image.

      image_path: Absolute or relaitve filepath to the image.

      Returns a dictionary with count data. 
      """


      if not isinstance(image_path, str):
            
            print(f"The file path '{image_path}' has an invalid type: {type(image_path)}. Please provide a {str}.")

            return

      elif len(image_path) == 0:

            print(f"The file path has an length: {len(image_path)}. Please provide a string filepath with a length > 1.")

            return
      
      print(f"Starting scan for image: {image_path}")
      start_time:float = time.time()

      try:

            colors:dict[tuple,int] = {}

            # Load the image and grab pixel data.
            image = Image.open(image_path)

            pixels = image.load()
            
            print(f"Image size: {image.size}")
            # Loop through the pixels, store the rgb values, and increment a count
            for x in range(image.size[0]):
                  for y in range(image.size[1]):
                        
                        rgba:tuple[int] = pixels[x,y]

                        colors[rgba[:3]] = 1 + colors.get(rgba[:3], 0)

      except FileNotFoundError:
            print(f"No such file or directory: {image_path}. Is the file in the correct directory?")

            return

      end_time:float = time.time()
      print(f"Scan complete. Time elapsed: {end_time - start_time}")


      return colors

    

    


    


