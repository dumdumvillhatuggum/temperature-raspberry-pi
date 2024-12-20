import argparse
import subprocess
from gpiozero import CPUTemperature
from time import sleep, strftime, time

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--timestamp', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-f', '--filename', action='store', default="cputemp.csv")
parser.add_argument('-p', '--path', action='store', default="")
args = parser.parse_args()

tmp = ""
if(args.path):
    if(args.path[-1] != "/"):
        tmp = "/"
FILE = args.path + tmp + args.filename

print("FILE: ", FILE)

if(args.verbose):
    print("Program started at " + strftime("%Y-%m-%d %H:%M:%S"))
    print("Arguments:")
    print("timestamp:", args.timestamp)
    print("verbose:", args.verbose)
    print("file: ", args.file)
    print()

def write_temp(temp):
    with open("cputemp.csv", "a") as log:
        if args.timestamp:
            lineToWrite = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp))
        else:
            lineToWrite = "{0}\n".format(str(temp))
        log.write(lineToWrite)
        # TODO if verbose print temp

write_temp(69)

ls = subprocess.run(["sysbench", "cpu", "run", "--threads=4", "--time=10"], shell=True, capture_output=True, text=True)
print(ls.stdout)

#while True:
#    temp = cpu.temperature
#    write_temp(temp)
#    sleep(1)
