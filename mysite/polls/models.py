from django.db import models



# 불러오는 데이터
# "result": 1,
#     "cur_unit": "AED",
#     "ttb": "371.05",
#     "tts": "378.54",
#     "deal_bas_r": "374.8",
#     "bkpr": "374",
#     "yy_efee_r": "0",
#     "ten_dd_efee_r": "0",
#     "kftc_bkpr": "374",
#     "kftc_deal_bas_r": "374.8",
#     "cur_nm": "아랍에미리트 디르함"

# decimalField
class All_Data(models.Model) :
    result = models.CharField(max_length=40)
    cur_unit = models.CharField(max_length=40)
    ttb = models.CharField(max_length=40) 
    tts = models.CharField(max_length=40)
    deal_bas_r = models.CharField(max_length=40)
    bkpr = models.CharField(max_length=40)
    yy_efee_r = models.CharField(max_length=40)
    ten_dd_efee_r = models.CharField(max_length=40)
    kftc_bkpr = models.CharField(max_length=40)
    kftc_deal_bas_r = models.CharField(max_length=40)
    cur_nm = models.CharField(max_length=40)