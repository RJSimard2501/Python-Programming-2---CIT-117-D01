#Name: Remi Simard
#Assignment: Real Estate and Files
#Reflection:
#What did you like about this assignment?
#I enjoyed working with an actual file to get get input from and then throwing that into the code.
#
#What did you struggle with?
#The hardest thing was line 107 to create a for loop that outputs the data in a way that lines up with the sample. The dictionary work was hard too but mostly because there was alot of sorting, math, and aranging to be done with it. And keeping tack of which does what.
#
#Which approach did you use to import the data and why?
#I used with open because that is what Ive used the most and feel more comfortable using.
#
#How many dictionaries did you use?
#I used three dictionaries. One for City totals, one for Zip totals, and one for Property Type totals.
#
#Top 2 things learned:
#1. I learned how to calculate a median in python using dictionaries. 
#2. I learned how to input data from a csv file and put it into multiple dictionaries

#GetDataInput Function
def getDataInput():
    sFileNameRS = "RealEstateData.csv"
    with open(sFileNameRS, "r") as f:
        lRecordsRS = f.readlines()

    #Remove header row
    return lRecordsRS[1:]


#GetMedian Function
def getMedian(lValuesRS):
    lSortedRS = sorted(lValuesRS)
    iCountRS = len(lSortedRS)

    #Odd count calculation
    if iCountRS % 2 == 1:
        iMiddleIndexRS = iCountRS // 2
        return float(lSortedRS[iMiddleIndexRS])

    #Even count calculation
    else:
        iMiddleIndexRS = iCountRS // 2
        fMedianRS = (lSortedRS[iMiddleIndexRS] + lSortedRS[iMiddleIndexRS - 1]) / 2
        return float(fMedianRS)
    
#Main Function
def main():
    #Read all the records
    lRecordsRS = getDataInput()

    #Lists & dictionaries
    lPricesRS = []  #list of all prices
    dCityTotalsRS = {}  #totals by city
    dZipTotalsRS = {}  #totals by zip
    dTypeTotalsRS = {}  #totals by property type

    #Process the records
    for sRecordRS in lRecordsRS:
        sRecordRS = sRecordRS.strip()
        lFieldsRS = sRecordRS.split(",")

        #Extract the fields
        sCityRS = lFieldsRS[1]
        sZipRS = lFieldsRS[2]
        sTypeRS = lFieldsRS[7]
        fPriceRS = float(lFieldsRS[8])

        #Add prices to list
        lPricesRS.append(fPriceRS)

        #City totals
        if sCityRS not in dCityTotalsRS:
            dCityTotalsRS[sCityRS] = 0
        dCityTotalsRS[sCityRS] += fPriceRS

        #Zip totals
        if sZipRS not in dZipTotalsRS:
            dZipTotalsRS[sZipRS] = 0
        dZipTotalsRS[sZipRS] += fPriceRS

        #Property type totals
        if sTypeRS not in dTypeTotalsRS:
            dTypeTotalsRS[sTypeRS] = 0
        dTypeTotalsRS[sTypeRS] += fPriceRS

    #Sort prices
    lPricesRS.sort()

    #Summary calculations
    fMinRS = min(lPricesRS)
    fMaxRS = max(lPricesRS)
    fTotalRS = sum(lPricesRS)
    fAvgRS = fTotalRS / len(lPricesRS)
    fMedianRS = getMedian(lPricesRS)

    #Sample Output
    print("Sample Output")
    print(f"Minimum        {fMinRS:,.2f}")
    print(f"Maximum        {fMaxRS:,.2f}")
    print(f"Sum            {fTotalRS:,.2f}")
    print(f"Avg            {fAvgRS:,.2f}")
    print(f"Median         {fMedianRS:,.2f}")
    print()

    #Summary by City
    print("Summary by City")
    for city, total in sorted(dCityTotalsRS.items(), key=lambda x: x[1], reverse=True):
        print(f"{city:20} ${total:,.2f}")
    print()

    #Summary by Property Type
    print("Summary by Property Type")
    for ptype, total in sorted(dTypeTotalsRS.items(), key=lambda x: x[1], reverse=True):
        print(f"{ptype:15} ${total:,.2f}")
    print()

#Program Start
main()
