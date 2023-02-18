from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(second):
    time_elapsd = 0
    print(CLEAR)
    while time_elapsd < second:
        time.sleep(1)
        time_elapsd += 1

        time_left = second - time_elapsd
        minutes_left = time_left // 60
        second_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURN} Alarm will Sound in: {minutes_left:02d}:{second_left:02d}")
    playsound("Alarm_Sound.wav")


minutes = int(input("Minutes to Wait: "))
seconds = int(input("Seconds to Wait: "))

total_time = minutes * 60 + seconds
alarm(total_time)
