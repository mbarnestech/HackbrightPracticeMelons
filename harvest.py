############
# Part 1   #
############

import sys

harvest_log = sys.argv[1]

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # self.pairings.append(pairing) # adds a single item
        self.pairings.extend(pairing) # adds a list to the list [1,2]

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, False, 'Muskmelon')
    musk.add_pairing(['mint'])
    all_melon_types.append(musk)

    crenshaw = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    crenshaw.add_pairing(['prosciutto'])
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing(['ice cream'])
    all_melon_types.append(yellow_watermelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing(['strawberries','mint'])
    all_melon_types.append(casaba)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print('')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # key: value -> melon.code: melon.name

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon.name
    
    return melon_dict


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    # Needs __init__ and is_sellable methods

    def __init__(
        self, melon_type, shape_rating, color_rating, harvested_from, harvested_by, melon_number
        ):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        self.melon_number = melon_number
        

    def is_sellable(self):
        #both its shape and color ratings are greater than 5, and it didn’t come from field 3
        return self.harvested_from != 3 and self.shape_rating > 5 and self.color_rating > 5
        
def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []

    melon_list.append(Melon('yw', 8, 7, 2, 'Sheila', 1))
    melon_list.append(Melon('yw', 3, 4, 2, 'Sheila', 2))
    melon_list.append(Melon('yw', 9, 8, 3, 'Sheila', 3))
    melon_list.append(Melon('cas', 10, 6, 35, 'Sheila', 4))
    melon_list.append(Melon('cren', 8, 9, 35, 'Michael', 5))
    melon_list.append(Melon('cren', 8, 2, 35, 'Michael', 6))
    melon_list.append(Melon('cren', 2, 3, 4, 'Michael', 7))
    melon_list.append(Melon('musk', 6, 7, 4,'Michael', 8))
    melon_list.append(Melon('yw', 7, 10, 3, 'Sheila', 9))

    return melon_list

def make_melons2(melon_types, file = harvest_log):
    """Returns a list of Melon objects."""
    melon_list = []
    melon_counter = 1
    data = open(file)

    for line in data:
        _, shape, _, color, _, type, _, _, person, _, _, field = line.rstrip().split(' ')
        melon_list.append(Melon(type, int(shape), int(color), int(field), person, melon_counter))
        melon_counter += 1

    return melon_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sellable = 'NOT SELLABLE' 
        if melon.is_sellable():
            sellable = 'CAN BE SOLD' 
        print(f'Harvested by {melon.harvested_by} from Field {melon.harvested_from} ({sellable})')
