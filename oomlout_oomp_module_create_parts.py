
import importlib
import oomlout_oomp_module_src as oomp

part_types = []

part_types.append("connector")
part_types.append("crystal")
part_types.append("ic")
part_types.append("led")
part_types.append("mcu")
part_types.append("power")


for type in part_types:
    importlib.import_module(f'oomlout_oomp_module_create_parts_{type}')

def load_parts(**kwargs):
    print("loading parts from modules")
    for type in part_types:
        importlib.import_module(f'oomlout_oomp_module_create_parts_{type}').load_parts(**kwargs)


def load_parts_from_yaml(**kwargs):
    print("loading parts from yaml")
    import yaml
    with open("parts.yaml", "r") as infile:
        parts = yaml.load(infile, Loader=yaml.FullLoader)
    oomp.parts = parts

def save_parts_to_yaml(**kwargs):
    print("saving parts to yaml")
    import yaml
    with open("parts.yaml", "w") as outfile:
        yaml.dump(oomp.parts, outfile, indent=4)