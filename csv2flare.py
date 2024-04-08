# CSV 2 flare.json
# Convert a CSV file to flare.json for use with many D3.js visualizations
# This script outputs a flare.json file with 2 levels of nesting.
# For additional nested layers, modifications are needed in the loop where children are appended.
# Sample: http://bl.ocks.org/mbostock/1283663
# Author: Andrew Heekin
# MIT License

import pandas as pd
import json
import sys

def csv_to_flare(csv_file_path, json_file_path):
    try:
        df = pd.read_csv(csv_file_path)

        # Choose columns to keep, in the desired nested json hierarchical order
        df = df[["parent", "child", "child_value"]]

        # Order in the groupby here matters, it determines the json nesting
        # The groupby call makes a pandas series by grouping 'parent' and 'child', while summing the numerical column 'child_value'
        df1 = df.groupby(['parent', 'child'])['child_value'].sum().reset_index()

        # Start a new flare.json document
        flare = {"name": "flare", "children": []}
        parents_index = {}  # Keeps track of parent indices in flare['children']

        for line in df1.values:
            parent, child, child_value = line

            # Check if parent exists, and if not, add it
            if parent not in parents_index:
                flare['children'].append({"name": parent, "children": [{"name": child, "size": child_value}]})
                parents_index[parent] = len(flare['children']) - 1
            else:
                # Add a new child to the existing parent
                parent_index = parents_index[parent]
                flare['children'][parent_index]['children'].append({"name": child, "size": child_value})

        # Export the final result to a json file
        with open(json_file_path, 'w') as outfile:
            json.dump(flare, outfile, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv2flare.py <path_to_csv_file> <path_to_json_output_file>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    json_file_path = sys.argv[2]

    csv_to_flare(csv_file_path, json_file_path)
