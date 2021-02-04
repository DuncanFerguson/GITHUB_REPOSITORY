import pandas as pd
import csv

#Student: Duncan Ferguson
#Student Id: 871641260
#Class: 3005-2
#Assignment: Midterm

'''This Program takes a list of Mineral Owner and NRA values then creates a NRA dictionary with reorganized
 reorganizes names. There is the option to use the list that is in the file, or rewrite the file path. There is also
 the option just to print the list, or save it as a csv file'''

# List of Suffix Types that should remain at the end of a name swap
suffixtypes = ["JR", "II", "III", "IV", "V", "ESTATE", "TR", "TRUSTEE"]

# List of company endings to skip on
companynames = ["LLC", "COMPANY", "ESTATE", "INC", "FDN", "FOUNDATION", "EXPLORATION", "ROYALTIES", "CORP",
                "PARTNERSHIP", "INC", "CO", "LTD", "PARTNERS", "FDN", "LP", "MINERALS", "PROPERTIES", "TRUST"]

# List of realistic company names and NRAs
embeddedlist = [['ABEL DONALD A', 2.00192], ['DODSON FAMILY LLC', 27.07140096], ['HANZEL ALICE', 1.74848],
                ['FEEHAN HARVEY ANDREW', 0.10479024], ['CROXTON ELEANOR ANN', 0.8755200000000001],
                ['SHAW JOHN B', 0.47103999999999996], ['SHAW JOHN B', 0.23551999999999998],
                ['WATSON DANIEL B', 1.70381168], ['KOCH SUZANNE B', 5.05505536], ['WELLS JOHN C & BECKY', 3.978128],
                ['WELLS JOHN C & BECKY', 0.16688816], ['WELLS JOHN C & BECKY', 0.08533712],
                ['SCHWETHELM ELLEN BOONE', 20.1541264], ['SCHWETHELM ELLEN BOONE', 5.042648000000001],
                ['FEEHAN BRIAN', 0.10479024], ['MONROE W BRUCE', 1.99250808], ['STEVENS FARISH BURNS', 11.78428048],
                ['STEVENS FARISH BURNS', 20.23058016], ['TAYLOR NICHOLAS C', 4.00384], ['ABEL JOSEPH C', 2.00192],
                ['KASSAB LANCE C', 2.0181824], ['CONSIDINE MARGUERITE CAMBIAS', 2.0181824],
                ['BURNS REED CAWTHRA', 47.091736], ['BURNS REED CAWTHRA', 11.78428048],
                ['PROTESTANT EPISCOPAL CHURCH', 3.2135008], ['PROTESTANT EPISCOPAL CHURCH', 0.80294472],
                ['BHP BILLITON PET (TXLA OP) CO', 3.99024584], ['BHP BILLITON PET (TXLA OP) CO', 4020.3165],
                ['LAMBERT OIL & GAS ROYALTIES CO', 15.0016], ['BHP BILLITON PET (TXLA OP) CO', 3905.28],
                ['M D ABEL CO', 326.0700518], ['PENSCO TRUST COMPANY', 1.5427556],
                ['MEWBOURNE OIL COMPANY', 4036.3520000000003], ['ABEL M D COMPANY', 11.002880000000001],
                ['MEWBOURNE OIL COMPANY', 4018.56], ['MEWBOURNE OIL COMPANY', 3963.01824],
                ['KING J ROBERT COMPANY', 5.68195968], ['MEWBOURNE OIL COMPANY', 3774.6585600000003],
                ['DURANGO PRODUCTION CORP', 11.82953616], ['TEXAS CAPITAL DEVELOPMENT CORP', 23.920432],
                ['TEXAS CAPITAL DEVELOPMENT CORP', 2.0181824], ['TEXAS CAPITAL DEVELOPMENT CORP', 1.0085296000000001],
                ['SCHMIDT ERIC D', 1.7510400000000002], ['ZAVIDNY MICHAEL DAVID', 2.84097984],
                ['WELLS JOHN DAVID', 0.08538464], ['WELLS JOHN DAVID', 0.04266856], ['HISSOM ROBERT DAVIS', 3.01568],
                ['MCCONNELL DIANE', 160.0], ['PHILLIPS ANN LOUISE DODSON', 6.769152],
                ['SANDERFORD ELSIE GAY DODSON', 6.769152], ['CARR PHILLIP E', 3.8541343999999995],
                ['CARR PHILLIP E', 0.96586104], ['SPENCER ANGELA ESSMAN', 44.00128],
                ['CHAMBERS C H ESTATE', 3.99024584], ['CERF MARGARET MARY LIFE ESTATE', 10.04032],
                ['LOW ANN G LIFE ESTATE', 2.0181824], ['HUBBARD PATRICIA P LIFE ESTATE', 6.88122576],
                ['WILLIS ELIZABETH F', 0.10479024], ['BROWN JUDITH FATH', 35.55328], ['LIVELY PENNY FATH', 35.55328],
                ['BAYLOR HEALTH CARE SYSTEM FDN', 107.6316112], ['BAYLOR HEALTH CARE SYSTEM FDN', 53.85054],
                ['BAYLOR HEALTH CARE SYSTEM FDN', 26.92774032], ['CHANCELLOR FLYNT', 3.99024584],
                ['DODSON DAVID GAYER', 6.769152], ['ESSMAN JAMES H', 21.995520000000003],
                ['JUSTICE ELOUISE H', 37.65248], ['JUSTICE ELOUISE H', 18.82624], ['FEEHAN JOHN H', 0.10479024],
                ['JOHNSON W D JR TR FBO HAGGERTY', 64.0], ['VANGENDEREN HEIDI', 1.74848],
                ['BUDD TAMRA HISSOM', 3.01568], ['HAMMONS RUTH ANNE HOFFSTADT', 53.33504],
                ['HUBBARD FORD III', 1.32346192], ['SABRE EXPLORATION INC', 66.13453328],
                ['SILVERTON PETROLEUM INC', 12.51462424], ['CHEVRON USA INC', 640.0], ['CHEVRON USA INC', 640.0],
                ['W P X ENERGY INC', 4160.0], ['CHEVRON USA INC', 640.0], ['W P X ENERGY INC', 141.44],
                ['W P X ENERGY INC', 160.0], ['CHEVRON USA INC', 299.99872], ['CHEVRON USA INC', 696.81152],
                ['CHEVRON USA INC', 920.00256], ['W P X ENERGY INC', 217.6], ['W P X ENERGY INC', 3852.8],
                ['CHEVRON USA INC', 1128.925], ['CHEVRON USA INC', 1200.0], ['CHEVRON USA INC', 324.0618766],
                ['BADON HILL INC', 0.03104896], ['CHEROKEE LAND & MINERALS INC', 3.78797312],
                ['CHEVRON USA INC', 525.3275528], ['CHEVRON USA INC', 485.9668598], ['CHEVRON USA INC', 647.5184078],
                ['FLACKMAN DAVID J', 9.37472], ['FLACKMAN DAVID J', 80.725], ['WELLS MATTHEW J', 0.08538464],
                ['FLACKMAN DAVID J', 20.19774472], ['WELLS MATTHEW J', 0.04266856],
                ['TOMLINSON CLAUDIA JANE', 2.00192], ['TYNES TERRY JO', 31.391046399999997],
                ['CROXTON EVERETT HUBERT JR', 0.8755200000000001], ['DOWNING RICHARD JR', 1.7510400000000002],
                ['FATH CHARLES JR', 35.55328], ['DODSON DWAIN FREEMAN JR', 6.769152],
                ['NEZWORSKI CHRISTOPHER & KEELY', 0.4075176], ['CAMBIAS JAMES LESLIE', 2.0181824],
                ['RKI EXPLORATION & PROD LLC', 83.2], ['RKI EXPLORATION & PROD LLC', 320.0],
                ['DORR PETROLEUM LAND MANGMT LLC', 25.08288], ['RKI EXPLORATION & PROD LLC', 3941.09952],
                ['TEAL ROYALTIES LLC', 19.998720000000002], ['ALOR LLC', 83.99871999999999],
                ['RKI EXPLORATION & PROD LLC', 3840.0], ['BERGMAN MINERAL HOLDINGS LLC', 0.47103999999999996],
                ['TILDEN CAPITAL LLC', 8.93952], ['NM&T RESOURCES LLC', 131.7888],
                ['RKI EXPLORATION & PROD LLC', 3880.0332799999996], ['SBR PARTNERS LLC', 0.65536],
                ['RKI EXPLORATION & PROD LLC', 2099.59936], ['RKI EXPLORATION & PROD LLC', 32.0],
                ['MILBURN INVESTMENTS LLC', 56.0], ['BERGMAN MINERAL HOLDINGS LLC', 0.23551999999999998],
                ['TILDEN CAPITAL LLC', 4.46976], ['NM&T RESOURCES LLC', 65.8944],
                ['RKI EXPLORATION & PROD LLC', 1940.0166399999998], ['RKI EXPLORATION & PROD LLC', 141.44],
                ['RKI EXPLORATION & PROD LLC', 80.0], ['ANADARKO E&P ONSHORE LLC', 3907.0951659999996],
                ['ZPZ DELAWARE I LLC', 129.16], ['ANADARKO E&P ONSHORE LLC', 3870.6],
                ['ANADARKO E&P ONSHORE LLC', 3840.0], ['SOURCING ROCK LLC', 0.20958048],
                ['BREEZY BEACH LLC', 4.04024592], ['FORTIS MINERALS LLC', 11.10776544],
                ['CAPULATA INVESTMENTS LLC', 3.0272736], ['RANCHO OIL CO LLC', 4.10234384],
                ['TOPPER HARLEY INVESTMENTS LLC', 1.68440608], ['JAMCO ENERGY LLC', 0.03104896],
                ['ZPZ DELAWARE I LLC', 80.77775056], ['BLAZE INTERESTS LLC', 0.58993024],
                ['ANADARKO E&P ONSHORE LLC', 2982.601909], ['WW WORLDWIDE LLC', 0.7374128000000001],
                ['TD MINERALS LLC', 18.96703344], ['GATOREX HOLDINGS LLC', 3.0272736],
                ['VIPER ENERGY PARTNERS LLC', 4.04024592], ['ANADARKO E&P ONSHORE LLC', 2907.753753],
                ['SOURCING ROCK LLC', 0.08921608], ['ZPZ DELAWARE I LLC', 40.3993684],
                ['TD MINERALS LLC', 8.029447200000002], ['VIKING MINERALS LLC', 0.32195368],
                ['ANADARKO E&P ONSHORE LLC', 5837.58], ['SUEDE OIL & GAS LLC', 10.14852096],
                ['RPR I LLC', 40.59929088], ['KNEBEL FAMILY HOLDINGS LLC', 40.59929088],
                ['TANGO LIMA LLC', 3.03510496], ['ZPZ DELAWARE I LLC', 80.91714128],
                ['MDJ MINERALS LLP', 161.8291032], ['FISCHER CHARLES A & LOIS', 38.4],
                ['FISCHER CHARLES A & LOIS', 76.8], ['MCCONNELL RHONDA LOUISE', 160.0],
                ['LOVING COUNTY MINERALS LP', 882.4980406], ['DEVON ENERGY PRODUCTION CO LP', 49.9968],
                ['THAMS FAMILY PARTNERSHIP LP', 4.79744], ['LOVING COUNTY MINERALS LP', 575.99488],
                ['SNEED COMPANY LP', 16.0], ['LOVING COUNTY MINERALS LP', 1152.0],
                ['BLACK STONE MINERALS CO LP', 138.49088], ['BOLDRICK FAMILY PROPERTIES LP', 8.94464],
                ['LOVING COUNTY MINERALS LP', 821.888], ['BLACK STONE MINERALS CO LP', 69.24544],
                ['BOLDRICK FAMILY PROPERTIES LP', 4.47232], ['LOVING COUNTY MINERALS LP', 410.944],
                ['WALKER ROYALTY LP', 15.9435104], ['HED ENTERPRISES LP', 31.897353600000002],
                ['MALCOLM REED VENTURES LP', 31.391046399999997], ['KWF ENTERPRISES LP', 31.897353600000002],
                ['KWF ENTERPRISES LP', 2.69349728], ['HAZELWOOD PARTNERS LP', 0.17465039999999998],
                ['SANTA ELENA MINERALS LP', 3.23297296], ['WALKER ROYALTY LP', 1.34674864],
                ['ALLDALE MINERALS II LP', 2.93800784], ['HED ENTERPRISES LP', 2.69349728],
                ['MALCOLM REED VENTURES LP', 13.46360528], ['BLACK STONE MINERALS CO LP', 1.89786768],
                ['MALCOLM REED VENTURES LP', 7.854894], ['WALKER ROYALTY LP', 0.67493904],
                ['DOUBLE EAGLE ROYALTY LP', 0.80294472], ['KWF ENTERPRISES LP', 1.34599912],
                ['HED ENTERPRISES LP', 1.34599912], ['ALLDALE MINERALS II LP', 57.65145616],
                ['WAGNER & BROWN LTD', 100.10130490000002], ['DONEGAL LTD', 6.00064],
                ['COWAN OIL & GAS LTD', 3.00032], ['HERD PARTNERS LTD', 32.29], ['HERD PARTNERS LTD', 8.07987368],
                ['GLEASON BOBBY M', 3.99024584], ['SCHMIDT GREGORY M', 1.7510400000000002],
                ['WATSON MELODY M', 1.70381168], ['EVERS JANET MADELEY', 9.6508352],
                ['STEVESON SUSAN C MADELEY', 9.6508352], ['EVERS JANET MADELEY', 2.41659208],
                ['STEVESON SUSAN C MADELEY', 2.41659208], ['HAGGERTY DOROTHY MAE', 91.32032],
                ['HAGGERTY DOROTHY MAE', 45.66016], ['MAP2015-OK', 26.92721056], ['MAP2015-OK', 13.46774912],
                ['ZAVIDNY DENNIS MICHAEL', 2.84097984], ['P & P MINERALS', 0.22016],
                ['WITT DAVIEANN MONROE', 1.99773776], ['JOSEY DONNA PEARSON NEUHOFF', 5.04933712],
                ['TRUITT MARY P', 2.24768], ['PEC MINERALS L P', 84.3776], ['WAIKIKI PARTNERS L P', 48.435],
                ['WAIKIKI PARTNERS L P', 12.11787104], ['NEWSOM PATRICIA PAULL', 33.2544],
                ['SCHREIBER ARLINE PHILLIPS', 1.2864336], ['MJG OIL PROPERTIES', 4.10234384],
                ['MIRAMAR PROPERTIES', 3.36493104], ['WILEY OIL & GAS LIMITED PRTN', 4.10234384],
                ['ANDREW OIL & GAS PTRSHP', 9.79968], ['MERSIOVSKY A R', 3.99024584], ['COOK ZELDA REED', 94.1783056],
                ['COOK ZELDA REED', 40.38693472], ['COOK ZELDA REED', 23.564682], ['CRAIN JACK LEE ROY', 3.99024584],
                ['JEB ROYALTIES', 3.1101728], ['JEB ROYALTIES', 0.775792], ['ALLISON WILLIAM S', 4.11575816],
                ['CARMAN BRENDA S', 12.8], ['BOONE SANDRA S', 20.1541264], ['BOONE SANDRA S', 5.042648000000001],
                ['MADELEY SHELLEY', 9.6508352], ['MADELEY SHELLEY', 2.41659208], ['RAY SMITH', 5.0022400000000005],
                ['ROWLAND STACI', 53.33504], ['PETERSEN SCOTT T', 10.04032], ['BARNETT TOMMILYN', 1.74848],
                ['JOHNSON W D JR', 98.0565], ['ROBINSON MARGARET SUZANNE C TR', 13.46360528],
                ['KEEBLE WILLIAM RITCHIE III', 27.06619392], ['WOOD FAMILY TRUST', 4.79744],
                ['WALLACE CAROLINE HISSOM TR', 3.01568], ['HISSOM JULIA ANN TR', 3.01568],
                ['HISSOM ALEXANDRA CARSON TR', 3.01568], ['JOHNSON W D JR', 128.0],
                ['ROBINSON MARGARET S C TR', 31.391046399999997], ['TEXAS PACIFIC LAND TRUST', 161.275],
                ['TEXAS PACIFIC LAND TRUST', 80.0], ['WATTS/PORTER LIVING TRUST', 0.67143376],
                ['HILL FAMILY LIVING TRUST', 0.84220304], ['DEWOODY LIVING TRUST', 0.03104896],
                ['LIPSCOMB FAMILY TRUST', 0.41916096], ['ROBINSON MARGARET S C TR', 7.854894],
                ['TEXAS PACIFIC LAND TRUST', 121.2291369], ['TEXAS PACIFIC LAND TRUST', 161.9889533],
                ['GRIFFIN RICKER TR', 20.30224896], ['KAHLE MIMIPA TR', 40.59929088],
                ['KEEBLE FLOYD C DODSON TR', 27.06619392], ['DODSON FLOYD TR', 54.13238784],
                ['ROBINSON MARGARET S C TR', 13.48705344], ['COSTELLO JOEL TRUSTEE', 1.5427556],
                ['HOWERTON ELIZE TUMMINELLO', 0.8755200000000001], ['HADDEN TERRY COCKE TYNES', 13.46360528],
                ['HADDEN TERRY COCKE TYNES', 7.854894], ['HADDEN TERRY COCKE TYNES', 13.48705344],
                ['ESSMAN JAMES W', 44.0064], ['KENTZEL JOHN W', 106.66496000000001], ['NEWKUMET WAYNE', 3.09597056]]


def startoption(listinfile):
    """This functions determines how we are going to start this program.
    There are two options. 1) Using the list that is defined embedded list above. Or 2) Opening a file from the path
    that is listed in openfile()"""
    selectedlist = []
    startselection = int(input("Press (1) To use embedded Mineral Owner List:\n"
                               "Press (2) To select a file that you would like to upload:\n"))
    if startselection == 2:
        selectedlist = openfile()  # Goes to open file to open the file location
    elif startselection == 1:
        selectedlist = listinfile  # This uses the embedded list in line 20
    else:
        print('Good Bye!')
        exit()
    print("Raw List: ", selectedlist)
    return selectedlist


def openfile():
    """This function opens the file that is listed in taxrollfilelocation, and places the values into a list"""
    taxrollfilelocation = pd.read_csv('Raw_Tax_Roll_Example.csv')  # File name
    taxrollfile = pd.DataFrame(taxrollfilelocation, columns=['Owner', 'NRA'])  # Grabbing Headers
    listfromfile = taxrollfile.values.tolist()  # Placing file columns into a list
    return listfromfile


def totalnra(list2nradict):
    """This Function takes in a list of [names, NRA]. It then makes and returns a dictionary with the NRA sums"""
    list2nrasumdict = {}  # Blank Dictionary
    for (name, NRA_Amount) in list2nradict:
        if name in list2nrasumdict:
            list2nrasumdict[name] += NRA_Amount  # If Name exists, add NRA Amount
        else:
            list2nrasumdict[name] = NRA_Amount  # If Name doesn't exist, make dictionary entry
    return list2nrasumdict


def fixnames(fixdict):
    """This function returns the NRA Dictionary with the proper names"""
    newnrasum = {}
    nrasumlist = []
    for i in fixdict:
        nrasumlist += [[i, fixdict[i]]]  # Casting nrsSum dictionary into a list with the rawnames
    for i in nrasumlist:
        names = [i[0]]  # This is really a string that I am representing as a list so that I can split it later
        newname = determineswap(names, suffixtypes,
                                companynames)  # running through the name swapper and returning a name in list value
        newnrasum[newname[0]] = [i[1]]  # Adding NRA to the new Dictionary with the newname
        newnrasum[newname[0]].append(i[0])  # Adding the Raw name to the dictionary for safe keeping
    return newnrasum


def determineswap(names, suffixtypes, companynames):
    """This funcation looks at the name and determines which other function to run the name through
    this way we can send the name to the right area"""
    for i in range(len(names)):  # This loops through the list
        namesplit = names[i].split(" ")  # This takes the name, splits the different types of names into a list
        if len(namesplit) == 1 or namesplit[-1] in companynames:  # If one word or  a company name, just keep as is
            names[i] = names[i]
        elif namesplit[-1] in suffixtypes:  # This looks to see if there is a suffix type at the end
            names[i] = lastnamesuffixswap(namesplit)
        else:  # This assumes if there is no suffix or company name, run normal name swap
            names[i] = lastnameswap(namesplit)
    return names  # Returning the properly modified name


def lastnameswap(namesplit):
    """This changes the order of the names. Example: Last, First, Middle
    Ending Example: First, Middle, Last. The returned value is in string form"""
    newname = ""  # Creating a new blank string
    z = 1
    while z < len(namesplit):
        newname += " " + namesplit[z]  # adding a space then the name starting from the second position
        z += 1
    newname += " " + namesplit[0]
    newname = newname.lstrip()  # Stripping out the leading space
    return newname


def lastnamesuffixswap(namesplit):
    """This changes the order of the names if it sees a suffix for a swap. Example: Last, First, Middle, Suffix
    Ending Example: First, Middle, Last, Suffix. The returned value is in string form"""
    newname = ""
    z = 1
    while z < len(namesplit) - 1:
        newname += " " + namesplit[z]
        z += 1
    newname += " " + namesplit[0] + " " + namesplit[-1]  # Moves the lastname right before the suffix
    newname = newname.lstrip()
    return newname


def endoption(newnrasum):
    """This function lets you choose whether to save the dictionary or
    print it newnrasum dictionary or saves it to a CSV File"""
    print("\nThe Raw List has been scrubbed\n")
    ending = input("Press 'P' or 'p' to print NRA Sum Dictionary\n"
                   "Press 'S' or 's' to save CSV File\n"
                   "Press 'Any other Key to Exit\n")
    if ending == 's' or ending == 'S':
        makefile(newnrasum)  # This runs makefile()
        print("File is now saved in the Same Directory")
    elif ending == 'p' or ending == 'P':  # Simple Printing of dictionary
        print("Key = New Owner Name : Value = [NRA, Raw Name]")
        print(newnrasum)
    else:
        exit()


def makefile(newnrasum):
    """This Function takes in a dictionary and writes it to a csv file"""
    filename = input("What would you like the new file to be named: ")
    filename = filename + ".csv"
    fields = ['Name', 'NRA', 'Raw Name']
    rows = []
    for i in newnrasum:  # Casting newNRA Sum dictionary back into a list
        name = i
        nra = newnrasum[i][0]
        rawname = newnrasum[i][1]
        rows.append([name, nra, rawname])
    with open(filename, 'w', newline='') as csvfile:  # writing my csv file
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    exit()


rawlist = startoption(embeddedlist)  # Opens the list and returns the choice of which rawlist to use
nrasum = totalnra(rawlist)  # Place raw list into a dictionary
modifiednradict = fixnames(nrasum)  # This is returning back the new name values in a NRA Dictionary
endoption(modifiednradict)  # This is giving you an option for how to end

