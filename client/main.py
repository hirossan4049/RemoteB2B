import time
import rtmidi


midiin = rtmidi.MidiIn()
midiin.open_port(0)
print(midiin.get_ports())

class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()
        print("init")

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        print(','.join([f'{num}' for num in message]))
        # print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))

midiin.set_callback(MidiInputHandler(midiin.get_ports()[0]))

time.sleep(10000)

