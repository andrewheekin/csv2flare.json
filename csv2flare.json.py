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
df = df[["keep_me", "and_me", "me_too"]]


# order in the groupby here matters, it determines the json nesting
# the groupby call makes a pandas series by grouping 'keep_me' and 'and_me', while summing the numerical column 'me_too'
df1 = df.groupby(['keep_me', 'and_me'])['me_too'].sum()
df1 = df1.reset_index()


# start a new flare.json document
flare = dict()
flare = {"name":"flare", "children": []}


for line in df1.values:
    keep_me = line[0]
    and_me = line[1]
    me_too = line[2]

    # make a list of keys
    keys_list = []
    for item in d['children']:
        keys_list.append(item['name'])

    # if 'keep_me' is NOT a key in the flare.json yet, append it
    if not keep_me in keys_list:
        d['children'].append({"name":keep_me, "children":[{"name":and_me, "size":me_too}]})

    # if 'keep_me' IS a key in the flare.json, add a new child to it
    else:
        d['children'][districtslist.index(keep_me)]['children'].append({"name":and_me, "size":me_too})

flare = d


# export the final result to a json file
with open('output/path/flare.json', 'w') as outfile:
    json.dump(flare, outfile)