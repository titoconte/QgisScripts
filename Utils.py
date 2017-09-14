
from glob import glob
from os import path

class Loader:
    def __init__(self, iface):
        """Initialize using the qgis.utils.iface
        object passed from the console.

        """
        self.iface = iface

    def load_shapefiles(self, shp_path):
        """Load all shapefiles found in shp_path"""
        print "Loading shapes from %s" % path.join(shp_path, "*.shp")
        shps = glob(path.join(shp_path, "*.shp"))
        for shp in shps:
            (shpdir, shpfile) = path.split(shp)
            self.iface.addVectorLayer(shp, shpfile, 'ogr' )