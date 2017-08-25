/*
 Navicat Premium Data Transfer

 Source Server         : homestead
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : 127.0.0.1
 Source Database       : ipricejot

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : utf-8

 Date: 08/25/2017 01:07:08 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `py_salesrankings`
-- ----------------------------
DROP TABLE IF EXISTS `py_salesrankings`;
CREATE TABLE `py_salesrankings` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `sk_id` int(11) NOT NULL COMMENT 'salesranking_id',
  `rank` int(11) NOT NULL COMMENT '排名',
  `classify` varchar(150) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '分类',
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '爬取时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
