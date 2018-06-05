import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, \
    QHBoxLayout, QVBoxLayout, QGroupBox, QSpinBox, QLabel, QFormLayout, QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from subprocess import call
from shutil import copy
import os
from csvReader import processCSV
from csvWriter import processGeneratedCsv


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 30
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

        self.csvName = ""

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        open_csv_button = QPushButton('Load CSV/MIDI')
        open_csv_button.clicked.connect(self.openCsvMidiDialog)

        seq_length_label = QLabel("seq_length")
        self.seq_length_spin = QSpinBox()
        self.seq_length_spin.setRange(1, 64)

        epoch_label = QLabel("epoch")
        self.epoch_spin = QSpinBox()
        self.epoch_spin.setRange(50, 200)

        batch_size_label = QLabel("batch_size")
        self.batch_size_combo = QComboBox()
        self.batch_size_combo.addItems(["32", "64", "128", "256"])

        train_button = QPushButton('TRAIN')
        train_button.clicked.connect(self.train)

        load_train_file_button = QPushButton('Load HDF5')
        load_train_file_button.clicked.connect(self.openHdf5Dialog)

        song_length_label = QLabel("Song Length (s)")
        self.song_length_spin = QSpinBox()
        self.song_length_spin.setMinimum(1)

        song_name_label = QLabel("Song Name")
        self.song_name_le = QLineEdit()

        generate_button = QPushButton('GENERATE')
        generate_button.clicked.connect(self.generate)

        train_group = QGroupBox("Train")
        generate_group = QGroupBox("Generate")

        hbox = QHBoxLayout()
        hbox.addWidget(train_group)
        hbox.addWidget(generate_group)

        train_vbox = QFormLayout()
        train_vbox.addWidget(open_csv_button)
        train_vbox.addRow(seq_length_label,self.seq_length_spin)
        train_vbox.addRow(epoch_label, self.epoch_spin)
        train_vbox.addRow(batch_size_label, self.batch_size_combo)
        train_vbox.addWidget(train_button)

        train_group.setLayout(train_vbox)

        generate_vbox = QFormLayout()
        generate_vbox.addWidget(load_train_file_button)
        generate_vbox.addRow(song_length_label, self.song_length_spin)
        generate_vbox.addRow(song_name_label, self.song_name_le)
        generate_vbox.addWidget(generate_button)

        generate_group.setLayout(generate_vbox)






        self.setLayout(hbox)

        self.show()

    @pyqtSlot()
    def train(self):
        print("training")

    @pyqtSlot()
    def generate(self):
        print("generating")
        songName = self.song_name_le.text()
        if not songName.endswith(".csv"):
            songName = songName + ".csv"
        midiName = songName.split('.')[0]+".mid"
        processGeneratedCsv(songName)
        if call("csvmidi data/processed_generated/" + songName + " data/processed_midi/" + midiName) == 0:
            print("csv file converted into " + midiName)
            filePath = str(QFileDialog.getExistingDirectory(self, "Select Save Directory"))
            if filePath and not os.path.isfile(filePath + midiName):
                copy(os.getcwd() + "\\data\\processed_midi\\" + midiName, filePath)
                print("midi file " + midiName + " saved to folder " + filePath)
            else:
                print("no directory selected or file already exists")

        else:
            print("csv to midi conversion failed")


    @pyqtSlot()
    def openCsvMidiDialog(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "MIDI Sequence (*.mid);;CSV Files (*.csv)")
        if filePath:
            self.fileName = filePath.split('/')[-1].split('.')[0] + ".csv"
            if filePath[-4:] == ".mid":
                self.convertMidiToCsv(filePath)
            else:
                if not os.path.isfile("data\\raw_csv\\" + self.fileName):
                    copy(filePath, os.getcwd() + "\\data\\raw_csv")
                    print("csv file " + self.fileName + " copied to data folder")
            processCSV(self.fileName)

    def openHdf5Dialog(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "MIDI Sequence (*.mid);;CSV Files (*.csv)")
        if filePath:
            print('hdf5 file loaded')

    def convertMidiToCsv(self, filePath):
        midiFileName = filePath.split('/')[-1]
        genericFileName = midiFileName.split('.')[0]
        csvFileName = genericFileName + ".csv"

        if not os.path.isfile("data\\raw_midi\\" + midiFileName):
            copy(filePath, os.getcwd() + "\\data\\raw_midi")
            print("midi file " + midiFileName + " copied to data folder")
        if call("midicsv data/raw_midi/" + midiFileName + " data/raw_csv/" + csvFileName) == 0:
            print("midi file converted into " + csvFileName)
        else:
            print("midi to csv conversion failed")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())