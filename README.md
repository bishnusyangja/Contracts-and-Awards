# Contracts-and-Awards
Combining two files contracts.csv and awards.csv

This project is done python 2.7 and simply installing the python on your machine, you can run this project.

Basic Algorighm
1  If you have the folder named files, it creates a file named folder where your main.py file resides.
2  Then it searches the files contracts.csv and awards.csv in files folder, if not exist, it downloads from the
   git.
3  Then it reads the two files and merge them
4  At that moment, it also finds the geocode (longitued and latitude) of awardeeLocation.
5  Finally all these data are dislpalyed in output_contracts.xml file on the files folder.


# To run this code.
1  Install python 2.7 on your machine.
2  Go to settings file and add google api_key to get geocode for location. By default I have provided my own api_key.
3  Finally run the command
   "python main.py"