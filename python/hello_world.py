##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2016, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')
worksheet.write('B1', 'B1 Hello')
# Text with formatting.
worksheet.write('A2', 'World', bold)
worksheet.write('B2', 'B2 World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)
worksheet.write(4, 0, 987.456)
worksheet.write(3, 1, 756.456)
# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()