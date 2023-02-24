SELECT COUNT(DISTINCT AuctionUser.UserID)
FROM Items, AuctionUser
WHERE Items.SellerID = AuctionUser.UserID 
AND AuctionUser.Rating > 1000;