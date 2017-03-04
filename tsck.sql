PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE 	LE "user" (
"id"  INTEGER NOT NULL,
"user"  TEXT(20) NOT NULL,
"port"  INTEGER NOT NULL,
"password"  TEXT(50) NOT NULL,
PRIMARY KEY ("id")
);
INSERT INTO "user" VALUES(1,'root',22,'Qzmp123!@#');
INSERT INTO "user" VALUES(2,'zhuser',22,'zhuser@2015');
CREATE 	LE "_public_old_20160311" (
"id "  TEXT,
"ip"  TEXT,
"hostname"  TEXT,
"publicname"  TEXT,
"startcmd"  TEXT,
"publicpath"  TEXT,
"port"  TEXT,
"cpname"  TEXT
);
INSERT INTO "_public_old_20160311" VALUES('2','99.12.90.102','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/','7000','CP1');
INSERT INTO "_public_old_20160311" VALUES('3','99.12.90.102','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/','7010','CP1');
INSERT INTO "_public_old_20160311" VALUES('4','99.12.90.102','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/','','CP1');
INSERT INTO "_public_old_20160311" VALUES('8','99.12.90.102','test','webmanager','/opt/webapp/tomcat_webmanager/bin/startup.sh','/opt/webhome/','9716','CP1');
INSERT INTO "_public_old_20160311" VALUES('9','99.12.90.102','test','pub_cmbc_interface','/opt/webapp/tomcat_pub_cmbc_interface/bin/startup.sh','/opt/webhome/','9066','CP1');
INSERT INTO "_public_old_20160311" VALUES('10','99.12.90.5','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/','7000','CP2');
INSERT INTO "_public_old_20160311" VALUES('11','99.12.90.5','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/','7010','CP2');
INSERT INTO "_public_old_20160311" VALUES('12','99.12.90.5','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/','','CP2');
INSERT INTO "_public_old_20160311" VALUES('13','99.12.90.102','test','pub_oauth_interface','/opt/webapp/tomcat_pub_oauth_interface/bin/startup.sh','/opt/webhome/','9065','CP1');
INSERT INTO "_public_old_20160311" VALUES('14','99.12.90.102','test','pub_platform','/opt/webapp/tomcat_pub_platform/bin/startup.sh','/opt/webhome/','8110','CP1');
INSERT INTO "_public_old_20160311" VALUES('15','99.12.90.102','test','pub_system','/opt/webapp/tomcat_pub_system/bin/startup.sh','/opt/webhome/','8100','CP1');
INSERT INTO "_public_old_20160311" VALUES('17','99.12.90.6','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/','7000','CP3');
INSERT INTO "_public_old_20160311" VALUES('18','99.12.90.6','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/','7010','CP3');
INSERT INTO "_public_old_20160311" VALUES('19','99.12.90.6','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/','','CP3');
INSERT INTO "_public_old_20160311" VALUES('23','99.12.90.102','test','message_redis','/opt/webhome/message_redis/start.sh','/opt/webhome/','','CP1');
CREATE 	LE "module" ("id" TEXT,"ip" TEXT,"hostname" TEXT,"modulename" TEXT,"mid" TEXT,"port" TEXT,"path" TEXT,"CPname" TEXT);
INSERT INTO "module" VALUES('1','99.12.90.100','test','acp','','8086','/opt/innerapp/acp_1','CP1');
INSERT INTO "module" VALUES('2','99.12.90.100','test','cgc','','6011','/opt/innerapp/cgc_1','CP1');
INSERT INTO "module" VALUES('3','99.12.90.100','test','cmp','','6041;9086','/opt/innerapp/cmp_1','CP1');
INSERT INTO "module" VALUES('4','99.12.90.100','test','conc','','6051','/opt/innerapp/conc_1','CP1');
INSERT INTO "module" VALUES('5','99.12.90.100','test','configcenter','','30001','/opt/innerapp/configcenter_1','CP1');
INSERT INTO "module" VALUES('6','99.12.90.100','test','csc','','6081','/opt/innerapp/csc_1','CP1');
INSERT INTO "module" VALUES('7','99.12.90.100','test','dtc','','6091','/opt/innerapp/dtc_1','CP1');
INSERT INTO "module" VALUES('8','99.12.90.100','test','msc','','7041','/opt/innerapp/msc_1','CP1');
INSERT INTO "module" VALUES('9','99.12.90.100','test','msc4pp','','7071','/opt/innerapp/msc4pp_1','CP1');
INSERT INTO "module" VALUES('10','99.12.90.100','test','nav','','7090;18084','/opt/innerapp/nav_1','CP1');
INSERT INTO "module" VALUES('11','99.12.90.100','test','pbc','','8021','/opt/innerapp/pbc_1','CP1');
INSERT INTO "module" VALUES('12','99.12.90.100','test','rep','','8041','/opt/innerapp/rep_1','CP1');
INSERT INTO "module" VALUES('13','99.12.90.100','test','rep','','8042','/opt/innerapp/rep_2','CP2');
INSERT INTO "module" VALUES('14','99.12.90.100','test','trc','','8051','/opt/innerapp/trc_1','CP1');
INSERT INTO "module" VALUES('15','99.12.90.100','test','trc','','8052','/opt/innerapp/trc_2','CP2');
INSERT INTO "module" VALUES('16','99.12.90.100','test','uidc','','9011','/opt/innerapp/uidc_1','CP1');
INSERT INTO "module" VALUES('17','99.12.90.100','test','uidc','','9012','/opt/innerapp/uidc_2','CP2');
INSERT INTO "module" VALUES('18','99.12.90.100','test','vcs','','9021','/opt/innerapp/vcs_1','CP1');
INSERT INTO "module" VALUES('19','99.12.90.100','test','ucc','','8061','/opt/innerapp/ucc_1','CP1');
INSERT INTO "module" VALUES('20','99.12.90.5','test','cgc','','6012','/opt/innerapp/cgc_2','CP2');
INSERT INTO "module" VALUES('21','99.12.90.5','test','cgc','','6013','/opt/innerapp/cgc_3','CP3');
INSERT INTO "module" VALUES('22','99.12.90.5','test','cmp','','6042;9087','/opt/innerapp/cmp_2','CP2');
INSERT INTO "module" VALUES('23','99.12.90.5','test','cmp','','6043;9088','/opt/innerapp/cmp_3','CP3');
INSERT INTO "module" VALUES('24','99.12.90.5','test','dtc','','6092','/opt/innerapp/dtc_2','CP2');
INSERT INTO "module" VALUES('25','99.12.90.5','test','dtc','','6093','/opt/innerapp/dtc_3','CP3');
INSERT INTO "module" VALUES('26','99.12.90.5','test','mdbc','','7021','/opt/innerapp/mdbc_1','CP1');
INSERT INTO "module" VALUES('27','99.12.90.102','test','mpp','','7031','/opt/innerapp/mpp_1','CP1');
INSERT INTO "module" VALUES('28','99.12.90.5','test','msc','','7042','/opt/innerapp/msc_2','CP2');
INSERT INTO "module" VALUES('29','99.12.90.5','test','msc','','7043','/opt/innerapp/msc_3','CP3');
INSERT INTO "module" VALUES('30','99.12.90.5','test','msc4pp','','7072','/opt/innerapp/msc4pp_2','CP2');
INSERT INTO "module" VALUES('31','99.12.90.5','test','msc4pp','','7073','/opt/innerapp/msc4pp_3','CP3');
INSERT INTO "module" VALUES('32','99.12.90.5','test','ucc','','8062','/opt/innerapp/ucc_2','CP2');
INSERT INTO "module" VALUES('33','99.12.90.5','test','ucc','','8063','/opt/innerapp/ucc_3','CP3');
INSERT INTO "module" VALUES('34','99.12.90.6','test','cgc','','6014','/opt/innerapp/cgc_4','CP4');
INSERT INTO "module" VALUES('35','99.12.90.6','test','cmc','','6031','/opt/innerapp/cmc_1','CP1');
INSERT INTO "module" VALUES('36','99.12.90.6','test','cmp','','6044;9089','/opt/innerapp/cmp_4','CP4');
INSERT INTO "module" VALUES('37','99.12.90.6','test','counter','','6071','/opt/innerapp/counter_1','CP1');
INSERT INTO "module" VALUES('38','99.12.90.6','test','dtc','','6094','/opt/innerapp/dtc_4','CP4');
INSERT INTO "module" VALUES('39','99.12.90.6','test','log','','7011','/opt/innerapp/log_1','CP1');
INSERT INTO "module" VALUES('40','99.12.90.6','test','mdbc','','7022','/opt/innerapp/mdbc_2','CP2');
INSERT INTO "module" VALUES('41','99.12.90.6','test','msc','','7044','/opt/innerapp/msc_4','CP4');
INSERT INTO "module" VALUES('42','99.12.90.6','test','msc4pn','','7061','/opt/innerapp/msc4pn_1','CP1');
INSERT INTO "module" VALUES('43','99.12.90.6','test','msc4pp','','7074','/opt/innerapp/msc4pp_4','CP4');
INSERT INTO "module" VALUES('44','99.12.90.6','test','omc','','8011','/opt/innerapp/omc_1','CP1');
INSERT INTO "module" VALUES('45','99.12.90.6','test','poc','','8031','/opt/innerapp/poc_1','CP1');
INSERT INTO "module" VALUES('46','99.12.90.6','test','ucc','','8064','/opt/innerapp/ucc_4','CP4');
INSERT INTO "module" VALUES('47','99.12.90.6','test','ucc','','8065','/opt/innerapp/ucc_5','CP5');
INSERT INTO "module" VALUES('48','99.12.90.8','test','cgc','','6015','/opt/innerapp/cgc_5','CP5');
INSERT INTO "module" VALUES('49','99.12.90.8','test','cmc','','6032','/opt/innerapp/cmc_2','CP2');
INSERT INTO "module" VALUES('50','99.12.90.8','test','cmp','','6045;9090','/opt/innerapp/cmp_5','CP5');
INSERT INTO "module" VALUES('51','99.12.90.8','test','counter','','6072','/opt/innerapp/counter_2','CP2');
INSERT INTO "module" VALUES('52','99.12.90.8','test','dtc','','6095','/opt/innerapp/dtc_5','CP5');
INSERT INTO "module" VALUES('53','99.12.90.8','test','log','','7012','/opt/innerapp/log_2','CP2');
INSERT INTO "module" VALUES('54','99.12.90.102','test','mpp','','7032','/opt/innerapp/mpp_2','CP2');
INSERT INTO "module" VALUES('55','99.12.90.8','test','msc','','7045','/opt/innerapp/msc_5','CP5');
INSERT INTO "module" VALUES('56','99.12.90.8','test','msc4pn','','7062','/opt/innerapp/msc4pn_2','CP2');
INSERT INTO "module" VALUES('57','99.12.90.8','test','msc4pp','','7075','/opt/innerapp/msc4pp_5','CP5');
INSERT INTO "module" VALUES('58','99.12.90.8','test','omc','','8012','/opt/innerapp/omc_2','CP2');
INSERT INTO "module" VALUES('59','99.12.90.8','test','poc','','8032','/opt/innerapp/poc_2','CP2');
INSERT INTO "module" VALUES('60','99.12.90.8','test','ucc','','8066','/opt/innerapp/ucc_6','CP6');
INSERT INTO "module" VALUES('61','99.12.90.8','test','ucc','','8067','/opt/innerapp/ucc_7','CP7');
INSERT INTO "module" VALUES('62','99.12.90.8','test','ucc','','8068','/opt/innerapp/ucc_8','CP8');
INSERT INTO "module" VALUES('63','99.12.90.8','test','msc4pn','','7063','/opt/innerapp/msc4pn_3','CP3');
INSERT INTO "module" VALUES('63','99.12.90.8','test','msc4pn','','7064','/opt/innerapp/msc4pn_4','CP4');
INSERT INTO "module" VALUES('63','99.12.90.8','test','msc4pn','','7065','/opt/innerapp/msc4pn_5','CP5');
INSERT INTO "module" VALUES('65','99.12.90.8','test','acp','','18086','/opt/innerapp/acp_2','CP2');
INSERT INTO "module" VALUES('66','99.12.90.8','test','nav','','7090;18084','/opt/innerapp/nav_2','CP2');
INSERT INTO "module" VALUES('67','99.12.90.5','test','eyesight','','8932','/opt/innerapp/eyesight_1','CP1');
INSERT INTO "module" VALUES('68','99.12.90.6','test','eyesight','','8932','/opt/innerapp/eyesight_2','CP2');
INSERT INTO "module" VALUES('69','99.12.90.5','test','djob','','','/opt/innerapp/djob_1','CP1');
INSERT INTO "module" VALUES('70','99.12.90.5','test','djob','','','/opt/innerapp/djob_2','CP2');
CREATE 	LE "mysql" ("id" INTEGER,"ip" TEXT(50));
CREATE 	LE "hadoop" ("id" INTEGER,"ip" TEXT(50));
CREATE 	LE "fastdfs" ("id" INTEGER,"ip" TEXT(50));
CREATE 	LE "redis" ("id " INTEGER,"ip" TEXT(50));
CREATE 	LE "public" (
"id"  TEXT,
"ip"  TEXT,
"hostname"  TEXT,
"publicname"  TEXT,
"startcmd"  TEXT,
"publicpath"  TEXT,
"port"  TEXT,
"cpname"  TEXT
);
INSERT INTO "public" VALUES('2','99.12.90.102','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/pub_interface','7000','CP1');
INSERT INTO "public" VALUES('3','99.12.90.102','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/pub_message','7010','CP1');
INSERT INTO "public" VALUES('4','99.12.90.102','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/pub_message_server','','CP1');
INSERT INTO "public" VALUES('8','99.12.90.102','test','webmanager','/opt/webapp/tomcat_webmanager/bin/startup.sh','/opt/webhome/webmanager','9716','CP1');
INSERT INTO "public" VALUES('9','99.12.90.6','test','pub_cmbc_interface','/opt/webapp/tomcat_pub_cmbc_interface/bin/startup.sh','/opt/webhome/pub_cmbc_interface','9066','CP1');
INSERT INTO "public" VALUES('10','99.12.90.5','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/pub_interface','7000','CP2');
INSERT INTO "public" VALUES('11','99.12.90.5','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/pub_message','7010','CP2');
INSERT INTO "public" VALUES('12','99.12.90.5','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/pub_message_server','','CP2');
INSERT INTO "public" VALUES('13','99.12.90.5','test','pub_oauth_interface','/opt/webapp/tomcat_pub_oauth_interface/bin/startup.sh','/opt/webhome/pub_oauth_interface','9065','CP1');
INSERT INTO "public" VALUES('14','99.12.90.102','test','pub_platform','/opt/webapp/tomcat_pub_platform/bin/startup.sh','/opt/webhome/pub_platform','8110','CP1');
INSERT INTO "public" VALUES('15','99.12.90.102','test','pub_system','/opt/webapp/tomcat_pub_system/bin/startup.sh','/opt/webhome/pub_system','8100','CP1');
INSERT INTO "public" VALUES('17','99.12.90.6','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/pub_interface','7000','CP3');
INSERT INTO "public" VALUES('18','99.12.90.6','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/pub_message','7010','CP3');
INSERT INTO "public" VALUES('19','99.12.90.6','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/pub_message_server','','CP3');
INSERT INTO "public" VALUES('23','99.12.90.102','test','message_redis','/opt/webhome/message_redis/start.sh','/opt/webhome/message_redis','','CP1');
INSERT INTO "public" VALUES('24','99.12.90.6','test','pub_authorization','/opt/webapp/jboss_pub_authorization/bin/start.sh','/opt/webhome/pub_authorization_jboss','9110','CP1');
INSERT INTO "public" VALUES('25','99.12.90.102','test','pub_wcmp','/opt/webapp/tomcat_pub_wcmp/bin/startup.sh','/opt/webhome/pub_wcmp','7110','CP1');
INSERT INTO "public" VALUES('26','99.12.90.5','test','pub_crash_system','/opt/webapp/tomcat_pub_crash_system/bin/startup.sh','/opt/webhome/pub_crash_system','9123','CP1');
INSERT INTO "public" VALUES('27','99.12.90.5','test','pub_groupmsg','/opt/webapp/tomcat_pub_groupmsg/bin/startup.sh','/opt/webhome/pub_groupmsg_jboss','8085','CP1');
INSERT INTO "public" VALUES('28','99.12.90.102','test','pub_portrait','/opt/webapp/tomcat_pub_portrait/bin/startup.sh','/opt/webhome/pub_portrait','3110','CP1');
INSERT INTO "public" VALUES('29','99.12.90.6','test','pub_mzhaohu','/opt/webapp/tomcat_pub_mzhaohu/bin/startup.sh','/opt/webhome/pub_mzhaohu','8081','CP1');
INSERT INTO "public" VALUES('29','99.12.90.6','test','pub_mzhaohuManager','/opt/webapp/tomcat_pub_mzhaohuManager/bin/startup.sh','/opt/webhome/pub_mzhaohuManager','8082','CP1');
INSERT INTO "public" VALUES('31','99.12.90.5','test','pub_es_interface','/opt/webapp/tomcat_pub_es_interface/bin/startup.sh','/opt/webhome/pub_es_interface','18100','CP1');
COMMIT;

