-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 11, 2019 at 08:02 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.2.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_ecom`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_admin`
--

CREATE TABLE `tb_admin` (
  `admin_id` int(11) NOT NULL,
  `admin_email` varchar(60) NOT NULL,
  `admin_pass` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_admin`
--

INSERT INTO `tb_admin` (`admin_id`, `admin_email`, `admin_pass`) VALUES
(1, 'admin@gmail.com', '123'),
(2, 'akash.padhiyar@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `tb_category`
--

CREATE TABLE `tb_category` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(100) NOT NULL,
  `is_deleted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_category`
--

INSERT INTO `tb_category` (`category_id`, `category_name`, `is_deleted`) VALUES
(1, 'Fruit', 0),
(2, 'Vegetables', 0),
(3, 'ddsasad', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tb_contact`
--

CREATE TABLE `tb_contact` (
  `contact_id` int(11) NOT NULL,
  `contact_name` varchar(50) NOT NULL,
  `contact_mobile` varchar(50) NOT NULL,
  `contact_email` varchar(50) NOT NULL,
  `contact_details` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_contact`
--

INSERT INTO `tb_contact` (`contact_id`, `contact_name`, `contact_mobile`, `contact_email`, `contact_details`) VALUES
(1, 'ty', 'tytrytry', 'ty', 'tryty');

-- --------------------------------------------------------

--
-- Table structure for table `tb_feedback`
--

CREATE TABLE `tb_feedback` (
  `feedback_id` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `details` text NOT NULL,
  `fdate` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_feedback`
--

INSERT INTO `tb_feedback` (`feedback_id`, `user_id`, `user_name`, `details`, `fdate`) VALUES
(1, '1', 'sdsad', 'sads', '2019-09-29 14:58:18'),
(2, '2', 'sadsad', 'sadasd', '2019-09-29 14:58:23'),
(3, 'akash@gmail.com', 'akash@gmail.com', 'dfdsf', '0000-00-00 00:00:00'),
(4, 'gfdg', 'gfdg', 'fdgfd', '2019-10-11 02:46:22'),
(5, 'akash@gmail.com', 'akash@gmail.com', 'Nice Website', '2019-10-11 04:40:49');

-- --------------------------------------------------------

--
-- Table structure for table `tb_order_details`
--

CREATE TABLE `tb_order_details` (
  `order_details_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_order_details`
--

INSERT INTO `tb_order_details` (`order_details_id`, `order_id`, `product_id`, `qty`, `amount`) VALUES
(1, 1, 3, 1, 4323);

-- --------------------------------------------------------

--
-- Table structure for table `tb_order_master`
--

CREATE TABLE `tb_order_master` (
  `order_id` int(11) NOT NULL,
  `order_date` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tb_product`
--

CREATE TABLE `tb_product` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_details` varchar(300) NOT NULL,
  `product_price` float NOT NULL,
  `product_image` varchar(500) NOT NULL,
  `category_id` int(11) NOT NULL,
  `is_active` int(11) NOT NULL,
  `is_deleted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_product`
--

INSERT INTO `tb_product` (`product_id`, `product_name`, `product_details`, `product_price`, `product_image`, `category_id`, `is_active`, `is_deleted`) VALUES
(2, 'asds', 'd', 23, '/product/asds.jpg', 1, 0, 0),
(3, 'aaa', 'aaa', 4323, '/product/aaa.jpg', 1, 0, 0),
(4, 'ft', 'tytry', 565, '/product/ft.jpg', 2, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tb_user`
--

CREATE TABLE `tb_user` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `gender` text NOT NULL,
  `email` varchar(60) NOT NULL,
  `mobile` bigint(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `address` varchar(500) NOT NULL,
  `photo` varchar(500) NOT NULL,
  `is_active` int(11) NOT NULL,
  `is_deleted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_user`
--

INSERT INTO `tb_user` (`user_id`, `user_name`, `gender`, `email`, `mobile`, `password`, `address`, `photo`, `is_active`, `is_deleted`) VALUES
(1, 'Nisha', 'Female', 'nisha@gmail.com', 8141673006, '123', 'Surat', 'ÿØÿà\0JFIF\0\0\0\0\0\0ÿÛ\0„\0	( \Z%!1!%)+...383-7(-.+\n\n\n\r-% %/-+--/----------+-----------5---------/-----------ÿÀ\0\0á\0á\"\0ÿÄ\0\0\0\0\0\0\0\0\0\0\0\0\0\0ÿÄ\0?\0\0\0\0\0!1AQaq‘¡\"±Áð2bÑB‚²Ò#3RSr’áñCƒÂÿÄ\0\Z\0\0\0\0\0\0\0\0\0\0\0\0\0ÿÄ\0*\0\0\0\0\0\0\0\0\0!12AQBa‘¡ð#qÿÚ\0\0\0?\0î \0\0\0\0\0\0\0\0_JŽ¤#Ãâ”VzÛ6Z–ÖÃ«Þ½%ewzÉ>/34iâ©ÉÚ3‹v½”“v|rà^2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0±[û’÷{»öøwï»~ÖÎÀ]1»Soaðÿ\0ÞÔJZî¯ŠyñÝYØÐûE·ñ°“§V^íåuKáÉñOñ4ú3S›', 1, 0),
(2, 'sds', 'male', 'dsad@dsdfdsfsd.fdsf', 1234567890, '123', 'qwe', '/user/sds.jpg', 0, 0),
(3, 'sdsadsad', 'male', 'abc@gmail.com', 9898132455, '123', 'fdsf', '/user/sdsadsad.jpg', 0, 0),
(4, 'sdsadsad', 'male', 'abc@gmail.com', 9898132455, '123', 'fdsf', '/user/sdsadsad.jpg', 0, 0),
(5, 'sdsadsad', 'male', 'abc@gmail.com', 9898132455, '123', 'fdsf', '/user/sdsadsad.jpg', 0, 0),
(6, 'sdsadsad', 'male', 'abc@gmail.com', 9898132455, '123', 'fdsf', '/user/sdsadsad.jpg', 0, 0),
(7, 'dsfdf', 'male', 'abcd@gmail.com', 1234567890, '123', 'sdsd', '/user/dsfdf.jpg', 0, 0),
(8, 'dsfdsfdf', 'male', 'sdsad@fdgdfgdf', 343434, '23232', '3434', '/user/dsfdsfdf.jpg', 0, 0),
(9, 'dsfdsfdf', 'male', 'sdsad@fdgdfgdf', 343434, '23232', '3434', '/user/dsfdsfdf.jpg', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tb_vendor`
--

CREATE TABLE `tb_vendor` (
  `vendor_id` int(11) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `gender` varchar(8) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_vendor`
--

INSERT INTO `tb_vendor` (`vendor_id`, `user_name`, `gender`, `email`, `mobile`, `address`) VALUES
(2, 'fdgf', 'fdgfd', '454', 43545, 'fdgfdg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_admin`
--
ALTER TABLE `tb_admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `tb_category`
--
ALTER TABLE `tb_category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `tb_contact`
--
ALTER TABLE `tb_contact`
  ADD PRIMARY KEY (`contact_id`);

--
-- Indexes for table `tb_feedback`
--
ALTER TABLE `tb_feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `tb_order_details`
--
ALTER TABLE `tb_order_details`
  ADD PRIMARY KEY (`order_details_id`);

--
-- Indexes for table `tb_order_master`
--
ALTER TABLE `tb_order_master`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tb_product`
--
ALTER TABLE `tb_product`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `tb_vendor`
--
ALTER TABLE `tb_vendor`
  ADD PRIMARY KEY (`vendor_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_admin`
--
ALTER TABLE `tb_admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tb_category`
--
ALTER TABLE `tb_category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_contact`
--
ALTER TABLE `tb_contact`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_feedback`
--
ALTER TABLE `tb_feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_order_details`
--
ALTER TABLE `tb_order_details`
  MODIFY `order_details_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_order_master`
--
ALTER TABLE `tb_order_master`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_product`
--
ALTER TABLE `tb_product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tb_vendor`
--
ALTER TABLE `tb_vendor`
  MODIFY `vendor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_order_master`
--
ALTER TABLE `tb_order_master`
  ADD CONSTRAINT `tb_order_master_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`user_id`);

--
-- Constraints for table `tb_product`
--
ALTER TABLE `tb_product`
  ADD CONSTRAINT `tb_product_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `tb_category` (`category_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
