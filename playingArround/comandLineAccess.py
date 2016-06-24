#https://docs.python.org/2/library/subprocess.html
#http://cmdlinetips.com/2014/03/how-to-run-a-shell-command-from-python-and-get-the-output/
import subprocess

print("I print before")

subprocess.Popen(['ls', '-al'])
# the cmd calls will be executed one after another
# and nothing in between these will be
# printed or executed at this point.  they either
# happen before or after the command line calls
print("I print before")
subprocess.call(["ls", "-al"])

print("I print after")
