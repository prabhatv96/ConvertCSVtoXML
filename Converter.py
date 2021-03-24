import csv
import os

print("Start writing XML")

package_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(package_dir+'/resources', 'sample.csv')


# same output file name
idx = input.rfind("\\")
outputfilename = input[idx+1:-4]
output = os.path.join(package_dir+'/output', outputfilename+'.xml')

reader = csv.reader(open(input, 'r'))

# open xml file
f = open(output, 'w')

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write("<Employee>\n")

# header row
header = next(reader)

for row in reader:

    f.write("    <Record>\n")
    f.write('       ' + '<'+header[0]+'>' + row[0] + '</'+header[0]+'>\n')
    f.write('       ' + '<'+header[1]+'>' + row[1] + '</'+header[1]+'>\n')
    f.write('       ' + '<'+header[2]+'>' + row[2] + '</'+header[2]+'>\n')
    f.write("    </Record>\n")

# complete root tag
f.write('</Employee>')

f.close()
print("Finished writing XML: Successfully converted into XMl")
