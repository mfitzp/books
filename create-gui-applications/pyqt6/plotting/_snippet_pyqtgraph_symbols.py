pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.PenStyle.DashLine)
self.graphWidget.plot(hour, temperature, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))
