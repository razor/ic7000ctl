from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
import Hamlib, logging, time

freqTab = { "b160m":1840000, "b80m":3573000, "b40m":7074000, "b30m":10136000, "b20m":14074000, "b17m":18100000, "b15m":21074000, "b12m":24915000, "b10m":28047000, "b6m":50313000,"b6m2":50323000}

logging.Logger.setLevel(logging.getLogger(), logging.INFO)
app = QApplication([])
statusLabel = QLabel("Status")
b160m = QPushButton('160m 1.840MHz')
b80m = QPushButton('80m 3.573MHz')
b40m = QPushButton('40m 7.074MHz')
b30m = QPushButton('30m 10.136MHz')
b20m = QPushButton('20m 14.074MHz')
b17m = QPushButton('17m 18.100MHz')
b15m = QPushButton('15m 21.074MHz')
b12m = QPushButton('12m 24.915MHz')
b10m = QPushButton('10m 28.074MHz')
b6m = QPushButton('6m 50.313MHz')
b6m2 = QPushButton('6m 50.323MHz')


def initMain():
    window = QWidget()
    window.setWindowTitle('Set IC-7000')
    layout = QVBoxLayout()
    layout.addWidget(statusLabel)
    viewBottom = QWidget()
    layoutBottom = QGridLayout()
    layoutBottom.addWidget(b160m)
    layoutBottom.addWidget(b80m)
    layoutBottom.addWidget(b40m)
    layoutBottom.addWidget(b30m)
    layoutBottom.addWidget(b20m)
    layoutBottom.addWidget(b17m)
    layoutBottom.addWidget(b15m)
    layoutBottom.addWidget(b12m)
    layoutBottom.addWidget(b10m)
    layoutBottom.addWidget(b6m)
    layoutBottom.addWidget(b6m2)

    viewBottom.setLayout(layoutBottom)
    layout.addWidget(viewBottom)

    window.setLayout(layout)
    window.show()

    getRigStatus()
    app.exec_()

def setFreq(freq):
    try:
        Hamlib.rig_set_debug(Hamlib.RIG_DEBUG_NONE)
        rig = Hamlib.Rig(Hamlib.__dict__['RIG_MODEL_IC7000'])  # Look up the model's numerical index in Hamlib's symbol dictionary.
        rig.set_conf("rig_pathname", '/dev/ttyUSB0')
        rig.set_conf("ptt_type", "RTS")
        rig.open()
    except:
        logging.error("Could not open a communication channel to the rig via Hamlib!")
        return
    try:
        rig.set_freq(Hamlib.RIG_VFO_CURR, freq)
    except:
        logging.error("Could not set frequency")
        return
    try:
        rig.set_mode(Hamlib.RIG_MODE_USB, 2400)
    except:
        logging.error("Could not set mode")
        return
    logging.info("%s\tset to freq %s"%(time.asctime(), getMegaHerz(freq)))
    rig.close()
    getRigStatus()
   
def tune160m():
    setFreq(freqTab['b160m'])

def tune80m():
    setFreq(freqTab['b80m'])


def tune40m():
    setFreq(freqTab['b40m'])


def tune30m():
    setFreq(freqTab['b30m'])


def tune20m():
    setFreq(freqTab['b20m'])


def tune17m():
    setFreq(freqTab['b17m'])

def tune15m():
    setFreq(freqTab['b15m'])

def tune12m():
    setFreq(freqTab['b12m'])

def tune10m():
    setFreq(freqTab['b10m'])


def tune6m():
    setFreq(freqTab['b6m'])

def tune6m2():
    setFreq(freqTab['b6m2'])

def getMegaHerz(freq):
    return "%.3fMHz"%(round(freq/1000000.0, 3))

def getRigStatus():
    try:
        Hamlib.rig_set_debug(Hamlib.RIG_DEBUG_NONE)
        rig = Hamlib.Rig(Hamlib.__dict__['RIG_MODEL_IC7000'])  # Look up the model's numerical index in Hamlib's symbol dictionary.
        rig.set_conf("rig_pathname", '/dev/ttyUSB0')
        rig.set_conf("ptt_type", "RTS")
        rig.open()
    except:
        logging.error("Could not open a communication channel to the rig via Hamlib!")
        return
    try:
        freq = rig.get_freq()
        (mode, width) = rig.get_mode()
    except:
        logging.error("Could not get freq and mode.")
        return
    rig.close()
    statusLabel.setText("Freq: %s"%(getMegaHerz(freq)))


b160m.clicked.connect(tune160m)
b80m.clicked.connect(tune80m)
b40m.clicked.connect(tune40m)
b30m.clicked.connect(tune30m)
b20m.clicked.connect(tune20m)
b17m.clicked.connect(tune17m)
b15m.clicked.connect(tune15m)
b12m.clicked.connect(tune12m)
b10m.clicked.connect(tune10m)
b6m.clicked.connect(tune6m)
b6m2.clicked.connect(tune6m2)

initMain()
