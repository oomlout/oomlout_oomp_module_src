import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    part_details = {}
    part_details["classification"] = "led"
    part_details["type"] = ""
    part_details["size"] = ["0603"]
    part_details["color"] = ["red"]
    part_details["description_main"] = ["2_leds", "4_leds", "100_leds", "200_leds"]
    part_details["description_extra"] = ["common_ground", "common_supply", "common_supply_and_common_ground_no_resistors"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "R"



    #add the part to the list of parts
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    