import oomlout_oomp_module_src as ooms




def main():
    #ooms.clone_data_files()
    filter = "power"
    filter = ""
    ooms.load_parts(from_yaml=False, make_files=True, filter=filter)
    ooms.save_parts()




if __name__ == "__main__":
    main()