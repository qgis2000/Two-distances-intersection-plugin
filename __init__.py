# -*- coding: utf-8 -*-
# __init__.py  -  A Python Plugin Two distances intersection for QGIS
#     begin             : 2023-07-18
#     version           : 1.0.11
#.....version date......: 2023-08-21
#     author            : Szymon Kędziora

def classFactory(iface):
    from .twoDistancesIntersectionPlugin import TwoDistancesIntersectionPlugin
    return TwoDistancesIntersectionPlugin(iface)


