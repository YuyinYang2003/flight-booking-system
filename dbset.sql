-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: aircraft
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `administrator_info`
--

DROP TABLE IF EXISTS `administrator_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator_info` (
  `administrator_id` char(30) NOT NULL COMMENT '管理员的唯一编号',
  `password` varchar(30) NOT NULL COMMENT '登陆密码',
  `phone` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '手机号码',
  `email` varchar(30) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`administrator_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator_info`
--

LOCK TABLES `administrator_info` WRITE;
/*!40000 ALTER TABLE `administrator_info` DISABLE KEYS */;
INSERT INTO `administrator_info` VALUES ('1','1','1','1');
/*!40000 ALTER TABLE `administrator_info` ENABLE KEYS */;
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
INSERT INTO `airplane_info` VALUES ('1','yangyuyin','杨羽因大笨蛋',50,50,50),('CA','yy','DA',50,50,50),('CB','yz','D',5,5,5),('CC','yd','B',50,60,60);
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
INSERT INTO `airport_info` VALUES ('1','上海1','上海',8),('2','北京1','北京',8),('3','日本1','日本',9),('4','韩国1','韩国',9),('5','旧金山1','美国',-5);
/*!40000 ALTER TABLE `airport_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add flight',8,'add_flight'),(30,'Can change flight',8,'change_flight'),(31,'Can delete flight',8,'delete_flight'),(32,'Can view flight',8,'view_flight'),(33,'Can add order',9,'add_order'),(34,'Can change order',9,'change_order'),(35,'Can delete order',9,'delete_order'),(36,'Can view order',9,'view_order'),(37,'Can add ticket',10,'add_ticket'),(38,'Can change ticket',10,'change_ticket'),(39,'Can delete ticket',10,'delete_ticket'),(40,'Can view ticket',10,'view_ticket'),(41,'Can add user_info',11,'add_user_info'),(42,'Can change user_info',11,'change_user_info'),(43,'Can delete user_info',11,'delete_user_info'),(44,'Can view user_info',11,'view_user_info'),(45,'Can add administrator_info',12,'add_administrator_info'),(46,'Can change administrator_info',12,'change_administrator_info'),(47,'Can delete administrator_info',12,'delete_administrator_info'),(48,'Can view administrator_info',12,'view_administrator_info'),(49,'Can add passenger_info',13,'add_passenger_info'),(50,'Can change passenger_info',13,'change_passenger_info'),(51,'Can delete passenger_info',13,'delete_passenger_info'),(52,'Can view passenger_info',13,'view_passenger_info'),(53,'Can add airplane_info',14,'add_airplane_info'),(54,'Can change airplane_info',14,'change_airplane_info'),(55,'Can delete airplane_info',14,'delete_airplane_info'),(56,'Can view airplane_info',14,'view_airplane_info'),(57,'Can add airport_info',15,'add_airport_info'),(58,'Can change airport_info',15,'change_airport_info'),(59,'Can delete airport_info',15,'delete_airport_info'),(60,'Can view airport_info',15,'view_airport_info'),(61,'Can add flight_info',16,'add_flight_info'),(62,'Can change flight_info',16,'change_flight_info'),(63,'Can delete flight_info',16,'delete_flight_info'),(64,'Can view flight_info',16,'view_flight_info'),(65,'Can add favorites',17,'add_favorites'),(66,'Can change favorites',17,'change_favorites'),(67,'Can delete favorites',17,'delete_favorites'),(68,'Can view favorites',17,'view_favorites'),(69,'Can add order_info',18,'add_order_info'),(70,'Can change order_info',18,'change_order_info'),(71,'Can delete order_info',18,'delete_order_info'),(72,'Can view order_info',18,'view_order_info'),(73,'Can add passenger_user',19,'add_passenger_user'),(74,'Can change passenger_user',19,'change_passenger_user'),(75,'Can delete passenger_user',19,'delete_passenger_user'),(76,'Can view passenger_user',19,'view_passenger_user'),(77,'Can add flight_result',20,'add_flight_result'),(78,'Can change flight_result',20,'change_flight_result'),(79,'Can delete flight_result',20,'delete_flight_result'),(80,'Can view flight_result',20,'view_flight_result'),(81,'Can add flight_city2',21,'add_flight_city2'),(82,'Can change flight_city2',21,'change_flight_city2'),(83,'Can delete flight_city2',21,'delete_flight_city2'),(84,'Can view flight_city2',21,'view_flight_city2');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(12,'aircraft','administrator_info'),(14,'aircraft','airplane_info'),(15,'aircraft','airport_info'),(17,'aircraft','favorites'),(8,'aircraft','flight'),(21,'aircraft','flight_city2'),(16,'aircraft','flight_info'),(20,'aircraft','flight_result'),(9,'aircraft','order'),(18,'aircraft','order_info'),(13,'aircraft','passenger_info'),(19,'aircraft','passenger_user'),(10,'aircraft','ticket'),(7,'aircraft','user'),(11,'aircraft','user_info'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-06-17 11:21:21.629235'),(2,'auth','0001_initial','2023-06-17 11:21:22.015854'),(3,'admin','0001_initial','2023-06-17 11:21:22.119498'),(4,'admin','0002_logentry_remove_auto_add','2023-06-17 11:21:22.130498'),(5,'admin','0003_logentry_add_action_flag_choices','2023-06-17 11:21:22.139516'),(6,'contenttypes','0002_remove_content_type_name','2023-06-17 11:21:22.202481'),(7,'auth','0002_alter_permission_name_max_length','2023-06-17 11:21:22.250442'),(8,'auth','0003_alter_user_email_max_length','2023-06-17 11:21:22.279411'),(9,'auth','0004_alter_user_username_opts','2023-06-17 11:21:22.293407'),(10,'auth','0005_alter_user_last_login_null','2023-06-17 11:21:22.330409'),(11,'auth','0006_require_contenttypes_0002','2023-06-17 11:21:22.334416'),(12,'auth','0007_alter_validators_add_error_messages','2023-06-17 11:21:22.351408'),(13,'auth','0008_alter_user_username_max_length','2023-06-17 11:21:22.394407'),(14,'auth','0009_alter_user_last_name_max_length','2023-06-17 11:21:22.434415'),(15,'auth','0010_alter_group_name_max_length','2023-06-17 11:21:22.454408'),(16,'auth','0011_update_proxy_permissions','2023-06-17 11:21:22.468407'),(17,'auth','0012_alter_user_first_name_max_length','2023-06-17 11:21:22.516408'),(18,'sessions','0001_initial','2023-06-17 11:21:22.545746');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorites` (
  `favorite_id` int unsigned NOT NULL COMMENT '唯一标识收藏飞行的编号',
  `user_name` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '收藏属于哪个用户',
  `flight_num1` char(30) DEFAULT NULL COMMENT '收藏的唯一标识飞机飞行的编号1',
  `flight_num2` char(30) DEFAULT NULL COMMENT '收藏的唯一标识飞机飞行的编号2',
  `set_class1` enum('经济舱','头等舱','公务舱') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '第一个航班的舱位',
  `set_class2` enum('经济舱','头等舱','公务舱','无') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '第二个航班的舱位',
  `total_price` decimal(6,0) NOT NULL COMMENT '航班的原始价格',
  `transfer` datetime DEFAULT NULL COMMENT '两个航班中间的转机时间',
  PRIMARY KEY (`favorite_id`),
  KEY `flight_num1` (`flight_num1`),
  KEY `flight_num2` (`flight_num2`),
  KEY `user_name` (`user_name`)
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
 1 AS `id`,
 1 AS `flight_num1`,
 1 AS `airplane_num1`,
 1 AS `depart_time1`,
 1 AS `arrive_time1`,
 1 AS `depart_airport_name`,
 1 AS `depart_city`,
 1 AS `depart_time_zone`,
 1 AS `baggage_info1`,
 1 AS `current_bussiness_set1`,
 1 AS `current_economy_set1`,
 1 AS `current_first_set1`,
 1 AS `transfer_airport_name`,
 1 AS `transfer_city`,
 1 AS `tranfer_time_zone`,
 1 AS `economy_class_price`,
 1 AS `first_class_price`,
 1 AS `business_class_price`,
 1 AS `flight_num2`,
 1 AS `airplane_num2`,
 1 AS `arrive_airport_name`,
 1 AS `depart_time2`,
 1 AS `arrive_time2`,
 1 AS `arrive_city`,
 1 AS `arrive_time_zone`,
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
INSERT INTO `flight_info` VALUES ('1','1','CA','2','2023-06-24 17:46:55','2023-06-25 17:47:03',30,50,40,0,0,0,'0'),('2','2','CB','3','2023-06-26 12:48:14','2023-06-26 19:48:20',30,50,40,20,14,100,'0'),('3','1','CC','3','2023-06-23 17:48:39','2023-06-24 17:48:47',20,40,30,20,20,20,'1'),('4','1','CC','5','2023-06-23 15:50:10','2023-06-24 10:50:22',200,300,240,50,47,49,'0');
/*!40000 ALTER TABLE `flight_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_info`
--

DROP TABLE IF EXISTS `order_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_info` (
  `order_id` int NOT NULL AUTO_INCREMENT COMMENT '唯一标识订单的编号',
  `order_time` datetime NOT NULL COMMENT '订单时间',
  `passenger_identity_id` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '乘机人身份证号',
  `flight_num1` char(10) DEFAULT NULL COMMENT '航班号1',
  `flight_num2` char(10) DEFAULT NULL COMMENT '航班号2',
  `set_class1` enum('经济舱','头等舱','公务舱') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '舱位1',
  `set_class2` enum('经济舱','头等舱','公务舱','无') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '舱位2',
  `set_num1` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '座位号1',
  `set_num2` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '座位号2',
  `order_state` enum('正常','航班取消','退款申请','已退款') DEFAULT '正常' COMMENT '订单的状态',
  `point_use` enum('是','否') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '否' COMMENT '是否使用积分',
  `price` decimal(8,2) DEFAULT NULL COMMENT '用户实际支付的价格',
  `user_name` char(30) DEFAULT NULL COMMENT '下单的用户名',
  PRIMARY KEY (`order_id`),
  KEY `user_name` (`user_name`),
  KEY `flight_num1` (`flight_num1`),
  KEY `flight_num2` (`flight_num2`),
  KEY `passenger_identity_id` (`passenger_identity_id`),
  CONSTRAINT `order_info_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `user_info` (`user_name`),
  CONSTRAINT `order_info_ibfk_4` FOREIGN KEY (`passenger_identity_id`) REFERENCES `passenger_info` (`passenger_identity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_info`
--

LOCK TABLES `order_info` WRITE;
/*!40000 ALTER TABLE `order_info` DISABLE KEYS */;
INSERT INTO `order_info` VALUES (3,'2023-06-23 06:04:55','333333333333333333','1','','经济舱','无','JJ-45','','航班取消','否',30.00,'qq'),(4,'2023-06-23 06:05:24','333333333333333333','2','','经济舱','无','JJ-94','','已退款','否',30.00,'qq'),(5,'2023-06-23 06:05:29','333333333333333333','3','','经济舱','无','JJ-149','','已退款','否',20.00,'qq'),(6,'2023-06-23 06:13:30','333333333333333333','1','2','经济舱','经济舱','JJ-43','JJ-92','航班取消','否',60.00,'qq'),(7,'2023-06-23 06:22:20','333333333333333333','1','2','经济舱','经济舱','JJ-42','JJ-91','航班取消','否',60.00,'qq'),(8,'2023-06-23 06:35:33','333333333333333333','1','2','经济舱','经济舱','JJ-33','JJ-82','航班取消','否',60.00,'qq'),(9,'2023-06-23 06:35:37','333333333333333333','1','2','经济舱','经济舱','JJ-32','JJ-81','航班取消','是',60.00,'qq'),(10,'2023-06-23 06:38:13','333333333333333333','3','','公务舱','无','SW56','','正常','是',30.00,'qq'),(11,'2023-06-23 06:38:21','333333333333333333','3','','经济舱','无','JJ-148','','正常','否',20.00,'qq'),(12,'2023-06-23 07:28:46','333333333333333333','1','','经济舱','无','JJ1','','航班取消','否',30.00,'qq'),(13,'2023-06-23 08:49:34','1','1','2','头等舱','头等舱','TD1','TD1','航班取消','否',100.00,'qq'),(14,'2023-06-23 10:56:54','333333333333333333','4','','头等舱','无','TD13','','正常','是',300.00,'qq'),(15,'2023-06-23 11:16:03','333333333333333333','2','','头等舱','无','TD-9','','正常','否',50.00,'qq');
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
INSERT INTO `passenger_info` VALUES ('1','杨','男','133','133','普通乘客'),('222222222222222222','笨蛋','男','22222222222','CA','普通乘客'),('333333333333333333','测试','女','13333333333','133','普通乘客');
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
  `passenger_user_key` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`passenger_user_key`),
  KEY `passenger_identity_id` (`passenger_identity_id`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `passenger_user_ibfk_1` FOREIGN KEY (`passenger_identity_id`) REFERENCES `passenger_info` (`passenger_identity_id`),
  CONSTRAINT `passenger_user_ibfk_2` FOREIGN KEY (`user_name`) REFERENCES `user_info` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger_user`
--

LOCK TABLES `passenger_user` WRITE;
/*!40000 ALTER TABLE `passenger_user` DISABLE KEYS */;
INSERT INTO `passenger_user` VALUES ('1','qq',1),('333333333333333333','qq',2);
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
INSERT INTO `user_info` VALUES ('qq','123456','33333333333','unknown1@qq.com','非会员',0),('yy','123456','13333333333','unknown@host.com','非会员',0),('yyy','123456','13333333333','unknown@host.com','非会员',0);
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
/*!50001 VIEW `filght_result` (`id`,`flight_num1`,`airplane_num1`,`depart_time1`,`arrive_time1`,`depart_airport_name`,`depart_city`,`depart_time_zone`,`baggage_info1`,`current_bussiness_set1`,`current_economy_set1`,`current_first_set1`,`transfer_airport_name`,`transfer_city`,`tranfer_time_zone`,`economy_class_price`,`first_class_price`,`business_class_price`,`flight_num2`,`airplane_num2`,`arrive_airport_name`,`depart_time2`,`arrive_time2`,`arrive_city`,`arrive_time_zone`,`baggage_info2`,`current_bussiness_set2`,`current_economy_set2`,`current_first_set2`) AS select concat(`a`.`flight_num`,`b`.`flight_num`) AS `concat(a.flight_num,b.flight_num)`,`a`.`flight_num` AS `flight_num`,`a`.`airplane_num` AS `airplane_num`,`a`.`depart_time` AS `depart_time`,`a`.`arrive_time` AS `arrive_time`,`a`.`depart_airport_name` AS `depart_airport_name`,`a`.`depart_city` AS `depart_city`,`a`.`depart_time_zones` AS `depart_time_zones`,`a`.`baggage_info` AS `baggage_info`,`a`.`current_bussiness_set` AS `current_bussiness_set`,`a`.`current_economy_set` AS `current_economy_set`,`a`.`current_first_set` AS `current_first_set`,`a`.`arrive_airport_name` AS `arrive_airport_name`,`a`.`arrive_city` AS `arrive_city`,`a`.`arrive_time_zones` AS `arrive_time_zones`,(`a`.`economy_class_price` + `b`.`economy_class_price`) AS `a.economy_class_price+b.economy_class_price`,(`a`.`first_class_price` + `b`.`first_class_price`) AS `a.first_class_price+b.first_class_price`,(`a`.`business_class_price` + `b`.`business_class_price`) AS `a.business_class_price+b.business_class_price`,`b`.`flight_num` AS `flight_num`,`b`.`airplane_num` AS `airplane_num`,`b`.`arrive_airport_name` AS `arrive_airport_name`,`b`.`depart_time` AS `depart_time`,`b`.`arrive_time` AS `arrive_time`,`b`.`arrive_city` AS `arrive_city`,`b`.`arrive_time_zones` AS `arrive_time_zones`,`b`.`baggage_info` AS `baggage_info`,`b`.`current_bussiness_set` AS `current_bussiness_set`,`b`.`current_economy_set` AS `current_economy_set`,`b`.`current_first_set` AS `current_first_set` from (`flight_city2` `a` join `flight_city2` `b` on((`a`.`arrive_airport_name` = `b`.`depart_airport_name`))) where ((((`a`.`current_bussiness_set` >= 1) and (`b`.`current_bussiness_set` >= 1)) or ((`a`.`current_first_set` >= 1) and (`b`.`current_first_set` >= 1)) or ((`a`.`current_economy_set` >= 1) and (`b`.`current_economy_set` >= 1))) and (`a`.`arrive_time` < `b`.`depart_time`) and (timestampdiff(HOUR,`a`.`arrive_time`,`b`.`depart_time`) <= 24)) */;
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

-- Dump completed on 2023-06-23 11:21:41
