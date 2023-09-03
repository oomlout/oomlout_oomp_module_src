import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
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
    parts.append(part_details)

    #### ibbc
    part_details = {}
    part_details["classification"] = "connector"
    part_details["type"] = "ibbc"
    part_details["size"] = ["soic_14_wide","2d54_12_pin_two_rows"]
    part_details["color"] = [""]
    part_details["description_main"] = "basic"
    part_details["description_extra"] = ["helicopter","landing"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "J"
    parts.append(part_details)

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

    #### qwiic

    part_details = {}
    part_details["classification"] = "connector"
    part_details["type"] = "qwiic"
    part_details["size"] = ""
    part_details["color"] = [""]
    part_details["description_main"] = ""
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
    part_details["description_extra"] = ["","back_power_protected"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "J"
    parts.append(part_details)





    
    

    
    oomp.add_parts(parts, **kwargs)
    