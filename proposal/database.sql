CREATE TABLE Residents (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Sex CHAR(1),
    Address VARCHAR(255),
    ContactInformation VARCHAR(100),
    PublicInformation VARCHAR(255)
);

CREATE TABLE Officials (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    ContactInformation VARCHAR(100),
    Position VARCHAR(50),
    TermStart DATE,
    TermEnd DATE
);

CREATE TABLE Roles (
    OfficialID INT,
    Role VARCHAR(50),
    FOREIGN KEY (OfficialID) REFERENCES Officials(ID)
);

CREATE TABLE EventsProjects (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Date DATE,
    Description VARCHAR(255)
);

CREATE TABLE OfficialsInCharge (
    OfficialID INT,
    EventProjectID INT,
    FOREIGN KEY (OfficialID) REFERENCES Officials(ID),
    FOREIGN KEY (EventProjectID) REFERENCES EventsProjects(ID)
);

CREATE TABLE ResidentsInvolved (
    ResidentID INT,
    EventProjectID INT,
    FOREIGN KEY (ResidentID) REFERENCES Residents(ID),
    FOREIGN KEY (EventProjectID) REFERENCES EventsProjects(ID)
);

CREATE TABLE FormRequests (
    ID INT PRIMARY KEY,
    RequesterID INT,
    RequestDate DATE,
    FormDocumentType VARCHAR(50),
    Status VARCHAR(20),
    FOREIGN KEY (RequesterID) REFERENCES Residents(ID)
);