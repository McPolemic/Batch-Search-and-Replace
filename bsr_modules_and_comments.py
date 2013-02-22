import string

def generateOutput(template,csv):
    """ Writes data to the individual files.  i starts at 1 to
        skip the heading row of the CSV.
        outputLines is used to store lines from the template to
        allow the substitutions for writing to the file.
        After storing all of the substitutions in one outputLines[i],
        a file is opened with the respective <hostname> value if
        possible, or output<row number> otherwise. Then the output
        is written to the output file and the file is closed.        
    """
    outputLines = [''] * len(csv)
    for line in template:
        for i in range(1, len(csv)):
            outputLines[i] = line
            for j in range(0, len(csv[i])):
                outputLines[i] = outputLines[i].replace(csv[0][j],csv[i][j])

            outputName = determineFileName(csv, i)
            outputFile = open(outputName, 'a')

            outputFile.write(outputLines[i])
            outputFile.close()

def determineFileName(csv, offset):
    csv_heading = csv[0]
    csv_target  = csv[offset]

    # If we already have a hostname set, use that
    if csv_heading[0] == '<hostname' and csv_target[0] != '':
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
        return template.readlines()

if __name__ == '__main__':
    importedCSV = importCSV('bsr.csv')
    importedTemplate = importTemplate('bsr.txt')
    generateOutput(importedTemplate, importedCSV)
    print 'done'
