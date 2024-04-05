-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: covid_management
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `user` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('Jatin','test001'),('Harshit','test010'),('Shashwat','test100'),('Faraz','test111');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beds`
--

DROP TABLE IF EXISTS `beds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beds` (
  `bed_id` int(11) DEFAULT NULL,
  `bed_type` varchar(10) DEFAULT NULL,
  `Room` char(1) DEFAULT NULL,
  `Status` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beds`
--

LOCK TABLES `beds` WRITE;
/*!40000 ALTER TABLE `beds` DISABLE KEYS */;
INSERT INTO `beds` VALUES (1,'normal','a','O'),(2,'icu','a','N'),(3,'normal','b','N'),(4,'ventilator','b','N'),(5,'normal','a','O'),(6,'icu','c','N'),(7,'normal','c','O'),(8,'normal','d','O'),(9,'ventilator','d','O'),(10,'normal','f','N'),(11,'normal','d','N'),(12,'normal','f','N'),(13,'icu','f','O'),(14,'icu','e','O'),(15,'ventilator','e','N');
/*!40000 ALTER TABLE `beds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cases`
--

DROP TABLE IF EXISTS `cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cases` (
  `case_number` int(11) NOT NULL,
  `patient_name` char(20) DEFAULT NULL,
  `date_of_admission` date DEFAULT NULL,
  `father_name` char(20) DEFAULT NULL,
  `mother_name` char(20) DEFAULT NULL,
  `city` char(20) DEFAULT NULL,
  `date_Of_discharge` date DEFAULT NULL,
  `bed_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`case_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cases`
--

LOCK TABLES `cases` WRITE;
/*!40000 ALTER TABLE `cases` DISABLE KEYS */;
INSERT INTO `cases` VALUES (1001,'Gaurav','2020-12-26','Raghvendra Sharma','Poonam Sharma','Faridabad','2021-01-09',8),(1002,'Somdev Rajput','2021-01-08','Ramesh Rajput','Swarnima Rajput','Faridabad','2021-01-22',1),(1003,'Vishesh Batham','2020-12-26','Dharmendra Batham','Swati Batham','Kanpur','2021-01-25',13),(1004,'Durgesh Singh','2020-12-12','Avinesh Singh','Anjali Singh','Jalalabad','2020-12-26',9),(1005,'Suraj Jaiswal','2021-01-09','Harinath Jaiswal','Nisha Jaiswal','Kannauj','2021-01-23',7),(1006,'Devesh','2020-12-26','Dharmendra Kushwah','Jyoti Kushwah','Kanpur','2021-01-09',5),(1007,'Aryan Agrawal','2021-01-10','Narendra Agrawal','Nitu Agrawal','Farrukhabad','2021-01-24',14),(1008,'Anuj majrekar','2021-01-11','Surendr Majrekar','Sobha Manjrekar','Allahabad','2021-01-25',3),(1009,'Jalaj Agrawal','2021-01-10','Ramesh Agrawal','Pinki Agrawal','Kanpur','2021-01-24',11),(1010,'RAj','2021-01-13','Rahul Shakya','Ruchi Shakya','Faridabad','2021-01-27',15),(1011,'Shiv Agrawal','2021-01-14','Sunil Agrawal','Susma Agrawal','Kaimganj','2021-01-28',10);
/*!40000 ALTER TABLE `cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_details`
--

DROP TABLE IF EXISTS `staff_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_details` (
  `unique_id` int(11) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Post` varchar(20) DEFAULT NULL,
  `phone_number` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_details`
--

LOCK TABLES `staff_details` WRITE;
/*!40000 ALTER TABLE `staff_details` DISABLE KEYS */;
INSERT INTO `staff_details` VALUES (100,'Aditi Musunur','Doctor',987123987),(101,'Advitiya Sujeet','Asst. Doctor',987123456),(102,'Durvijay Dixit','Doctor',987988799),(103,'Surya Verma','Neurologist',787123987),(104,'Sarojini Agrawal','Nurse',546788793),(105,'Nandini Gupta','Nurse',997758588),(106,'Raj Agnihotri','Desk Manager',889798978),(107,'Jyoti Mathur','Doctor',678956789),(108,'Varun Singh','Doctor',735678875),(109,'HArsh Vardhan','Peon MAnager',658236758),(110,'Vanshika Rathore','Nurse',678456789),(111,'Vstav Kriplani','Doctor',789789156),(112,'Satendr Yadav','Asst. Doctor',567567891),(113,'Rupa Gangwar','Head Doctor',357895649),(114,'Azra Khan','Neurologist',562413567),(115,'Sanjeev Mishra','Paediatrician',658275628),(116,'Tushar Rastogi','Nurse',137548736),(117,'Avantas Ghosal','Asst. Doctor',782354581),(118,'Dhruv Rathee','Neurologist',786358237),(119,'Gaurang Agrawal','Host',289563985),(120,'Ankit Tiwari','Nurse',786435454);
/*!40000 ALTER TABLE `staff_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tested`
--

DROP TABLE IF EXISTS `tested`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tested` (
  `t_no` int(11) DEFAULT NULL,
  `t_name` varchar(20) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tested`
--

LOCK TABLES `tested` WRITE;
/*!40000 ALTER TABLE `tested` DISABLE KEYS */;
INSERT INTO `tested` VALUES (1,'Anuj','M'),(2,'Rita','F'),(3,'Aditya Pathak','M'),(4,'Ronit Joshi','M'),(5,'shruti','F'),(6,'Racit Verma','M'),(7,'Anup Joshi','M'),(8,'Gargi Dixit','F'),(9,'Prashant Agrawal','M'),(10,'Trishneet Arora','M'),(11,'Sara Ali Khan','F'),(12,'Urvashi Singh','F'),(13,'Mukund Rastogi','M');
/*!40000 ALTER TABLE `tested` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-31 18:03:30
