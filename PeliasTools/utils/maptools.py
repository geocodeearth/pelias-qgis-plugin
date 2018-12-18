# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PeliasTools
                                 A QGIS plugin
 QGIS plugin to query Pelias endpoints from configurable sources.
                             -------------------
        begin                : 2019-01-05
        copyright            : (C) 2019 by Nils Nolde
        email                : nils@gis-ops.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os.path

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtWidgets import QApplication

from qgis.core import (QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform,
                       QgsProject)
from qgis.gui import QgsMapTool

from PeliasTools import ICON_DIR


class PointTool(QgsMapTool):   
    def __init__(self, canvas, button):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.button = button
        self.cursor = QCursor(QPixmap(os.path.join(ICON_DIR, 'icon_locate.png')).scaledToWidth(48), 24, 24)
    
    canvasClicked = pyqtSignal(['QgsPointXY', 'QString'])
    def canvasReleaseEvent(self, event):
        #Get the click and emit a transformed point

        crsSrc = self.canvas.mapSettings().destinationCrs()
            
        crsWGS = QgsCoordinateReferenceSystem(4326)
    
        point_oldcrs = event.mapPoint()
        
        xform = QgsCoordinateTransform(crsSrc, crsWGS, QgsProject.instance())
        point_newcrs = xform.transform(point_oldcrs)
        
        QApplication.restoreOverrideCursor()
        
        self.canvasClicked.emit(point_newcrs, self.button)

    def activate(self):
        QApplication.setOverrideCursor(self.cursor)
