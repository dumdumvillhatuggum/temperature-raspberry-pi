import argparse
import subprocess
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
args = parser.parse_args()

SECONDS_CONST = args.seconds
STRESS_COMMAND = ["sysbench", "cpu", "run", 
"--threads=" + args.threads, 
"--time=" + args.seconds
]

tmp = ""
if(args.path):
    if(args.path[-1] != "/"):
        tmp = "/"
FILE = args.path + tmp + args.filename

if(args.verbose):
    print("Program started at " + strftime("%Y-%m-%d %H:%M:%S"))
    print("Arguments:")
    print("date:", args.date)
    print("verbose:", args.verbose)
    print("file: ", args.file)
    print()

def write_temp(temp):
    with open("cputemp.csv", "a") as log:
        if args.date:
            lineToWrite = "{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"      ",str(temp))
        else:
            lineToWrite = "{0}\n".format(str(temp))
        log.write(lineToWrite)
        # TODO if verbose print temp

cpu = CPUTemperature()

write_temp("Start stress")
ls = subprocess.Popen(STRESS_COMMAND,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(ls.stdout)
write_temp("End stress")

i = 0
while (i <= SECONDS_CONST):
    temp = cpu.temperature
    write_temp(temp)
    i += 1
    sleep(1)
