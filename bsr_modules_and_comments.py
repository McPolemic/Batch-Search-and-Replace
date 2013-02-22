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
            if csv[0][0] == '<hostname>' and csv[i][0] != '':
                outputFile = open(csv[i][0] + '.txt', 'a')
            else:
                outputFile = open('output' + str(i) + '.txt','a')
            outputFile.write(outputLines[i])
            outputFile.close()

def importCSV(CSVFileName):
    """Loads a CSV file CSVFileName and returns a list of lists "sample[x][y]"
       where "x" is the line of the CSV and "y" being each element 
       comma-separated."""
    with open(CSVFileName,'r') as csv:
        return [line.rstrip().split(',') for line in csv.readlines()]

def importTemplate(templateFileName):
    with open(templateFileName,'r') as template:
        return template.readlines()

importedCSV = importCSV('bsr.csv')
importedTemplate = importTemplate('bsr.txt')
generateOutput(importedTemplate, importedCSV)
print 'done'
