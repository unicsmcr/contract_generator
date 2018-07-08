# Usage: python pdfContract.py {template} {csvDataFile} {outputFolder}
# Note: the structure of the csv data file is defined within the template
# Dependencies:
#    Python 3
#    pdfkit (pip install pdfkit)
#    wkhtmltopdf (wkhtmltopdf.org for installation instructions)

import sys
import pdfkit
import csv
import os

# Makes contracts for each of the rows in dataFile with the template in templateFile and outputs everything to outputFolder
def makeContracts(templateFile, dataFile, outputFolder):
    contracts = csv.reader(open(dataFile, 'rt')) # Reading the dataFile
    for row in contracts: # Going over all row in the datFile
        generateContract(templateFile, row, outputFolder)

# Creates a single pdf contract in the outputFolder with the given template and data
def generateContract(templateFile, data, outputFolder):
    with open(templateFile, 'rt') as tFile:
        template = tFile.read() # Loading the template
        if not os.path.exists(outputFolder): # Creating the outputFolder if it doesn't exist already
          os.mkdir(outputFolder)
        for index, col in enumerate(data): # Going over all collumns in the data
            template = template.replace('[col' + str(index) + ']', col) # Replacing the placeholders in the template
        template = template.replace('Â£', u"\xA3") # For some reason can't encode the pound symbol properly, replacing it with its unicode character
        pdfkit.from_string(template, outputFolder + '/' + data[0] + '.pdf') # Generating the pdf file

makeContracts(sys.argv[1], sys.argv[2], sys.argv[3])