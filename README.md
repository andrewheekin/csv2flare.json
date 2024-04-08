# CSV to flare.json Converter

This Python script ingests a CSV file and converts it into the flare.json format, which is widely used by many D3.js visualizations to create hierarchical structures such as trees and radial trees.

## Getting Started

To use this script, ensure you have Python installed on your system and the Pandas library available. You can install Pandas using pip if you haven't already: `pip install pandas`


## Usage

The script is designed to be run from the command line. It takes two arguments: the path to the input CSV file and the path for the output JSON file.

```bash
python3 csv2flare.py <path_to_csv_file> <path_to_json_output_file>
```


### Expected CSV Format

The input CSV file should have at least three columns:
- `parent`: Names or identifiers of the parent nodes.
- `child`: Names or identifiers of the child nodes associated with their respective parent nodes.
- `child_value`: Numerical values representing a quantifiable attribute of each child node (e.g., size, width).

#### Sample CSV Input

```csv
parent,child,child_value
Parent1,Child1,100
Parent1,Child2,150
Parent2,Child3,200
Parent2,Child4,50
```


### Output Format

The script outputs a `flare.json` file structured for use with hierarchical D3.js visualizations. The JSON structure includes `name` for node names and `size` for the child nodes' numerical values.

#### Sample JSON Output

```json
{
  "name": "flare",
  "children": [
    {
      "name": "Parent1",
      "children": [
        {"name": "Child1", "size": 100},
        {"name": "Child2", "size": 150}
      ]
    },
    {
      "name": "Parent2",
      "children": [
        {"name": "Child3", "size": 200},
        {"name": "Child4", "size": 50}
      ]
    }
  ]
}
```

## Notes

- The script currently supports creating a JSON structure with up to two levels of nesting. To incorporate more levels, further customization of the script is required.
- Ensure that your CSV column names match those expected by the script (`parent`, `child`, `child_value`). If your CSV uses different column names, you will need to modify the script accordingly or adjust your CSV file.
- For a sample visualization using the `flare.json` output, visit: [Sample Visualization](http://bl.ocks.org/mbostock/1283663).

## License

This script is provided under the MIT License.
