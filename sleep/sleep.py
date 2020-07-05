import scipy.io.wavfile as scw
import sounddevice as sd
from time import sleep
from random import randint
import sys




f_sample_rate, full_alarm = scw.read(
    "full_alarm.wav")

t_sample_rate, truncated_alarm = scw.read(
    "truncated_alarm.wav")




def block():

    sleep(14400)

    sd.play(full_alarm)
    sd.wait()

    while True:

        sleep(
            randint(
                1, 5401))

        sd.play(truncated_alarm)
        sd.wait()




def wbtb():

    while True:

        sleep(
            randint(
                1, 5401))

        sd.play(truncated_alarm)
        sd.wait()




if __name__ == "__main__":

    try:

        mode = sys.argv[1]

        globals()[mode]()

    except Exception as error:

        print(
            "ERROR", 
            "\n" *2, 
            error)




