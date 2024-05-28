# WordPress Theme Comparison Script

## Overview

This Python script is designed to help developers and designers compare two versions of a WordPress theme. It identifies differences in files, including missing, added, and modified files, and provides a detailed report on the changes. This tool is invaluable for debugging, collaboration, and understanding changes between theme updates.

## Features

- Extracts ZIP files: Automatically extracts WordPress theme ZIP files for comparison.
- File Comparison: Compares each file in the two themes to identify missing, added, and modified files.
- Detailed Diff Reports: Generates a unified diff report for modified files, showing precise changes at the line level.
- Clear Output: Saves the comparison report with a timestamp and the names of the compared themes for easy reference.

## Use Cases

- Theme Updates: Quickly see what has changed between two versions of a theme.
- Debugging: Identify changes that may have introduced bugs or issues.
- Collaboration: Understand what modifications have been made by team members.
- Optimization: Track changes that affect performance or security.

## Requirements

- Python 3.x
- Standard Python libraries: zipfile, difflib, os, pathlib

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.

## Usage

1. Setup: Create a directory with the following structure:
<your_directory>/
├── script.py
└── input/
    ├── theme1.zip (or extracted folder theme1)
    └── theme2.zip (or extracted folder theme2)

2. Place your themes: Put the two theme ZIP files or extracted folders inside the input directory.
3. Run the script: Execute the script to generate the comparison report.

The script will generate a report file named in the format report_<theme1_name>_vs_<theme2_name>_yyyymmdd_hhmm.txt in the same directory as the script.

## Output

The output report includes:
- Missing files: Files present in one theme but missing in the other.
- Added files: Files added in one theme compared to the other.
- Modified files: Detailed differences for files that have been modified, using a unified diff format.

## Example Output

Format of differences:
@@ -a,b +c,d @@
a: Starting line number in the original file
b: Number of lines in the block from the original file
c: Starting line number in the modified file
d: Number of lines in the block from the modified file
-: Lines removed from the original file
+: Lines added to the modified file

Missing files in theme2:
file1.php
file2.css

Added files in theme2:
file3.js
file4.html

Modified file: style.css
--- theme1/style.css
+++ theme2/style.css
@@ -15,7 +15,7 @@
- old line 15
+ new line 15
  unchanged line 16
  unchanged line 17
  unchanged line 18
@@ -25,4 +25,4 @@
- old line 25
+ new line 25

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or suggestions, please contact [yourname](mailto:your.email@example.com).
