import sys
import json
import argparse

file = open('topology.json', 'r')
try:
  topo = json.load(file)
except ValueError as e:
  print("Invalid json format in : %s Error: %s" % (file, e))
  sys.exit(1)

for cluster in topo['clusters']:
  for node in cluster['nodes']:
    print(str(node['node']['hostnames']['manage'][0]))
