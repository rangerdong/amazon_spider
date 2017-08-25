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

 Date: 08/25/2017 01:07:19 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `salesrankings`
-- ----------------------------
DROP TABLE IF EXISTS `salesrankings`;
CREATE TABLE `salesrankings` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL COMMENT 'seller_uid',
  `asin` varchar(11) COLLATE utf8_unicode_ci NOT NULL COMMENT '商品asin号',
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(500) COLLATE utf8_unicode_ci NOT NULL COMMENT '商品名称',
  `link` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '亚马逊商品链接',
  `classify` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '商品分类',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '抓取状态 0抓取中 1成功 2抓取失败',
  `rank` int(11) NOT NULL DEFAULT '0' COMMENT '目前排名',
  `last_rank` int(11) NOT NULL DEFAULT '0' COMMENT '上次排名',
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
