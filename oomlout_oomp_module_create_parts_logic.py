import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "logic"
    part_details["type"] = "arduino_compatible"
    part_details["size"] = [""]
    part_details["color"] = [""]
    part_details["description_main"] = "auto_reset_circuit"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)
    
    #i2c
    part_details = {}
    part_details["classification"] = "logic"
    part_details["type"] = "i2c"
    part_details["size"] = [""]
    part_details["color"] = [""]
    part_details["description_main"] = "pull_up_resistors"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""    
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    