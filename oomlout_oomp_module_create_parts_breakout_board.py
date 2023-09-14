import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    # ibbc
    part_details = {}
    part_details["classification"] = "breakout_board"
    part_details["type"] = "sensor"
    part_details["size"] = ["ibbc"]
    part_details["color"] = [""]
    part_details["description_main"] = ["oobb_3_2"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "BB"
    parts.append(part_details)

    # motor_driver
    #      stepper_motor
    part_details = {}
    part_details["classification"] = "breakout_board"
    part_details["type"] = "motor_driver"
    part_details["size"] = ["step_stick"]
    part_details["color"] = [""]
    part_details["description_main"] = ["stepper_motor"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "BB"
    parts.append(part_details)
    




    
    oomp.add_parts(parts, **kwargs)
    