SELECT ProductID, ProductName
FROM Products 
WHERE Unit LIKE "% kg %" AND Price BETWEEN 30 AND 60;