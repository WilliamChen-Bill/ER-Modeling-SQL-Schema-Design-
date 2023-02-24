"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Helper method to deal with quotation mark and strings
"""

def skipQuotation(text):
   return '\"' + sub(r'\"','\"\"',text) + '\"'

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""

def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        auctionUserFile = open("AuctionUser.dat", "a")
        bidsFile = open("Bids.dat", "a")
        categoriesFile = open("Categories.dat", "a")
        itemsFile = open("Items.dat", "a")
        for item in items:
            """
            traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """    
            # parse seller user data to auctionUser file.
            Seller = item["Seller"]
            SellerID = Seller["UserID"]
            if SellerID == None:
                SellerID = "NULL"
            else:
                auctionUser_info = skipQuotation(SellerID)

            if Seller["Rating"] == None:
                auctionUser_info += columnSeparator + "NULL"        
            else:
                auctionUser_info += columnSeparator+ Seller["Rating"]

            if item["Location"] == None:
                auctionUser_info += columnSeparator + "NULL"
            else:
                auctionUser_info += columnSeparator + skipQuotation(item["Location"])

            if item["Country"] == None:
                auctionUser_info += columnSeparator + "NULL" + "\n"
            else:
                auctionUser_info += columnSeparator + skipQuotation(item["Country"]) + "\n"

            auctionUserFile.write(auctionUser_info)

            # parse bidder user data to auctionUser file.
            Bids = item["Bids"]
            if Bids != None:
                for bid in Bids:
                    bidder = bid["Bid"]["Bidder"]
                    if bidder["UserID"] == None:
                        auctionUser_info = "" + "NULL"
                    else:
                        auctionUser_info = "" + skipQuotation(bidder["UserID"])
                        
                    if bidder["Rating"] == None:
                        auctionUser_info += columnSeparator + "NULL"
                    else:
                        auctionUser_info += columnSeparator+ bidder["Rating"]

                    if "Location" in bidder.keys() and bidder["Location"] != None:
                        auctionUser_info += columnSeparator + skipQuotation(bidder["Location"])
                    else:
                        auctionUser_info += columnSeparator + "NULL"

                    if "Country" in bidder.keys() and bidder["Country"] != None:
                        auctionUser_info += columnSeparator + skipQuotation(bidder["Country"]) + "\n"
                    else:
                        auctionUser_info += columnSeparator + "NULL" + "\n"

                    auctionUserFile.write(auctionUser_info)
           
            # parse Bids data to bids file.
            Bids = item["Bids"]
            if not Bids == None:
                for bid in Bids:
                    if item["ItemID"] == None:
                        bids_info = "" + "NULL"
                    else:
                        bids_info = "" + item["ItemID"]

                    if bid["Bid"]["Bidder"]["UserID"] == None:
                        bids_info += columnSeparator + "NULL"
                    else:
                        bids_info += columnSeparator + skipQuotation(bid["Bid"]["Bidder"]["UserID"])

                    if bid["Bid"]["Time"] == None:
                        bids_info += columnSeparator + "NULL"
                    else:
                        bids_info += columnSeparator + transformDttm(bid["Bid"]["Time"])

                    if bid["Bid"]["Amount"] == None:
                        bids_info += columnSeparator + "NULL" + "\n"
                    else:
                        bids_info += columnSeparator + transformDollar(bid["Bid"]["Amount"]) + "\n"

                    bidsFile.write(bids_info)      

            # parse Categories data to categories file.
            if item["ItemID"] == None:
                for Category in Categories:
                    categories_info = "" + "NULL" + columnSeparator + skipQuotation(Category) + "\n"
                    categoriesFile.write(categories_info)
            else:
                for Category in item["Category"]:
                    categories_info = "" + item["ItemID"] + columnSeparator + skipQuotation(Category) + "\n"
                    categoriesFile.write(categories_info)


            # parse Items data to items file.
            items_info = "" + item["ItemID"] + columnSeparator + SellerID
            if item["Name"] == None:
                items_info += columnSeparator + "NULL"
            else:
                items_info += columnSeparator + skipQuotation(item["Name"]) 

            if "Buy_Price" in item.keys():
                items_info += columnSeparator + transformDollar(item["Buy_Price"])
            else:
                items_info += columnSeparator + "NULL"

            if item["First_Bid"] == None:
                items_info += columnSeparator + "NULL"
            else:
                items_info += columnSeparator + transformDollar(item["First_Bid"])

            if item["Currently"] == None:
                items_info += columnSeparator + "NULL"
            else:
                items_info += columnSeparator + transformDollar(item["Currently"]) 

            if item["Number_of_Bids"] == None:
                items_info += columnSeparator + "NULL"
            else:
                items_info += columnSeparator + item["Number_of_Bids"]

            if item["Started"] == None:
                items_info += columnSeparator + "NULL"
            else:
                items_info += columnSeparator + transformDttm(item["Started"])

            if item["Ends"] == None:
                items_info += columnSeparator + "NULL"
            else:
                items_info += columnSeparator + transformDttm(item["Ends"])

            if item["Description"] == None:
                items_info += columnSeparator + "NULL" + "\n"
            else:
                items_info += columnSeparator + skipQuotation(item["Description"]) + "\n" 

            itemsFile.write(items_info)

        auctionUserFile.close() 
        bidsFile.close()
        categoriesFile.close()
        itemsFile.close()

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print ("Success parsing " + f)

if __name__ == '__main__': 
    main(sys.argv)
