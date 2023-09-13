import os
import oom_yaml


file_list = []
file_list.append(f"working.yaml")
file_list.append(f"readme.md")
file_list.append(f"kicad/current_version/working/working_schematic_600.png")
file_list.append(f"kicad/current_version/working/working_schematic.pdf")
file_list.append(f"kicad/current_version/working/working_3d_600.png")
file_list.append(f"kicad/current_version/working/working_3d_front_600.png")
file_list.append(f"kicad/current_version/working/working_3d_back_600.png")
file_list.append(f"kicad/current_version/working/working_600.png")
file_list.append(f"kicad/current_version/working/working.pdf")


dir_doc_base = "C:/GH/oomlout_oomp_module_doc_v_2/modules"

def main(**kwargs):
    global file_list
    #iterate through all the directories in projects
    directory = "modules"    
    directories = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    for dir in directories:
        dir_src = f"{dir}/working"
        print(f"Generating docs for {dir_src}")
        yaml_dict = oom_yaml.load_yaml_directory(directory=f"{dir_src}")        
        pass
        classification = yaml_dict.get('classification', "")
        typ = yaml_dict.get('type', "")
        size = yaml_dict.get('size', "")
        color = yaml_dict.get('color', "")
        description_main = yaml_dict.get('description_main', "")
        description_extra = yaml_dict.get('description_extra', "")
        manufacturer = yaml_dict.get('manufacturer', "")
        part_number = yaml_dict.get('part_number', "")
        order = [classification, typ, size, color, description_main, description_extra, manufacturer, part_number]
        if typ == "ic":
            order = [classification, typ, color, description_main, description_extra, size, manufacturer, part_number]
        dir_level = ""
        for level in range(len(order)):
            #last_level test, see if the remaining levels are all empty
            level_value = order[level]
            last_level = True
            for level2 in range(level+1, len(order)):
                if order[level2] != "":
                    last_level = False
                    break
            if level_value == "":
                level_value = "blank"
            dir_level += f"/{level_value}"
            if last_level:
                break

        dir_dst = f"{dir_doc_base}/{dir_level}"

        for filename in file_list:
            #copy files across
            src = f"{dir_src}/{filename}"
            dst = f"{dir_dst}/{filename}"
            print(f"Copying {src} to {dst}")
            import shutil
            #if dst directory doesn't exist create it
            
            #if src exists
            if os.path.exists(src):   
                if not os.path.exists(os.path.dirname(dst)):
                    os.makedirs(os.path.dirname(dst))             
                shutil.copyfile(src, dst)
            else:
                pass
                #print(f"Warning: {src} doesn't exist")
        pass






if __name__ == '__main__':
    main()