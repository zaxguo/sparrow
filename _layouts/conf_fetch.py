#!/usr/bin/python3
import pandas as pd
import json

class conf:
    def __init__(self, id, name, ddl, where):
        self.id   = id
        self.content = name
        self.start = ddl
        self.where = where
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                          sort_keys=True, indent=4)
    def __str__(self):
        return "{id: " + self.id + ", content: " + self.name + ", start: '" + self.ddl + "'},\n" 

url = r'http://www.cs.technion.ac.il/~dan/index_sysvenues_deadline.html'
tables = pd.read_html(url) # Returns list of all tables on page
conf_table = tables[4] # Select table of interest
skip_first = True
confs = []
id = 1
for rows in conf_table.iterrows():
    if skip_first:
        skip_first = False
        continue
    bundle  = rows[1]
    name    = bundle[1]
    ddl     = bundle[2].split(' ')[0]
    where   = bundle[2].split(' ')[-1]
    if ddl != '-':
        conf_ = conf(id, name, ddl, where)
        id      += 1
        confs.append(conf_)

# generate data 
f = open("conf.json", "w") 
f.write("[\n")
for conf in confs:
    print(json.dumps(conf.__dict__))
    f.write(json.dumps(conf.__dict__))
    if conf != confs[-1]:
        f.write(',')
    f.write('\n')
f.write("]")
