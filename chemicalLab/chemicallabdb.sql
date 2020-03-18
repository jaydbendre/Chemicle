-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2020 at 01:51 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chemicallabdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add department', 7, 'add_department'),
(26, 'Can change department', 7, 'change_department'),
(27, 'Can delete department', 7, 'delete_department'),
(28, 'Can view department', 7, 'view_department'),
(29, 'Can add lab', 8, 'add_lab'),
(30, 'Can change lab', 8, 'change_lab'),
(31, 'Can delete lab', 8, 'delete_lab'),
(32, 'Can view lab', 8, 'view_lab'),
(33, 'Can add role', 9, 'add_role'),
(34, 'Can change role', 9, 'change_role'),
(35, 'Can delete role', 9, 'delete_role'),
(36, 'Can view role', 9, 'view_role'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user'),
(41, 'Can add sensor_log', 11, 'add_sensor_log'),
(42, 'Can change sensor_log', 11, 'change_sensor_log'),
(43, 'Can delete sensor_log', 11, 'delete_sensor_log'),
(44, 'Can view sensor_log', 11, 'view_sensor_log'),
(45, 'Can add request', 12, 'add_request'),
(46, 'Can change request', 12, 'change_request'),
(47, 'Can delete request', 12, 'delete_request'),
(48, 'Can view request', 12, 'view_request'),
(49, 'Can add notification', 13, 'add_notification'),
(50, 'Can change notification', 13, 'change_notification'),
(51, 'Can delete notification', 13, 'delete_notification'),
(52, 'Can view notification', 13, 'view_notification'),
(53, 'Can add association', 14, 'add_association'),
(54, 'Can change association', 14, 'change_association'),
(55, 'Can delete association', 14, 'delete_association'),
(56, 'Can view association', 14, 'view_association'),
(57, 'Can add code', 15, 'add_code'),
(58, 'Can change code', 15, 'change_code'),
(59, 'Can delete code', 15, 'delete_code'),
(60, 'Can view code', 15, 'view_code'),
(61, 'Can add nonce', 16, 'add_nonce'),
(62, 'Can change nonce', 16, 'change_nonce'),
(63, 'Can delete nonce', 16, 'delete_nonce'),
(64, 'Can view nonce', 16, 'view_nonce'),
(65, 'Can add user social auth', 17, 'add_usersocialauth'),
(66, 'Can change user social auth', 17, 'change_usersocialauth'),
(67, 'Can delete user social auth', 17, 'delete_usersocialauth'),
(68, 'Can view user social auth', 17, 'view_usersocialauth'),
(69, 'Can add partial', 18, 'add_partial'),
(70, 'Can change partial', 18, 'change_partial'),
(71, 'Can delete partial', 18, 'delete_partial'),
(72, 'Can view partial', 18, 'view_partial');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, '!YymUBtO8RRmuHOncDf6W1GMmfLyv8VfGHknZcFy7', '2020-03-18 08:49:26.323548', 0, 'jbendre8', 'Jay', 'Bendre', 'jbendre8@gmail.com', 0, 1, '2020-03-18 05:42:23.197938');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'Lab', 'department'),
(8, 'Lab', 'lab'),
(13, 'Lab', 'notification'),
(12, 'Lab', 'request'),
(9, 'Lab', 'role'),
(11, 'Lab', 'sensor_log'),
(10, 'Lab', 'user'),
(6, 'sessions', 'session'),
(14, 'social_django', 'association'),
(15, 'social_django', 'code'),
(16, 'social_django', 'nonce'),
(18, 'social_django', 'partial'),
(17, 'social_django', 'usersocialauth');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Lab', '0001_initial', '2020-03-13 03:53:46.206707'),
(2, 'contenttypes', '0001_initial', '2020-03-13 03:53:46.774893'),
(3, 'auth', '0001_initial', '2020-03-13 03:53:47.087939'),
(4, 'admin', '0001_initial', '2020-03-13 03:53:47.907990'),
(5, 'admin', '0002_logentry_remove_auto_add', '2020-03-13 03:53:48.094438'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2020-03-13 03:53:48.106511'),
(7, 'contenttypes', '0002_remove_content_type_name', '2020-03-13 03:53:48.205462'),
(8, 'auth', '0002_alter_permission_name_max_length', '2020-03-13 03:53:48.279954'),
(9, 'auth', '0003_alter_user_email_max_length', '2020-03-13 03:53:48.297948'),
(10, 'auth', '0004_alter_user_username_opts', '2020-03-13 03:53:48.309916'),
(11, 'auth', '0005_alter_user_last_login_null', '2020-03-13 03:53:48.381720'),
(12, 'auth', '0006_require_contenttypes_0002', '2020-03-13 03:53:48.385707'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2020-03-13 03:53:48.403628'),
(14, 'auth', '0008_alter_user_username_max_length', '2020-03-13 03:53:48.426089'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2020-03-13 03:53:48.451033'),
(16, 'auth', '0010_alter_group_name_max_length', '2020-03-13 03:53:48.474998'),
(17, 'auth', '0011_update_proxy_permissions', '2020-03-13 03:53:48.491679'),
(18, 'sessions', '0001_initial', '2020-03-13 03:53:48.553369'),
(19, 'Lab', '0002_remove_user_lab_id', '2020-03-17 11:45:30.057810'),
(20, 'Lab', '0003_user_lab_id', '2020-03-17 11:47:11.207537'),
(21, 'default', '0001_initial', '2020-03-18 05:15:03.924186'),
(22, 'social_auth', '0001_initial', '2020-03-18 05:15:03.928923'),
(23, 'default', '0002_add_related_name', '2020-03-18 05:15:04.138852'),
(24, 'social_auth', '0002_add_related_name', '2020-03-18 05:15:04.141807'),
(25, 'default', '0003_alter_email_max_length', '2020-03-18 05:15:04.151779'),
(26, 'social_auth', '0003_alter_email_max_length', '2020-03-18 05:15:04.155770'),
(27, 'default', '0004_auto_20160423_0400', '2020-03-18 05:15:04.165774'),
(28, 'social_auth', '0004_auto_20160423_0400', '2020-03-18 05:15:04.168734'),
(29, 'social_auth', '0005_auto_20160727_2333', '2020-03-18 05:15:04.197666'),
(30, 'social_django', '0006_partial', '2020-03-18 05:15:04.225408'),
(31, 'social_django', '0007_code_timestamp', '2020-03-18 05:15:04.259611'),
(32, 'social_django', '0008_partial_timestamp', '2020-03-18 05:15:04.294671'),
(33, 'social_django', '0004_auto_20160423_0400', '2020-03-18 05:15:04.315811'),
(34, 'social_django', '0001_initial', '2020-03-18 05:15:04.318838'),
(35, 'social_django', '0002_add_related_name', '2020-03-18 05:15:04.323793'),
(36, 'social_django', '0003_alter_email_max_length', '2020-03-18 05:15:04.327779'),
(37, 'social_django', '0005_auto_20160727_2333', '2020-03-18 05:15:04.331769');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4u99f13os3nl3nqk6uld19xqs0q6qvi1', 'ZDA5ZjhjMzAwYjZiMDEwNWU5OWYxY2U1MDg1ZmMzYTkzZmI5NjFiZTp7ImVtYWlsIjoiMjAxNy5qYXkuYmVuZHJlQHZlcy5hYy5pbiIsInVzZXJuYW1lIjoiSmF5IEJlbmRyZSJ9', '2020-04-01 11:18:41.867411'),
('dnf7fyqwsag2y79h6zse9suhdbpdn9wd', 'NDEyOGExMmExYjNmNmQzZDM5Yjg1OTRhZWY2NjJmYTNjZGE0NTcyOTp7Imdvb2dsZS1vYXV0aDJfc3RhdGUiOiJsMUJrY0lxa1VKSE1TNnk4QkNiVUg5WHlzTFV5VEJrTyIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMuZ29vZ2xlLkdvb2dsZU9BdXRoMiIsIl9hdXRoX3VzZXJfaGFzaCI6ImIyZDc3YzFiNzQxMzkyMTg0OTFhY2M2ZDhmYmQ5YTRmYzliZTk5YmEiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJnb29nbGUtb2F1dGgyIn0=', '2020-04-01 06:04:50.957432'),
('ebhzcm970x2wx2j4ehyvf85yxpbbs3b6', 'MWFkYzYxODk3NGZiYzI5OGYxZGViODQ2MWY4NzcxNWM1NTZjZDdmNjp7Imdvb2dsZS1vYXV0aDJfc3RhdGUiOiJOSmVjejlZV0dNTUYyWktudHUxOXhNYlhzaEdkZmM5SiIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMuZ29vZ2xlLkdvb2dsZU9BdXRoMiIsIl9hdXRoX3VzZXJfaGFzaCI6ImIyZDc3YzFiNzQxMzkyMTg0OTFhY2M2ZDhmYmQ5YTRmYzliZTk5YmEiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJnb29nbGUtb2F1dGgyIiwiZW1haWwiOiIyMDE3LmpheS5iZW5kcmVAdmVzLmFjLmluIiwidXNlcm5hbWUiOiJKYXkgQmVuZHJlIn0=', '2020-04-01 06:03:19.000336'),
('s3wb8rmmmc1izh45k2yz3n4gximgfhbg', 'YjE5OWI0Yzk3MjZjZWJmZmY0OWU5ZDFkZGMzNDI5M2M4MjA5NWJmZTp7ImVtYWlsIjoiMjAxNy5qYXkuYmVuZHJlQHZlcy5hYy5pbiIsInVzZXJuYW1lIjoiSmF5IEJlbmRyZSIsImdvb2dsZS1vYXV0aDJfc3RhdGUiOiJ6V3U3RGhYdUVHYWR1cjBrZFRHV1lyTVRUaGhXZXdwSSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMuZ29vZ2xlLkdvb2dsZU9BdXRoMiIsIl9hdXRoX3VzZXJfaGFzaCI6ImIyZDc3YzFiNzQxMzkyMTg0OTFhY2M2ZDhmYmQ5YTRmYzliZTk5YmEiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJnb29nbGUtb2F1dGgyIn0=', '2020-04-01 05:42:23.220907'),
('w54ijwn9s10yeoayl7wokoef188e5vrg', 'ZmQwMzFlZjEzOTYwM2MzYzcwYzgxYWVlNDgyOWJmODhjNTgzMDE1Zjp7ImVtYWlsIjoiMjAxNy5qYXkuYmVuZHJlQHZlcy5hYy5pbiIsInVzZXJuYW1lIjoiSmF5IEJlbmRyZSIsImdvb2dsZS1vYXV0aDJfc3RhdGUiOiJFZXRGem5RR2xzUHhhT0l4TUZyVEhZTzNzTjhKMzdpdSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMuZ29vZ2xlLkdvb2dsZU9BdXRoMiIsIl9hdXRoX3VzZXJfaGFzaCI6ImIyZDc3YzFiNzQxMzkyMTg0OTFhY2M2ZDhmYmQ5YTRmYzliZTk5YmEiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJnb29nbGUtb2F1dGgyIn0=', '2020-04-01 05:51:10.453600');

-- --------------------------------------------------------

--
-- Table structure for table `lab_department`
--

CREATE TABLE `lab_department` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lab_department`
--

INSERT INTO `lab_department` (`id`, `name`) VALUES
(100, 'Bio Chemical'),
(101, 'Environmental'),
(102, 'Textile');

-- --------------------------------------------------------

--
-- Table structure for table `lab_lab`
--

CREATE TABLE `lab_lab` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `dept_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lab_lab`
--

INSERT INTO `lab_lab` (`id`, `name`, `dept_id_id`) VALUES
(1001, 'Bio-chemical Lab 1', 100),
(1002, 'Bio-chemical Lab 2', 100),
(1003, 'Environmental Lab 1', 101),
(1004, 'Environmental Lab 2', 101),
(1005, 'Textile Lab 1', 102),
(1006, 'TextileLab 2', 102);

-- --------------------------------------------------------

--
-- Table structure for table `lab_notification`
--

CREATE TABLE `lab_notification` (
  `id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `timestamp` date NOT NULL,
  `category` varchar(100) NOT NULL,
  `Notification_to_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `lab_request`
--

CREATE TABLE `lab_request` (
  `id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `request_to` int(11) NOT NULL,
  `humidity` double NOT NULL,
  `temperature` double NOT NULL,
  `request_from_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `lab_role`
--

CREATE TABLE `lab_role` (
  `id` int(11) NOT NULL,
  `post` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lab_role`
--

INSERT INTO `lab_role` (`id`, `post`) VALUES
(0, 'Admin'),
(1, 'Lab Incharge'),
(2, 'Lab Operator');

-- --------------------------------------------------------

--
-- Table structure for table `lab_sensor_log`
--

CREATE TABLE `lab_sensor_log` (
  `id` int(11) NOT NULL,
  `temperature` double NOT NULL,
  `humidity` double NOT NULL,
  `air_quality` double NOT NULL,
  `timestamp` date NOT NULL,
  `lab_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `lab_user`
--

CREATE TABLE `lab_user` (
  `id` int(11) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(500) NOT NULL,
  `address` varchar(100) NOT NULL,
  `lab_id_id` int(11) NOT NULL,
  `role_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lab_user`
--

INSERT INTO `lab_user` (`id`, `fname`, `lname`, `email`, `password`, `address`, `lab_id_id`, `role_id_id`) VALUES
(10000, 'Jay', 'Bendre', '2017.jay.bendre@ves.ac.in', 'test', 'lorem Ipsum10000', 1001, 2),
(10001, 'user10001', 'lastname10001', 'user10001@gmail.com', 'user10001', 'lorem Ipsum10001', 1002, 2),
(10002, 'user10002', 'lastname10002', 'user10002@gmail.com', 'user10002', 'lorem Ipsum10002', 1002, 2),
(10003, 'user10003', 'lastname10003', 'user10003@gmail.com', 'user10003', 'lorem Ipsum10003', 1003, 0),
(10004, 'user10004', 'lastname10004', 'user10004@gmail.com', 'user10004', 'lorem Ipsum10004', 1005, 1),
(10005, 'user10005', 'lastname10005', 'user10005@gmail.com', 'user10005', 'lorem Ipsum10005', 1003, 2),
(10006, 'user10006', 'lastname10006', 'user10006@gmail.com', 'user10006', 'lorem Ipsum10006', 1005, 2),
(10007, 'user10007', 'lastname10007', 'user10007@gmail.com', 'user10007', 'lorem Ipsum10007', 1006, 2),
(10008, 'user10008', 'lastname10008', 'user10008@gmail.com', 'user10008', 'lorem Ipsum10008', 1006, 2),
(10009, 'user10009', 'lastname10009', 'user10009@gmail.com', 'user10009', 'lorem Ipsum10009', 1004, 1),
(10010, 'user10010', 'lastname10010', 'user10010@gmail.com', 'user10010', 'lorem Ipsum10010', 1001, 0),
(10011, 'user10011', 'lastname10011', 'user10011@gmail.com', 'user10011', 'lorem Ipsum10011', 1006, 1),
(10012, 'user10012', 'lastname10012', 'user10012@gmail.com', 'user10012', 'lorem Ipsum10012', 1001, 0),
(10013, 'user10013', 'lastname10013', 'user10013@gmail.com', 'user10013', 'lorem Ipsum10013', 1006, 1),
(10014, 'user10014', 'lastname10014', 'user10014@gmail.com', 'user10014', 'lorem Ipsum10014', 1002, 1),
(10015, 'user10015', 'lastname10015', 'user10015@gmail.com', 'user10015', 'lorem Ipsum10015', 1002, 2),
(10016, 'user10016', 'lastname10016', 'user10016@gmail.com', 'user10016', 'lorem Ipsum10016', 1005, 1),
(10017, 'user10017', 'lastname10017', 'user10017@gmail.com', 'user10017', 'lorem Ipsum10017', 1004, 1),
(10018, 'user10018', 'lastname10018', 'user10018@gmail.com', 'user10018', 'lorem Ipsum10018', 1005, 2),
(10019, 'user10019', 'lastname10019', 'user10019@gmail.com', 'user10019', 'lorem Ipsum10019', 1004, 1),
(10020, 'user10020', 'lastname10020', 'user10020@gmail.com', 'user10020', 'lorem Ipsum10020', 1006, 0),
(10021, 'user10021', 'lastname10021', 'user10021@gmail.com', 'user10021', 'lorem Ipsum10021', 1006, 2),
(10022, 'user10022', 'lastname10022', 'user10022@gmail.com', 'user10022', 'lorem Ipsum10022', 1002, 1),
(10023, 'user10023', 'lastname10023', 'user10023@gmail.com', 'user10023', 'lorem Ipsum10023', 1006, 2),
(10024, 'user10024', 'lastname10024', 'user10024@gmail.com', 'user10024', 'lorem Ipsum10024', 1006, 0),
(10025, 'user10025', 'lastname10025', 'user10025@gmail.com', 'user10025', 'lorem Ipsum10025', 1006, 1),
(10026, 'user10026', 'lastname10026', 'user10026@gmail.com', 'user10026', 'lorem Ipsum10026', 1004, 1),
(10027, 'user10027', 'lastname10027', 'user10027@gmail.com', 'user10027', 'lorem Ipsum10027', 1001, 2),
(10028, 'user10028', 'lastname10028', 'user10028@gmail.com', 'user10028', 'lorem Ipsum10028', 1001, 0),
(10029, 'user10029', 'lastname10029', 'user10029@gmail.com', 'user10029', 'lorem Ipsum10029', 1004, 2),
(10030, 'user10030', 'lastname10030', 'user10030@gmail.com', 'user10030', 'lorem Ipsum10030', 1006, 2),
(10031, 'user10031', 'lastname10031', 'user10031@gmail.com', 'user10031', 'lorem Ipsum10031', 1004, 2),
(10032, 'user10032', 'lastname10032', 'user10032@gmail.com', 'user10032', 'lorem Ipsum10032', 1003, 2),
(10033, 'user10033', 'lastname10033', 'user10033@gmail.com', 'user10033', 'lorem Ipsum10033', 1006, 1),
(10034, 'user10034', 'lastname10034', 'user10034@gmail.com', 'user10034', 'lorem Ipsum10034', 1004, 0),
(10035, 'user10035', 'lastname10035', 'user10035@gmail.com', 'user10035', 'lorem Ipsum10035', 1002, 1),
(10036, 'user10036', 'lastname10036', 'user10036@gmail.com', 'user10036', 'lorem Ipsum10036', 1003, 0),
(10037, 'user10037', 'lastname10037', 'user10037@gmail.com', 'user10037', 'lorem Ipsum10037', 1005, 2),
(10038, 'user10038', 'lastname10038', 'user10038@gmail.com', 'user10038', 'lorem Ipsum10038', 1004, 0),
(10039, 'user10039', 'lastname10039', 'user10039@gmail.com', 'user10039', 'lorem Ipsum10039', 1006, 1),
(10040, 'user10040', 'lastname10040', 'user10040@gmail.com', 'user10040', 'lorem Ipsum10040', 1002, 2),
(10041, 'user10041', 'lastname10041', 'user10041@gmail.com', 'user10041', 'lorem Ipsum10041', 1004, 2),
(10042, 'user10042', 'lastname10042', 'user10042@gmail.com', 'user10042', 'lorem Ipsum10042', 1002, 2),
(10043, 'user10043', 'lastname10043', 'user10043@gmail.com', 'user10043', 'lorem Ipsum10043', 1006, 2),
(10044, 'user10044', 'lastname10044', 'user10044@gmail.com', 'user10044', 'lorem Ipsum10044', 1004, 0),
(10045, 'user10045', 'lastname10045', 'user10045@gmail.com', 'user10045', 'lorem Ipsum10045', 1006, 2),
(10046, 'user10046', 'lastname10046', 'user10046@gmail.com', 'user10046', 'lorem Ipsum10046', 1004, 1),
(10047, 'user10047', 'lastname10047', 'user10047@gmail.com', 'user10047', 'lorem Ipsum10047', 1005, 2),
(10048, 'user10048', 'lastname10048', 'user10048@gmail.com', 'user10048', 'lorem Ipsum10048', 1004, 0);

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_association`
--

CREATE TABLE `social_auth_association` (
  `id` int(11) NOT NULL,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int(11) NOT NULL,
  `lifetime` int(11) NOT NULL,
  `assoc_type` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_code`
--

CREATE TABLE `social_auth_code` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_nonce`
--

CREATE TABLE `social_auth_nonce` (
  `id` int(11) NOT NULL,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `salt` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_partial`
--

CREATE TABLE `social_auth_partial` (
  `id` int(11) NOT NULL,
  `token` varchar(32) NOT NULL,
  `next_step` smallint(5) UNSIGNED NOT NULL CHECK (`next_step` >= 0),
  `backend` varchar(32) NOT NULL,
  `data` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_usersocialauth`
--

CREATE TABLE `social_auth_usersocialauth` (
  `id` int(11) NOT NULL,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `social_auth_usersocialauth`
--

INSERT INTO `social_auth_usersocialauth` (`id`, `provider`, `uid`, `extra_data`, `user_id`) VALUES
(1, 'google-oauth2', 'jbendre8@gmail.com', '{\"auth_time\": 1584510209, \"expires\": 3599, \"token_type\": \"Bearer\", \"access_token\": \"ya29.a0Adw1xeVtBZEroQz6VZ12NSfJj-MLzArVDBqc6nHe9YXU7rPGgA_ywjxehrnAg8_lyJOlOCERiAFNl2mXDovolirPyB0qXaPKnIF9vLpeSwXQ5JIY3RsTgoAN_Srkrr7BbJ2cSm-J4NVqWO_WTdMlA9r_g-UpsN9wfqw\"}', 1),
(2, 'google-oauth2', '2017.jay.bendre@ves.ac.in', '{\"auth_time\": 1584521366, \"expires\": 3599, \"token_type\": \"Bearer\", \"access_token\": \"ya29.a0Adw1xeVvntBuqPPJlNvBwNxy_OHBvnGiaBGF-BXvunbDnTI-RBThMEjoH1JV6lzHjsqF4iiCaoU3yMSJRhSpCfBcOOs-Bd8kqlfTruKU46FGASmzQtckIDn5dRqJ6H48HzxcSXAEdIp3ZHUDEInIzU6P4nOmBkVp738\"}', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `lab_department`
--
ALTER TABLE `lab_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lab_lab`
--
ALTER TABLE `lab_lab`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Lab_lab_dept_id_id_35cb9cee_fk_Lab_department_id` (`dept_id_id`);

--
-- Indexes for table `lab_notification`
--
ALTER TABLE `lab_notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Lab_notification_Notification_to_id_44441f71_fk_Lab_user_id` (`Notification_to_id`);

--
-- Indexes for table `lab_request`
--
ALTER TABLE `lab_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Lab_request_request_from_id_a0e59863_fk_Lab_user_id` (`request_from_id`);

--
-- Indexes for table `lab_role`
--
ALTER TABLE `lab_role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lab_sensor_log`
--
ALTER TABLE `lab_sensor_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Lab_sensor_log_lab_id_id_31f3f23b_fk_Lab_lab_id` (`lab_id_id`);

--
-- Indexes for table `lab_user`
--
ALTER TABLE `lab_user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Lab_user_role_id_id_4814c79b_fk_Lab_role_id` (`role_id_id`),
  ADD KEY `Lab_user_lab_id_id_2afa2527_fk_Lab_lab_id` (`lab_id_id`);

--
-- Indexes for table `social_auth_association`
--
ALTER TABLE `social_auth_association`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`);

--
-- Indexes for table `social_auth_code`
--
ALTER TABLE `social_auth_code`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  ADD KEY `social_auth_code_code_a2393167` (`code`),
  ADD KEY `social_auth_code_timestamp_176b341f` (`timestamp`);

--
-- Indexes for table `social_auth_nonce`
--
ALTER TABLE `social_auth_nonce`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`);

--
-- Indexes for table `social_auth_partial`
--
ALTER TABLE `social_auth_partial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_auth_partial_token_3017fea3` (`token`),
  ADD KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`);

--
-- Indexes for table `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  ADD KEY `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `lab_department`
--
ALTER TABLE `lab_department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `lab_lab`
--
ALTER TABLE `lab_lab`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1007;

--
-- AUTO_INCREMENT for table `lab_notification`
--
ALTER TABLE `lab_notification`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lab_request`
--
ALTER TABLE `lab_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lab_role`
--
ALTER TABLE `lab_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lab_sensor_log`
--
ALTER TABLE `lab_sensor_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lab_user`
--
ALTER TABLE `lab_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10049;

--
-- AUTO_INCREMENT for table `social_auth_association`
--
ALTER TABLE `social_auth_association`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_code`
--
ALTER TABLE `social_auth_code`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_nonce`
--
ALTER TABLE `social_auth_nonce`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_partial`
--
ALTER TABLE `social_auth_partial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `lab_lab`
--
ALTER TABLE `lab_lab`
  ADD CONSTRAINT `Lab_lab_dept_id_id_35cb9cee_fk_Lab_department_id` FOREIGN KEY (`dept_id_id`) REFERENCES `lab_department` (`id`);

--
-- Constraints for table `lab_notification`
--
ALTER TABLE `lab_notification`
  ADD CONSTRAINT `Lab_notification_Notification_to_id_44441f71_fk_Lab_user_id` FOREIGN KEY (`Notification_to_id`) REFERENCES `lab_user` (`id`);

--
-- Constraints for table `lab_request`
--
ALTER TABLE `lab_request`
  ADD CONSTRAINT `Lab_request_request_from_id_a0e59863_fk_Lab_user_id` FOREIGN KEY (`request_from_id`) REFERENCES `lab_user` (`id`);

--
-- Constraints for table `lab_sensor_log`
--
ALTER TABLE `lab_sensor_log`
  ADD CONSTRAINT `Lab_sensor_log_lab_id_id_31f3f23b_fk_Lab_lab_id` FOREIGN KEY (`lab_id_id`) REFERENCES `lab_lab` (`id`);

--
-- Constraints for table `lab_user`
--
ALTER TABLE `lab_user`
  ADD CONSTRAINT `Lab_user_lab_id_id_2afa2527_fk_Lab_lab_id` FOREIGN KEY (`lab_id_id`) REFERENCES `lab_lab` (`id`),
  ADD CONSTRAINT `Lab_user_role_id_id_4814c79b_fk_Lab_role_id` FOREIGN KEY (`role_id_id`) REFERENCES `lab_role` (`id`);

--
-- Constraints for table `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  ADD CONSTRAINT `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
