/*
 Navicat Premium Data Transfer

 Source Server         : 学生管理系统
 Source Server Type    : MySQL
 Source Server Version : 80036
 Source Host           : localhost:3306
 Source Schema         : db_student

 Target Server Type    : MySQL
 Target Server Version : 80036
 File Encoding         : 65001

 Date: 02/04/2024 22:20:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tb_class
-- ----------------------------
DROP TABLE IF EXISTS `tb_class`;
CREATE TABLE `tb_class`  (
  `classID` int NOT NULL COMMENT '班级编号',
  `gradeID` int NULL DEFAULT NULL COMMENT '年级编号',
  `className` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '班级名称',
  PRIMARY KEY (`classID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_class
-- ----------------------------
INSERT INTO `tb_class` VALUES (1, 1, '一班');

-- ----------------------------
-- Table structure for tb_examkinds
-- ----------------------------
DROP TABLE IF EXISTS `tb_examkinds`;
CREATE TABLE `tb_examkinds`  (
  `kindID` int NOT NULL COMMENT '考试类别编号',
  `kindName` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`kindID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_examkinds
-- ----------------------------
INSERT INTO `tb_examkinds` VALUES (1, '期中考试');
INSERT INTO `tb_examkinds` VALUES (2, '期末考试');

-- ----------------------------
-- Table structure for tb_grade
-- ----------------------------
DROP TABLE IF EXISTS `tb_grade`;
CREATE TABLE `tb_grade`  (
  `gradeID` int NOT NULL AUTO_INCREMENT COMMENT '年级编号',
  `gradeName` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL COMMENT '年级名称',
  PRIMARY KEY (`gradeID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_grade
-- ----------------------------
INSERT INTO `tb_grade` VALUES (1, '初一');
INSERT INTO `tb_grade` VALUES (4, '初四');

-- ----------------------------
-- Table structure for tb_result
-- ----------------------------
DROP TABLE IF EXISTS `tb_result`;
CREATE TABLE `tb_result`  (
  `ID` int NOT NULL AUTO_INCREMENT COMMENT '自动编号',
  `stuID` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '学生编号',
  `kindID` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '考试类别编号',
  `subID` int NULL DEFAULT NULL COMMENT '考试科目编号',
  `result` double NULL DEFAULT NULL COMMENT '考试成绩',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_result
-- ----------------------------
INSERT INTO `tb_result` VALUES (1, 'BS0101002', '1', 1, 80);
INSERT INTO `tb_result` VALUES (2, 'BS0101002', '1', 2, 60);
INSERT INTO `tb_result` VALUES (12, 'BS0101003', '1', 1, 45);
INSERT INTO `tb_result` VALUES (13, 'BS0101003', '2', 2, 100);

-- ----------------------------
-- Table structure for tb_student
-- ----------------------------
DROP TABLE IF EXISTS `tb_student`;
CREATE TABLE `tb_student`  (
  `stuID` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL COMMENT '学生编号',
  `stuName` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `classID` int NULL DEFAULT NULL COMMENT '班级编号',
  `age` int NULL DEFAULT NULL COMMENT '年龄',
  `sex` char(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '性别',
  `phone` char(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '联系电话',
  `address` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '家庭地址',
  `gradeID` int NULL DEFAULT NULL COMMENT '年级编号',
  PRIMARY KEY (`stuID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_student
-- ----------------------------
INSERT INTO `tb_student` VALUES ('BS0101002', '小二', 1, 45, '男', '13565894578', '北京', 1);
INSERT INTO `tb_student` VALUES ('BS0101003', '小天', 1, 45, '男', '13456789', '北京', 1);
INSERT INTO `tb_student` VALUES ('BS0101004', '美丽', 1, 12, '女', '14565789856', '北京', 1);

-- ----------------------------
-- Table structure for tb_subject
-- ----------------------------
DROP TABLE IF EXISTS `tb_subject`;
CREATE TABLE `tb_subject`  (
  `subID` int NOT NULL COMMENT '科目编号',
  `subName` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '科目名称',
  PRIMARY KEY (`subID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_subject
-- ----------------------------
INSERT INTO `tb_subject` VALUES (1, '数学');
INSERT INTO `tb_subject` VALUES (2, '语文');
INSERT INTO `tb_subject` VALUES (3, '编程');

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user`  (
  `userName` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL COMMENT '用户姓名',
  `userPwd` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '用户密码',
  PRIMARY KEY (`userName`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES ('admin', 'admin');

-- ----------------------------
-- View structure for v_classinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_classinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_classinfo` AS select `tb_class`.`classID` AS `classID`,`tb_class`.`className` AS `className`,`tb_grade`.`gradeID` AS `gradeID`,`tb_grade`.`gradeName` AS `gradeName` from (`tb_class` join `tb_grade`) where (`tb_class`.`gradeID` = `tb_grade`.`gradeID`);

-- ----------------------------
-- View structure for v_resultinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_resultinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_resultinfo` AS select `tb_result`.`ID` AS `ID`,`tb_result`.`stuID` AS `stuID`,`v_studentinfo`.`stuName` AS `stuName`,`tb_examkinds`.`kindName` AS `kindName`,`tb_subject`.`subName` AS `subName`,`v_studentinfo`.`className` AS `className`,`v_studentinfo`.`gradeName` AS `gradeName`,`tb_result`.`result` AS `result` from (((`tb_result` join `v_studentinfo`) join `tb_examkinds`) join `tb_subject`) where ((`tb_result`.`stuID` = `v_studentinfo`.`stuID`) and (`tb_result`.`kindID` = `tb_examkinds`.`kindID`) and (`tb_result`.`subID` = `tb_subject`.`subID`));

-- ----------------------------
-- View structure for v_studentinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_studentinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_studentinfo` AS select `tb_student`.`stuID` AS `stuID`,`tb_student`.`stuName` AS `stuName`,`tb_student`.`age` AS `age`,`tb_student`.`sex` AS `sex`,`tb_student`.`phone` AS `phone`,`tb_student`.`address` AS `address`,`tb_class`.`className` AS `className`,`tb_grade`.`gradeName` AS `gradeName` from ((`tb_student` join `tb_class`) join `tb_grade`) where ((`tb_student`.`classID` = `tb_class`.`classID`) and (`tb_student`.`gradeID` = `tb_grade`.`gradeID`));

SET FOREIGN_KEY_CHECKS = 1;
