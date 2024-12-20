import argparse
import glob
import subprocess
import threading
import multiprocessing
from gpiozero import CPUTemperature
from time import sleep, strftime, time

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--date', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-f', '--filename', action='store', default="cputemp.csv")
parser.add_argument('-p', '--path', action='store', default="")
parser.add_argument('-t', '--threads', action='store', default=str(multiprocessing.cpu_count()))
parser.add_argument('-s', '--seconds', action='store', default="10")
parser.add_argument('-c', '--cooldown', action='store', default="2")
parser.add_argument('-b', '--beginoffset', action='store', default="2")
args = parser.parse_args()

SECONDS_CONST = int(args.seconds)
STRESS_COMMAND = ["sysbench", "cpu", "run", 
"--threads=" + args.threads, 
"--time=" + args.seconds
]

def ts():
    return strftime("%Y-%m-%d %H:%M:%S")

def run_stress(command, delay):
    print(ts() + "Sleeping for " + args.beginoffset + " seconds (beginoffset)")
    sleep(int(args.beginoffset))

    print(ts() + "Beggining stress test now")
    stress_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    stdout, stderr = stress_process.communicate()
    if(args.verbose):
        print("-------------")
        print("stdout:")
        print(stdout)
        print("-------------")
        print("stderr:")
        print(stderr)

tmp = ""
if(args.path):
    if(args.path[-1] != "/"):
        tmp = "/"
FILE = args.path + tmp + args.filename

if(args.verbose):
    print("Program started at " + ts())
    print("Arguments:")
    print("date:", args.date)
    print("verbose:", args.verbose)
    print("file: ", args.filename)
    print()

def write_temp(temp):
    with open("cputemp.csv", "a") as log:
        if args.date:
            lineToWrite = "{0} {1},".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp))
        else:
            lineToWrite = "{0},".format(str(temp))
        log.write(lineToWrite)

cpu = CPUTemperature()

stress_thread = threading.Thread(target=run_stress, args=(STRESS_COMMAND, args.beginoffset))
stress_thread.start()

i = 0
print(ts() + "Starting logging")
while (i <= SECONDS_CONST):
    temp = cpu.temperature
    write_temp(temp)
    i += 1
    sleep(1)
print(ts() + "Stopped logging at " + " after " + str(i) + " seconds")

print(ts() + "Sleeping for " + args.cooldown + " seconds (cooldown)")
sleep(int(args.beginoffset))
