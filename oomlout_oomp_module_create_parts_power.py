import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "power"
    part_details["type"] = "linear"
    part_details["size"] = ["sot_223"]
    part_details["color"] = ["1117"]    
    part_details["description_main"] = ["3_3_volt_output","5_volt_output"]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "R"

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    