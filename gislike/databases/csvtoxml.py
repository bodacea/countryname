# -*- coding: cp1252 -*-

import csv

#Read in csv file
#Write out xml text
fin = open('Country_crosswalks.csv', 'rb')
fout = open('countrycrossrefs.xml', 'wb')

csvin = csv.reader(fin)
headers = csvin.next()
fout.write('<country_entries>\n')
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
