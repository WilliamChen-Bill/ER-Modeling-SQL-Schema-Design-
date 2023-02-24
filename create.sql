drop table if exists Items;
drop table if exists AuctionUser;
drop table if exists Bids;
drop table if exists Categories;
create table AuctionUser(UserID CHAR(255) PRIMARY KEY,
                      Rating INTEGER NOT NULL,
                      Location CHAR(255),
                      Country CHAR(255));
create table Items(ItemID INTEGER NOT NULL PRIMARY KEY,
                   Name CHAR(255) NOT NULL,
                   Buy_Price DECIMAL,
                   First_Bid DECIMAL NOT NULL,
                   Currently DECIMAL NOT NULL,
                   Number_of_Bids INTEGER NOT NULL,
                   Started TIMESTAMP NOT NULL,
                   Ends TIMESTAMP NOT NULL,
                   Description TEXT NOT NULL,
                   SellerID CHAR(255) NOT NULL,
                   FOREIGN KEY (SellerID) REFERENCES AuctionUser DEFERRABLE INITIALLY DEFERRED
                   );
create table Bids(ItemID INTEGER NOT NULL,
                  BidderID CHAR(255) NOT NULL,
                  Time TIMESTAMP NOT NULL,
                  Amount DECIMAL NOT NULL,
                  FOREIGN KEY (ItemID) REFERENCES Items DEFERRABLE INITIALLY DEFERRED,
                  FOREIGN KEY (BidderID) REFERENCES AuctionUser DEFERRABLE INITIALLY DEFERRED,
                  PRIMARY KEY(ItemID, BidderID, Amount)
                 );
create table Categories(ItemID INTEGER NOT NULL,
                 Category CHAR(255) NOT NULL,
                 FOREIGN KEY (ItemID) REFERENCES Items DEFERRABLE INITIALLY DEFERRED,
                 PRIMARY KEY(ItemID, Category)
                 );