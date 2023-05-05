#!/usr/bin/python3
"""
Markdown to HTML converter

Usage: ./markdown2html.py input_file output_file
"""

import sys
import re
import markdown

# Define regex patterns for headings
heading_pattern = re.compile(r'^(#+)\s(.*)$')

def main():
    """
    Main function that converts a markdown file to HTML
    """
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py input_file output_file")
        sys.exit(1)

    # Get the input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    try:
        with open(input_file, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"Missing {input_file}")
        sys.exit(1)

    # Read the input file
    with open(input_file, 'r') as f:
        # Parse the headings syntax
        lines = []
        for line in f.readlines():
            match = heading_pattern.match(line.strip())
            if match:
                level = len(match.group(1))
                title = match.group(2)
                lines.append(f"<h{level}>{title}</h{level}>")
            else:
                lines.append(line)

        # Convert the markdown file to HTML
        html = markdown.markdown('\n'.join(lines), output_format='html5')

    # Write the HTML to the output file
    with open(output_file, 'w') as f:
        f.write(html)

    sys.exit(0)

if __name__ == "__main__":
    main()
