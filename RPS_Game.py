import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from random import randint
from PyQt5.QtGui import QPixmap, QFont

labelFont = QFont("Times", 14)
compPoint = 0
playerPoint = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle("ROCK PAPER SCISSORS GAME")
        self.ui()

    def ui(self):
        self.choice = 0
        wallpaper = QLabel(self)
        wallpaper.setStyleSheet(
            "background-image : url(images/bgwall.jpg); background-repeat: no-repeat; background-position: center;")
        wallpaper.resize(810, 510)
        self.compScore = QLabel("Computer score: 0", self)
        self.compScore.setFont(labelFont)
        self.compScore.setStyleSheet("background-color: red")
        self.compScore.move(570, 50)
        self.yourScore = QLabel("Your score: 0", self)
        self.yourScore.setStyleSheet("background-color: blue")
        self.yourScore.setFont(labelFont)
        self.yourScore.move(120, 50)
        startup = QPushButton("START", self)
        startup.move(300, 300)
        startup.setFont(labelFont)
        startup.setStyleSheet("background-color: green")
        startup.clicked.connect(self.begin)
        stops = QPushButton("STOP", self)
        stops.move(430, 300)
        stops.setFont(labelFont)
        stops.setStyleSheet("background-color: red")
        stops.clicked.connect(self.ending)
        vsimage = QLabel(self)
        vsimage.setPixmap(QPixmap("images/vspic.jpg"))
        vsimage.resize(100, 100)
        vsimage.move(360, 150)
        self.rock_button = QPushButton("ROCK", self)
        self.rock_button.move(200, 400)
        self.rock_button.setFont(labelFont)
        self.rock_button.clicked.connect(self.rock)
        self.paper_button = QPushButton("PAPER", self)
        self.paper_button.move(350, 400)
        self.paper_button.setFont(labelFont)
        self.paper_button.clicked.connect(self.paper)
        self.scissor_button = QPushButton("SCISSOR", self)
        self.scissor_button.move(500, 400)
        self.scissor_button.setFont(labelFont)
        self.scissor_button.clicked.connect(self.scissor)
        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("images/rock.jpg"))
        self.imagePlayer.move(100, 100)
        self.imageComp = QLabel(self)
        self.imageComp.setPixmap(QPixmap("images/rock.jpg"))
        self.imageComp.move(530, 100)
        self.timer = QTimer(self)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.startgame)
        self.show()

    def rock(self):
        self.choice = 1
        self.imagePlayer.setPixmap(QPixmap("images/rock.jpg"))
        self.rock_button.setDisabled(True)
        self.paper_button.setDisabled(True)
        self.scissor_button.setDisabled(True)

    def paper(self):
        self.choice = 2
        self.imagePlayer.setPixmap(QPixmap("images/paper.jpg"))
        self.rock_button.setDisabled(True)
        self.paper_button.setDisabled(True)
        self.scissor_button.setDisabled(True)

    def scissor(self):
        self.choice = 3
        self.imagePlayer.setPixmap(QPixmap("images/scissors.jpg"))
        self.rock_button.setDisabled(True)
        self.paper_button.setDisabled(True)
        self.scissor_button.setDisabled(True)

    def startgame(self):
        self.rndComp = randint(1, 3)

        if self.rndComp == 1:
            self.imageComp.setPixmap(QPixmap("images/rock.jpg"))
        elif self.rndComp == 2:
            self.imageComp.setPixmap(QPixmap("images/paper.jpg"))
        else:
            self.imageComp.setPixmap(QPixmap("images/scissors.jpg"))

    def begin(self):
        self.timer.start()

    def ending(self):
        self.rock_button.setEnabled(True)
        self.paper_button.setEnabled(True)
        self.scissor_button.setEnabled(True)
        global compPoint
        global playerPoint
        self.timer.stop()
        if self.rndComp == self.choice:
            mbox = QMessageBox.information(self, "INFORMATION", "DRAW GAME")
        else:
            if self.rndComp == 1:
                if self.choice == 2:
                    mbox = QMessageBox.information(self, "INFORMATION", "YOU WIN")
                    playerPoint += 1
                    self.yourScore.setText("Your score:{}".format(playerPoint))
                else:
                    mbox = QMessageBox.information(self, "INFORMATION", "COMPUTER WINS")
                    compPoint += 1
                    self.compScore.setText("Computer score:{}".format(compPoint))
            elif self.rndComp == 2:
                if self.choice == 3:
                    mbox = QMessageBox.information(self, "INFORMATION", "YOU WIN")
                    playerPoint += 1
                    self.yourScore.setText("Your score:{}".format(playerPoint))
                else:
                    mbox = QMessageBox.information(self, "INFORMATION", "COMPUTER WINS")
                    compPoint += 1
                    self.compScore.setText("Computer score:{}".format(compPoint))
            elif self.rndComp == 3:
                if self.choice == 1:
                    mbox = QMessageBox.information(self, "INFORMATION", "YOU WIN")
                    playerPoint += 1
                    self.yourScore.setText("Your score:{}".format(playerPoint))
                else:
                    mbox = QMessageBox.information(self, "INFORMATION", "COMPUTER WINS")
                    compPoint += 1
                    self.compScore.setText("Computer score:{}".format(compPoint))

            if compPoint == 3 or playerPoint == 3:
                if compPoint > playerPoint:
                    mbox = QMessageBox.information(self, "INFORMATION", "GAME OVER COMPUTER WON")
                    fbox = QMessageBox.question(self, "INFORMATION", "WANNA PLAY AGAIN??", QMessageBox.Yes | QMessageBox.No)
                    if fbox == QMessageBox.Yes:
                        compPoint = 0
                        playerPoint = 0
                        self.compScore.setText("Computer score:{}".format(compPoint))
                        self.yourScore.setText("Your score:{}".format(playerPoint))
                    else:
                        sys.exit()

                else:
                    mbox = QMessageBox.information(self, "INFORMATION", "GAME OVER YOU WON")
                    fbox = QMessageBox.question(self, "INFORMATION", "WANNA PLAY AGAIN??", QMessageBox.Yes | QMessageBox.No)
                    if fbox == QMessageBox.Yes:
                        compPoint = 0
                        playerPoint = 0
                        self.compScore.setText("Computer score:{}".format(compPoint))
                        self.yourScore.setText("Your score:{}".format(playerPoint))
                    else:
                        sys.exit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
