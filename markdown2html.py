#!/usr/bin/python3
import markdown
import re
import sys
""" takea a markdown file and converts it to html"""


heading_pattern = re.compile(r'^(#+)\s(.*)$')

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

"""check if the input file exists"""
try:
    with open(input_file, 'r') as f:
        pass
except FileNotFoundError:
    print(f"Missing {input_file}")
    sys.exit(1)


with open(input_file, 'r') as f:
    """ parse headings syntax"""
    lines = []
    for line in f.readlines():
        match = heading_pattern.match(line.strip())
        if match:
            level = len(match.group(1))
            title = match.group(2)
            lines.append(f"<h{level}>{title}</h{level}>")
        else:
            lines.append(line)

    """ convert markdown to html"""
    html = markdown.markdown('\n'.join(lines), output_format='html5')
with open(output_file, 'w') as f:
    f.write(html)

sys.exit(0)
