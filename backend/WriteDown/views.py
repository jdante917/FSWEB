from django.shortcuts import render
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from backend import settings
from rest_framework.views import APIView
import os
import pandas as pd
# # Create your views here.


def WriteDown(APIView):
    cur = connection.cursor()
    cur.execute('''
select top 10 tti_num_type_tiers_tti, 
tir_num_tiers, 
pay_code_pays_pay,
org_num_organisation_eln,
niv_num_niveau_eln,eln_num_elt_niveau_eln
from ods.mds_tiers_ref tr
where tr.tti_num_type_tiers_tti in (21)
and pay_code_pays_pay = 'CN'
and niv_num_niveau_eln in (0,4)
group by 1,2,3,4,5,6
order by 1 desc
''')
    header = ['Type', 'third', 'Country', 'DPP', 'Level', 'DeptNum']
    df = pd.DataFrame(cur.fetchall(), columns=header)
    print(df)
    return HttpResponse(df)
