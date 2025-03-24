from django import template
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.utils import timezone
register = template.Library()

@register.filter(name='calucurate_datetime_to_now')
def calcurate_datetime_to_now(value):
    # 2018/1/10入力された日付をdate型に変換
    join_date = datetime.strptime(value, '%Y/%m/%d').date()
    
    # 現在日付を取得
    now_date = date.today()
    
    # 日付の差を計算
    diff = relativedelta(now_date, join_date)
    
    return f'{diff.years}年{diff.months}ヶ月'