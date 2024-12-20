from gpiozero import CPUTemperature
from time import sleep, strftime, time

cpu = CPUTemperature()

def write_temp(temp):
    with open("/home/huser/my-fanshim/templog/cputemp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

while True:
    temp = cpu.temperature
    write_temp(temp)
