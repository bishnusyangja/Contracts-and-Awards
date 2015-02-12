# Contracts-and-Awards
Combining two files contracts.csv and awards.csv

This project is done python 2.7 and simply installing the python on your machine, you can run this project.

# Basic Algorighm
  If you have the folder named files, it creates a file named folder where your main.py file resides.
  Then it searches the files contracts.csv and awards.csv in files folder, if not exist, it downloads from the
   git.
  Then it reads the two files and merge them
  At that moment, it also finds the geocode (longitued and latitude) of awardeeLocation.
  Finally all these data are dislpalyed in output_contracts.xml file on the files folder.


# To run this code.
Install python 2.7 on your machine.
Go to settings file and add google api_key to get geocode for location. By default I have provided my own api_key.
Finally run the command
   "python main.py"