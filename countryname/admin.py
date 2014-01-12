#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
admin.py: do routine administration on country name files

__author__ = "Sara-Jayne Terp"
__status__ = "Prototype"
"""

import csv

def create_crosswalk_xmlfile(csvfile):
  """Creates an xml file from a csv list of matches between countryname standards.
  
  :param csvfile: name of file containing standards matches (as a string)
  :returns:  nothing
  """
  
  fin = open(csvfile, 'rb')
  csvin = csv.reader(fin)
  fout = open('countrycrossrefs.xml', 'wb')
  
  fout.write('<country_entries>\n')
  headers = csvin.next()
  
  for row in csvin:
    
    #Ignore territories and blank data
    etype = row[0]
    if not etype in ['country', 'region', 'economic']:
      continue
    
    #Label with UN name, with CIA name as backup
    cianame = row[1].strip()
    unname = row[3].strip()
    if unname != "":
      name = unname
    else:      
      if cianame != "":
        name = cianame
      else:
        continue
    
    #Have got this far, so have enough data to create a table entry
    fout.write('    <' + etype + '_entry\n')
    fout.write('        name="' + name + '"\n')

    #And add in the details from the spreadsheet
    cols = {5:'fips10', 7:'iso3166alpha3', 9:'unstatsm49', 10:'stanag',11:'internet'}
    for col in cols:
      if row[col] != "":
        fout.write('        '+cols[col]+'="' + row[col]+'"\n')
        
    fout.write('    />\n')
  fout.write('</country_entries>\n')

  #tidy up
  fin.close()
  fout.close()


if __name__ == "__main__":
  csvfile = "databases/giscrossrefs.csv"
  create_crosswalk_xmlfile(csvfile)
  
  