# PDF Contract Generator

### Dependencies:
* **Python 3** - download [here](https://www.python.org/download/releases/3.0/)
* **pdfkit** - to install run ```pip install pdfkit```
* **wkhtmltopdf** - installation instructions [here](https://wkhtmltopdf.org/)

### Usage:
The script takes an html template and a csv data file and produce a pdf file for each of the rows in the data file. The name of the generated file is: {firstColumnValueInDataFile}.pdf

Script can be run with:
```python pdfContract.py {template} {csvDataFile} {outputFolder}```
> **NOTE:** the structure of the csv file is defined within the template

### Creating templates:
The templates for the script are defined in HTML and CSS

Placeholders can be defined with the following syntax: ```[colx]``` where x is the column number (starting from 0) in the csv data file.

> **EXAMPLE:**
> The template:
>```html
><html>
><p>First name: [col0]</p>
><p>Last name: [col1]</p>
></html>
>```
>and the data file:
>```html
>Kristijonas,Zalys
>```
>would result in a pdf file:
>**Kristijonas.pdf:**
>```html
>First name:  Kristijonas
>Last name: Zalys
>```