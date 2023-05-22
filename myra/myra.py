from myra.scan import Scan
import os
import uuid
import csv


class Myra:
		"""Overall class to manage image scans."""

		def __init__(self):
			"""Initalizes the Myra image scan class."""

			self.temp_folder:str = None
			

		def scan(self, image_path:str) -> Scan:
			"""
			Scans every pixel in an image and counts the occurance of each color.

			`image_path`: Absolute or relative filepath to the image.

			`to_disk`: Outputs results to disk as a csv in a new folder.

			`returns`: A dictionary with count data. 
			"""

			if not isinstance(image_path, str):

				error:str = f"ERROR: The provided file path '{image_path}' has an invalid type: {type(image_path)}. Please provide an image path with a type: {str}."
				
				print(error)

				return error

			elif len(image_path) == 0:
						
						error:str = f"ERROR: The file path has an length: {len(image_path)}. Please provide a string filepath with a length > 1."

						print(error)

						return error
			
			try:
						# Initalize scan class that stores image rgb data.
						scan = Scan(image_path)

			except FileNotFoundError:
				return f"No such file or directory: {image_path}. Is the image file in the correct directory?"

			return scan
		

		def to_csv(self, file_name:str, scan:Scan) -> None:
			"""
			Generates a csv for the provided image scan.

			Outputs the csv in the current root directory.

			`file_name`: The name of the to-be-generated csv file.

			`scan`: The myra scan object to be output to csv.
			"""

			with open(file_name, "w", newline='') as csv_file:
				
				csv_writer = csv.writer(csv_file, delimiter=',')
				
				csv_writer.writerow(['rgb_color', 'pixel_count'])
				
				for rgb, count in scan.rgb_count.items():
					
					csv_writer.writerow([rgb, count])



		
		def __generate_temp_folder(self) -> str:
			"""
			Generates a new folder in the current directory with a random filename.

			Returns the file directory name.
			"""

			folder_name:str = f"myra_temp_{str(uuid.uuid4())}"

			while True:
						current_directory:str = os.getcwd()
						
						final_directory:str = os.path.join(current_directory, f'{folder_name}')

						
						if not os.path.exists(final_directory):

									os.makedirs(final_directory)

									break

			self.temp_folder = final_directory

			return 

		
		def __generate_csv(self, color_data:dict[tuple,int]) -> None:
			"""
			Generates a csv for the provided color data.

			Outputs in a generated folder located in the projects root directory.

			Returns nothing. 
			"""

			out_file:str = self.temp_folder + "/myra_scan.csv"

			with open(out_file, "w", newline='') as csv_file:

						csv_writer = csv.writer(csv_file, delimiter=',')

						# Add headers
						csv_writer.writerow(['rgb_color', 'pixel_count'])

						for rgb, count in color_data.items():

									csv_writer.writerow([rgb, count])


			


		


		


