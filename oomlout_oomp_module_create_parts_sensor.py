import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "sensor"
    part_details["type"] = ""
    part_details["size"] = [""]
    part_details["color"] = [""]
    part_details["description_main"] = ["pressure_temperature"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = "bme280"
    part_details["kicad_reference"] = "U"

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    