from qgis.utils import iface
from qgis.core import *

layer = iface.activeLayer()
features = layer.getFeatures()

delete_ids = []

for feature in features:
    point = feature.geometry().asPoint()
    if point.x() < 0 or point.y() < 0:
        delete_ids.append(feature.id())
        
        
if delete_ids:
    layer.startEditing()
    layer.deleteFeatures(delete_ids)
    layer.commitChanges()