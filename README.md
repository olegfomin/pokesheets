# Introduction
The **pokesheets** take away test for Saurabh Patro. The src/pokesheets.py produces the CSV
records of the format as follows: ID,NAME,WEIGHT,TYPES. TYPES are separated by
the pipe character  

# Building
Please navigate into the project root and execute the command as follows:

**docker build -t pokesheets .**

# Execution
**docker run -it pokesheets:latest <list_of_pokemon_names>**

# Example of execution:
oleg@LivingRoomComp ~/git/pokesheets $ **docker run -it pokesheets:latest pikachu bulbasaur**
ID,NAME,WEIGHT,TYPES

25,pikachu,60,electric

1,bulbasaur,69,poison|grass
