import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "ic"
    part_details["type"] = ""
    part_details["size"] = ["sop_16"]
    part_details["color"] = [""]
    part_details["description_main"] = ["usb_to_serial_bridge"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = "ch340c"
    part_details["kicad_reference"] = "U"

    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    