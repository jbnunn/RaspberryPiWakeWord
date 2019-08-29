from sense_hat import SenseHat

import time
import logging
import sys

sense = SenseHat()

sense.set_rotation(180)
#sense.show_message("Hello World")

red = (255, 0, 0)

# sense.clear(red)
# time.sleep(2)
# sense.clear(off)

from agt import AlexaGadget

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

class WakewordGadget(AlexaGadget):
    """
    An Alexa Gadget that turns an LED on and off in sync with the detection
    of the wake word
    """

    def __init__(self):
        super().__init__(gadget_config_path='./wakeword.ini')

    def on_alexa_gadget_statelistener_stateupdate(self, directive):
        for state in directive.payload.states:
            if state.name == 'wakeword':
                if state.value == 'active':
                    logger.info('Wake word active - turn on LED')
                    sense.clear(red)
                elif state.value == 'cleared':
                    logger.info('Wake word cleared - turn off LED')
                    sense.clear()

if __name__ == '__main__':
    try:
        print("Attempting")
        WakewordGadget().main()
    finally:
        logger.debug('Cleaning up')
        sense.clear()
