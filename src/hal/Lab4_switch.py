from time import sleep, time
from hal import hal_input_switch as SW
from hal import hal_led as LED

#########################################
#
#    M A I N   P R O G R A M
#
#########################################
def main():
    # Initialize servo HAL driver
    LED.init()
    SW.init()

    while True:
        status = SW.read_slide_switch()  # Read position of slide switch
        if status == 0:
            # Turn off LED
            LED.set_output(0, 0)
            sleep(0.1)
            # Turn on LED
            LED.set_output(0, 1)
            sleep(0.1)
        else:
            # Turn off LED
            LED.set_output(0, 0)
            sleep(0.2)
            # Turn on LED
            LED.set_output(0, 1)
            sleep(0.2)

        # Check if the switch is in the right position
        if status == 0:
            # Blink the LED at 10 Hz for 5 seconds
            start_time = time()
            while time() - start_time < 5:
                LED.set_output(0, 1)  # Turn on the LED
                sleep(0.05)  # 1/10th of a second (10 Hz)
                LED.set_output(0, 0)  # Turn off the LED
                sleep(0.05)  # 1/10th of a second (10 Hz)
            # Break out of the loop after 5 seconds
            break

if _name_ == "_main_":
    main()