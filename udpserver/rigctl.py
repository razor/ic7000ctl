import Hamlib, logging, time

class RigCtl:

    rig = None
    freq = 0

    def __init__(self):
        try:
            Hamlib.rig_set_debug(Hamlib.RIG_DEBUG_NONE)
            self.rig = Hamlib.Rig(Hamlib.__dict__['RIG_MODEL_IC7000'])  # Look up the model's numerical index in Hamlib's symbol dictionary.
            self.rig.set_conf("rig_pathname", '/dev/ttyUSB0')
            self.rig.set_conf("ptt_type", "RTS")
            self.rig.open()
        except:
            logging.error("Could not open a communication channel to the rig via Hamlib!")
            return
 
    def setFreq(self, freq):
        if freq == self.getFreq():
            return
        try:
            self.rig.set_freq(Hamlib.RIG_VFO_CURR, freq)
        except:
            logging.error("Could not set frequency")
            return
        try:
            self.rig.set_mode(Hamlib.RIG_MODE_USB, 2400)
        except:
            logging.error("Could not set mode")
            return
        logging.info("%s\tset to freq %s"%(time.asctime(), self.getMegaHerz(freq)))

    def getFreq(self):
        try:
            freq = self.rig.get_freq()
            (mode, width) = self.rig.get_mode()
        except:
            logging.error("Could not get freq and mode.")
            return
        return freq

    def getMegaHerz(self, freq):
        return "%.3fMHz"%(round(freq/1000000.0, 3))
 
    def close(self):
        self.rig.close()

