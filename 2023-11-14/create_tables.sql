DROP TABLE IF EXISTS SalesFact;
DROP TABLE IF EXISTS CustomerDim;
DROP TABLE IF EXISTS ProductDim;

CREATE TABLE SalesFact (
    Sale_ID INT PRIMARY KEY,
    User_ID INT,
    Product_ID VARCHAR(20),
    Amount FLOAT,
    Orders INT,
    FOREIGN KEY (User_ID) REFERENCES CustomerDim(User_ID),
    FOREIGN KEY (Product_ID) REFERENCES ProductDim(Product_ID)
);

CREATE TABLE CustomerDim (
    User_ID INT PRIMARY KEY,
    Cust_name VARCHAR(50),
    Gender CHAR(1),
    Age INT,
    Marital_Status INT,
    State VARCHAR(20),
    Occupation VARCHAR(50),
    FOREIGN KEY (Age) REFERENCES AgeDim(Age),
    FOREIGN KEY (State) REFERENCES LocationDim(State)
);

CREATE TABLE AgeDim (
    Age INT PRIMARY KEY,
    Age_Group VARCHAR(10),

CREATE TABLE LocationDim (
    State VARCHAR(20) PRIMARY KEY,
    Zone VARCHAR(20),
);

CREATE TABLE ProductDim (
    Product_ID VARCHAR(20) PRIMARY KEY,
    Product_Category VARCHAR(20)
);
