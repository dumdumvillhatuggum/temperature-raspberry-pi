import argparse
from gpiozero import CPUTemperature
from time import sleep, strftime, time

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--timestamp', action='store_true')
#parser.add_argument('-o', '--output-dir')
args = parser.parse_args('-t'.split())

if(args.timestamp):
    print("flag recognozed")
else:
    print("no flag")

cpu = CPUTemperature()

def write_temp(temp):
    with open("cputemp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

while True:
    temp = cpu.temperature
    write_temp(temp)
    sleep(1)
