import MySQLdb
import csv
import time
import datetime
start_time = time.time()
timestamp = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
db = MySQLdb.connect(host="comm-infocntr-amer-dev-01.ciean0huuvrb.us-east-1.rds.amazonaws.com",
                     user="infocntrdevmstr",         # your username
                     passwd="infocntrdevmstr_201708A",  # your password
                     db="devinfocntr")
target = db.cursor()
target.execute(" TRUNCATE TABLE STG_TPAMT")
print "Truncating TPAMT"
target.execute(" TRUNCATE TABLE STG_TPALT")
print "Truncating TPALT"
target.execute(" TRUNCATE TABLE STG_TPAMH")
print "Truncating TPAMH"
target.execute(" TRUNCATE TABLE STG_TPALH")
print "Truncating TPALH"
target.execute(" TRUNCATE TABLE STG_DETCG")
print "Truncating DETCG"
file = open ('Data\Q4 2016 DET.txt','r')
overpunch_no = {'{':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'}':0,'J':1,'K':2,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9}
overpunch_multiplier = {'}':'-','J':'-','K':'-','L':'-','M':'-','N':'-','O':'-','P':'-','Q':'-','R':'-'}
commit_count = 0
for line in file:
    line_id = line[0:5]
    if line_id == 'TPAMT':
        print "Writing STG_TPAMT"
        TRGDPA_TPAMT = line[50:63]+str(overpunch_no.get(line[63]))
        TRGDCA_TPAMT = line[64:77]+str(overpunch_no.get(line[77]))
        TGDATP_TPAMT = line[78:91]+str(overpunch_no.get(line[91]))
        target.execute ("Insert into STG_TPAMT VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
        %(line[0:5],line[5:11],line[11:18],line[18:26],line[26:32],line[32:37],line[37:42],line[42:50],overpunch_multiplier.get(line[65],'')+TRGDPA_TPAMT[0:12]+'.'+TRGDPA_TPAMT[12:14],line[50:64],overpunch_multiplier.get(line[79],'')+TRGDCA_TPAMT[0:12]+'.'+TRGDCA_TPAMT[12:14],line[64:78],overpunch_multiplier.get(line[91],'')+TGDATP_TPAMT[0:12]+'.'+TGDATP_TPAMT[12:14],line[78:92],'',timestamp))
    if line_id == 'TPALT':
        print "Writing STG_TPALT"
        TRGDPA_TPALT = line[55:65]+str(overpunch_no.get(line[65]))
        TRGDCA_TPALT = line[66:76]+str(overpunch_no.get(line[76]))
        TGDATP_TPALT = line[77:87]+str(overpunch_no.get(line[87]))
        target.execute ("Insert into STG_TPALT VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
        %(line[0:5],line[5:11],line[11:18],line[18:24],line[24:32],line[32:38],line[38:43],line[43:48],line[48:55],overpunch_multiplier.get(line[65],'')+TRGDPA_TPALT[0:9]+'.'+TRGDPA_TPALT[9:11],line[55:66],overpunch_multiplier.get(line[76],'')+TRGDCA_TPALT[0:9]+'.'+TRGDCA_TPALT[9:11],line[66:77],overpunch_multiplier.get(line[87],'')+TGDATP_TPALT[0:9]+'.'+TGDATP_TPALT[9:11],line[77:88],'',timestamp))
        db.commit()
    if line_id == 'TPAMH':
        print "Writing STG_TPAMH"
        target.execute ("Insert into STG_TPAMH VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
        %(line[0:5],line[5:11],line[11:18],line[18:26],line[26:32],line[32:37],line[37:42],'',timestamp))
        db.commit()
    if line_id == 'TPALH':
        print "Writing STG_TPALH"
        target.execute ("Insert into STG_TPALH VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
        %(line[0:5],line[5:11],line[11:18],line[18:24],line[24:32],line[32:38],line[38:43],line[43:48],'',timestamp))
        db.commit()
    if line_id == 'DETCG':

        RGDPA = line[115:125]+str(overpunch_no.get(line[125]))
        RGDCA = line[126:136]+str(overpunch_no.get(line[136]))
        GDATP = line[137:147]+str(overpunch_no.get(line[147]))
        target.execute ("Insert into STG_DETCG VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
        %(line[0:5],line[5:11],line[11:18],line[18:38],line[38:44],line[44:63],line[63:75],line[75:77],line[77:80],line[80:90],line[90:98],line[99:100],line[100:115],overpunch_multiplier.get(line[125],'')+RGDPA[0:9]+'.'+RGDPA[9:11],line[115:126],overpunch_multiplier.get(line[136],'')+RGDCA[0:9]+'.'+RGDCA[9:11],line[126:137],overpunch_multiplier.get(line[147],'')+GDATP[0:9]+'.'+GDATP[9:11],line[137:148],line[148:154],line[154:160],'',timestamp))
        commit_count += 1
        if commit_count ==10000:
            db.commit()
            commit_count = 0
            print "commited 10k recs"



db.commit()
db.close()
print "Done"
print("--- %s seconds ---" % (time.time() - start_time))
