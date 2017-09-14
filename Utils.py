
from glob import glob
from os import path

class Loader:
    def __init__(self, iface):
        """Initialize using the qgis.utils.iface
        object passed from the console.

        """
        self.iface = iface

    def LoadBasemap(self):
        shp_path='U:/Basemap'
        shps = glob(path.join(shp_path, "*.shp"))
        for shp in shps:
            (shpdir, shpfile) = path.split(shp)
            layer = self.iface.addVectorLayer(shp, shpfile, 'ogr' )

    def LoadProb(self, shp_path):
        """Load all shapefiles found in shp_path"""
        print("Loading shapes from %s" % path.join(shp_path, "*.shp"))
        shps = glob(path.join(shp_path, "*.shp"))
        for shp in shps:
            (shpdir, shpfile) = path.split(shp)
            layer = self.iface.addVectorLayer(shp, shpfile, 'ogr' )
            layer.loadNamedStyle('/home/tito/Desktop/Oocpy/data/lixo.qml')
            layer.triggerRepaint()

    def LoadThickness(self, shp_path):
        """Load all shapefiles found in shp_path"""
        print("Loading shapes from %s" % path.join(shp_path, "*.shp"))
        shps = glob(path.join(shp_path, "*.shp"))
        for shp in shps:
            (shpdir, shpfile) = path.split(shp)
            layer = self.iface.addVectorLayer(shp, shpfile, 'ogr' )
            layer.loadNamedStyle('/home/tito/Desktop/Oocpy/data/lixo.qml')
            layer.triggerRepaint()
