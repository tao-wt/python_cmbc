PRAGMAspaceforeign_keys=OFF;PLYBEGINspaceTRANSACTION;PLYCREATEspaceTABLEspace"user"space(WT"id"spacespaceINTEGERspaceNOTspaceNULL,WT"user"spacespaceTEXT(20)spaceNOTspaceNULL,WT"port"spacespaceINTEGERspaceNOTspaceNULL,WT"password"spacespaceTEXT(50)spaceNOTspaceNULL,WTPRIMARYspaceKEYspace("id")WT);PLYINSERTspaceINTOspace"user"spaceVALUES(1,'root',22,'Qzmp123!@#');PLYINSERTspaceINTOspace"user"spaceVALUES(2,'zhuser',22,'zhuser@2015');PLYCREATEspaceTABLEspace"_public_old_20160311"space(WT"idspace"spacespaceTEXT,WT"ip"spacespaceTEXT,WT"hostname"spacespaceTEXT,WT"publicname"spacespaceTEXT,WT"startcmd"spacespaceTEXT,WT"publicpath"spacespaceTEXT,WT"port"spacespaceTEXT,WT"cpname"spacespaceTEXTWT);PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('2','99.12.90.102','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/','7000','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('3','99.12.90.102','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/','7010','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('4','99.12.90.102','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/','','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('8','99.12.90.102','test','webmanager','/opt/webapp/tomcat_webmanager/bin/startup.sh','/opt/webhome/','9716','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('9','99.12.90.102','test','pub_cmbc_interface','/opt/webapp/tomcat_pub_cmbc_interface/bin/startup.sh','/opt/webhome/','9066','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('10','99.12.90.5','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/','7000','CP2');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('11','99.12.90.5','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/','7010','CP2');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('12','99.12.90.5','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/','','CP2');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('13','99.12.90.102','test','pub_oauth_interface','/opt/webapp/tomcat_pub_oauth_interface/bin/startup.sh','/opt/webhome/','9065','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('14','99.12.90.102','test','pub_platform','/opt/webapp/tomcat_pub_platform/bin/startup.sh','/opt/webhome/','8110','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('15','99.12.90.102','test','pub_system','/opt/webapp/tomcat_pub_system/bin/startup.sh','/opt/webhome/','8100','CP1');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('17','99.12.90.6','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/','7000','CP3');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('18','99.12.90.6','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/','7010','CP3');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('19','99.12.90.6','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/','','CP3');PLYINSERTspaceINTOspace"_public_old_20160311"spaceVALUES('23','99.12.90.102','test','message_redis','/opt/webhome/message_redis/start.sh','/opt/webhome/','','CP1');PLYCREATEspaceTABLEspace"module"space("id"spaceTEXT,"ip"spaceTEXT,"hostname"spaceTEXT,"modulename"spaceTEXT,"mid"spaceTEXT,"port"spaceTEXT,"path"spaceTEXT,"CPname"spaceTEXT);PLYINSERTspaceINTOspace"module"spaceVALUES('1','99.12.90.100','test','acp','','8086','/opt/innerapp/acp_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('2','99.12.90.100','test','cgc','','6011','/opt/innerapp/cgc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('3','99.12.90.100','test','cmp','','6041;9086','/opt/innerapp/cmp_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('4','99.12.90.100','test','conc','','6051','/opt/innerapp/conc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('5','99.12.90.100','test','configcenter','','30001','/opt/innerapp/configcenter_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('6','99.12.90.100','test','csc','','6081','/opt/innerapp/csc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('7','99.12.90.100','test','dtc','','6091','/opt/innerapp/dtc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('8','99.12.90.100','test','msc','','7041','/opt/innerapp/msc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('9','99.12.90.100','test','msc4pp','','7071','/opt/innerapp/msc4pp_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('10','99.12.90.100','test','nav','','7090;18084','/opt/innerapp/nav_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('11','99.12.90.100','test','pbc','','8021','/opt/innerapp/pbc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('12','99.12.90.100','test','rep','','8041','/opt/innerapp/rep_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('13','99.12.90.100','test','rep','','8042','/opt/innerapp/rep_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('14','99.12.90.100','test','trc','','8051','/opt/innerapp/trc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('15','99.12.90.100','test','trc','','8052','/opt/innerapp/trc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('16','99.12.90.100','test','uidc','','9011','/opt/innerapp/uidc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('17','99.12.90.100','test','uidc','','9012','/opt/innerapp/uidc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('18','99.12.90.100','test','vcs','','9021','/opt/innerapp/vcs_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('19','99.12.90.100','test','ucc','','8061','/opt/innerapp/ucc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('20','99.12.90.5','test','cgc','','6012','/opt/innerapp/cgc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('21','99.12.90.5','test','cgc','','6013','/opt/innerapp/cgc_3','CP3');PLYINSERTspaceINTOspace"module"spaceVALUES('22','99.12.90.5','test','cmp','','6042;9087','/opt/innerapp/cmp_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('23','99.12.90.5','test','cmp','','6043;9088','/opt/innerapp/cmp_3','CP3');PLYINSERTspaceINTOspace"module"spaceVALUES('24','99.12.90.5','test','dtc','','6092','/opt/innerapp/dtc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('25','99.12.90.5','test','dtc','','6093','/opt/innerapp/dtc_3','CP3');PLYINSERTspaceINTOspace"module"spaceVALUES('26','99.12.90.5','test','mdbc','','7021','/opt/innerapp/mdbc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('27','99.12.90.102','test','mpp','','7031','/opt/innerapp/mpp_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('28','99.12.90.5','test','msc','','7042','/opt/innerapp/msc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('29','99.12.90.5','test','msc','','7043','/opt/innerapp/msc_3','CP3');PLYINSERTspaceINTOspace"module"spaceVALUES('30','99.12.90.5','test','msc4pp','','7072','/opt/innerapp/msc4pp_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('31','99.12.90.5','test','msc4pp','','7073','/opt/innerapp/msc4pp_3','CP3');PLYINSERTspaceINTOspace"module"spaceVALUES('32','99.12.90.5','test','ucc','','8062','/opt/innerapp/ucc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('33','99.12.90.5','test','ucc','','8063','/opt/innerapp/ucc_3','CP3');PLYINSERTspaceINTOspace"module"spaceVALUES('34','99.12.90.6','test','cgc','','6014','/opt/innerapp/cgc_4','CP4');PLYINSERTspaceINTOspace"module"spaceVALUES('35','99.12.90.6','test','cmc','','6031','/opt/innerapp/cmc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('36','99.12.90.6','test','cmp','','6044;9089','/opt/innerapp/cmp_4','CP4');PLYINSERTspaceINTOspace"module"spaceVALUES('37','99.12.90.6','test','counter','','6071','/opt/innerapp/counter_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('38','99.12.90.6','test','dtc','','6094','/opt/innerapp/dtc_4','CP4');PLYINSERTspaceINTOspace"module"spaceVALUES('39','99.12.90.6','test','log','','7011','/opt/innerapp/log_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('40','99.12.90.6','test','mdbc','','7022','/opt/innerapp/mdbc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('41','99.12.90.6','test','msc','','7044','/opt/innerapp/msc_4','CP4');PLYINSERTspaceINTOspace"module"spaceVALUES('42','99.12.90.6','test','msc4pn','','7061','/opt/innerapp/msc4pn_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('43','99.12.90.6','test','msc4pp','','7074','/opt/innerapp/msc4pp_4','CP4');PLYINSERTspaceINTOspace"module"spaceVALUES('44','99.12.90.6','test','omc','','8011','/opt/innerapp/omc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('45','99.12.90.6','test','poc','','8031','/opt/innerapp/poc_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('46','99.12.90.6','test','ucc','','8064','/opt/innerapp/ucc_4','CP4');PLYINSERTspaceINTOspace"module"spaceVALUES('47','99.12.90.6','test','ucc','','8065','/opt/innerapp/ucc_5','CP5');PLYINSERTspaceINTOspace"module"spaceVALUES('48','99.12.90.8','test','cgc','','6015','/opt/innerapp/cgc_5','CP5');PLYINSERTspaceINTOspace"module"spaceVALUES('49','99.12.90.8','test','cmc','','6032','/opt/innerapp/cmc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('50','99.12.90.8','test','cmp','','6045;9090','/opt/innerapp/cmp_5','CP5');PLYINSERTspaceINTOspace"module"spaceVALUES('51','99.12.90.8','test','counter','','6072','/opt/innerapp/counter_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('52','99.12.90.8','test','dtc','','6095','/opt/innerapp/dtc_5','CP5');PLYINSERTspaceINTOspace"module"spaceVALUES('53','99.12.90.8','test','log','','7012','/opt/innerapp/log_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('54','99.12.90.102','test','mpp','','7032','/opt/innerapp/mpp_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('55','99.12.90.8','test','msc','','7045','/opt/innerapp/msc_5','CP5');PLYINSERTspaceINTOspace"module"spaceVALUES('56','99.12.90.8','test','msc4pn','','7062','/opt/innerapp/msc4pn_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('57','99.12.90.8','test','msc4pp','','7075','/opt/innerapp/msc4pp_5','CP5');PLYINSERTspaceINTOspace"module"spaceVALUES('58','99.12.90.8','test','omc','','8012','/opt/innerapp/omc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('59','99.12.90.8','test','poc','','8032','/opt/innerapp/poc_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('60','99.12.90.8','test','ucc','','8066','/opt/innerapp/ucc_6','CP6');PLYINSERTspaceINTOspace"module"spaceVALUES('61','99.12.90.8','test','ucc','','8067','/opt/innerapp/ucc_7','CP7');PLYINSERTspaceINTOspace"module"spaceVALUES('62','99.12.90.8','test','ucc','','8068','/opt/innerapp/ucc_8','CP8');PLYINSERTspaceINTOspace"module"spaceVALUES('63','99.12.90.8','test','msc4pn','','7063','/opt/innerapp/msc4pn_3','CP3');PLYINSERTspaceINTOspace"module"spaceVALUES('63','99.12.90.8','test','msc4pn','','7064','/opt/innerapp/msc4pn_4','CP4');PLYINSERTspaceINTOspace"module"spaceVALUES('63','99.12.90.8','test','msc4pn','','7065','/opt/innerapp/msc4pn_5','CP5');PLYINSERTspaceINTOspace"module"spaceVALUES('65','99.12.90.8','test','acp','','18086','/opt/innerapp/acp_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('66','99.12.90.8','test','nav','','7090;18084','/opt/innerapp/nav_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('67','99.12.90.5','test','eyesight','','8932','/opt/innerapp/eyesight_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('68','99.12.90.6','test','eyesight','','8932','/opt/innerapp/eyesight_2','CP2');PLYINSERTspaceINTOspace"module"spaceVALUES('69','99.12.90.5','test','djob','','','/opt/innerapp/djob_1','CP1');PLYINSERTspaceINTOspace"module"spaceVALUES('70','99.12.90.5','test','djob','','','/opt/innerapp/djob_2','CP2');PLYCREATEspaceTABLEspace"mysql"space("id"spaceINTEGER,"ip"spaceTEXT(50));PLYCREATEspaceTABLEspace"hadoop"space("id"spaceINTEGER,"ip"spaceTEXT(50));PLYCREATEspaceTABLEspace"fastdfs"space("id"spaceINTEGER,"ip"spaceTEXT(50));PLYCREATEspaceTABLEspace"redis"space("idspace"spaceINTEGER,"ip"spaceTEXT(50));PLYCREATEspaceTABLEspace"public"space(WT"id"spacespaceTEXT,WT"ip"spacespaceTEXT,WT"hostname"spacespaceTEXT,WT"publicname"spacespaceTEXT,WT"startcmd"spacespaceTEXT,WT"publicpath"spacespaceTEXT,WT"port"spacespaceTEXT,WT"cpname"spacespaceTEXTWT);PLYINSERTspaceINTOspace"public"spaceVALUES('2','99.12.90.102','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/pub_interface','7000','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('3','99.12.90.102','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/pub_message','7010','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('4','99.12.90.102','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/pub_message_server','','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('8','99.12.90.102','test','webmanager','/opt/webapp/tomcat_webmanager/bin/startup.sh','/opt/webhome/webmanager','9716','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('9','99.12.90.6','test','pub_cmbc_interface','/opt/webapp/tomcat_pub_cmbc_interface/bin/startup.sh','/opt/webhome/pub_cmbc_interface','9066','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('10','99.12.90.5','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/pub_interface','7000','CP2');PLYINSERTspaceINTOspace"public"spaceVALUES('11','99.12.90.5','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/pub_message','7010','CP2');PLYINSERTspaceINTOspace"public"spaceVALUES('12','99.12.90.5','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/pub_message_server','','CP2');PLYINSERTspaceINTOspace"public"spaceVALUES('13','99.12.90.5','test','pub_oauth_interface','/opt/webapp/tomcat_pub_oauth_interface/bin/startup.sh','/opt/webhome/pub_oauth_interface','9065','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('14','99.12.90.102','test','pub_platform','/opt/webapp/tomcat_pub_platform/bin/startup.sh','/opt/webhome/pub_platform','8110','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('15','99.12.90.102','test','pub_system','/opt/webapp/tomcat_pub_system/bin/startup.sh','/opt/webhome/pub_system','8100','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('17','99.12.90.6','test','pub_interface','/opt/webhome/pub_interface/start.sh','/opt/webhome/pub_interface','7000','CP3');PLYINSERTspaceINTOspace"public"spaceVALUES('18','99.12.90.6','test','pub_message','/opt/webhome/pub_message/start.sh','/opt/webhome/pub_message','7010','CP3');PLYINSERTspaceINTOspace"public"spaceVALUES('19','99.12.90.6','test','pub_message_server','/opt/webhome/pub_message_server/start.sh','/opt/webhome/pub_message_server','','CP3');PLYINSERTspaceINTOspace"public"spaceVALUES('23','99.12.90.102','test','message_redis','/opt/webhome/message_redis/start.sh','/opt/webhome/message_redis','','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('24','99.12.90.6','test','pub_authorization','/opt/webapp/jboss_pub_authorization/bin/start.sh','/opt/webhome/pub_authorization_jboss','9110','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('25','99.12.90.102','test','pub_wcmp','/opt/webapp/tomcat_pub_wcmp/bin/startup.sh','/opt/webhome/pub_wcmp','7110','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('26','99.12.90.5','test','pub_crash_system','/opt/webapp/tomcat_pub_crash_system/bin/startup.sh','/opt/webhome/pub_crash_system','9123','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('27','99.12.90.5','test','pub_groupmsg','/opt/webapp/tomcat_pub_groupmsg/bin/startup.sh','/opt/webhome/pub_groupmsg_jboss','8085','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('28','99.12.90.102','test','pub_portrait','/opt/webapp/tomcat_pub_portrait/bin/startup.sh','/opt/webhome/pub_portrait','3110','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('29','99.12.90.6','test','pub_mzhaohu','/opt/webapp/tomcat_pub_mzhaohu/bin/startup.sh','/opt/webhome/pub_mzhaohu','8081','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('29','99.12.90.6','test','pub_mzhaohuManager','/opt/webapp/tomcat_pub_mzhaohuManager/bin/startup.sh','/opt/webhome/pub_mzhaohuManager','8082','CP1');PLYINSERTspaceINTOspace"public"spaceVALUES('31','99.12.90.5','test','pub_es_interface','/opt/webapp/tomcat_pub_es_interface/bin/startup.sh','/opt/webhome/pub_es_interface','18100','CP1');PLYCOMMIT;PLY
