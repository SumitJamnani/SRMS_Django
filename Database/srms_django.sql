-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 23, 2021 at 05:20 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `srms_django`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add extended user', 1, 'add_extendeduser'),
(2, 'Can change extended user', 1, 'change_extendeduser'),
(3, 'Can delete extended user', 1, 'delete_extendeduser'),
(4, 'Can view extended user', 1, 'view_extendeduser'),
(5, 'Can add course_m', 2, 'add_course_m'),
(6, 'Can change course_m', 2, 'change_course_m'),
(7, 'Can delete course_m', 2, 'delete_course_m'),
(8, 'Can view course_m', 2, 'view_course_m'),
(9, 'Can add semester_m', 3, 'add_semester_m'),
(10, 'Can change semester_m', 3, 'change_semester_m'),
(11, 'Can delete semester_m', 3, 'delete_semester_m'),
(12, 'Can view semester_m', 3, 'view_semester_m'),
(13, 'Can add division_m', 4, 'add_division_m'),
(14, 'Can change division_m', 4, 'change_division_m'),
(15, 'Can delete division_m', 4, 'delete_division_m'),
(16, 'Can view division_m', 4, 'view_division_m'),
(17, 'Can add batch_m', 5, 'add_batch_m'),
(18, 'Can change batch_m', 5, 'change_batch_m'),
(19, 'Can delete batch_m', 5, 'delete_batch_m'),
(20, 'Can view batch_m', 5, 'view_batch_m'),
(21, 'Can add subject_m', 6, 'add_subject_m'),
(22, 'Can change subject_m', 6, 'change_subject_m'),
(23, 'Can delete subject_m', 6, 'delete_subject_m'),
(24, 'Can view subject_m', 6, 'view_subject_m'),
(25, 'Can add faculty_m', 7, 'add_faculty_m'),
(26, 'Can change faculty_m', 7, 'change_faculty_m'),
(27, 'Can delete faculty_m', 7, 'delete_faculty_m'),
(28, 'Can view faculty_m', 7, 'view_faculty_m'),
(29, 'Can add exam_m', 8, 'add_exam_m'),
(30, 'Can change exam_m', 8, 'change_exam_m'),
(31, 'Can delete exam_m', 8, 'delete_exam_m'),
(32, 'Can view exam_m', 8, 'view_exam_m'),
(33, 'Can add result_m', 9, 'add_result_m'),
(34, 'Can change result_m', 9, 'change_result_m'),
(35, 'Can delete result_m', 9, 'delete_result_m'),
(36, 'Can view result_m', 9, 'view_result_m'),
(37, 'Can add log entry', 10, 'add_logentry'),
(38, 'Can change log entry', 10, 'change_logentry'),
(39, 'Can delete log entry', 10, 'delete_logentry'),
(40, 'Can view log entry', 10, 'view_logentry'),
(41, 'Can add permission', 11, 'add_permission'),
(42, 'Can change permission', 11, 'change_permission'),
(43, 'Can delete permission', 11, 'delete_permission'),
(44, 'Can view permission', 11, 'view_permission'),
(45, 'Can add group', 12, 'add_group'),
(46, 'Can change group', 12, 'change_group'),
(47, 'Can delete group', 12, 'delete_group'),
(48, 'Can view group', 12, 'view_group'),
(49, 'Can add user', 13, 'add_user'),
(50, 'Can change user', 13, 'change_user'),
(51, 'Can delete user', 13, 'delete_user'),
(52, 'Can view user', 13, 'view_user'),
(53, 'Can add content type', 14, 'add_contenttype'),
(54, 'Can change content type', 14, 'change_contenttype'),
(55, 'Can delete content type', 14, 'delete_contenttype'),
(56, 'Can view content type', 14, 'view_contenttype'),
(57, 'Can add session', 15, 'add_session'),
(58, 'Can change session', 15, 'change_session'),
(59, 'Can delete session', 15, 'delete_session'),
(60, 'Can view session', 15, 'view_session');

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
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$5eXgJAeVqytH7hRhOouvfA$MnGc9NDor/RldOh9JA6xzH4wiE5d4AdpG23ZJofM+lU=', '2021-07-23 14:57:16.728030', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2021-07-19 00:38:12.177788'),
(27, 'pbkdf2_sha256$260000$5plUHwRllrVwjdmoCTqeGb$j67zd43VcjEcgVi+1yEw1G0UNoLt+bwCGsvfTZm/pEY=', '2021-07-23 14:05:47.692005', 0, 'hardiksoni', '', '', 'hs@gmail.com', 0, 1, '2021-07-23 13:50:51.863618'),
(28, 'pbkdf2_sha256$260000$o38eS4BJFZiVsEDvBnQzzD$/EaARC4Z42UNy5XucZBPaQCPMyIvNf+wqyzlp1aSVyU=', '2021-07-23 14:08:43.811819', 0, 'tinalparikh', '', '', 'tp@gmail.com', 0, 1, '2021-07-23 13:59:24.472790'),
(29, 'pbkdf2_sha256$260000$K5YdqDPk5KyBYJdgse0VfD$tq1309LO7i6RP8bpbS7ATyZV3avhPe22gVTPQrrFc1I=', NULL, 0, 'krutijani', '', '', 'kj@gmail.com', 0, 1, '2021-07-23 13:59:48.522819'),
(30, 'pbkdf2_sha256$260000$gqZLh1GxZ784idOgCn8IfM$Q0gnVtjLLQ3GGLNiAqK6POuZktm7KCS+lNnPUwV27jc=', '2021-07-23 14:14:28.611278', 0, 'sumitjamnani', '', '', 'sumitjamnani786@gmail.com', 0, 1, '2021-07-23 14:00:30.712987'),
(31, 'pbkdf2_sha256$260000$CYQwLFKNFyMwbEnkiEa9fd$TsyDbE9pEpkUV2oM8LN0v9xIW52xpXJ5IFN7ZHxXvPc=', '2021-07-23 14:15:56.651159', 0, 'avishapatel', '', '', 'ap@gmail.com', 0, 1, '2021-07-23 14:01:11.142885'),
(32, 'pbkdf2_sha256$260000$w65Bs9VRpHJehMtv953X42$+cteR2oZQ9owkzjeqM+Ta4FwXSJFc3yt5y1NdZCKmFY=', '2021-07-23 14:16:33.551312', 0, 'niyatipathak', '', '', 'np@gmail.com', 0, 1, '2021-07-23 14:01:53.022865');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `batch_m`
--

CREATE TABLE `batch_m` (
  `batch_id` int(11) NOT NULL,
  `batch_name` varchar(30) NOT NULL,
  `course_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `batch_m`
--

INSERT INTO `batch_m` (`batch_id`, `batch_name`, `course_id`, `semester_id`) VALUES
(6, 'MCA 2020', 19, 9);

-- --------------------------------------------------------

--
-- Table structure for table `course_m`
--

CREATE TABLE `course_m` (
  `course_id` int(11) NOT NULL,
  `course_name` varchar(30) NOT NULL,
  `director_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course_m`
--

INSERT INTO `course_m` (`course_id`, `course_name`, `director_id`) VALUES
(19, 'MCA', 27);

-- --------------------------------------------------------

--
-- Table structure for table `division_m`
--

CREATE TABLE `division_m` (
  `division_id` int(11) NOT NULL,
  `division_name` varchar(30) NOT NULL,
  `course_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `division_m`
--

INSERT INTO `division_m` (`division_id`, `division_name`, `course_id`, `semester_id`) VALUES
(8, 'Division A', 19, 9);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'Accounts', 'extendeduser'),
(10, 'admin', 'logentry'),
(12, 'auth', 'group'),
(11, 'auth', 'permission'),
(13, 'auth', 'user'),
(5, 'Batch', 'batch_m'),
(14, 'contenttypes', 'contenttype'),
(2, 'Course', 'course_m'),
(4, 'Division', 'division_m'),
(8, 'Exam', 'exam_m'),
(7, 'Faculty_Subject', 'faculty_m'),
(9, 'Result', 'result_m'),
(3, 'Semester', 'semester_m'),
(15, 'sessions', 'session'),
(6, 'Subject', 'subject_m');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-07-19 00:29:39.741030'),
(2, 'auth', '0001_initial', '2021-07-19 00:29:48.076781'),
(3, 'admin', '0001_initial', '2021-07-19 00:29:50.344455'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-07-19 00:29:50.402545'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-07-19 00:29:50.590563'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-07-19 00:29:52.380668'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-07-19 00:29:54.124076'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-07-19 00:29:57.227458'),
(9, 'auth', '0004_alter_user_username_opts', '2021-07-19 00:29:57.333277'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-07-19 00:29:58.093166'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-07-19 00:29:58.153087'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-07-19 00:29:58.230705'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-07-19 00:30:00.356248'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-07-19 00:30:01.404096'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-07-19 00:30:02.315729'),
(16, 'auth', '0011_update_proxy_permissions', '2021-07-19 00:30:02.413494'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-07-19 00:30:03.527487'),
(18, 'sessions', '0001_initial', '2021-07-19 00:30:04.050088'),
(19, 'Accounts', '0001_initial', '2021-07-19 00:30:52.964104'),
(20, 'Course', '0001_initial', '2021-07-19 00:31:36.849775'),
(21, 'Semester', '0001_initial', '2021-07-19 00:31:50.467402'),
(22, 'Batch', '0001_initial', '2021-07-19 00:32:04.319016'),
(23, 'Division', '0001_initial', '2021-07-19 00:32:16.986143'),
(24, 'Subject', '0001_initial', '2021-07-19 00:33:01.042976'),
(25, 'Faculty_Subject', '0001_initial', '2021-07-19 00:33:26.848071'),
(26, 'Exam', '0001_initial', '2021-07-19 00:33:51.115670'),
(27, 'Result', '0001_initial', '2021-07-19 00:34:07.644479'),
(28, 'Faculty_Subject', '0002_alter_faculty_m_table', '2021-07-19 00:36:43.123535'),
(29, 'Accounts', '0002_rename_subject_name_extendeduser_elective_subject', '2021-07-19 01:22:54.774820'),
(30, 'Accounts', '0003_auto_20210720_0138', '2021-07-19 20:08:34.280827'),
(31, 'Accounts', '0004_alter_extendeduser_enrollment_number', '2021-07-19 20:44:33.382058'),
(32, 'Result', '0002_alter_result_m_enrollment_number', '2021-07-19 20:59:14.739781'),
(33, 'Semester', '0002_alter_semester_m_semester_name', '2021-07-20 18:15:30.851862'),
(34, 'Division', '0002_alter_division_m_division_name', '2021-07-20 20:09:08.494986'),
(35, 'Subject', '0002_subject_m_subject_code', '2021-07-20 20:45:04.468390'),
(36, 'Subject', '0003_alter_subject_m_subject_type', '2021-07-20 20:48:48.265880'),
(37, 'Course', '0002_alter_course_m_director_id', '2021-07-23 09:04:00.035403');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('72jagc0k7u0n4jfbtmbffp71fhvy1im6', '.eJxVjMEOwiAQRP-FsyFAYaUevfsNZHcBqRpISnsy_rtt0oMeZ96beYuA61LC2tMcpiguwojTb0fIz1R3EB9Y701yq8s8kdwVedAuby2m1_Vw_w4K9rKtUevEQDgiG2O9jQDOsht5cNpAJlR-iI637IHYKTgPWZnsAcgoz1l8vuESN58:1m5IIG:zK8qzTi9a13Lga-VNTQeUeU_pYeRSOBc9qKXRqCLZ9c', '2021-08-02 01:42:04.557894'),
('krobvh2hm5lsqi8gndbmuxfr82cih9re', '.eJxVjMEOwiAQRP-FsyFAYaUevfsNZHcBqRpISnsy_rtt0oMeZ96beYuA61LC2tMcpiguwojTb0fIz1R3EB9Y701yq8s8kdwVedAuby2m1_Vw_w4K9rKtUevEQDgiG2O9jQDOsht5cNpAJlR-iI637IHYKTgPWZnsAcgoz1l8vuESN58:1m5UVF:2d6bar9HqtK5NhnAjynnItzQ5NT3uT_b_pDJ2Yf370k', '2021-08-02 14:44:17.737815'),
('ooxfz0zt8mgh3gogqgngu9ky7pxnkziw', '.eJxVjDsOwyAQBe9CHSEwLIaU6X0GtMsnOIlAMnYV5e6xJRdJ-2bmvZnHbS1-62nxc2RXJh27_I6E4ZnqQeID673x0Oq6zMQPhZ-086nF9Lqd7t9BwV722lCALGQQlLVyDiCNNlMWqJw0BiIKDUSgklVZx4SDMWHUaOOuD6iQfb4UDjhn:1m5zGI:YBDMnukJB5L849H1Wg0iXD1Iil0-BZ7f59xXB7VKFKo', '2021-08-03 23:34:54.213757'),
('w38my999zf8tfatkevvwnxsu6z00n1f6', '.eJxVjMEOwiAQRP-FsyFAYaUevfsNZHcBqRpISnsy_rtt0oMeZ96beYuA61LC2tMcpiguwojTb0fIz1R3EB9Y701yq8s8kdwVedAuby2m1_Vw_w4K9rKtUevEQDgiG2O9jQDOsht5cNpAJlR-iI637IHYKTgPWZnsAcgoz1l8vuESN58:1m5txk:wDjmcp9XsfgmVsbuQ0JIXBYlwg1bTCq0rGcJ9Tj5AVE', '2021-08-03 17:55:24.533640');

-- --------------------------------------------------------

--
-- Table structure for table `exam_m`
--

CREATE TABLE `exam_m` (
  `exam_id` int(11) NOT NULL,
  `exam_name` varchar(30) NOT NULL,
  `total_marks` decimal(3,0) NOT NULL,
  `passing_marks` decimal(3,0) NOT NULL,
  `exam_date` date NOT NULL,
  `batch_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `exam_m`
--

INSERT INTO `exam_m` (`exam_id`, `exam_name`, `total_marks`, `passing_marks`, `exam_date`, `batch_id`, `course_id`, `faculty_id`, `semester_id`, `subject_id`) VALUES
(4, 'PHP Unit 1', '50', '25', '2021-07-24', 6, 19, 28, 9, 9);

-- --------------------------------------------------------

--
-- Table structure for table `extendeduser`
--

CREATE TABLE `extendeduser` (
  `id` bigint(20) NOT NULL,
  `user_role` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `enrollment_number` bigint(20) DEFAULT NULL,
  `course_name` varchar(30) DEFAULT NULL,
  `semester_name` varchar(30) DEFAULT NULL,
  `division_name` varchar(30) DEFAULT NULL,
  `batch_name` varchar(30) DEFAULT NULL,
  `elective_subject` varchar(30) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `extendeduser`
--

INSERT INTO `extendeduser` (`id`, `user_role`, `name`, `email`, `enrollment_number`, `course_name`, `semester_name`, `division_name`, `batch_name`, `elective_subject`, `user_id`) VALUES
(7, 'Admin', 'Sumit Jamnani', 'admin@gmail.com', NULL, 'MCA', NULL, NULL, NULL, NULL, 1),
(19, 'Director', 'Hardik Soni', 'hs@gmail.com', 0, 'MCA', NULL, NULL, NULL, NULL, 27),
(20, 'Faculty', 'Tinal Parikh', 'tp@gmail.com', 0, 'MCA', NULL, NULL, NULL, NULL, 28),
(21, 'Faculty', 'Kruti Jani', 'kj@gmail.com', 0, 'MCA', NULL, NULL, NULL, NULL, 29),
(22, 'Student', 'Sumit Jamnani', 'sumitjamnani786@gmail.com', 205350694034, 'MCA', 'Semester 1', 'Division A', 'MCA 2020', 'BCC', 30),
(23, 'Student', 'Avisha Patel', 'ap@gmail.com', 205350694021, 'MCA', 'Semester 1', 'Division A', 'MCA 2020', 'BCC', 31),
(24, 'Student', 'Niyati Pathak', 'np@gmail.com', 205350694013, 'MCA', 'Semester 1', 'Division A', 'MCA 2020', 'BCC', 32);

-- --------------------------------------------------------

--
-- Table structure for table `faculty_subject_m`
--

CREATE TABLE `faculty_subject_m` (
  `fact_subject_id` int(11) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faculty_subject_m`
--

INSERT INTO `faculty_subject_m` (`fact_subject_id`, `batch_id`, `course_id`, `faculty_id`, `semester_id`, `subject_id`) VALUES
(6, 6, 19, 28, 9, 9),
(7, 6, 19, 29, 9, 10);

-- --------------------------------------------------------

--
-- Table structure for table `result_m`
--

CREATE TABLE `result_m` (
  `result_id` int(11) NOT NULL,
  `enrollment_number` bigint(20) DEFAULT NULL,
  `marks_obtained` decimal(3,0) NOT NULL,
  `status` varchar(30) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `result_m`
--

INSERT INTO `result_m` (`result_id`, `enrollment_number`, `marks_obtained`, `status`, `batch_id`, `course_id`, `exam_id`, `faculty_id`, `semester_id`, `subject_id`) VALUES
(8, 205350694034, '20', 'Fail', 6, 19, 4, 28, 9, 9),
(9, 205350694021, '45', 'Pass', 6, 19, 4, 28, 9, 9),
(10, 205350694013, '47', 'Pass', 6, 19, 4, 28, 9, 9);

-- --------------------------------------------------------

--
-- Table structure for table `semester_m`
--

CREATE TABLE `semester_m` (
  `semester_id` int(11) NOT NULL,
  `semester_name` varchar(30) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `semester_m`
--

INSERT INTO `semester_m` (`semester_id`, `semester_name`, `course_id`) VALUES
(9, 'Semester 1', 19),
(10, 'Semester 2', 19);

-- --------------------------------------------------------

--
-- Table structure for table `subject_m`
--

CREATE TABLE `subject_m` (
  `subject_id` int(11) NOT NULL,
  `subject_name` varchar(30) NOT NULL,
  `subject_type` varchar(30) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL,
  `subject_code` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject_m`
--

INSERT INTO `subject_m` (`subject_id`, `subject_name`, `subject_type`, `batch_id`, `course_id`, `semester_id`, `subject_code`) VALUES
(9, 'PHP', 'Regular', 6, 19, 9, 'A001'),
(10, 'BCC', 'Elective', 6, 19, 9, 'A002');

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
-- Indexes for table `batch_m`
--
ALTER TABLE `batch_m`
  ADD PRIMARY KEY (`batch_id`),
  ADD UNIQUE KEY `batch_name` (`batch_name`),
  ADD KEY `batch_m_course_id_c8316d0a_fk_course_m_course_id` (`course_id`),
  ADD KEY `batch_m_semester_id_616a55a2_fk_semester_m_semester_id` (`semester_id`);

--
-- Indexes for table `course_m`
--
ALTER TABLE `course_m`
  ADD PRIMARY KEY (`course_id`),
  ADD UNIQUE KEY `course_name` (`course_name`),
  ADD KEY `course_m_director_id_ed4debe7_fk_auth_user_id` (`director_id`);

--
-- Indexes for table `division_m`
--
ALTER TABLE `division_m`
  ADD PRIMARY KEY (`division_id`),
  ADD KEY `division_m_course_id_4162f3da_fk_course_m_course_id` (`course_id`),
  ADD KEY `division_m_semester_id_d0a4b971_fk_semester_m_semester_id` (`semester_id`);

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
-- Indexes for table `exam_m`
--
ALTER TABLE `exam_m`
  ADD PRIMARY KEY (`exam_id`),
  ADD UNIQUE KEY `exam_name` (`exam_name`),
  ADD KEY `exam_m_batch_id_e30b30db_fk_batch_m_batch_id` (`batch_id`),
  ADD KEY `exam_m_course_id_fcac8d8f_fk_course_m_course_id` (`course_id`),
  ADD KEY `exam_m_faculty_id_1054fa4c_fk_auth_user_id` (`faculty_id`),
  ADD KEY `exam_m_semester_id_3f24bbb9_fk_semester_m_semester_id` (`semester_id`),
  ADD KEY `exam_m_subject_id_9beb4753_fk_subject_m_subject_id` (`subject_id`);

--
-- Indexes for table `extendeduser`
--
ALTER TABLE `extendeduser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `faculty_subject_m`
--
ALTER TABLE `faculty_subject_m`
  ADD PRIMARY KEY (`fact_subject_id`),
  ADD KEY `faculty_m_batch_id_8c0a1ff6_fk_batch_m_batch_id` (`batch_id`),
  ADD KEY `faculty_m_course_id_17e5e885_fk_course_m_course_id` (`course_id`),
  ADD KEY `faculty_m_faculty_id_623482ff_fk_auth_user_id` (`faculty_id`),
  ADD KEY `faculty_m_semester_id_64c80bbf_fk_semester_m_semester_id` (`semester_id`),
  ADD KEY `faculty_m_subject_id_2586ca24_fk_subject_m_subject_id` (`subject_id`);

--
-- Indexes for table `result_m`
--
ALTER TABLE `result_m`
  ADD PRIMARY KEY (`result_id`),
  ADD KEY `result_m_batch_id_fe15b90f_fk_batch_m_batch_id` (`batch_id`),
  ADD KEY `result_m_course_id_f5569aef_fk_course_m_course_id` (`course_id`),
  ADD KEY `result_m_exam_id_95aa8a11_fk_exam_m_exam_id` (`exam_id`),
  ADD KEY `result_m_faculty_id_2d88837c_fk_auth_user_id` (`faculty_id`),
  ADD KEY `result_m_semester_id_f61edc4c_fk_semester_m_semester_id` (`semester_id`),
  ADD KEY `result_m_subject_id_d6aee5b3_fk_subject_m_subject_id` (`subject_id`);

--
-- Indexes for table `semester_m`
--
ALTER TABLE `semester_m`
  ADD PRIMARY KEY (`semester_id`),
  ADD KEY `semester_m_course_id_be1c5d73_fk_course_m_course_id` (`course_id`);

--
-- Indexes for table `subject_m`
--
ALTER TABLE `subject_m`
  ADD PRIMARY KEY (`subject_id`),
  ADD UNIQUE KEY `subject_name` (`subject_name`),
  ADD KEY `subject_m_batch_id_2519c655_fk_batch_m_batch_id` (`batch_id`),
  ADD KEY `subject_m_course_id_e84dcd18_fk_course_m_course_id` (`course_id`),
  ADD KEY `subject_m_semester_id_47af8f56_fk_semester_m_semester_id` (`semester_id`);

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `batch_m`
--
ALTER TABLE `batch_m`
  MODIFY `batch_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `course_m`
--
ALTER TABLE `course_m`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `division_m`
--
ALTER TABLE `division_m`
  MODIFY `division_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `exam_m`
--
ALTER TABLE `exam_m`
  MODIFY `exam_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `extendeduser`
--
ALTER TABLE `extendeduser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `faculty_subject_m`
--
ALTER TABLE `faculty_subject_m`
  MODIFY `fact_subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `result_m`
--
ALTER TABLE `result_m`
  MODIFY `result_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `semester_m`
--
ALTER TABLE `semester_m`
  MODIFY `semester_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `subject_m`
--
ALTER TABLE `subject_m`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

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
-- Constraints for table `batch_m`
--
ALTER TABLE `batch_m`
  ADD CONSTRAINT `batch_m_course_id_c8316d0a_fk_course_m_course_id` FOREIGN KEY (`course_id`) REFERENCES `course_m` (`course_id`),
  ADD CONSTRAINT `batch_m_semester_id_616a55a2_fk_semester_m_semester_id` FOREIGN KEY (`semester_id`) REFERENCES `semester_m` (`semester_id`);

--
-- Constraints for table `course_m`
--
ALTER TABLE `course_m`
  ADD CONSTRAINT `course_m_director_id_ed4debe7_fk_auth_user_id` FOREIGN KEY (`director_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `division_m`
--
ALTER TABLE `division_m`
  ADD CONSTRAINT `division_m_course_id_4162f3da_fk_course_m_course_id` FOREIGN KEY (`course_id`) REFERENCES `course_m` (`course_id`),
  ADD CONSTRAINT `division_m_semester_id_d0a4b971_fk_semester_m_semester_id` FOREIGN KEY (`semester_id`) REFERENCES `semester_m` (`semester_id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `exam_m`
--
ALTER TABLE `exam_m`
  ADD CONSTRAINT `exam_m_batch_id_e30b30db_fk_batch_m_batch_id` FOREIGN KEY (`batch_id`) REFERENCES `batch_m` (`batch_id`),
  ADD CONSTRAINT `exam_m_course_id_fcac8d8f_fk_course_m_course_id` FOREIGN KEY (`course_id`) REFERENCES `course_m` (`course_id`),
  ADD CONSTRAINT `exam_m_faculty_id_1054fa4c_fk_auth_user_id` FOREIGN KEY (`faculty_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `exam_m_semester_id_3f24bbb9_fk_semester_m_semester_id` FOREIGN KEY (`semester_id`) REFERENCES `semester_m` (`semester_id`),
  ADD CONSTRAINT `exam_m_subject_id_9beb4753_fk_subject_m_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject_m` (`subject_id`);

--
-- Constraints for table `extendeduser`
--
ALTER TABLE `extendeduser`
  ADD CONSTRAINT `extendeduser_user_id_11149204_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `faculty_subject_m`
--
ALTER TABLE `faculty_subject_m`
  ADD CONSTRAINT `faculty_m_batch_id_8c0a1ff6_fk_batch_m_batch_id` FOREIGN KEY (`batch_id`) REFERENCES `batch_m` (`batch_id`),
  ADD CONSTRAINT `faculty_m_course_id_17e5e885_fk_course_m_course_id` FOREIGN KEY (`course_id`) REFERENCES `course_m` (`course_id`),
  ADD CONSTRAINT `faculty_m_faculty_id_623482ff_fk_auth_user_id` FOREIGN KEY (`faculty_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `faculty_m_semester_id_64c80bbf_fk_semester_m_semester_id` FOREIGN KEY (`semester_id`) REFERENCES `semester_m` (`semester_id`),
  ADD CONSTRAINT `faculty_m_subject_id_2586ca24_fk_subject_m_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject_m` (`subject_id`);

--
-- Constraints for table `result_m`
--
ALTER TABLE `result_m`
  ADD CONSTRAINT `result_m_batch_id_fe15b90f_fk_batch_m_batch_id` FOREIGN KEY (`batch_id`) REFERENCES `batch_m` (`batch_id`),
  ADD CONSTRAINT `result_m_course_id_f5569aef_fk_course_m_course_id` FOREIGN KEY (`course_id`) REFERENCES `course_m` (`course_id`),
  ADD CONSTRAINT `result_m_exam_id_95aa8a11_fk_exam_m_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `exam_m` (`exam_id`),
  ADD CONSTRAINT `result_m_faculty_id_2d88837c_fk_auth_user_id` FOREIGN KEY (`faculty_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `result_m_semester_id_f61edc4c_fk_semester_m_semester_id` FOREIGN KEY (`semester_id`) REFERENCES `semester_m` (`semester_id`),
  ADD CONSTRAINT `result_m_subject_id_d6aee5b3_fk_subject_m_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject_m` (`subject_id`);

--
-- Constraints for table `semester_m`
--
ALTER TABLE `semester_m`
  ADD CONSTRAINT `semester_m_course_id_be1c5d73_fk_course_m_course_id` FOREIGN KEY (`course_id`) REFERENCES `course_m` (`course_id`);

--
-- Constraints for table `subject_m`
--
ALTER TABLE `subject_m`
  ADD CONSTRAINT `subject_m_batch_id_2519c655_fk_batch_m_batch_id` FOREIGN KEY (`batch_id`) REFERENCES `batch_m` (`batch_id`),
  ADD CONSTRAINT `subject_m_course_id_e84dcd18_fk_course_m_course_id` FOREIGN KEY (`course_id`) REFERENCES `course_m` (`course_id`),
  ADD CONSTRAINT `subject_m_semester_id_47af8f56_fk_semester_m_semester_id` FOREIGN KEY (`semester_id`) REFERENCES `semester_m` (`semester_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
