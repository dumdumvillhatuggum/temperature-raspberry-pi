import argparse
from gpiozero import CPUTemperature
from time import sleep, strftime, time

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--timestamp', action='store_true')
#parser.add_argument('-o', '--output-dir')
args = parser.parse_args('-t'.split())

<<<<<<< Updated upstream
if(args.timestamp):
    print("flag recognozed")
else:
    print("no flag")
=======
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

print("Start stress")
def write_temp(temp):
    with open("cputemp.csv", "a") as log:
        if args.date:
            lineToWrite = "{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"      ",str(temp))
        else:
            lineToWrite = "{0}\n".format(str(temp))
        log.write(lineToWrite)
        # TODO if verbose print temp
print("End stress")
>>>>>>> Stashed changes

cpu = CPUTemperature()

def write_temp(temp):
    with open("cputemp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

while True:
    temp = cpu.temperature
    write_temp(temp)
    sleep(1)
