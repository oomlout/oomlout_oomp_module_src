import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    #      button
    part_details = {}
    part_details["classification"] = "button"
    part_details["type"] = "reset"
    part_details["size"] = ["3_5_mm_x_6_mm_x_2_5_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "B"
    parts.append(part_details)

    #      switch
    
    #            single_pole_double_throw"
    part_details = {}
    part_details["classification"] = "switch_slide"
    part_details["type"] = "single_pole_double_throw"
    part_details["size"] = ["2d54_header", "2_8_mm_x_8_mm_x_1_4"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "B"
    parts.append(part_details)

    oomp.add_parts(parts, **kwargs)
    