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

 Date: 08/25/2017 01:07:14 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `salesranking_keywords`
-- ----------------------------
DROP TABLE IF EXISTS `salesranking_keywords`;
CREATE TABLE `salesranking_keywords` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `sk_id` int(11) NOT NULL COMMENT 'saleranking_id',
  `keyword` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '关键字',
  `rank` int(11) NOT NULL COMMENT '当前排名',
  `last_rank` int(11) NOT NULL COMMENT '上次排名',
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `salesranking_keywords_sk_id_keyword_unique` (`sk_id`,`keyword`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
