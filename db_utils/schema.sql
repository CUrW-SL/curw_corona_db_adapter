CREATE TABLE `patient_data` (
  `Patient_No` int(11) NOT NULL,
  `Confirmed_Date` date DEFAULT NULL,
  `Confined_Date` date DEFAULT NULL,
  `Symptoms_Start_Date` date DEFAULT NULL,
  `Symptoms_Start_Location` varchar(45) DEFAULT NULL,
  `Residence_City` varchar(45) DEFAULT NULL,
  `Detected_City` varchar(45) DEFAULT NULL,
  `Detected_Prefecture` varchar(45) DEFAULT NULL,
  `Gender` enum('Female','Male') DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Transmission_Type` enum('Local','Foreign') DEFAULT NULL,
  `Status` enum('Hospitalized','Discharged','Recovered','Deceased','Unspecified') DEFAULT NULL,
  `Notes` varchar(225) NOT NULL,
  PRIMARY KEY (`Patient_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
