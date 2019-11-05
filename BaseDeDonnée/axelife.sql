
CREATE DATABASE IF NOT EXISTS axelife DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE axelife;

DROP TABLE IF EXISTS users ;
CREATE TABLE `users` (
  `ID` bigint(20) NOT NULL ,
  `NOM` varchar(30) NOT NULL,
  `PRENOM` varchar(30) NOT NULL,
  `AGE` int NOT NULL,
  `POIDS` int NOT NULL,
  `TAILLE` int NOT NULL,
  `SEXE` varchar(5) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 ;

DROP TABLE IF EXISTS Medecin ;
CREATE TABLE Medecin (
  ID_MEDECIN SMALLINT AUTO_INCREMENT NOT NULL,
  Nom varchar(20),
  Prenom varchar(20),
  Mail varchar (50),
  Telephone varchar(20),
  ID_USERS bigint(20),
  PRIMARY KEY (ID_MEDECIN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS user_data ;
CREATE TABLE user_data (
 Dates date,
 Horaire time,
 bpm int,
 csp int,
 cdp int,
 psp int,
 pdp int,
 si int,
 oxymetrie int,
 temp varchar(5),
 Alert_PSP int,
 Alert_BPM int,
 Alert_CSP int,
 Alert_PDP int,
 Alert_SI int,
 Alert_Oxy int,
 Alert_Temp int,
 LimitBasse_BPM int,
 LimitHaute_BPM int,
 LimitBasse_CSP int,
 LimitHaute_CSP int,
 LimitBasse_CDP int,
 LimitHaute_CDP int,
 LimitBasse_PSP int,
 LimitHaute_PSP int,
 LimitBasse_PDP int,
 LimitHaute_PDP int,
 LimitBasse_SI int,
 LimitHaute_SI int,
 LimitBasse_Oxy int,
 LimitHaute_Oxy int,
 LimitBasse_Temp int,
 LimitHaute_Temp int,
 Latitude varchar(10),
 Longitude varchar(10),
 City varchar(255)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE Medecin ADD CONSTRAINT FK_Medecin_id_user FOREIGN KEY(ID_USERS) REFERENCES users(ID);

