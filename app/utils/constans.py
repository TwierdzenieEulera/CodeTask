from enum import Enum

region_list = ["Europe", "Antarctic", "Asia", "Oceania", "Americas", "Africa"]
sub_region_list = ["Southern Europe", "Southeast Europe", "Central Europe", "Western Europe", "Northern Europe",
                   "Eastern Asia", "South-Eastern Asia", "Central Asia", "Western Asia", "Southern Asia"
                   "Polynesia", "Micronesia", "Caribbean",
                   "Western Africa", "Northern Africa", "Eastern Africa", "Middle Africa", "Southern Africa"
                   "Central America", "South America", "North America"]


class Formats(Enum):
    JSON = "json"
    CSV = "csv"
