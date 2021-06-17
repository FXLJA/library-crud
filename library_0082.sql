-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 17, 2021 at 11:11 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_0082`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(255) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('32180018', 'ferdy');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` varchar(255) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `thumbnail` text DEFAULT NULL,
  `file_path` text DEFAULT NULL,
  `category_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `title`, `author`, `thumbnail`, `file_path`, `category_id`) VALUES
('T001', 'It', 'Stephen King', 'thumbnails/T001/It.jpg', 'books/T001/It.txt', 'HRR'),
('T002', 'Percy Jackson & The Olympians: The Lightning Thief', 'Rick Riordan', 'thumbnails/T002/Percy_Jackson__The_Olympians_The_Lightning_Thief.jpg', 'books/T002/Percy_Jackson__The_Olympians_The_Lightning_Thief.txt', 'FAN');

--
-- Triggers `book`
--
DELIMITER $$
CREATE TRIGGER `on_book_delete` AFTER DELETE ON `book` FOR EACH ROW INSERT INTO log VALUES(
    null,
    CONCAT('Delete ', old.book_id),
    now()
    )
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `on_book_insert` AFTER INSERT ON `book` FOR EACH ROW INSERT INTO log VALUES(
    null,
    CONCAT('Insert ', new.book_id),
    now()
    )
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `on_book_update` AFTER UPDATE ON `book` FOR EACH ROW INSERT INTO log VALUES(
    null,
    CONCAT('Update ', new.book_id),
    now()
    )
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `borrow`
--

CREATE TABLE `borrow` (
  `borrow_id` int(10) NOT NULL,
  `book_id` varchar(10) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `secret_key` text DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` varchar(10) NOT NULL,
  `category_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `category_name`) VALUES
('CLS', 'Classics'),
('DCM', 'Documentary'),
('EDU', 'Education'),
('ESA', 'Essay'),
('FAN', 'Fantasy'),
('FCT', 'Fiction'),
('HRR', 'Horror'),
('MYT', 'Mystery'),
('POT', 'Poetry'),
('RLG', 'Religion'),
('ROM', 'Romance'),
('SCF', 'Sci-Fi');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `log_id` int(11) NOT NULL,
  `action_type` varchar(255) DEFAULT NULL,
  `last_update` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`log_id`, `action_type`, `last_update`) VALUES
(1, 'Insert a', '2021-06-17 17:55:35'),
(2, 'Update a', '2021-06-17 17:57:30'),
(3, 'Delete a', '2021-06-17 17:57:43'),
(4, 'Insert F001', '2021-06-18 00:20:26'),
(5, 'Delete F001', '2021-06-18 00:25:17'),
(6, 'Insert B002', '2021-06-18 00:45:03'),
(7, 'Delete B002', '2021-06-18 00:50:23'),
(8, 'Insert E001', '2021-06-18 01:12:56'),
(9, 'Update E001', '2021-06-18 01:17:57'),
(10, 'Update E001', '2021-06-18 01:18:04'),
(11, 'Insert F001', '2021-06-18 01:19:51'),
(12, 'Delete E001', '2021-06-18 01:19:57'),
(13, 'Delete F001', '2021-06-18 01:22:54'),
(14, 'Insert F001', '2021-06-18 01:25:17'),
(15, 'Delete F001', '2021-06-18 01:27:28'),
(16, 'Insert F001', '2021-06-18 01:27:58'),
(17, 'Delete E002', '2021-06-18 01:29:43'),
(18, 'Update F001', '2021-06-18 01:30:57'),
(19, 'Update F001', '2021-06-18 02:31:30'),
(20, 'Update F001', '2021-06-18 02:32:18'),
(21, 'Insert T001', '2021-06-18 03:18:50'),
(22, 'Delete F001', '2021-06-18 03:22:38'),
(23, 'Insert T002', '2021-06-18 03:24:27');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `password` text NOT NULL,
  `gender` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `name`, `password`, `gender`) VALUES
('32180082', 'Jason Alexander', 'pbkdf2:sha256:150000$OjL6Eu85$10e7662dae7631c77214c9229c4afb67d7f52d383175648abc993e144353b879', 'Pria'),
('32180088', 'Jayaku Brilliantio', 'pbkdf2:sha256:150000$PKmIuyBs$2f7d908d7933b995dcd44567d14b0c2f92edc3f0342c4fef6657201c257f8db8', 'Pria');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `borrow`
--
ALTER TABLE `borrow`
  ADD PRIMARY KEY (`borrow_id`),
  ADD KEY `book_id` (`book_id`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`log_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `borrow`
--
ALTER TABLE `borrow`
  MODIFY `borrow_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`);

--
-- Constraints for table `borrow`
--
ALTER TABLE `borrow`
  ADD CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`),
  ADD CONSTRAINT `borrow_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
