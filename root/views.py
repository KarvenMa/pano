# -*- coding: utf-8 -*-
import os
import django
from django.http import HttpResponse
from django.db import connection
from settings import BASE_DIR


def index(request):
    return HttpResponse(
        'django version: {0} <br/><br/>'
        '<a href="/panorama/view?scene_id=first">查看场景first</a><br/>'
        '<a href="/panorama/edit?scene_id=first">编辑场景first</a><br/>'
        '<a href="/panorama/view?scene_id=second">查看场景second</a><br/>'
        '<a href="/panorama/edit?scene_id=second">编辑场景second</a><br/>'
        '<br/><br/><a href="/static/f22fight.html">3D场景</a>'.format(django.get_version())
    )


def init_database(request):
    """
    将数据重置
    :param request:
    :return:
    """
    import MySQLdb
    dbname = "eaAAGHWPjQlnoZxLhJxE"  # 数据库名称
    api_key = "4c7d384d945d44c4ac7301d11d377535"  # 用户AK
    secret_key = "3c4a1893d499411ca51b68e5deec281c"  # 用户SK

    # 连接MySQL服务
    mydb = MySQLdb.connect(
        host="sqld.duapp.com",
        port=4050,
        user=api_key,
        passwd=secret_key,
        db=dbname)

    cursor = mydb.cursor()
    file_path = os.path.join(BASE_DIR, 'panorama/fixtures/panorama.sql'),
    sql = open(file_path[0], 'r').read()
    cursor = connection.cursor()
    cursor.execute(sql)
    mydb.close()
    return HttpResponse("reset database succeed!")
