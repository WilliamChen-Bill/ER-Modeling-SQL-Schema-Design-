SELECT COUNT(DISTINCT Categories.Category)
FROM Categories, Bids
WHERE Categories.ItemID = Bids.ItemID
AND Bids.Amount > 100;