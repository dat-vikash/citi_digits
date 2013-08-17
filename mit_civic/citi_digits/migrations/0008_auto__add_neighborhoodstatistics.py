# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NeighborhoodStatistics'
        db.create_table(u'citi_digits_neighborhoodstatistics', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('percent_income', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('net_win', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('daily_win', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('map_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total_households', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total_18_and_up', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total_retailers', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('adults_per_store', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('net_loss_per_store', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'citi_digits', ['NeighborhoodStatistics'])

    def populate(self,orm):
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (0,'Flatlands','1.837712','-52207.54','61694.3399999999','9486.8','171.71','235','19605','41381','42')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (1,'Gerritsen Beach','0.875213','-4746.84','5238.47','491.63','183.65','239','3268','7001','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (2,'Bergen Beach','0.292137','-1229.21','1229.21','0','240.14','205','1757','3866','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (3,'Canarsie','1.258051','-47393.8399999999','50778.0599999999','3384.22','178.59','215','22663','51195','36')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (4,'Mill Basin','0.70597','-3617.76','3690.37','72.61','214.04','248','2449','5110','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (5,'MIDWOOD','0.857069','-26773.08','28127.8899999999','1354.81','149.21','246','22056','47486','24')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (6,'Sheepshead Bay','2.231778','-128201.89','134874.429999999','6672.53','130.98','260','46268','98573','107')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (7,'Farragut','1.441125','-18772.2599999999','21598.9399999999','2826.68','145.37','232','10338','21193','16')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (8,'Brighton Beach','2.930529','-25812.1699999999','26300.84','488.67','79.71','209','11290','24077','20')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (9,'Flatbush','2.329194','-81219.71','86835.7899999999','5616.08','128.93','234','28995','61211','72')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (10,'Manhattan Beach','0.313108','-1126.09','1218.88','92.79','190.32','244','2051','4783','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (11,'Brownsville','4.903312','-65500.8099999999','71313.5099999999','5812.71','71.04','212','20528','41671','63')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (12,'Starrett City','3.489198','-12347.1399999999','13648.73','1301.6','75.14','265','5220','8723','2')");
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (13,'Bedford Stuyvesant','2.766751','-142336.25','153210.09','10873.84','98.4','203','56433','115224','144')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (14,'East New York','3.25628','82679.3399999999','71501.4299999999','154180.769999999','88.73','231','24814','54203','63')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (15,'Highland Park','2.99269','-24773.83','26777','2003.17','108.87','242','8241','20466','31')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (16,'City Line','3.115347','-19561.07','20994.59','1433.53','89.52','217','7549','17071','25')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (17,'Cypress Hill','1.904482','-9010.45','9866.3','855.84','114.1','224','4553','11491','14')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (18,'Ocean Hill','3.921067','-33501.8','36837.66','3335.86','86.79','251','10854','21825','36')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (19,'Bushwick','3.200205','-94462.7299999999','102213.5','7750.77','95.48','214','35146','82064','111')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (20,'Wingate','1.993934','-33820.3399999999','37318.73','3498.38','102.81','223','18255','36700','39')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (21,'New Lots','2.939582','-58261.6999999999','65085.75','6824.05','121.02','250','18345','38795','42')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (22,'Spring Creek','0.385803','-318.35','334.09','15.74','72.66','264','1195','2096','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (23,'Prospect Lefferts Gardens','3.112478','-30108.09','32821.55','2713.45','112.12','254','9431','18203','16')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (24,'Crown Heights','2.847965','-76805.2299999999','90365.8','13560.57','99.24','222','32062','61742','78')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (25,'Greenpoint','2.036212','-71299.77','80469.5299999999','9169.75','154.65','241','25624','53041','90')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (26,'East Flatbush','2.611346','-120356.509999999','139780.149999999','19423.6399999999','122.01','230','43991','94776','109')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (27,'West Brighton','1.77138','-14628.08','15657.08','1029','115.35','268','7684','15361','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (28,'Coney Island','4.268452','-26193.61','27793.86','1600.25','70.17','221','9305','18934','19')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (29,'Dyker Heights','2.202501','-46062.7099999999','48126.72','2064','145.19','229','15091','34810','44')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (30,'Borough Park','4.023124','-137606.549999999','145534.34','7927.78','97.13','208','37346','87750','102')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (31,'Prospect Park','3.825719','-34045.69','37217.3','3171.6','106.91','255','9124','18848','21')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (32,'South Slope','0.577776','-11451.78','12223.94','772.16','236.99','263','8952','16754','26')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (33,'Gowanus','0.757305','-4413.87','4778.61','364.74','242.24','240','2612','4686','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (34,'Kensington','1.902','-36669.0599999999','38824.32','2155.26','118.77','243','17233','37205','35')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (35,'Prospect Park South','2.929388','805.38','8288.57','9093.95','203.09','0','0','0','7')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (36,'Bensonhurst','2.814304','-234833.359999999','272381.39','37548.0199999999','113.8','204','85280','195822','248')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (37,'Bayridge','1.721303','95838.4199999999','86401.07','182239.489999999','151.84','202','33148','61576','86')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (38,'Windsor Terrace','0.895542','-11240.42','11388.7','148.28','211.27','272','6036','10726','9')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (39,'Fort Hamilton','0.000014','-0.02','0.02','0','162.7','237','1121','2477','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (40,'Sunset Park','3.162456','-86067.6999999999','94859.55','8791.85','111.31','266','27021','64630','101')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (41,'Bush Terminal','0','0','0','0','109.72','213','543','2981','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (42,'Sea Gate','0','0','0','0','170.2','259','1480','3399','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (43,'Bath Beach','0.620874','-3589.91','3986.65','396.75','136.67','201','4711','11254','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (44,'Fort Greene','1.412594','-12200.23','13026.7','826.47','147.41','236','6273','13122','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (45,'Prospect Heights','0.974255','-17300.5999999999','18056.5499999999','755.95','226.28','253','8213','14126','17')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (46,'Brooklyn Academy Of Music','4.401764','-6274.74','6904.58','629.84','161.49','210','974','1769','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (47,'Park Slope','0.584411','-23750.2','28525.1699999999','4774.97','270.93','252','18065','32353','22')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (48,'Clinton Hill','1.529682','-32775.2099999999','35218.8499999999','2443.64','161.15','218','14326','26657','30')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (49,'Navy Hill','3.182233','-4561.56','4801.04','239.48','137.66','249','1099','2395','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (50,'Williamsburg','2.681941','-83638.35','90000.1499999999','6361.8','89.27','271','37695','79710','105')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (51,'Vinegar Hill','1.12754','-2570.5','2690.99','120.48','417.65','267','573','1389','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (52,'Dumbo','0.286463','-390.39','395.65','5.27','448.21','228','309','765','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (53,'Carroll Gardens','0.643188','-7574.4','8505.65','931.24','247.63','216','5355','9111','11')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (54,'Brooklyn Heights','0.599388','-17663.74','18562.0099999999','898.27','302.31','211','10272','17757','16')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (55,'Red Hook','3.305204','-11484.75','12065.92','581.17','83.08','257','4406','7552','10')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (56,'South Brooklyn','1.925284','-9288.01','9769.66','481.65','185.91','261','2737','4607','10')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (57,'Columbia St','0.735708','-3160.22','3412.66','252.44','252.38','220','1843','3510','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (58,'Fulton Ferry','0.489059','-1018.26','1071.68','53.42','332.43','238','661','1379','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (59,'Downtown Brooklyn','9.005695','-59637.3899999999','64277.7099999999','4640.31','165.56','227','4323','9065','33')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (60,'Cobble Hill','0.684957','-6144.52','6346.74','202.22','270.02','219','3441','6075','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (61,'Boerum Hill','1.463261','-24307.58','25826.74','1519.15','187.84','207','9422','17967','29')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (62,'Floyd Bennett Field','0','-4533.36','4590.3','56.94','0','0','0','0','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (63,'Marine Park','1.517045','-33092.94','35854.5999999999','2761.66','209.69','245','11302','24186','36')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (64,'Unionport','1.102039','-6208.09','7200.96','992.87','121.4','162','5397','12333','13')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (65,'Westchester Square','10.644912','-32133.9199999999','34162.57','2028.66','106.79','169','4859','11939','27')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (66,'Van Nest','1.679049','-9306.55','9868.36','561.81','112.66','164','5231','11267','15')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (67,'Eastchester Bay','0.493639','-1258.42','1382.27','123.85','198.86','120','1412','3065','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (68,'Locust Point','0.098494','-208.13','208.13','0','199.71','134','1061','2639','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (69,'Spencer Estates','0.37593','-945.72','1024.94','79.22','183.48','160','1490','3362','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (70,'Silver Beach','0.675076','-890.75','895.54','4.78','204.96','156','649','1665','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (71,'Edgewater Park','0.000285','16.12','0.32','16.44','160.14','122','692','1337','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (72,'Schuylerville','1.196219','-7292.86','7880.62','587.75','154.93','155','4264','8741','11')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (73,'Castle Hill','2.617117','-11148.36','12076.65','928.28','102.46','108','4516','9606','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (74,'Norwood','3.761931','-43156.9499999999','46756.8799999999','3599.93','90.21','146','13815','28660','36')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (75,'Morris Park','2.238678','-11321.74','11817.8899999999','496.16','165.01','139','3208','6788','11')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (76,'Clason Point','1.364063','-3616.96','4263.89','646.93','195.9','111','1600','4142','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (77,'Parkchester','2.971506','-46441.54','49696.9','3255.36','127.3','149','13174','24432','21')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (78,'Park Stratton','1.703106','-3835.56','4303.6','468.04','82.86','148','3058','6431','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (79,'Harding Park','0.000025','-0.05','0.05','0','164.53','126','1199','2898','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (80,'Throgs Neck','2.463497','-30502.25','32182.48','1680.22','160.18','161','8178','17147','17')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (81,'Pelham Gardens','0.887908','-8447.51','9195.89','748.38','198.34','151','5236','12436','7')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (82,'Historic Village of Baychester','0','0','0','0','141.6','128','1052','1769','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (83,'Wakefield','2.281924','-30663.59','34426.8','3763.21','141.46','165','10694','23097','24')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (84,'Baychester','2.562245','-15809.3799999999','18106.52','2297.15','174.58','102','4059','9009','16')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (85,'Coop City','2.655761','-40149.08','45989.0599999999','5839.98','134.45','113','12915','24089','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (86,'North Baychester','2.836966','-15308.28','20460.27','5151.99','164.66','144','4392','10000','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (87,'Eastchester','1.560896','-7409.74','7651.06','241.32','120.26','119','4087','9372','7')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (88,'Edenwald','1.322408','-3011.47','3253.91','242.43','81.4','121','3031','6017','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (89,'Fishbay','3.283154','-8681.86','9552.01','870.15','118.21','124','2468','5502','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (90,'City Island','1.107463','-3643.64','3790.79','147.15','177.75','109','1931','3624','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (91,'Laconia','1.438243','-8046.02','8366.65','320.63','145.43','133','4011','8940','9')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (92,'Country Club','1.552141','-3611.71','3852.44','240.73','184.63','114','1348','3023','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (93,'Pelham Bay','4.250433','-32153.75','36789.41','4635.66','135.21','150','6419','12212','27')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (94,'Ollinville','1.637521','-11180.52','11829.75','649.24','115.92','147','6249','12716','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (95,'Williamsbridge','2.153831','-40906.51','44254.4599999999','3347.95','120.56','170','17090','37545','38')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (96,'Woodlawn','1.121524','-5224.74','6221.75','997.01','167.55','171','3320','6141','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (97,'Bronxdale','2.942703','-32941.5599999999','35598.4','2656.84','99.12','107','12238','24308','24')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (98,'Pelham Parkway','2.051382','-24171.52','29037.0499999999','4865.53','131.56','152','10789','22347','23')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (99,'Morrisania','3.222469','-8652.18','9428.45','776.27','60.39','140','4858','10518','13')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (100,'Hunt\'s Point','7.530542','-26024.09','28200.66','2176.57','59.22','129','6341','14195','23')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (101,'East Concourse','4.267354','-39596.8899999999','42535.3399999999','2938.45','66.65','117','14996','31958','33')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (102,'Mount Eden','4.220064','-14720.51','15830.95','1110.44','85.98','142','4375','9813','11')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (103,'Longwood','6.174068','-37963.75','40372.9499999999','2409.2','64.62','135','10147','23034','35')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (104,'East Tremont','3.747587','-18572.9399999999','20931.2799999999','2358.34','66.32','118','8445','17881','22')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (105,'Crotona Park East','5.030003','-23634.1199999999','26321.47','2687.35','63','116','8329','18443','30')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (106,'Woodstock','2.68268','-5094.93','5407.22','312.29','56.74','172','3562','7854','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (107,'Soundview','2.810551','-11047.8799999999','26730.58','15682.7','91.9','157','10378','20528','20')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (108,'Claremont','4.090762','-10002.8899999999','12432.86','2429.97','49.67','110','6136','12997','17')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (109,'Melrose','8.489362','-30446.25','33585.3799999999','3139.14','53.41','137','7428','17263','37')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (110,'West Farms','1.753981','-922.7','1369.25','446.55','59.76','167','1310','2874','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (111,'Bronx Park South','6.73735','-14727.77','15731.35','1003.57','51.47','105','4549','9441','14')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (112,'Port Morris','6.465511','-1807.93','2817.2','1009.28','68.38','153','639','1379','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (113,'West Concourse','5.442783','-49879.4','54805.7699999999','4926.37','77.43','166','13041','28215','34')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (114,'Highbridge','2.631558','-20306.73','22486.1699999999','2179.44','73.43','127','11668','24455','21')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (115,'Mott Haven','5.558707','-66559.0399999999','70984.25','4425.21','57.52','141','22260','47623','62')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (116,'Concourse Village','3.013752','-8866.07','9638.47','772.4','93.23','112','3440','6401','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (117,'Marble Hill','5.2128','-3911.09','4217.83','306.74','200.83','136','404','748','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (118,'North Riverdale','0.843715','-9767','10143.2999999999','376.3','196.56','145','6133','12385','9')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (119,'Riverdale','0.850341','-12024.41','12024.41','0','219.67','154','6455','12677','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (120,'South Riverdale','0.241336','-2165.08','2165.08','0','230.6','159','3901','7195','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (121,'Bedford Park','2.991816','-38722.8799999999','42014.69','3291.81','83.32','103','16900','36105','33')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (122,'Jerome Park','1.306747','-20086.8699999999','21371.65','1284.78','108.5','130','15115','31344','19')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (123,'Fieldston','0','0','0','0','202.69','123','1559','3968','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (124,'Fordham','4.713427','-46842.6399999999','51267.61','4424.98','65.75','125','16589','37325','49')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (125,'Belmont','6.311673','-23675.6699999999','33892.1999999999','10216.53','59.41','104','9063','20823','29')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (126,'Soundview Bruckner','2.410455','-22450.73','23537.27','1086.54','86.99','158','11256','24967','33')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (127,'Bronx River','4.356937','-30091.34','32877.68','2786.35','88.55','106','8545','18998','24')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (128,'Bathgate','4.516399','-13144.61','15926.7999999999','2782.19','66.46','101','5321','11722','24')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (129,'Crotona Park','0','0','0','0','63.13','115','350','770','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (130,'Kingsbridge','4.692589','-32183.32','32183.32','0','124.02','131','5545','11174','24')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (131,'Mount Hope','3.906524','-26724.29','28014.61','1290.32','74.7','143','9626','21473','26')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (132,'University Heights','2.381571','-12240.41','15968.09','3727.68','73.06','163','9202','20144','14')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (133,'Kingsbridge Heights','1.461347','-8649.79','9069.78','419.98','88.72','132','7015','14193','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (134,'Morris Heights','3.058258','-24083.38','26174.4','2091.02','69.08','138','12423','26674','14')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (135,'Van Cortlandt Park','0','-5918.54','6226.43','307.89','0','0','0','0','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (136,'Pelham Bay Park','0','-598.56','598.56','0','0','0','0','0','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (137,'East Fifties','1.273684','-46446.9199999999','46991.54','544.61','299.49','308','12353','20243','25')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (138,'East Forties','2.247997','-39648.68','40812.76','1164.09','297.37','309','6122','9643','21')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (139,'Turtle Bay','0.869478','-12512.32','12540.67','28.35','322.18','338','4489','7262','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (140,'Upper East Side','0.287035','-28450.4399999999','28866.7599999999','416.32','429.11','341','23501','40218','12')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (141,'Tudor City','0.084251','-478.47','478.47','0','286.46','337','1988','3176','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (142,'Central Park','0','0','0','0','327.15','327','2054','3849','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (143,'Murray Hill','0.659683','-15823.9699999999','17154.83','1330.86','272.79','326','9559','15654','19')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (144,'Peter Cooper','1.050043','-7016.77','7445.64','428.87','275.27','328','2583','4438','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (145,'Stuyvesant Town','0.796354','-17353.74','17375.81','22.07','244.21','334','8959','16556','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (146,'Kips Bay','0.607426','-8174.74','8260.77','86.03','265.62','318','5134','8631','10')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (147,'Bellevue Area','0.976571','-11139.2099999999','11430.36','291.16','213.05','302','5509','10135','9')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (148,'Sutton Place','0','0','0','0','347.5','335','774','1214','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (149,'Hamilton Grange','0.929663','-1223.14','1422.06','198.92','109.95','314','1395','2509','7')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (150,'East Harlem','2.803433','-122206.55','129820.31','7613.76','105.99','310','43811','87375','123')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (151,'Hamilton Heights','2.71517','-35781.11','38455.6699999999','2674.56','96.79','315','14673','32172','38')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (152,'Inwood','1.816146','-51258.37','56508.7399999999','5250.37','112.1','317','27832','56347','40')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (153,'Washington Heights','2.914855','-126468.2','140551.679999999','14083.49','99.13','344','48775','109740','108')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (154,'St. Nicholas Terrace','0.560101','-1189.32','1244.12','54.79','98.55','332','2260','4360','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (155,'Harlem','2.717695','-118259.07','127246.56','8987.48','96.27','316','48771','88222','89')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (156,'Lenox Hill','0.423548','-39884.12','41024.5299999999','1140.41','257.76','319','37680','58705','32')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (157,'Manhattan Valley','1.013529','-10622.0599999999','17425.43','6803.37','140.88','322','12237','21811','10')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (158,'Manhattanville','4.187551','-29404.97','35464.58','6059.61','78.81','323','10776','23662','28')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (159,'Morningside Heights','0.47634','-9051.75','9300.54','248.8','163.87','325','11948','32395','11')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (160,'Soho','0.921664','-16856.97','17662.65','805.68','255.34','330','7526','13009','19')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (161,'World Trade Center','0','354.96','0','354.96','453.37','346','1146','2489','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (162,'Two Bridges','4.683048','-63916.82','66477.5399999999','2560.72','81.58','339','17449','36205','40')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (163,'Little Italy','5.242074','-37932.4599999999','39030.66','1098.19','148.23','320','5037','9411','26')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (164,'South Street Seaport','1.536127','-1775.75','1800.9','25.15','109.05','331','1078','2221','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (165,'Tribeca','2.061999','-44504.76','46114.41','1609.65','357.38','336','6275','12887','29')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (166,'East Village','1.157343','-61427.6699999999','68996.6799999999','7569.01','170.62','312','35038','67677','79')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (167,'East Twenties','0.963793','-24464.3499999999','25545.91','1081.55','236.19','311','11253','19613','21')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (168,'City Hall','4.71722','-30709.77','32073.68','1363.91','205.79','306','3313','8319','25')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (169,'Battery Park','0.392192','-9549.14','10824.3799999999','1275.24','404.91','301','6835','12195','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (170,'Wall Street','4.426655','-92922.1999999999','95778.38','2856.17','300.04','343','7231','18392','58')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (171,'Chinatown','15.286616','-19601.8499999999','24035.73','4433.88','76.84','305','2052','4865','16')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (172,'Stuyvesant Park','0.088','-593.55','627.8','34.25','242.74','333','2947','5327','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (173,'Union Square Area','0.40341','-9969.89','10449.7199999999','479.83','327.8','340','7924','13844','13')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (174,'Gramercy Park','0','0','0','0','291.35','313','824','1433','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (175,'Yorkville','0.611411','-72208.02','75457.1699999999','3249.15','260.1','347','47579','75036','55')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (176,'Upper West Side','0.418035','-97793.0399999999','104123.62','6330.58','273.09','342','91458','149842','67')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (177,'Midtown','5.155656','-309156.89','319831.69','10674.7999999999','269.1','324','23116','40391','202')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (178,'Bowery','3.942841','-6272.94','6540.93','267.99','117.4','303','1417','3108','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (179,'Lower East Side','2.558884','-53790.8799999999','56588.36','2797.48','119.55','321','18549','37705','44')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (180,'Clinton','1.249602','-62463.1999999999','65815.85','3352.65','186.5','307','28319','49730','53')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (181,'Chelsea','0.926736','-45758.93','48509.7399999999','2750.81','225.73','304','23253','38705','40')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (182,'West Village','0.623625','-51383.4199999999','55727.94','4344.52','269.32','345','33272','54108','47')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (183,'Roosevelt Island','0.492955','-3241.08','3446.62','205.54','181.26','329','3868','9834','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (184,'Laurelton','0.696886','21119.2799999999','18999.2799999999','40118.5599999999','228.45','436','11967','28426','18')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (185,'Auburndale','1.181715','-28422.16','29226.7','804.54','192.88','402','12858','29364','23')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (186,'Springfield Gardens South','2.005698','-7768.51','8170.29','401.78','202.21','458','2020','5792','9')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (187,'Rosedale','1.131526','-9132.53','10512.9','1380.36','223.79','454','4163','10245','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (188,'Kew Gardens Hills','1.489128','-26345.75','28151.52','1805.77','136.33','435','13905','29095','18')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (189,'Jamaica Hills','3.936977','-22033.98','23167.2099999999','1133.23','128.92','433','4577','11943','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (190,'Pomonok','1.299439','-9667.52','10085.16','417.64','154.23','447','5046','11787','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (191,'Briarwood','1.753178','-28216.0099999999','30826.72','2610.71','156.16','407','11291','24250','12')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (192,'South Jamaica','2.8158','-48577.2699999999','51780.91','3203.65','163.27','455','11294','27578','24')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (193,'Jamaica','3.125106','-76006.3899999999','81849.75','5843.36','116.04','431','22633','57328','89')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (194,'Arverne-Edgemere','0.668675','-4220.65','4756.33','535.68','101.87','401','7002','15968','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (195,'Seaside','1.97033','-8602.29','9382.55','780.26','129.26','425','3694','7327','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (196,'Far Rockaway','3.07282','-32411.5099999999','34054.4','1642.89','90.55','419','12272','27166','23')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (197,'Brookville','0.578391','-5019.26','5284.84','265.58','211.06','409','4341','10686','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (198,'St. Albans','1.272703','-34269.9499999999','38502.08','4232.13','174.72','459','17362','42596','48')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (199,'Edgemere','0.758145','-3285.81','4970.46','1684.65','134.27','404','4896','11185','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (200,'Bellerose And Floral Park','0.579166','-11328.5499999999','11917.58','589.02','209.95','405','9828','23807','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (201,'Oakland Gardens','0.694594','-12329.99','13491.23','1161.24','203.28','444','9581','18566','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (202,'Jamaica Estates','1.460941','-10683.65','11468.1399999999','784.49','180.83','432','4353','9185','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (203,'Queens Village','1.359745','-29563.07','31386.65','1823.57','188.99','448','12247','29892','30')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (204,'Douglaston & Little Neck','0.488222','-8639.26','9887.31','1248.05','217.12','415','9353','20073','12')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (205,'Glen Oaks','1.130033','-8691.82','9812.23','1120.42','189.08','423','4605','8325','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (206,'Fresh Meadows','0.830913','-4597.27','5181.48','584.22','173.12','422','3612','7224','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (207,'Bayside','0.890098','-11708.7','24741.6399999999','13032.93','199.92','403','13942','30162','22')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (208,'Murry Hill','1.836595','-41585.7099999999','43240.33','1654.62','144.16','441','16376','39751','25')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (209,'East Flushing','1.695551','-31578.82','33718.0199999999','2139.19','140.68','417','14175','35242','25')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (210,'Hillcrest','1.811121','-22033.81','37906.2699999999','15872.4599999999','192.09','426','10926','27949','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (211,'Bowne Park','0.55481','-5693.34','6046.89','353.55','201.6','410','5421','12610','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (212,'Utopia','0.848268','-3826.1','4062.41','236.31','204','462','2354','5435','7')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (213,'Hollis','0.942508','-7867.29','9427.67','1560.39','172.82','427','5804','15651','9')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (214,'Whitestone','1.003831','-11371.09','11843.42','472.32','228.08','463','5187','10385','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (215,'Clearview','0.729373','-19245.9','19997.08','751.18','201.07','412','13673','26523','11')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (216,'Springfield Gardens North','1.188966','-19599.18','20852.2599999999','1253.08','155.8','457','11288','23364','13')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (217,'Old Howard Beach','4.310676','-18668.8499999999','20185.09','1516.24','193.39','445','2428','5460','12')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (218,'South Ozone Park','2.669029','-83367.8899999999','87052.88','3684.99','159.24','456','20539','54527','67')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (219,'Lindenwood','2.028709','-12237.29','16196.08','3958.79','158.37','437','5055','9102','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (220,'Woodhaven','2.582065','-57442.41','61602.6299999999','4160.22','151.06','464','15837','41157','57')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (221,'Sunnyside','2.067037','-65793.1799999999','70746.1699999999','4952.99','151.5','461','22653','47116','74')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (222,'Ridgewood','2.376648','-47372.4199999999','50098.73','2726.31','128.32','452','16473','36738','68')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (223,'Middle Village','1.400807','-28205.07','29749.22','1544.15','179.56','440','11860','25011','19')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (224,'Elmhurst','2.04529','-83870.07','95603.44','11733.36','125.73','418','37281','93501','69')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (225,'Glendale','2.335329','-62424.1699999999','65209.3499999999','2785.18','142.22','424','19688','43274','81')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (226,'Breezy Point & Roxbury','0.702561','-2829.44','2874.27','44.83','229.05','406','1791','3407','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (227,'Richmond Hill','1.366706','-43143.08','46917.72','3774.64','155.78','451','22097','57485','66')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (228,'Howard Beach','0','0','0','0','252.23','428','2576','5562','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (229,'Ozone Park','1.272673','-12112.58','12519.5','406.92','162.94','446','6054','13891','12')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (230,'Rockaway Park','4.401066','-18507.23','20593.52','2086.3','125.59','453','3736','7800','22')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (231,'Neponsit & Belle Harbor','0.123599','-1474.78','1485.65','10.88','245.18','442','4916','9527','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (232,'Queensboro Hill','1.647178','-25267.4399999999','27919.9199999999','2652.48','134.57','449','12630','30855','13')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (233,'North Corona','3.4987','-34953.5599999999','37417.58','2464.02','126.61','443','8470','29068','34')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (234,'Rego Park','1.328103','-65605.66','68273.6199999999','2667.95','157.21','450','32789','61320','42')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (235,'Kew Gardens','2.043931','-18639.54','20605.2099999999','1965.68','151.49','434','6673','12825','17')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (236,'College Point','1.197593','-18049.38','20321.3899999999','2272.02','187.12','413','9093','22246','20')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (237,'Cambria Heights','1.317733','-28117.22','31034.5','2917.28','206.62','411','11430','27948','28')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (238,'East Elmhurst','2.403471','-19222.06','21495.75','2273.68','144.79','416','6194','17539','21')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (239,'Flushing','7.459312','-79189.1699999999','96627.1199999999','17437.95','110.96','420','11706','27303','43')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (240,'Long Island City & Astoria','2.119485','-138908.079999999','150032.89','11124.82','129.54','438','54796','109926','149')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (241,'Hunters Point','3.411238','-16275.42','17432.9599999999','1157.54','189.45','429','2705','6255','19')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (242,'Maspeth','2.058169','-30325.6199999999','32174.7599999999','1849.14','161.24','439','9722','21182','34')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (243,'Woodside','1.836373','-38860.1299999999','42810.87','3950.74','143.49','465','16292','36641','26')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (244,'Corona','1.720658','-39170','44551.08','5381.08','127.8','414','20315','56616','50')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (245,'Forest Hills','0.867651','-31202.88','35326.26','4123.38','217.73','421','18751','33440','27')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (246,'Jackson Heights','2.633908','-125318.82','134366.04','9047.22','138.12','430','37035','86996','86')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (247,'Steinway','1.731953','-47910.1699999999','53648.55','5738.38','152.16','460','20413','39378','50')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (248,'Broad Channel','1.048778','-1954.04','2061.58','107.54','220.98','408','892','1890','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (249,'Randall Manor','0.422504','-452.92','459.77','6.85','290.99','524','375','780','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (250,'Rosebank','1.130915','-11763.91','13627.92','1864.01','189.96','525','6361','14399','10')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (251,'Castleton Corners','2.162897','-26669.97','28370.4199999999','1700.45','238.97','505','5504','11002','14')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (252,'Silver Lake','0.808125','-3199.78','3222.21','22.43','165.9','528','2410','5194','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (253,'Grasmere','1.69032','-6120.91','6766.51','645.61','150.23','511','2672','5748','12')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (254,'Todt Hill','1.593178','-14313.65','15155.51','841.86','213.54','533','4467','9910','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (255,'Oakwood Beach','0.986526','-7884.76','8205.63','320.87','178.22','520','4680','9919','10')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (256,'Fort Wadsworth','0','0','0','0','158.29','507','380','652','0')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (257,'South Beach','0.706666','-3297.77','3460.29','162.52','176.24','529','2786','6834','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (258,'New Brighton','0.515855','-1305.89','1362.6','56.71','129.77','517','2041','4437','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (259,'Shore Acres','5.710755','-7199.87','7475.3','275.43','120.75','527','1087','1868','10')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (260,'St. George','1.604835','-8457.66','8781.16','323.49','115.83','530','4737','9318','12')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (261,'Ward Hill','1.62694','-1167.66','1341.91','174.25','144.85','535','571','1383','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (262,'Clifton','1.751908','-6344.28','7103.6','759.32','90.49','506','4493','9326','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (263,'West Brighton','2.467527','-26352','30340.3899999999','3988.39','174.02','268','7684','15361','26')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (264,'Stapleton','7.049447','-24284.0499999999','25575.8699999999','1291.81','97.46','531','3733','8666','34')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (265,'Grymes Hill','0.446991','-2615.37','2741.58','126.22','173.44','513','3546','8007','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (266,'Livingston','0.394704','-776','892.44','116.44','215.31','515','1053','2779','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (267,'Rossville','1.171046','-14472.52','18204.81','3732.29','226.94','526','6869','15914','5')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (268,'Annadale','0.785028','-7187.25','7544.56','357.31','282.2','501','3415','8076','6')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (269,'Bloomfield','1.856184','-19773.15','21769.59','1996.44','209.37','503','5617','12329','14')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (270,'Port Ivory','12.971022','-6747.35','6927.36','180.01','87.65','521','611','1145','2')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (271,'Great Kills','1.147379','-76123.52','87265.0899999999','11141.57','234.95','512','32460','70057','39')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (272,'Lighthouse Hill','0.211601','-1372.66','1718.42','345.76','257.13','514','3167','7371','3')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (273,'Port Richmond','3.75014','-21893.36','23353.2999999999','1459.94','149.89','522','4166','10186','22')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (274,'Tottenville','1.758737','-20301.56','21940.16','1638.6','253.58','534','4933','11031','13')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (275,'Fresh Kills','2.913376','-15702.54','16130.94','428.4','223.87','508','2480','6528','13')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (276,'Sunnyside','0.826188','-6844.18','6945.38','101.19','206.66','461','22653','47116','8')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (277,'Port Richmond Center','0.763217','-4360.31','4360.31','0','207.71','523','2758','5776','1')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (278,'New Dorp','2.954403','-34905.72','39457.4199999999','4551.71','194.85','518','6873','14875','29')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (279,'Grant City','2.799666','-21464.82','22112.88','648.05','142.45','509','5560','11439','15')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (280,'Arlington','0.439725','-812.77','834.69','21.92','121.55','502','1566','3231','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (281,'New Springville','2.078624','-26386.99','27817.8499999999','1430.86','192.42','519','6974','14535','11')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (282,'Bull\'s Head','0.484315','-7277.68','7684.31','406.63','228.72','504','6956','14747','7')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (283,'Graniteville','1.142318','-7222.14','8308.77','1086.64','198.36','510','3677','7799','4')")
        db.execute("INSERT INTO `citi_digits_neighborhoodstatistics` VALUES (284,'Mariners Harbor','4.236409','-22482.4199999999','24082.25','1599.83','138.19','516','4125','9516','11')")

    def backwards(self, orm):
        # Deleting model 'NeighborhoodStatistics'
        db.delete_table(u'citi_digits_neighborhoodstatistics')


    models = {
        u'citi_digits.citydigitsuser': {
            'Meta': {'object_name': 'CityDigitsUser'},
            'entityId': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'citi_digits.interview': {
            'Meta': {'object_name': 'Interview'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entityId': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewType': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Location']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Student']"})
        },
        u'citi_digits.interviewcomment': {
            'Meta': {'object_name': 'InterviewComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interview': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Interview']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'citi_digits.interviewplayer': {
            'Meta': {'object_name': 'InterviewPlayer'},
            'do_you_ever_buy_lottery_tickets': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'have_you_ever_won_the_lottery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jackpot_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'money_spent_on_lottery_in_average_week': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'most_won': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'why_or_why_not_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'citi_digits.interviewretailer': {
            'Meta': {'object_name': 'InterviewRetailer'},
            'amount_tickets_bought_per_visit': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'customers_in_a_day': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'do_you_sell_lottery_tickets': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage_buy_lottery_tickets': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'storeName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'why_or_why_not_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'why_or_why_not_lottery_neighborhood_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'citi_digits.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'citi_digits.neighborhoodstatistics': {
            'Meta': {'object_name': 'NeighborhoodStatistics'},
            'adults_per_store': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'daily_win': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'map_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'net_loss_per_store': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'net_win': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'percent_income': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_18_and_up': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_households': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_retailers': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'citi_digits.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'citi_digits.student': {
            'Meta': {'object_name': 'Student'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Team']"})
        },
        u'citi_digits.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'className': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.School']"})
        },
        u'citi_digits.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Teacher']"})
        },
        u'citi_digits.tour': {
            'Meta': {'object_name': 'Tour'},
            'coverPhoto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Student']"}),
            'teamPhoto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'citi_digits.tourauthors': {
            'Meta': {'object_name': 'TourAuthors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Student']"}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Tour']"})
        },
        u'citi_digits.tourslide': {
            'Meta': {'object_name': 'TourSlide'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Tour']"})
        }
    }

    complete_apps = ['citi_digits']