from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from backend import settings
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import os
import csv
import pandas as pd


# Create your views here.


class WriteDown(APIView):
    def post(self, request):
        cursor = connection.cursor()
        startTime = request.data.get("startTime")
        endTime = request.data.get("endTime")
        cursor.execute('''
                    select * from dvdbredshift02.ods_retail.cis_writedown wd
                     where wd.store in (
                       select t.tir_num_tiers from dvdbredshift02.ods.mds_tiers_ref t
                       where t.tti_num_type_tiers_tti=7
                       and t.pay_code_pays_pay='CN'
                       and t.dev_code_devise_dev='CNY'
                    ) and wd.creationdate > to_date('%s', 'dd/mm/yyyy') --by month
                    and wd.creationdate < to_date('%s', 'dd/mm/yyyy')
                     and wd.type != 'CLAIM_BURGLARY'
                     '''% (startTime, endTime))
        rows = cursor.fetchall()
        download_file_path = os.path.join(settings.BASE_DIR,"test.csv")
        df=pd.DataFrame(rows)
        df.to_csv(download_file_path)
        return HttpResponse(rows)


