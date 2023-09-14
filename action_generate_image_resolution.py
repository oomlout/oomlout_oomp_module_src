import oom_base



def main():
    #go through all files in symbols/    
    directory = "modules"
    overwrite = True
    oom_base.image_resolutions_dir(directory=directory, overwrite=overwrite)



if __name__ == '__main__':
    main()