import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    
    ###### ch340
    models = []
    models.append(["c", "sop_16"])    
    models.append(["g", "sop_16"])
    models.append(["b", "sop_16"])
    models.append(["t", "ssop_20"])
    models.append(["e", "msop_10"])
    models.append(["x", "msop_10"])
    #models.append(["k", "sop_16"])

                  
    for model in models:
        #define a part 
        mod = model[0]
        size = model[1]
        part_details = {}
        part_details["classification"] = "ic"
        part_details["type"] = "usb_to_serial_bridge"
        part_details["size"] = f"{size}"
        part_details["color"] = ""
        part_details["description_main"] = ["5_volt","3_3_volt"]
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = f"ch340{mod}"
        part_details["kicad_reference"] = "U"
        parts.append(part_details)


    #      rs22227 usb 2 to 1 multiplexer

    part_details = {}
    part_details["classification"] = "ic"
    part_details["type"] = "usb_multiplexer"
    part_details["size"] = f"msop_10"
    part_details["color"] = ""
    part_details["description_main"] = "two_to_one"
    part_details["manufacturer"] = ""
    part_details["part_number"] = "rs2227xn"
    part_details["kicad_reference"] = "U"
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    