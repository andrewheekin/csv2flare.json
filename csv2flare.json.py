# CSV 2 flare.json
# convert a csv file to flare.json for use with many D3.js viz's
# This script creates outputs a flare.json file with 2 levels of nesting.
# For additional nested layers, add them in lines 32 - 47
# sample: http://bl.ocks.org/mbostock/1283663

# author: Andrew Heekin
# MIT License

import pandas as pd
import json


df = pd.read_csv('path/to/csv/file.csv')


# choose columns to keep, in the desired nested json hierarchical order
df = df[["the_parent", "the_child", "child_size"]]


# order in the groupby here matters, it determines the json nesting
# the groupby call makes a pandas series by grouping 'keep_me' and 'and_me', while summing the numerical column 'me_too'
df1 = df.groupby(['the_parent', 'the_child'])['child_size'].sum()
df1 = df1.reset_index()


# start a new flare.json document
flare = dict()
flare = {"name":"flare", "children": []}


for line in df1.values:
    the_parent = line[0]
    the_child = line[1]
    child_size = line[2]

    # make a list of keys
    keys_list = []
    for item in d['children']:
        keys_list.append(item['name'])

    # if 'keep_me' is NOT a key in the flare.json yet, append it
    if not keep_me in keys_list:
        d['children'].append({"name":the_parent, "children":[{"name":the_child, "size":child_size}]})

    # if 'keep_me' IS a key in the flare.json, add a new child to it
    else:
        d['children'][keys_list.index(the_parent)]['children'].append({"name":the_child, "size":child_size})

flare = d


# export the final result to a json file
with open('output/path/flare.json', 'w') as outfile:
    json.dump(flare, outfile)
