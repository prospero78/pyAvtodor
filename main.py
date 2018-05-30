# -*- coding: utf-8 -*-

if True:
    import sys, random
    from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
    from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
    from PyQt5.QtGui import QPainter, QColor

class клсОкноТетрис(QMainWindow):
    def __init__(сам):
        QMainWindow.__init__(сам)
        сам.Окно_Настроить()

    def Окно_Настроить(сам):
        сам.доска = клсДоска(сам)
        сам.setCentralWidget(сам.доска)

        сам.статус_бар = сам.statusBar()
        сам.доска.msg2Statusbar[str].connect(сам.статус_бар.showMessage)

        сам.доска.Начать()

        сам.resize(180, 380)
        сам.Центр_Уст()
        сам.setWindowTitle('Тетрис')
        сам.show()

    def Центр_Уст(сам):
        экран = QDesktopWidget().screenGeometry()
        размер = сам.geometry()
        сам.move((экран.width()-размер.width())/2,
            (экран.height()-размер.height())/2)

class клсДоска(QFrame):
    msg2Statusbar = pyqtSignal(str)
    ширина = 10
    высота = 22
    скорость = 300

    def __init__(сам, родитель):
        QFrame.__init__(сам, родитель)
        сам.Доска_Настроить()

    def Доска_Настроить(сам):
        сам.таймер = QBasicTimer()
        сам.isWaitingAfterLine = False

        сам.curX = 0
        сам.curY = 0
        сам.numLinesRemoved = 0
        сам.board = []

        сам.setFocusPolicy(Qt.StrongFocus)
        сам.бРаботает = False
        сам.бПауза = False
        сам.__Очистить()

    def shapeAt(сам, x, y):
        return сам.board[(y * клсДоска.ширина) + x]

    def setShapeAt(сам, x, y, shape):
        сам.board[(y * клсДоска.ширина) + x] = shape

    def squareWidth(сам):
        return сам.contentsRect().width() // клсДоска.ширина

    def squareHeight(сам):
        return сам.contentsRect().height() // клсДоска.высота

    def Начать(сам):
        if сам.бПауза:
            return

        сам.бРаботает = True
        сам.isWaitingAfterLine = False
        сам.numLinesRemoved = 0
        сам.__Очистить()

        сам.msg2Statusbar.emit(str(сам.numLinesRemoved))

        сам.newPiece()
        сам.таймер.start(клсДоска.скорость, сам)

    def Приостановить(сам):
        if not сам.бРаботает:
            return
        
        сам.бПауза = not сам.бПауза
        
        if сам.бПауза:
            сам.таймер.stop()
            сам.msg2Statusbar.emit("paused")
        else:
            сам.таймер.start(Board.скорость, сам)
            сам.msg2Statusbar.emit(str(сам.numLinesRemoved))

        сам.update()

    def paintEvent(сам, event):
        painter = QPainter(сам)
        rect = сам.contentsRect()

        boardTop = rect.bottom() - клсДоска.высота * сам.squareHeight()

        for i in range(клсДоска.высота):
            for j in range(клсДоска.ширина):
                shape = сам.shapeAt(j, клсДоска.высота - i - 1)
                if shape != Tetrominoe.NoShape:
                    сам.drawSquare(painter,
                        rect.left() + j * сам.squareWidth(),
                        boardTop + i * сам.squareHeight(), shape)
        if сам.фиг_текущ.shape() != Tetrominoe.NoShape:
            for i in range(4):
                x = сам.curX + сам.фиг_текущ.x(i)
                y = сам.curY - сам.фиг_текущ.y(i)
                сам.drawSquare(painter, rect.left() + x * сам.squareWidth(),
                    boardTop + (клсДоска.высота - y - 1) * сам.squareHeight(),
                    сам.фиг_текущ.shape())

    def keyPressEvent(сам, event):
        if not сам.бРаботает or сам.фиг_текущ.shape() == Tetrominoe.NoShape:
            super(Board, сам).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_P:
            сам.Приостановить()
            return

        if сам.бПауза:
            return
        elif key == Qt.Key_Left:
            сам.tryMove(сам.фиг_текущ, сам.curX - 1, сам.curY)
        elif key == Qt.Key_Right:
            сам.tryMove(сам.фиг_текущ, сам.curX + 1, сам.curY)
        elif key == Qt.Key_Down:
            сам.tryMove(сам.фиг_текущ.Вращать_Право(), сам.curX, сам.curY)
        elif key == Qt.Key_Up:
            сам.tryMove(сам.фиг_текущ.Вращать_Лево(), сам.curX, сам.curY)
        elif key == Qt.Key_Space:
            сам.dropDown()
        elif key == Qt.Key_D:
            сам.oneLineDown()
        else:
            super(Board, сам).keyPressEvent(event)

    def timerEvent(сам, event):

        if event.timerId() == сам.таймер.timerId():

            if сам.isWaitingAfterLine:
                сам.isWaitingAfterLine = False
                сам.newPiece()
            else:
                сам.oneLineDown()

        else:
            super(Board, сам).timerEvent(event)

    def __Очистить(сам):
        for i in range(клсДоска.высота * клсДоска.ширина):
            сам.board.append(Tetrominoe.NoShape)

    def dropDown(сам):
        newY = сам.curY
        while newY > 0:
            if not сам.tryMove(сам.фиг_текущ, сам.curX, newY - 1):
                break
            newY -= 1
        сам.pieceDropped()

    def oneLineDown(сам):
        if not сам.tryMove(сам.фиг_текущ, сам.curX, сам.curY - 1):
            сам.pieceDropped()

    def pieceDropped(сам):
        for i in range(4):
            x = сам.curX + сам.фиг_текущ.x(i)
            y = сам.curY - сам.фиг_текущ.y(i)
            сам.setShapeAt(x, y, сам.фиг_текущ.shape())

        сам.removeFullLines()

        if not сам.isWaitingAfterLine:
            сам.newPiece()

    def removeFullLines(сам):
        numFullLines = 0
        rowsToRemove = []
        for i in range(клсДоска.высота):
            n = 0
            for j in range(клсДоска.ширина):
                if not сам.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1
            if n == 10:
                rowsToRemove.append(i)
        rowsToRemove.reverse()

        for m in rowsToRemove:
            for k in range(m, клсДоска.высота):
                for l in range(клсДоска.ширина):
                        сам.setShapeAt(l, k, сам.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)
        if numFullLines > 0:
            сам.numLinesRemoved = сам.numLinesRemoved + numFullLines
            сам.msg2Statusbar.emit(str(сам.numLinesRemoved))
            сам.isWaitingAfterLine = True
            сам.фиг_текущ.Фигура_Уст(Tetrominoe.NoShape)
            сам.update()

    def newPiece(сам):
        сам.фиг_текущ = клсФигуры()
        сам.фиг_текущ.ФигураСлуч_Уст()
        сам.curX = клсДоска.ширина // 2 + 1
        сам.curY = клсДоска.высота - 1 + сам.фиг_текущ.minY()

        if not сам.tryMove(сам.фиг_текущ, сам.curX, сам.curY):
            сам.фиг_текущ.Фигура_Уст(Tetrominoe.NoShape)
            сам.таймер.stop()
            сам.бРаботает = False
            сам.msg2Statusbar.emit("Game over")

    def tryMove(сам, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x < 0 or x >= клсДоска.ширина or y < 0 or y >= клсДоска.высота:
                return False
            if сам.shapeAt(x, y) != Tetrominoe.NoShape:
                return False
        сам.фиг_текущ = newPiece
        сам.curX = newX
        сам.curY = newY
        сам.update()

        return True

    def drawSquare(сам, painter, x, y, shape):

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, сам.squareWidth() - 2,
            сам.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + сам.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + сам.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + сам.squareHeight() - 1,
            x + сам.squareWidth() - 1, y + сам.squareHeight() - 1)
        painter.drawLine(x + сам.squareWidth() - 1,
            y + сам.squareHeight() - 1, x + сам.squareWidth() - 1, y + 1)

class Tetrominoe(object):

    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

class клсФигуры(object):
    табл_крд = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))   )

    def __init__(сам):
        сам.coords = [[0,0] for i in range(4)]
        сам.pieceShape = Tetrominoe.NoShape
        сам.Фигура_Уст(Tetrominoe.NoShape)

    def shape(сам):
        return сам.pieceShape

    def Фигура_Уст(сам, фигура):
        табл = клсФигуры.табл_крд[фигура]

        for i in range(4):
            for j in range(2):
                сам.coords[i][j] = табл[i][j]
        сам.pieceShape = фигура

    def ФигураСлуч_Уст(сам):
        сам.Фигура_Уст(random.randint(1, 7))

    def x(сам, index):
        return сам.coords[index][0]

    def y(сам, index):
        return сам.coords[index][1]

    def setX(сам, index, x):
        сам.coords[index][0] = x

    def setY(сам, index, y):
        сам.coords[index][1] = y

    def minX(сам):
        m = сам.coords[0][0]
        for i in range(4):
            m = min(m, сам.coords[i][0])
        return m

    def maxX(сам):
        m = сам.coords[0][0]
        for i in range(4):
            m = max(m, сам.coords[i][0])
        return m

    def minY(сам):
        m = сам.coords[0][1]
        for i in range(4):
            m = min(m, сам.coords[i][1])
        return m

    def maxY(сам):
        m = сам.coords[0][1]
        for i in range(4):
            m = max(m, сам.coords[i][1])
        return m

    def Вращать_Лево(сам):
        if сам.pieceShape == Tetrominoe.SquareShape:
            return сам
        result = клсФигуры()
        result.pieceShape = сам.pieceShape
        for i in range(4):
            result.setX(i, сам.y(i))
            result.setY(i, -сам.x(i))
        return result

    def Вращать_Право(сам):
        if сам.pieceShape == Tetrominoe.SquareShape:
            return сам

        result = клсФигуры()
        result.pieceShape = сам.pieceShape

        for i in range(4):
            result.setX(i, -сам.y(i))
            result.setY(i, сам.x(i))

        return result

if __name__ == '__main__':
    приложение = QApplication([])
    тетрис = клсОкноТетрис()
    sys.exit(приложение.exec_())
