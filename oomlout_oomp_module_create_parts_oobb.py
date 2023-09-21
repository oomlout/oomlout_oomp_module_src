import oomlout_oomp_module_src as oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []


    # oobb_connector
    part_details = {}
    part_details["classification"] = "connector"
    part_details["type"] = ""
    part_details["size"] = ["oobb_basic","oobb_ic"]
    part_details["color"] = [""]
    part_details["description_main"] = ["through_hole"]
    part_details["description_extra"] = ["single","double","triple"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "CON"
    parts.append(part_details)

   





    
    

    
    oomp.add_parts(parts, **kwargs)
    