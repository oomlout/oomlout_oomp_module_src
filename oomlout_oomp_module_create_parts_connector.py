import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []


    #### icsp
    part_details = {}
    part_details["classification"] = "connector"
    part_details["type"] = ""
    part_details["size"] = "icsp"
    part_details["color"] = [""]
    part_details["description_main"] = "through_hole"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "J"
    parts.append(part_details)

    #### usb mini
    part_details = {}
    part_details["classification"] = "connector"
    part_details["type"] = ""
    part_details["size"] = "usb_mini"
    part_details["color"] = [""]
    part_details["description_main"] = "surface_mount_only"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "J"
    parts.append(part_details)

    #arduino shennie
    part_details = {}
    part_details["classification"] = "connector"
    part_details["type"] = "arduino_compatible"
    part_details["size"] = ["shennie","nano"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "R"



    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    