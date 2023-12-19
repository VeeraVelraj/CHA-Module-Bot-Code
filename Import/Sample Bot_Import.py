# import json
# body = json.loads(r'''{"body": {"input": {"EID_v3oct9e561": null, "EID_gqgkd6wxsx": null, "freight_inr": "0", "EID_3tgg46t14j": "Sea Import", "insurance_exchange_rate": null, "EID_9v1sfj4lty": null, "EID_hcfa2natdy": "2023-05-17T06:29:54.491Z", "freight_currency": null, "EID_a76z9gibst": "884542.0", "EID_zclitod22i": [{"EID_babo38ltc1": {"extraLabels": [], "select": 56.45, "view": 56.45}, "EID_8idwkluq9k": "2023-05-17T06:31:27.306Z", "EID_jl37x8j7hu": null, "EID_7ng8113art": "https://neo.timelapse-nexus.com/tasks/81591", "EID_tinjlqjzrr": "https://neo.timelapse-nexus.com/tasks/81590", "EID_vifciz13im": "4234", "EID_8jesrg17sj": {"extraLabels": [], "select": "AUD", "view": "AUD"}, "EID_zsjazm2a4a": "FOB", "EID_pix36qxa9r": "1", "EID_rxvrawwj72": null, "EID_1tiuyw6lbg": null, "EID_d2qjcctcc3": 876867, "EID_hmrelyhis2": null}, {"EID_babo38ltc1": {"extraLabels": [], "select": 56.45, "view": 56.45}, "EID_8idwkluq9k": "2023-05-17T06:31:29.155Z", "EID_jl37x8j7hu": null, "EID_7ng8113art": "https://neo.timelapse-nexus.com/tasks/81594", "EID_tinjlqjzrr": "https://neo.timelapse-nexus.com/tasks/81593", "EID_vifciz13im": "43243", "EID_8jesrg17sj": {"extraLabels": [], "select": "AUD", "view": "AUD"}, "EID_zsjazm2a4a": "FOB", "EID_pix36qxa9r": "2", "EID_rxvrawwj72": null, "EID_1tiuyw6lbg": null, "EID_d2qjcctcc3": 7675, "EID_hmrelyhis2": null}], "EID_svizwe8pp8": null, "freight_rate": "0", "misc_charge_amount": "0", "EID_8kke3n8kbt": null, "EID_tkme1m6amh": null, "misc_charge_inr": "0", "EID_fah9ujd5ps": "Yes", "EID_7qns9ivn2e": "https://neo.timelapse-nexus.com/tasks/81595", "misc_charge_currency": null, "formID": "63d75eee93f63a33a8a82732", "EID_ny4flsqa4w": [{"EID_s2x1g3aq5r": null, "EID_k39deuxlpa": null, "EID_zbtujcgo6f": null, "EID_52m57g8juj": null, "EID_ap54sp7hkp": "Product Value", "EID_3icbhioyng": "None", "EID_a14vs1fyxy": null, "EID_lo4nq6iwk4": null, "EID_5ggeb2n37k": null, "EID_zuiwrf57mo": null, "EID_ubd1iujie4": null, "EID_st3smz5fca": null, "EID_2vhwysh3d1": null, "EID_5vxp9nieow": null}], "insurance_inr": "0", "freight_amount": "0", "EID_78m286hdg9": "2284", "EID_hxdq2uruyy": null, "EID_ss7lmg7ygl": true, "EID_4tn7aeswv3": null, "insurance_currency": null, "EID_inch42r73z": null, "EID_cx4srcfynp": null, "EID_gzw9c3eaza": false, "freight_exchange_rate": null, "misc_charge_rate": "0", "EID_wxa48ie597": "Thilak", "EID_2o9ztk2r1p": null, "EID_dfwkcpfgkz": [{"extraLabels": [], "select": "LCL", "view": "LCL"}], "EID_sx47ci37zj": null, "EID_uh8kvktt7f": null, "misc_charge_exchange_rate": null, "insurance_amount": "0", "EID_jzw955h3se": null, "EID_ioygscm695": "03/SI/01393/23-24", "EID_3u8u6q9dm6": null, "insurance_rate": "0", "EID_8gdrvterm7": null}, "automation": {"codeSnippet": "", "description": "", "title": "Invoice Details(import/Export)task_Link", "id": 11, "framework": "LEGACY", "version": 184, "codeUrl": "https://neo.timelapse-nexus.com/storj/TM_ORG_98NCMBD2KBZ4R_TM_S3_TEMP_FILES_1684303220_485748728_ExporttaskLink.py", "createdAt": "2023-02-20T03:53:51.172Z"}}, "log_level": "WARNING", "message": "requested body", "pid": 19, "DateCreated": "2023-05-17 06:41:25"}

# ''')

# automation_inputs = body["body"]["input"]
import json
import datetime
import re
import operator
from dateutil import tz
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from python.classes.modules.zmodule_v2.zutility import sheet_widget_manipulation, data_copying, elements_utility
from python.classes.modules.zmodule_v2.zutility import random_password_generator, public_links, user_management, \
    communications, data_copying, elements_utility
from python.classes.modules.zmodule_v2 import zsubmissions, ztasks, zautomation
from python.classes.modules.common.loggerClass import LoggerClass as LogClass
from python.classes.modules.common import common_util
from python.classes.modules.zmodule_v2 import zsubmissions
from python.classes.modules.zmodule_v2.zutility import sheet_widget_manipulation, data_copying, elements_utility
from python.classes.modules.zmodule_v2 import zforms
from python.classes.modules.zmodule_v2.zutility.elements_casting import ElementCasting
from python.classes.modules.zmodule_v2.zutility import elements_utility
from datetime import datetime, time, date, timedelta

Shipment = []
flag = []
table = automation_inputs["EID_mpowf52xtn"]
if table:
    for row in table:
        if row["EID_q29k2c88qh"]:
            Container_No =  row["EID_q29k2c88qh"]
            if int(Container_No) in Shipment:
                flag.append(Container_No)
            else:
                Shipment.append(Container_No)


if flag:
    validate_error_flag = True
else:
    validate_error_flag = False
response = {"error": validate_error_flag}
response = {"message":"New commit"}
