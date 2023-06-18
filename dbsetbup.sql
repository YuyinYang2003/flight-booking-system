-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: flighter
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator` (
  `administrator_id` char(30) NOT NULL COMMENT '管理员的唯一编号',
  `password` varchar(30) NOT NULL COMMENT '登陆密码',
  `phone` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '手机号码',
  `email` varchar(30) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`administrator_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airplane_info`
--

DROP TABLE IF EXISTS `airplane_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airplane_info` (
  `airplane_id` char(10) NOT NULL COMMENT '飞机的客机编号',
  `plane_type` char(10) DEFAULT NULL COMMENT '飞机机型',
  `company_id` char(10) DEFAULT NULL COMMENT '飞机所属的航空公司',
  `economy_set` smallint unsigned NOT NULL DEFAULT '0' COMMENT '经济舱座位数量',
  `first_set` smallint unsigned NOT NULL DEFAULT '0' COMMENT '飞机头等舱座位数',
  `bussiness_set` smallint NOT NULL DEFAULT '0' COMMENT '飞机公务舱座位数量',
  PRIMARY KEY (`airplane_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airplane_info`
--

LOCK TABLES `airplane_info` WRITE;
/*!40000 ALTER TABLE `airplane_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `airplane_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airport_info`
--

DROP TABLE IF EXISTS `airport_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport_info` (
  `airport_id` char(10) NOT NULL COMMENT '唯一标识机场的代码',
  `airport_name` char(10) DEFAULT NULL COMMENT '机场名字',
  `location` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '机场所在城市',
  `time_zones` tinyint NOT NULL COMMENT '机场所在城市的时区',
  PRIMARY KEY (`airport_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport_info`
--

LOCK TABLES `airport_info` WRITE;
/*!40000 ALTER TABLE `airport_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `airport_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorites` (
  `favorite_id` smallint unsigned NOT NULL COMMENT '唯一标识收藏飞行的编号',
  `user_name` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '收藏属于哪个用户',
  `flight_num1` char(30) DEFAULT NULL COMMENT '收藏的唯一标识飞机飞行的编号1',
  `flight_num2` char(30) DEFAULT NULL COMMENT '收藏的唯一标识飞机飞行的编号2',
  `set_class1` enum('经济舱','头等舱','公务舱') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '第一个航班的舱位',
  `set_class2` enum('经济舱','头等舱','公务舱') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '第二个航班的舱位',
  `total_price` decimal(6,0) NOT NULL COMMENT '航班的原始价格',
  `transfer_time` time DEFAULT NULL COMMENT '两个航班中间的转机时间',
  PRIMARY KEY (`user_name`,`favorite_id`),
  KEY `flight_num1` (`flight_num1`),
  KEY `flight_num2` (`flight_num2`),
  CONSTRAINT `favorites_ibfk_1` FOREIGN KEY (`flight_num1`) REFERENCES `flight_info` (`flight_num`),
  CONSTRAINT `favorites_ibfk_2` FOREIGN KEY (`flight_num2`) REFERENCES `flight_info` (`flight_num`),
  CONSTRAINT `favorites_ibfk_3` FOREIGN KEY (`user_name`) REFERENCES `user_info` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `filght_result`
--

DROP TABLE IF EXISTS `filght_result`;
/*!50001 DROP VIEW IF EXISTS `filght_result`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `filght_result` AS SELECT 
 1 AS `flight_num1`,
 1 AS `airplane_num1`,
 1 AS `depart_time1`,
 1 AS `arrive_time1`,
 1 AS `depart_airport_name`,
 1 AS `depart_city`,
 1 AS `baggage_info1`,
 1 AS `current_bussiness_set1`,
 1 AS `current_economy_set1`,
 1 AS `current_first_set1`,
 1 AS `transfer_airport_name`,
 1 AS `transfer_city`,
 1 AS `economy_class_price`,
 1 AS `first_class_price`,
 1 AS `business_class_price`,
 1 AS `flight_num2`,
 1 AS `airplane_num2`,
 1 AS `arrive_airport_name`,
 1 AS `depart_time2`,
 1 AS `arrive_time2`,
 1 AS `arrive_city`,
 1 AS `baggage_info2`,
 1 AS `current_bussiness_set2`,
 1 AS `current_economy_set2`,
 1 AS `current_first_set2`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `flight_city`
--

DROP TABLE IF EXISTS `flight_city`;
/*!50001 DROP VIEW IF EXISTS `flight_city`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `flight_city` AS SELECT 
 1 AS `flight_num`,
 1 AS `dapart_airport_name`,
 1 AS `depart_city`,
 1 AS `airplane_num`,
 1 AS `arrive_airport`,
 1 AS `depart_time`,
 1 AS `arrive_time`,
 1 AS `economy_class_price`,
 1 AS `first_class_price`,
 1 AS `business_class_price`,
 1 AS `baggage_info`,
 1 AS `current_bussiness_set`,
 1 AS `current_economy_set`,
 1 AS `current_first_set`,
 1 AS `depart_time_zones`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `flight_city2`
--

DROP TABLE IF EXISTS `flight_city2`;
/*!50001 DROP VIEW IF EXISTS `flight_city2`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `flight_city2` AS SELECT 
 1 AS `flight_num`,
 1 AS `depart_airport_name`,
 1 AS `depart_city`,
 1 AS `airplane_num`,
 1 AS `arrive_airport_name`,
 1 AS `arrive_city`,
 1 AS `depart_time`,
 1 AS `arrive_time`,
 1 AS `economy_class_price`,
 1 AS `first_class_price`,
 1 AS `business_class_price`,
 1 AS `baggage_info`,
 1 AS `current_bussiness_set`,
 1 AS `current_economy_set`,
 1 AS `current_first_set`,
 1 AS `depart_time_zones`,
 1 AS `arrive_time_zones`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `flight_info`
--

DROP TABLE IF EXISTS `flight_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_info` (
  `flight_num` char(10) NOT NULL COMMENT '唯一标识一趟飞行的编号',
  `depart_airport` char(10) NOT NULL COMMENT '出发机场编号',
  `airplane_num` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '飞机的客机编号',
  `arrive_airport` char(10) DEFAULT NULL COMMENT '到达机场代码',
  `depart_time` datetime DEFAULT NULL COMMENT '出发时间（出发地时区）',
  `arrive_time` datetime DEFAULT NULL COMMENT '到达时间（到达地时区）',
  `economy_class_price` decimal(6,0) DEFAULT NULL COMMENT '经济舱价格',
  `first_class_price` decimal(6,0) DEFAULT NULL COMMENT '头等舱价格',
  `business_class_price` decimal(6,0) DEFAULT NULL COMMENT '公务舱价格',
  `current_economy_set` smallint unsigned DEFAULT NULL COMMENT '航班经济舱的剩余数量',
  `current_first_set` smallint DEFAULT NULL COMMENT '航班头等舱剩余数量',
  `current_bussiness_set` smallint unsigned DEFAULT NULL COMMENT '当前公务舱所剩数量',
  `baggage_info` enum('0','1') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0',
  PRIMARY KEY (`flight_num`),
  KEY `airplane_num` (`airplane_num`),
  KEY `depart_airport` (`depart_airport`),
  KEY `arrive_airport` (`arrive_airport`),
  CONSTRAINT `flight_info_ibfk_1` FOREIGN KEY (`airplane_num`) REFERENCES `airplane_info` (`airplane_id`),
  CONSTRAINT `flight_info_ibfk_2` FOREIGN KEY (`depart_airport`) REFERENCES `airport_info` (`airport_id`),
  CONSTRAINT `flight_info_ibfk_3` FOREIGN KEY (`arrive_airport`) REFERENCES `airport_info` (`airport_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_info`
--

LOCK TABLES `flight_info` WRITE;
/*!40000 ALTER TABLE `flight_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `flight_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_info`
--

DROP TABLE IF EXISTS `order_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_info` (
  `order_id` char(20) NOT NULL COMMENT '唯一标识订单的编号',
  `order_time` datetime NOT NULL COMMENT '订单时间',
  `passenger_identity_id` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '乘机人身份证号',
  `flight_num1` char(10) DEFAULT NULL COMMENT '航班号1',
  `flight_num2` char(10) DEFAULT NULL COMMENT '航班号2',
  `set_class1` enum('经济舱','头等舱','公务舱') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '舱位1',
  `set_class2` enum('经济舱','头等舱','公务舱') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '舱位2',
  `set_num1` char(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '座位号1',
  `set_num2` char(4) DEFAULT NULL COMMENT '座位号2',
  `order_state` enum('正常','航班取消','退款申请','已退款') DEFAULT '正常' COMMENT '订单的状态',
  `piont_use` enum('是','否') DEFAULT '否' COMMENT '是否使用积分',
  `price` decimal(8,2) DEFAULT NULL COMMENT '用户实际支付的价格',
  `user_name` char(30) DEFAULT NULL COMMENT '下单的用户名',
  PRIMARY KEY (`order_id`),
  KEY `user_name` (`user_name`),
  KEY `flight_num1` (`flight_num1`),
  KEY `flight_num2` (`flight_num2`),
  KEY `passenger_identity_id` (`passenger_identity_id`),
  CONSTRAINT `order_info_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `user_info` (`user_name`),
  CONSTRAINT `order_info_ibfk_2` FOREIGN KEY (`flight_num1`) REFERENCES `flight_info` (`flight_num`),
  CONSTRAINT `order_info_ibfk_3` FOREIGN KEY (`flight_num2`) REFERENCES `flight_info` (`flight_num`),
  CONSTRAINT `order_info_ibfk_4` FOREIGN KEY (`passenger_identity_id`) REFERENCES `passenger_info` (`passenger_identity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_info`
--

LOCK TABLES `order_info` WRITE;
/*!40000 ALTER TABLE `order_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger_info`
--

DROP TABLE IF EXISTS `passenger_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger_info` (
  `passenger_identity_id` char(18) NOT NULL COMMENT '乘机人身份证号唯一标识',
  `passenger_name` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '乘机人姓名',
  `sex` enum('男','女') DEFAULT NULL,
  `birthdate` datetime DEFAULT NULL COMMENT '出生日期',
  `phone` char(15) DEFAULT NULL COMMENT '个人手机号码',
  `passport` char(10) DEFAULT NULL COMMENT '护照号码',
  `passenger_type` enum('留学生','普通乘客') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '普通乘客' COMMENT '是否为留学生',
  PRIMARY KEY (`passenger_identity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger_info`
--

LOCK TABLES `passenger_info` WRITE;
/*!40000 ALTER TABLE `passenger_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `passenger_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger_user`
--

DROP TABLE IF EXISTS `passenger_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger_user` (
  `passenger_identity_id` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '乘机人身份证号',
  `user_name` char(30) NOT NULL COMMENT '登记乘机人的用户名',
  PRIMARY KEY (`passenger_identity_id`,`user_name`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `passenger_user_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `user_info` (`user_name`),
  CONSTRAINT `passenger_user_ibfk_2` FOREIGN KEY (`passenger_identity_id`) REFERENCES `passenger_info` (`passenger_identity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger_user`
--

LOCK TABLES `passenger_user` WRITE;
/*!40000 ALTER TABLE `passenger_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `passenger_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `user_name` char(30) NOT NULL COMMENT '用户的唯一编号',
  `password` varchar(30) NOT NULL COMMENT '密码',
  `phone` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '国内11位手机号安全验证',
  `email` varchar(30) DEFAULT NULL COMMENT '邮箱安全验证',
  `user_type` enum('非会员','会员') NOT NULL DEFAULT '非会员' COMMENT '用户账号类型',
  `point` smallint unsigned DEFAULT '0' COMMENT '用户账号积分',
  PRIMARY KEY (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `filght_result`
--

/*!50001 DROP VIEW IF EXISTS `filght_result`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `filght_result` (`flight_num1`,`airplane_num1`,`depart_time1`,`arrive_time1`,`depart_airport_name`,`depart_city`,`baggage_info1`,`current_bussiness_set1`,`current_economy_set1`,`current_first_set1`,`transfer_airport_name`,`transfer_city`,`economy_class_price`,`first_class_price`,`business_class_price`,`flight_num2`,`airplane_num2`,`arrive_airport_name`,`depart_time2`,`arrive_time2`,`arrive_city`,`baggage_info2`,`current_bussiness_set2`,`current_economy_set2`,`current_first_set2`) AS select `a`.`flight_num` AS `flight_num`,`a`.`airplane_num` AS `airplane_num`,`a`.`depart_time` AS `depart_time`,`a`.`arrive_time` AS `arrive_time`,`a`.`depart_airport_name` AS `depart_airport_name`,`a`.`depart_city` AS `depart_city`,`a`.`baggage_info` AS `baggage_info`,`a`.`current_bussiness_set` AS `current_bussiness_set`,`a`.`current_economy_set` AS `current_economy_set`,`a`.`current_first_set` AS `current_first_set`,`a`.`arrive_airport_name` AS `arrive_airport_name`,`a`.`arrive_city` AS `arrive_city`,(`a`.`economy_class_price` + `b`.`economy_class_price`) AS `a.economy_class_price+b.economy_class_price`,(`a`.`first_class_price` + `b`.`first_class_price`) AS `a.first_class_price+b.first_class_price`,(`a`.`business_class_price` + `b`.`business_class_price`) AS `a.business_class_price+b.business_class_price`,`b`.`flight_num` AS `flight_num`,`b`.`airplane_num` AS `airplane_num`,`b`.`arrive_airport_name` AS `arrive_airport_name`,`b`.`depart_time` AS `depart_time`,`b`.`arrive_time` AS `arrive_time`,`b`.`arrive_city` AS `arrive_city`,`b`.`baggage_info` AS `baggage_info`,`b`.`current_bussiness_set` AS `current_bussiness_set`,`b`.`current_economy_set` AS `current_economy_set`,`b`.`current_first_set` AS `current_first_set` from (`flight_city2` `a` join `flight_city2` `b` on((`a`.`arrive_airport_name` = `b`.`depart_airport_name`))) where ((((`a`.`current_bussiness_set` >= 1) and (`b`.`current_bussiness_set` >= 1)) or ((`a`.`current_first_set` >= 1) and (`b`.`current_first_set` >= 1)) or ((`a`.`current_economy_set` >= 1) and (`b`.`current_economy_set` >= 1))) and (`a`.`arrive_time` < `b`.`depart_time`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `flight_city`
--

/*!50001 DROP VIEW IF EXISTS `flight_city`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `flight_city` (`flight_num`,`dapart_airport_name`,`depart_city`,`airplane_num`,`arrive_airport`,`depart_time`,`arrive_time`,`economy_class_price`,`first_class_price`,`business_class_price`,`baggage_info`,`current_bussiness_set`,`current_economy_set`,`current_first_set`,`depart_time_zones`) AS select `a`.`flight_num` AS `flight_num`,`b`.`airport_name` AS `airport_name`,`b`.`location` AS `location`,`a`.`airplane_num` AS `airplane_num`,`a`.`arrive_airport` AS `arrive_airport`,`a`.`depart_time` AS `depart_time`,`a`.`arrive_time` AS `arrive_time`,`a`.`economy_class_price` AS `economy_class_price`,`a`.`first_class_price` AS `first_class_price`,`a`.`business_class_price` AS `business_class_price`,`a`.`baggage_info` AS `baggage_info`,`a`.`current_bussiness_set` AS `current_bussiness_set`,`a`.`current_economy_set` AS `current_economy_set`,`a`.`current_first_set` AS `current_first_set`,`b`.`time_zones` AS `time_zones` from (`flight_info` `a` join `airport_info` `b` on((`a`.`depart_airport` = `b`.`airport_id`))) where ((`a`.`current_economy_set` >= 1) or (`a`.`current_first_set` >= 1) or (`a`.`current_bussiness_set` >= 1)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `flight_city2`
--

/*!50001 DROP VIEW IF EXISTS `flight_city2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `flight_city2` (`flight_num`,`depart_airport_name`,`depart_city`,`airplane_num`,`arrive_airport_name`,`arrive_city`,`depart_time`,`arrive_time`,`economy_class_price`,`first_class_price`,`business_class_price`,`baggage_info`,`current_bussiness_set`,`current_economy_set`,`current_first_set`,`depart_time_zones`,`arrive_time_zones`) AS select `a`.`flight_num` AS `flight_num`,`a`.`dapart_airport_name` AS `dapart_airport_name`,`a`.`depart_city` AS `depart_city`,`a`.`airplane_num` AS `airplane_num`,`b`.`airport_name` AS `airport_name`,`b`.`location` AS `location`,`a`.`depart_time` AS `depart_time`,`a`.`arrive_time` AS `arrive_time`,`a`.`economy_class_price` AS `economy_class_price`,`a`.`first_class_price` AS `first_class_price`,`a`.`business_class_price` AS `business_class_price`,`a`.`baggage_info` AS `baggage_info`,`a`.`current_bussiness_set` AS `current_bussiness_set`,`a`.`current_economy_set` AS `current_economy_set`,`a`.`current_first_set` AS `current_first_set`,`a`.`depart_time_zones` AS `depart_time_zones`,`b`.`time_zones` AS `time_zones` from (`flight_city` `a` join `airport_info` `b` on((`a`.`arrive_airport` = `b`.`airport_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-18 14:45:55
