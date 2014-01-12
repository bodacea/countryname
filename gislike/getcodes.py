def getcodes(codeused):
  '''
  Load in list of countries and regions from the 'official' standards;
  Currently either the UN list from data.un.org or ISO3166
  NB some UN indices have no codes associated with them
  FIXIT: add code to bomb out if the input file doesn't exist

  Sara-Jayne Farmer
  2012
  '''
  
  #Only create codes if they're not already on the list
  if not self.validindices.has_key(codeused):
    self.validindices[codeused] = {}
    self.validlower[codeused]   = {}

    if codeused == "ISO3166":
      #ISO3166 is being used: get the valid names from pycountry
      for i in range(0,len(pycountry.countries)):
        idict = list(pycountry.countries)[i]
        ccode = idict.alpha3
        cname = idict.name
        self.validlower[codeused][string.lower(cname)] = cname
        self.validindices[codeused][cname] = ccode

    else:
      #UNSTATS is being used: get the valid names from a file
      f = open('codes/UNSTATSPlaceCodes.csv', 'rb')
      csvReader = csv.reader(f)

      #Skip header row, then load in all the countries etc.
      #Make index lowercase, to make searching easier
      headers = csvReader.next()
      for row in csvReader:
        ccode = row[1]
        cname = row[2]
        self.validlower[codeused][string.lower(cname)] = cname
        self.validindices[codeused][cname] = ccode
      f.close()
      
  return()
