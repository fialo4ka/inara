BEGIN TRANSACTION;
INSERT INTO `index_arttype` VALUES (1,'PAINTINGS');
INSERT INTO `index_arttype` VALUES (2,'WATERCOLORS');
INSERT INTO `index_arttype` VALUES (3,'GRAPHICS');
INSERT INTO `index_arttype` VALUES (4,'DESIGN');

INSERT INTO `index_artstatus` VALUES (1,'In private collection');
INSERT INTO `index_artstatus` VALUES (2,'For Sale');

INSERT INTO `index_columnnumber` VALUES (1,'1');
INSERT INTO `index_columnnumber` VALUES (2,'2');
INSERT INTO `index_columnnumber` VALUES (3,'3');

COMMIT;

BEGIN TRANSACTION;
INSERT INTO `index_arttype` VALUES (5,'PRINTS');
COMMIT;