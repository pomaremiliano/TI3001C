SELECT FirstName, LastName
FROM Employees
WHERE BirthDate BETWEEN "1950-01-01" AND "1980-12-31"
    AND Notes Like "% Ph.D.%";