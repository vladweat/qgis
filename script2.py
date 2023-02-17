from qgis.utils import iface
from qgis.core import *

layer = iface.activeLayer()
features = layer.getFeatures()


def write_in_file(string: str) -> None:
    with open("C:\\Users\\konon\\OneDrive\\Рабочий стол\\Институт\\2022 Q1\\Программирование в ГИС\\Лабораторная 1\\file_red.txt", "a") as file:
        file.write(string)
    

for feature in features:
    if feature['color'] == "red":
        name = feature['name']
        geom = feature.geometry()
        x = geom.asPoint().x()
        y = geom.asPoint().y()
    
        data = f"{name}, {x}, {y} \n"
        write_in_file(data)
    else: pass

    