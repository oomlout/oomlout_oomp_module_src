import oom_kicad
import os

def go_through_directories():
    # go through all directories in projects
    for root, dirs, files in os.walk("modules"):
        #go through all files


 
  
   
    
     
        for file in files:
            #check for a brd file
            
            filename = os.path.join(root, file)
            filter = ["npoole"]
            #make filter all lower case
            filter = [x.lower() for x in filter]
            filter = [""]
            #if any of filter is in filename
            if any(x in filename.lower() for x in filter):
                if file.endswith(".kicad_pcb"):
                    oom_kicad.generate_outputs(filename=filename, overwrite=True)


if __name__ == '__main__':
    go_through_directories()