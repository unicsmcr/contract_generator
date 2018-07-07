import sys
import pdfkit
import csv
import os


def makeContracts(templateFile, dataFile, outputFolder):
    contracts = csv.reader(open(dataFile, 'rt'))
    for row in contracts:
        generateContract(templateFile, row, outputFolder)


def generateContract(templateFile, collumns, outputFolder):
    with open(templateFile, 'rt') as tFile:
        template = tFile.read()
        if not os.path.exists(outputFolder):
          os.mkdir(outputFolder)
        for index, col in enumerate(collumns):
            template = template.replace('[col' + str(index) + ']', col)
        template = template.replace('Â£', u"\xA3")
        pdfkit.from_string(template, outputFolder + '/' + collumns[0] + '.pdf')

makeContracts(sys.argv[1], sys.argv[2], sys.argv[3])