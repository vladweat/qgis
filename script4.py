from qgis.utils import iface
from qgis.core import *

layer = iface.activeLayer()

features = []
for x in range(2):
    for y in range(2):
        point = QgsPointXY(x, y)
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(point))
        features.append(feature)

layer.startEditing()
for feature in features:
    layer.addFeature(feature)
layer.commitChanges()

layer.triggerRepaint()
