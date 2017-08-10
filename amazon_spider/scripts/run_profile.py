import subprocess
import sys


p = subprocess.Popen('scrapy crawl profile -a asin=%s -o profile.json -L DEBUG' % sys.argv[1],
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line)

p.wait()