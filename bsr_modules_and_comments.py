def generateOutputFiles(template,csv):
    """Given a template, take all fields matching the first line of the CSV
    and generate a new output file with fields from each other line of the 
    CSV."""
    outputs = [] * len(csv)

    # Loop through each output file.
    for i in range(1, len(outputs)):
        outputs[i] = generateOutput(template, csv[0], csv[i])
    
def generateOutput(template, template_fields, target_fields):
    """Given a template file, replace all template_fields with target_fields"""
    outName = determineFileName(template_fields, target_fields)
    out = template

    for i in range(1, len(template_fields)):
        out.replace(template_fields[i], target_fields[i])

    # Write replaced version to file
    with open(outName, 'w') as outFile:
        outFile.write(out)

    return out

def determineFileName(csv_heading, csv_target):
    # If we already have a hostname set, use that
    if csv_heading[0] == '<hostname>' and csv_target[0] != '':
        return '%s.txt' % csv_target[0]
    return 'output%s.txt' % offset

def importCSV(CSVFileName):
    """Loads a CSV file CSVFileName and returns a list of lists "sample[x][y]"
       where "x" is the line of the CSV and "y" being each element 
       comma-separated."""
    with open(CSVFileName,'r') as csv:
        return [line.rstrip().split(',') for line in csv.readlines()]

def importTemplate(templateFileName):
    with open(templateFileName,'r') as template:
        return template.read()

if __name__ == '__main__':
    importedCSV = importCSV('bsr.csv')
    importedTemplate = importTemplate('bsr.txt')
    generateOutputFiles(importedTemplate, importedCSV)
    print 'done'
