import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "mechanical"
    part_details["type"] = "board_shape"
    part_details["size"] = ["ibbc"]
    part_details["color"] = [""]
    part_details["description_main"] = ["oobb_3_2"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "U"


    #oobb
    part_details = {}
    
    

    sizes_numbers = []
    sizes_numbers.append([3,3])
    sizes_numbers.append([3,5])
    sizes_numbers.append([4,5])
    sizes_numbers.append([5,5])
    sizes_numbers.append([7,5])
    sizes_numbers.append([8,5])
    sizes_numbers.append([9,5])
    sizes_string = []
    for size in sizes_numbers:
        sizes_string.append(f"plate_{size[0]}_{size[1]}")

    
    part_details["classification"] = "mechanical"
    part_details["type"] = "board_shape"
    part_details["size"] = ["oobb"]
    part_details["color"] = [""]
    part_details["description_main"] = sizes_string
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "U"

    #add the part to the list of parts

    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    