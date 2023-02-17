from qgis.utils import iface
from qgis.core import *

layer = iface.activeLayer()
layer.startEditing()
features = layer.getFeatures()

for feature in features:
    # изменение атрибутов
    geom = feature.geometry()
    x = geom.asPoint().x()
    y = geom.asPoint().y()
    
    feature.setAttribute('x', x)
    feature.setAttribute('y', y)
    
    layer.updateFeature(feature)
    
    # перемещениие согласно атрибутам
    new_geom = QgsGeometry.fromPointXY(QgsPointXY(x,y))
    layer.dataProvider().changeGeometryValues({ feature.id() : new_geom })

layer.commitChanges()
