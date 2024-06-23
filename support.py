# allows us to read from a csv file
from csv import reader



def import_csv_layout(path):
    terrain_map = []
    # you open the file, the as shows what you are naming this file
    with open(path) as level_map:
        # reads the file, delimiter is what is in the middle of it like the comma in csv
        layout = reader(level_map, delimiter= ',')
        # for statement to print the file that is read
        for row in layout:
            terrain_map.append(list(row)) #convert row to a list for the terrain map
        return terrain_map

            
    
    
# print(import_csv_layout('map/map_FloorBlocks.csv')) #this shows that 395 is the terrain of boundaries
    