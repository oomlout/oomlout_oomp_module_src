

def main(**kwargs):
    
    import action_generate_readme
    print("Generating Readme")
    action_generate_readme.main()

    import action_generate_image_resolution
    print("Generating Image Resolution")
    action_generate_image_resolution.main()

    import action_generate_kicad_outputs
    #print("Generating KiCad Outputs")
    #action_generate_kicad_outputs.main()

    import action_generate_doc
    print("Generating Doc")
    action_generate_doc.main()




if __name__ == '__main__':
    main()