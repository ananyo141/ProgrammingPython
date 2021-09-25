# communicate between two python scripts with pipe
# python writer.py | python reader.py
import sys
print("Got this '%s' from the writer script" % input())
num = sys.stdin.readline()[:-1] # discard the final eol character
print(int(num))
