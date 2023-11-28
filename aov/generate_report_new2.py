#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : anselzhu

import os
import json
import re, random
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(".//downloadapk//")
sys.path.append(".//downloadapk//wpyscripts_upload")
from tools.mysql_helper import MySQLHelper, get_package_size
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from perf_data_processing import check_maoyan_data, check_version_data
from send_mail import send_mail
import send_tips
import decimal
import time
from commons.const import *


def get_dlc_compare_result(platform):
    sql = "select different_info,new_info from t_package_size_info " \
          "where platform like '%%%s%%' and file_type='zip' order by created_time desc limit 1;" % platform
    res = MySQLHelper().execute_query(sql)
    diff_info, new_info = res[0][0], res[0][1]
    return diff_info, new_info


def get_apk_size(platform):
    sql = "select package_size from t_package_size_info " \
          "where platform like '%%%s%%' and file_type='apk' order by created_time desc limit 1;" % platform
    res = MySQLHelper().execute_query(sql)
    package_size = res[0][0]
    package_size = round(float(package_size)/(1024 * 1024), 2)
    return package_size


class GanerateReportHtml:
    def __init__(self, model):
        model_pkg_dict = get_model_pkg_dict()
        model_table_dict = get_model_table_dict()
        self.model = model

        self.device_list = get_tested_device_list()
        self.pkg_url = model_pkg_dict[model]
        self.title = "AOV-%s线性能监控测试报告" % model
        self.title = self.title.replace("optimize", "性能优化分支").replace("ftrunk", "FTrunk") \
            .replace("pub", "PUB").replace("trunk", "Trunk").replace("battle", "战场")
        self.table_name = model_table_dict[model]

    def ganerate_html(self):
        perfdog_taskid_dict = get_perfdog_taskid_dict()
        html = open('indexForChrome.html', 'w')

        perf_summ = self.perf_data_compare()
        benchmark_compare_sum = self.benchmark_compare()
        global perf_summ

        html.write("""<html>
        <head>
          <title>Test</title>
          <style>img{float:left;margin:5px;}</style>
        </head>
        <style>
        #header {
            background-color:black;
            color:white;
            text-align:center;
            padding:5px;
        }
        #section {
            width:1850px;
            float:left;
            padding:10px;        
        }

        body,p{margin: 0;}   
        .parentWrap{   
            overflow: hidden; 
        }   
        .child{   
            float: left;   
            height: 60px;   
            width: 380px;
            padding-left: 20px;   
            box-sizing: border-box;   
            background-clip: content-box;   
        }
        .childlog{   
            float: left;   
            width: 380px;   
            padding-right: 20px;   
            box-sizing: border-box;   
            background-clip: content-box;   
        }
        .childpicture{   
            float: left;   
            height: 670px;   
            width: 380px;   
            padding-right: 20px;   
            box-sizing: border-box;   
            background-clip: content-box;   
        }
        .childperf{   
            float: left;   
            height: 550px;   
            width: 780px;   
            padding-right: 20px;   
            box-sizing: border-box;   
            background-clip: content-box;   
        }
        .childperf1{   
            float: left;   
            height: 550;   
            width: 780px;   
            padding-right: 20px;   
            box-sizing: border-box;   
            background-clip: content-box;   
        }    

        </style>

        <style type="text/css">
        table
          {
          border-collapse:collapse;
          }
        table, td, th
          {
          border:1px solid black;
          }
        th
          {
        text-align:center;
        vertical-align:middle;
        height:50px;
          }
        td
          {
        text-align:center;
        vertical-align:middle;
          height:50px;
          }
        </style>

        <body>
        <div id="header">
            <h1>%s</h1>
        </div>
        <h4> 测试结论</h4>
        <p><b>&nbsp;&nbsp;&nbsp;&nbsp;1.对比性能基准数据：%s<br>
           &nbsp;&nbsp;&nbsp;&nbsp;2.对比最近性能趋势：%s<br>"""
                   % (self.title, benchmark_compare_sum, perf_summ))
        if self.model == "trunk":
            # apk_size = get_apk_size("Beta28H-Android")
            # compare_apk_size = apk_size - 422.11
            # if compare_apk_size >= 0:
            #     compare_apk_size_desc = "<font color=\"red\">增加%sM</font>" % compare_apk_size
            # else:
            #     compare_apk_size_desc = "减少%sM" % compare_apk_size
            # diff_info, new_info = get_dlc_compare_result("Beta28H-Android")

            apk_size_29 = get_apk_size("Beta29-Android")
            compare_apk_size = apk_size_29 - 439
            if compare_apk_size >= 0:
                compare_apk_size_desc_29 = "<font color=\"red\">增加%sM</font>" % compare_apk_size
            else:
                compare_apk_size_desc_29 = "<font color=\"green\">减少%sM</font>" % abs(compare_apk_size)
            diff_info_29, new_info_29 = get_dlc_compare_result("Beta29-Android")
            print diff_info_29
            print new_info_29
            diff_info_29_dict = json.loads(diff_info_29)
            new_info_29_dict = json.loads(new_info_29)
            if int(diff_info_29_dict['size']) > 300:
                diff_info = "<font color=\"red\">差异文件%s个，共%sM</font>" % (
                diff_info_29_dict['count'], diff_info_29_dict['size'])
            else:
                diff_info = "差异文件%s个，共%sM" % (diff_info_29_dict['count'], diff_info_29_dict['size'])

            html.write("""
            &nbsp;&nbsp;&nbsp;&nbsp;3.泰国主线包量监控：Android首包大小 %sM，%s；DLC详细文件对比，%s，新增文件%s个，共%sM</b></p>"""
                       % (apk_size_29, compare_apk_size_desc_29,
                          diff_info,
                          new_info_29_dict["count"], new_info_29_dict["size"],
                          ))

        package_info_list = self.get_version_pack()
        print "package_info_list: %s" % package_info_list
        package_name_list, package_size_list = [], []
        for p in package_info_list:
            package_name_list.append(p[0])
            package_size_list.append(p[1])
        package_info = ""
        for i in range(len(package_name_list)):
            # package_size = int(package_size_list[i])/(1024*1024)
            package_info += package_name_list[i]
            package_info += "(%sMb)" % package_size_list[i] + '; <br>' + '&nbsp;' * 7
        # package_info += '; <br>' + '&nbsp;'*7
        html.write("""
                <h4> 详细测试数据及结果如下：</h4>
                <div id="section">
                <h2>一、安装包信息</h2>
                <h3>包名： %s</h3>
                <h3>构建地址： %s</h3>
                <h3>tfs路径：\\\\tencent.com\\tfs\\跨部门项目\\WS_SGAME\\EOA基线库\\性能数据存档\\日构建数据</h3>
                <h2>二、最近两轮详细数据：</h2>
                <p><b>perfdog链接：https://perfdog.qq.com/taskdata/%s/cases</b></p>
                <I>备注：1.性能基准数据为Beta30 Pub线平均数据 
                         2.每日数据为测试至少3轮的平均数据</I>
                """ % (package_info, self.pkg_url, perfdog_taskid_dict[self.model]))
        # perf_data_list = get_daily_perf_data()
        perf_title_list = ["版本", "机型/画质", "日期", "平均帧率", "loading 时间均值",
                           "帧率>18比例(%)",
                           "帧率>25比例(%)", "帧率方差", "单帧>100ms比例(%)",
                           "卡顿次数(10m)", "严重卡顿次数(10m)",
                           "PSS内存均值(MB)", "PSS内存峰值(MB)",
                           "Mono已用内存峰值(MB)", "Mono堆内存峰值(MB)", "GC次数",
                           "Draw call均值", "三角形数均值", "顶点数均值",
                           "UI_dc", "HUD_dc", "Scene_dc", "Particle_dc",
                           "FrameSync", "LogicThr",
                           "SleepTime", "PostTime",
                           "平均CPU", "最高温度"]
        html.write("""
            <table>
                <tr>
            """)
        for title in perf_title_list:
            html.write("""
                    <th>%s</th>
                """ % title)
        html.write("""
                </tr>
            """)

        # 各机型性能红线基准
        sql = "select avg_fps, loading_time, fps_more_18, fps_more_25, var_fps, ftime_more_100, " \
              "jank_10m, big_jank_10m, avg_memory_MB, peak_memory_MB, " \
              "mono_max_used, mono_max_heap, gc_count, draw_calls_avg, tris_avg, verts_avg, " \
              "avg_ui_calls, avg_hud_calls, avg_scene_calls, avg_particle_dcs, LFrameSynchrTime, " \
              "LogicThreadTime, SleepTime, PostFrameTime, avg_cpu, ctemp from benchmark_performance_aov" \
              " where device_id = '{}' and branch_name = 'trunk' order by id desc limit 1;"

        # ios_benchmark = ["性能指标基准", "iPhone 6P", "-"]
        # res = MySQLHelper().execute_query(sql.format("11"))[0]
        # ios_benchmark += res
        #
        # lowest_device_benchmark = ["性能指标基准", "超低端机", "-"]
        # res = MySQLHelper().execute_query(sql.format("1"))[0]
        # lowest_device_benchmark += res
        #
        # low_device_benchmark = ["性能指标基准", "低端机", "-"]
        # res = MySQLHelper().execute_query(sql.format("2"))[0]
        # low_device_benchmark += res
        #
        # middle_device_benchmark = ["性能指标基准", "中端机", "-"]
        # res = MySQLHelper().execute_query(sql.format("3"))[0]
        # middle_device_benchmark += res
        #
        # high_device_benchmark = ["性能指标基准", "高端机", "-"]
        # res = MySQLHelper().execute_query(sql.format("4"))[0]
        # high_device_benchmark += res
        #
        # hd_device_benchmark = ["性能指标基准", "HD", "-"]
        # res = MySQLHelper().execute_query(sql.format("5"))[0]
        # hd_device_benchmark += res

        # if self.model == 'trunk':
        #     # 写入IOS数据
        #     html.write("""<tr>""")
        #     for ios in ios_benchmark:
        #         html.write("""<td><span style="color:red;">%s</span></td>
        #                                     """ % ios)
        #     html.write("""</tr>""")
        #
        #     ios_datas = self.get_daily_perf_by_device('f1af3d624c00d5ac1e09aeac90770c5a2344bdd4')
        #     for ios_data in ios_datas:
        #         html.write("""<tr>""")
        #         for data in ios_data:
        #             # print (data)
        #             if isinstance(data, (datetime.date, float, decimal.Decimal)):
        #                 data = str(data)
        #             elif data is None:
        #                 data = "-"
        #             else:
        #                 data = data.encode('utf-8')
        #             html.write("""<td>%s</td>
        #                         """ % data)
        #         html.write("""</tr>
        #                 """)

        level_device_dict = get_level_device_dict()
        for level in sorted(level_device_dict):
            device_list = level_device_dict[level]
            if len(device_list) == 0:
                continue
            for device_id in device_list:
                perf_datas = self.get_daily_perf_by_device(device_id)
                device_name = perf_datas[0][1]
                device_benchmark = ["性能指标基准", device_name, "-"]
                res = MySQLHelper().execute_query(sql.format(device_id))
                if not res:
                    res = ['-'] * 26
                else:
                    res = res[0]

                device_benchmark += res

                html.write("""<tr>""")
                for benchmark_data in device_benchmark:
                    html.write("""<td><span style="color:red;">%s</span></td>
                                    """ % benchmark_data)
                html.write("""</tr>
                            """)

                for perf_data in perf_datas:
                    html.write("""<tr>""")
                    for data in perf_data:
                        # print (data)
                        if isinstance(data, (datetime.date, float, decimal.Decimal)):
                            data = str(data)
                        elif data is None:
                            data = "-"
                        else:
                            data = data.encode('utf-8')
                        html.write("""<td>%s</td>
                                """ % data)
                    html.write("""</tr>
                            """)

        # # 写入超低端数据
        # lowest_perf_datas = self.get_daily_perf_by_device('92010e74c4b8c295') + self.get_daily_perf_by_device(
        #     '32012153ed2c74d9')
        #
        # html.write("""<tr>""")
        # for lowest in lowest_device_benchmark:
        #     html.write("""<td><span style="color:red;">%s</span></td>
        #                     """ % lowest)
        # html.write("""</tr>
        #             """)
        # for perf_data in lowest_perf_datas:
        #     html.write("""<tr>""")
        #     for data in perf_data:
        #         # print (data)
        #         if isinstance(data, (datetime.date, float, decimal.Decimal)):
        #             data = str(data)
        #         elif data is None:
        #             data = "-"
        #         else:
        #             data = data.encode('utf-8')
        #         html.write("""<td>%s</td>
        #                 """ % data)
        #     html.write("""</tr>
        #             """)
        #
        # # 写入低端机数据
        # html.write("""<tr>""")
        # for benchmark in low_device_benchmark:
        #     html.write("""<td><span style="color:red;">%s</span></td>
        #                         """ % benchmark)
        # html.write("""</tr>
        #                 """)
        # low_perf_datas = self.get_daily_perf_by_device('SW5TMBBELR4SYLDM')
        # for perf_data in low_perf_datas:
        #     html.write("""<tr>""")
        #     for data in perf_data:
        #         # print (data)
        #         if isinstance(data, (datetime.date, float, decimal.Decimal)):
        #             data = str(data)
        #         elif data is None:
        #             data = "-"
        #         else:
        #             data = data.encode('utf-8')
        #         html.write("""<td>%s</td>
        #                 """ % data)
        #     html.write("""</tr>
        #             """)
        # # 写入中端机数据
        # html.write("""<tr>""")
        # for benchmark in middle_device_benchmark:
        #     html.write("""<td><span style="color:red;">%s</span></td>
        #                             """ % benchmark)
        # html.write("""</tr>
        #                     """)
        # middle_perf_datas = self.get_daily_perf_by_device('DYN6R20430003422')
        # for perf_data in middle_perf_datas:
        #     html.write("""<tr>""")
        #     for data in perf_data:
        #         if isinstance(data, (datetime.date, float, decimal.Decimal)):
        #             data = str(data)
        #         elif data is None:
        #             data = "-"
        #         else:
        #             data = data.encode('utf-8')
        #         html.write("""<td>%s</td>
        #                     """ % data)
        #     html.write("""</tr>
        #                 """)
        #
        # # 写入高端机数据
        # html.write("""<tr>""")
        # for benchmark in high_device_benchmark:
        #     html.write("""<td><span style="color:red;">%s</span></td>
        #                             """ % benchmark)
        # html.write("""</tr>
        #                     """)
        # high_perf_datas = self.get_daily_perf_by_device('NJ5HS4SS4PCEFESC')
        # for perf_data in high_perf_datas:
        #     html.write("""<tr>""")
        #     for data in perf_data:
        #         if isinstance(data, (datetime.date, float, decimal.Decimal)):
        #             data = str(data)
        #         elif data is None:
        #             data = "-"
        #         else:
        #             data = data.encode('utf-8')
        #         html.write("""<td>%s</td>
        #                     """ % data)
        #     html.write("""</tr>
        #                 """)
        #
        #
        # # 写入极高端机数据
        # html.write("""<tr>""")
        # for benchmark in hd_device_benchmark:
        #     html.write("""<td><span style="color:red;">%s</span></td>
        #                                 """ % benchmark)
        # html.write("""</tr>
        #                         """)
        # hd_perf_datas = self.get_daily_perf_by_device('JAAZGV160485Y83')
        # for perf_data in hd_perf_datas:
        #     html.write("""<tr>""")
        #     for data in perf_data:
        #         if isinstance(data, (datetime.date, float, decimal.Decimal)):
        #             data = str(data)
        #         elif data is None:
        #             data = "-"
        #         else:
        #             data = data.encode('utf-8')
        #         html.write("""<td>%s</td>
        #                         """ % data)
        #     html.write("""</tr>
        #                     """)

        html.write("""</table>
        <h2>三、性能指标趋势图：</h2>
        </div>
        <div class="parentWrap" style='margin-top:-10px; margin-left:30px'>
                """)
        sum_pics = self.draw_picture()
        for pic in sum_pics:
            html.write("""
        <div class="childperf" style=' margin-left:0px'>
        <img src="cid:%s" width="1800" height="900"/>
        </div>""" % pic)

        html.write("""
        </div>
        </body>
        </html>
            """)

        html.close()
        return os.path.join(os.getcwd(), 'indexForChrome.html')

    # def get_daily_perf_data(self):
    #     get_max_date_sql = "select distinct(version), min(date(created_time)) " \
    #                        "from %s " \
    #                        "where device_id in ('92010e74c4b8c295', '32012153ed2c74d9', " \
    #                        "'SW5TMBBELR4SYLDM', 'DYN6R20430003422', 'NJ5HS4SS4PCEFESC')" \
    #                        "group by version order by min(date(created_time)) desc " \
    #                        "limit 2;" % self.table_name
    #     second_date = str(MySQLHelper().execute_query(get_max_date_sql)[1][1])
    #
    #     sql = """select version, device_name, date(min(created_time)),
    #        round(avg(avg_fps),2), round(avg(fps_more_18),2), round(avg(fps_more_25),2),
    #        round(avg(var_fps),2), round(avg(ftime_more_100),2),
    #        round(avg(jank_10m),2),round(avg(big_jank_10m),2),
    #        max(mono_max_heap), max(mono_max_used), max(peak_memory_MB),
    #        round(avg(avg_cpu),2),max(ctemp)
    #     from %s dp
    #     left join deviceInfo dI on dp.device_id = dI.device_id
    #     where created_time > '%s'
    #     and dI.device_id in ('92010e74c4b8c295', '32012153ed2c74d9', 'SW5TMBBELR4SYLDM',
    #     'DYN6R20430003422', 'NJ5HS4SS4PCEFESC')
    #     group by dp.device_id, version
    #     order by device_name, date(min(created_time)) desc ;""" \
    #           % (self.table_name, second_date)
    #     result = MySQLHelper().execute_query(sql)
    #     # for rows in result:
    #     #     print (rows)
    #     return result

    def get_daily_perf_by_device(self, device_id, status_limit=1, count=2):
        status_query = 'and status = 1' if status_limit else ''
        sql = """select version, device_name, date(min(dp.created_time)),
           round(avg(avg_fps),2), round(avg(tts.loading_time),1), 
           round(avg(fps_more_18),2), round(avg(fps_more_25),2),
           round(avg(var_fps),2), round(avg(ftime_more_100),2),
           round(avg(jank_10m),2),round(avg(big_jank_10m),2),
           round(avg(avg_memory_MB),2),round(avg(peak_memory_MB),2),
           round(avg(mono_max_used),2), round(avg(mono_max_heap),2),round(avg(gc_count), 1),
           round(avg(draw_calls_avg),2),round(avg(tris_avg),2),round(avg(verts_avg),2),
           round(avg(avg_ui_calls),1),round(avg(avg_hud_calls),1),
           round(avg(avg_scene_calls),1),round(avg(avg_particle_dcs)),
           round(avg(LFrameSynchrTime),1), round(avg(LogicThreadTime),1), 
           round(avg(SleepTime),1), round(avg(PostFrameTime),1),
           round(avg(avg_cpu),2), max(ctemp)
        from %s dp
        left join deviceInfo dI on dp.device_id = dI.device_id 
        left join t_time_statistic tts on dp.task_id = tts.task_id
        where dI.device_id = '%s' %s 
        group by dp.device_id, version, date(dp.created_time) 
        order by date(min(dp.created_time)) desc, version desc  limit %s;""" \
              % (self.table_name, device_id, status_query, count)
        result = MySQLHelper().execute_query(sql)
        # for rows in result:
        #     print (rows)
        return result

    def get_daily_perf_by_device_dict(self, device_id, count=2):
        sql = """select version, device_name, date(min(dp.created_time)),
           round(avg(avg_fps),2) as avg_fps, round(avg(tts.loading_time),1) as loading_time, 
           round(avg(fps_more_18),2) as fps_more_18, round(avg(fps_more_25),2) as fps_more_25,
           round(avg(var_fps),2) as var_fps, round(avg(ftime_more_100),2) as ftime_more_100,
           round(avg(jank_10m),2) as jank_10m,round(avg(big_jank_10m),2) as big_jank_10m,
           round(avg(avg_memory_MB),2) as avg_memory_MB,round(avg(peak_memory_MB),2) as peak_memory_MB,
           round(avg(mono_max_used),2) as mono_max_used, round(avg(mono_max_heap),2) as mono_max_heap,
           round(avg(gc_count), 1) as gc_count,
           round(avg(draw_calls_avg),2) as draw_calls_avg,round(avg(tris_avg),2) as tris_avg,
           round(avg(verts_avg),2) as verts_avg,
           round(avg(avg_ui_calls),1) as avg_ui_calls,round(avg(avg_hud_calls),1) as avg_hud_calls,
           round(avg(avg_scene_calls),1) as avg_scene_calls,round(avg(avg_particle_dcs)) as avg_particle_dcs,
           round(avg(LFrameSynchrTime),1) as LFrameSynchrTime, round(avg(LogicThreadTime),1) as LogicThreadTime, 
           round(avg(SleepTime),1) as SleepTime, round(avg(PostFrameTime),1) as PostFrameTime,
           round(avg(avg_cpu),2) as avg_cpu, max(ctemp) as ctemp
        from %s dp
        left join deviceInfo dI on dp.device_id = dI.device_id 
        left join t_time_statistic tts on dp.task_id = tts.task_id
        where dI.device_id = '%s' and status = 1 
        group by dp.device_id, version
        order by date(min(dp.created_time)) desc, version desc limit %s;""" \
              % (self.table_name, device_id, count)
        result = MySQLHelper(return_type='dict').execute_query(sql)
        return result

    def get_version_pack(self):
        get_max_date_sql = "select distinct(date(created_time)) " \
                           "from %s " \
                           "order by date(created_time) desc limit 1;" \
                           % self.table_name
        last_date = str(MySQLHelper().execute_query(get_max_date_sql)[0][0])
        sql = "select distinct package_name, version " \
              "from %s " \
              "where created_time > '%s';" % (self.table_name, last_date)
        result = MySQLHelper(return_type='dict').execute_query(sql)

        package_info_list = []
        for r in result:
            get_package_size_sql = "select package_size from t_task_queue where package_name = '%s'" % r["package_name"]
            package_size = MySQLHelper().execute_query(get_package_size_sql)[0][0]
            package_size = int(package_size) / (1024 * 1024)
            package_info_list.append([r["package_name"], package_size])
        # print (result)
        # if len(result) == 2:
        #     package_name = result[0]['package_name'] + '; <br>' + '&nbsp;'*7 + result[1]['package_name']
        # elif len(result) == 1:
        #     package_name = result[0]['package_name']
        # else:
        #     package_name = ''
        # version = result[0]['version']
        return package_info_list

    def get_perf_data_by_id(self, device_id):
        get_date_list_sql = """select date(min(dpi.created_time)), 
                                round(avg(avg_fps),1), round(avg(mono_max_heap),1),
                                round(avg(fps_more_25),1), round(avg(jank_10m),1),
                                round(avg(avg_memory_MB),1), round(avg(draw_calls_avg),1),
                                round(avg(tts.loading_time),1), max(peak_memory_MB), 
                                round(avg(LFrameSynchrTime),1)
                                from %s as dpi
                                join t_time_statistic tts on dpi.task_id = tts.task_id
                                where device_id = '%s' and status = 1 
                                group by version
                                order by date(min(dpi.created_time)) desc, version desc
                                limit 30;""" % (self.table_name, device_id)

        result = MySQLHelper().execute_query(get_date_list_sql)
        return result

    def get_device_name(self, device_id):
        sql = "select device_name from deviceInfo " \
              "where device_id = '%s';" % device_id
        return MySQLHelper().execute_query(sql)[0][0]

    def draw_picture(self):
        png_list = []
        # 绘图系数，使各项指标在1张图里展示
        jank_coefficient = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 11: 1.25, }
        pss_coefficient = {1: 0.3, 2: 0.16, 3: 0.14, 4: 0.14, 5: 0.14, 11: 0.25}
        pss_peak_coefficient = {1: 0.3, 2: 0.16, 3: 0.15, 4: 0.15, 5: 0.15, 11: 0.2}
        dc_coefficient = {1: 1, 2: 1, 3: 0.8, 4: 0.6, 5: 0.6, 11: 1}
        mono_coefficient = {1: 0.7, 2: 0.5, 3: 0.5, 4: 0.6, 5: 0.5, 11: 0.5}
        for device in self.device_list:
            device_name = self.get_device_name(device)
            perf_data_list = self.get_perf_data_by_id(device)
            date_list, fps_list, pss_avg_mem, mono_max_heap_list, \
            jank_10m, dc_avg, loading_time_avg, peak_mem, frame_sync_list \
                = [], [], [], [], [], [], [], [], []
            device_level_dict = get_android_device_level_dict()
            device_level = device_level_dict[device] % 100

            for perf_data in reversed(perf_data_list):
                date_list.append(str(perf_data[0]).replace('-', ''))
                fps_list.append(float(perf_data[1]))
                pss_avg_mem.append(float(perf_data[5]) * pss_coefficient[device_level])
                mono_max_heap_list.append(float(perf_data[2]) * mono_coefficient[device_level])  # 乘以绘图系数
                jank_10m.append(float(perf_data[4]) * jank_coefficient[device_level])
                dc_avg.append(float(perf_data[6] * dc_coefficient[device_level] if perf_data[7] else 0))
                loading_time_avg.append(float(perf_data[7] if perf_data[7] else 0))
                peak_mem.append(float(perf_data[8]) * pss_peak_coefficient[device_level])
                frame_sync_list.append(float(perf_data[9] if perf_data[9] else 0))

            try:
                plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 设置字体，用来正常显示中文标签
                plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
                plt.rcParams['savefig.dpi'] = 200
                plt.figure().set_size_inches(12, 6)

                # date_list = [datetime.datetime.strptime(d, '%Y%m%d').date() for d in date_list]
                # date_list.sort()
                # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y%m%d'))
                # plt.gca().xaxis.set_major_locator(mdates.DayLocator())

                # fig = plt.figure()
                # ax = fig.add_subplot(1, 1, 1)
                # plt.xticks(range(len(date_list)), date_list, rotation=30)
                # X轴日期防止被转换为科学计数
                plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
                plt.gca().get_xaxis().get_major_formatter().set_scientific(False)

                plt.plot(date_list, fps_list, 'o-', color='red', label=u'平均帧率')
                plt.plot(date_list, pss_avg_mem, 'o-', color='black', label=u'PSS内存均值(MB)')
                plt.plot(date_list, jank_10m, 'o-', color='green', label=u'卡顿次数(10m)')
                plt.plot(date_list, loading_time_avg, 'o-', color='cyan', label=u'loading时间均值')
                # if not self.model == "pub":
                plt.plot(date_list, mono_max_heap_list, 'o-', color='blue', label=u'Mono堆内存峰值')
                plt.plot(date_list, dc_avg, 'o-', color='yellow', label=u'Draw call均值')
                if self.model == "trunk":
                    plt.plot(date_list, frame_sync_list, 'o-', color='magenta', label=u'FrameSync')
                # plt.plot(date_list, peak_mem, 'o-', color='magenta', label=u'PSS内存峰值')
                plt.ylim(0, 180)
                plt.gca().axes.get_yaxis().set_visible(False)  # 不显示Y轴信息

                plt.title(u"%s" % device_name)
                plt.xlabel(u"测试日期")
                plt.ylabel(u"指标值")
                plt.gcf().autofmt_xdate()  # 自动旋转日期标记

                for a, b in zip(date_list, fps_list):
                    plt.text(a, b, b, ha='center', va='bottom', fontsize=5)
                for a, b in zip(date_list, pss_avg_mem):
                    plt.text(a, b, b * 1 / pss_coefficient[device_level], ha='center', va='bottom', fontsize=5)
                for a, b in zip(date_list, jank_10m):
                    plt.text(a, b, b * 1 / jank_coefficient[device_level], ha='center', va='bottom', fontsize=5)
                for a, b in zip(date_list, loading_time_avg):
                    plt.text(a, b, b, ha='center', va='bottom', fontsize=5)
                for a, b in zip(date_list, mono_max_heap_list):
                    plt.text(a, b, b * 1 / mono_coefficient[device_level], ha='center', va='bottom', fontsize=5)
                for a, b in zip(date_list, dc_avg):
                    plt.text(a, b, b * 1 / dc_coefficient[device_level], ha='center', va='bottom', fontsize=5)
                if self.model == "trunk":
                    for a, b in zip(date_list, frame_sync_list):
                        plt.text(a, b, b, ha='center', va='bottom', fontsize=5)

                # for a, b in zip(date_list, peak_mem):
                #     plt.text(a, b, b * 1/pss_peak_coefficient[device], ha='center', va='bottom', fontsize=7)
                plt.legend(loc=0, prop={'size': 6})
                plt.savefig('sum_%s.png' % device)
                # plt.show()
                plt.clf()
                png_list.append('sum_%s.png' % device)
            except Exception as e:
                plt.clf()
                print ("draw picture error: %s" % e)
                continue

        # 在trunk报告中绘制包量曲线
        if self.model == 'trunk':
            android_apk_list = [float(x / 1024.0 / 1024 / 10) for x in get_package_size("android", "apk")]
            android_dlc_list = [x / 1024.0 / 1024 * 0.04 for x in get_package_size("android", "zip")]
            ios_ipa_list = [x / 1024.0 / 1024 / 10 for x in get_package_size("ios", "ipa")]
            ios_dlc_list = [x / 1024.0 / 1024 * 0.04 for x in get_package_size("ios", "zip")]

            # android_package_data = self.get_package_size('android')
            # ios_package_data = self.get_package_size('ios')
            # android_date, ios_date, android_package_size, ios_package_size = [], [], [], []
            # for data in android_package_data:
            #     android_date.append(data[1])
            #     android_package_size.append(round(data[0]/(1024*1024*20.0), 2))
            # for data in ios_package_data:
            #     ios_date.append(data[1])
            #     ios_package_size.append(round(data[0]/(1024*1024*25.0), 2))
            # print("android_package_size: %s, ios_package_size: %s" % (android_package_size, ios_package_size))

            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 设置字体，用来正常显示中文标签
            plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
            plt.rcParams['savefig.dpi'] = 300
            plt.figure().set_size_inches(12, 6)

            plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
            plt.gca().get_xaxis().get_major_formatter().set_scientific(False)

            plt.ylim(0, 100)
            plt.gca().axes.get_yaxis().set_visible(False)  # 不显示Y轴信息
            plt.gca().axes.get_xaxis().set_visible(False)
            plt.title(u"包体趋势图")
            # plt.xlabel(u"日期")
            plt.ylabel(u"包体大小(MB)")
            # plt.gcf().autofmt_xdate()  # 自动旋转日期标记

            plt.plot(range(len(android_apk_list)), android_apk_list, 'o-', color='red', label=u'android首包(MB)')
            plt.plot(range(len(android_apk_list)), android_dlc_list, 'o-', color='cyan', label=u'android DLC(MB)')
            plt.plot(range(len(ios_ipa_list)), ios_ipa_list, 'o-', color='green', label=u'IOS首包(MB)')
            plt.plot(range(len(ios_ipa_list)), ios_dlc_list, 'o-', color='blue', label=u'IOS DLC(MB)')
            for a, b in zip(range(len(android_apk_list)), android_apk_list):
                plt.text(a, b, round(b * 10, 2), ha='center', va='bottom', fontsize=7)
            for a, b in zip(range(len(android_apk_list)), android_dlc_list):
                plt.text(a, b, round(b / 0.04, 2), ha='center', va='bottom', fontsize=7)
            for a, b in zip(range(len(ios_ipa_list)), ios_ipa_list):
                plt.text(a, b, round(b * 10, 2), ha='center', va='bottom', fontsize=7)
            for a, b in zip(range(len(ios_ipa_list)), ios_dlc_list):
                plt.text(a, b, round(b / 0.04, 2), ha='center', va='bottom', fontsize=7)

            plt.legend(loc=0, prop={'size': 6})
            plt.savefig('package_size.png')
            # plt.show()
            plt.clf()
            png_list.append('package_size.png')
        return png_list

    def get_package_size(self, platform):
        sql = "select package_size, date(created_time) from t_task_queue " \
              "where platform = '%s' and model = '%s' and package_size IS NOT NULL " \
              "order by created_time desc limit 30;" % (platform, self.model)
        return MySQLHelper().execute_query(sql)

    def perf_data_compare(self):
        perf_summ = ""
        for device in self.device_list:
            # sql = """select dp.device_id, device_name, round(avg(avg_fps),2),
            #     round(avg(fps_more_18),2), round(avg(avg_memory_MB),2),
            #     date(min(created_time)), version
            #     from %s dp
            #     join deviceInfo dI on dp.device_id = dI.device_id
            #     where dp.device_id = '%s'
            #     group by version
            #     order by date(min(created_time)) desc limit 15;"""\
            #       % (self.table_name, device)
            # perf_data = MySQLHelper().execute_query(sql)
            perf_data = self.get_daily_perf_by_device(device, status_limit=1, count=15)
            if perf_data:
                n = len(perf_data)
                fps_total = loading_time_total = more_18_total = jank_10m_total = big_jank_10m_total = pss_avg_total = \
                    pss_max_total = mono_used_max_total = mono_heap_max_total = dc_total = cpu_total = 0
                for i in range(n):
                    fps_total += perf_data[i][3]
                    loading_time_total += perf_data[i][4]
                    more_18_total += perf_data[i][5]
                    jank_10m_total += perf_data[i][9]
                    big_jank_10m_total += perf_data[i][10]
                    pss_avg_total += perf_data[i][11]
                    pss_max_total += perf_data[i][12]
                    mono_used_max_total += perf_data[i][13]
                    mono_heap_max_total += perf_data[i][14]
                    dc_total += perf_data[i][16]
                    cpu_total += perf_data[i][27]

                # fps_bench =
                fps_diff = round(float(perf_data[0][3]) - float(fps_total / n), 2)
                # fps_diff = 0
                # loading_time_diff = round(float(perf_data[0][4]) - float(loading_time_total/n), 2)
                loading_time_diff = 0
                more_18_diff = round(float(perf_data[0][5]) - float(more_18_total / n), 2)
                jank_10m_diff = round(float(perf_data[0][9]) - float(jank_10m_total / n), 2)
                big_jank_10m_diff = float(perf_data[0][10]) - float(big_jank_10m_total / n)
                pss_avg_diff = (float(perf_data[0][11]) - float(pss_avg_total / n)) / float(pss_avg_total / n)
                # pss_avg_diff = 0
                mono_heap_max_diff = round((float(perf_data[0][14]) - float(mono_heap_max_total / n))
                                           / float(mono_heap_max_total / n), 2)
                # mono_heap_max_diff = 0
                dc_diff = round(float(perf_data[0][16]) - float(dc_total / n), 2)
                # dc_diff = 0
                cpu_diff = float(perf_data[0][27]) - float(cpu_total / n)
                if fps_diff > 1.2 or loading_time_diff < -2 or more_18_diff > 2 or jank_10m_diff < -5 \
                        or pss_avg_diff < -0.1 or mono_heap_max_diff < -0.1 or dc_diff < -5 or cpu_diff < -10:
                    perf_summ += "%s: " % perf_data[0][1]
                    if fps_diff > 1.2:
                        perf_summ += "平均FPS增加%s帧，" % abs(fps_diff)
                    if loading_time_diff < -2:
                        perf_summ += "loading时间减少%s秒，" % abs(loading_time_diff)
                    if more_18_diff > 2:
                        perf_summ += "帧率>18比例增加%s%%，" % abs(more_18_diff)
                    if jank_10m_diff < -5:
                        perf_summ += "10分钟卡顿数减少%s次，" % abs(jank_10m_diff)
                    if pss_avg_diff < -0.1:
                        perf_summ += "PSS内存均值降低%s%%，" % '{:.2f}'.format(abs(pss_avg_diff) * 100)
                    if mono_heap_max_diff < -0.1:
                        perf_summ += "mono堆内存峰值减少%s%%，" % (abs(mono_heap_max_diff) * 100)
                    if dc_diff < -5:
                        perf_summ += "draw call均值减少%s，" % abs(dc_diff)
                    if cpu_diff < -10:
                        perf_summ += "CPU使用减少%s%%，" % abs(cpu_diff)
                    perf_summ = "<font color=\"green\">" + perf_summ[:-1] \
                                + "。  </font>\r"
                if fps_diff <= -1.2 or loading_time_diff >= 2 or more_18_diff <= -2 or jank_10m_diff >= 5 \
                        or pss_avg_diff >= 0.1 or mono_heap_max_diff >= 0.1 or dc_diff >= 5 or cpu_diff >= 10:
                    perf_summ += "%s: " % perf_data[0][1]
                    if fps_diff <= -1.2:
                        perf_summ += "平均FPS降低%s帧，" % abs(fps_diff)
                    if loading_time_diff >= 2:
                        perf_summ += "loading时间增加%s秒，" % abs(loading_time_diff)
                    if more_18_diff <= -2:
                        perf_summ += "帧率>18比例减少%s%%，" % abs(more_18_diff)
                    if jank_10m_diff >= 5:
                        perf_summ += "10分钟卡顿数增加%s次，" % abs(jank_10m_diff)
                    if pss_avg_diff >= 0.1:
                        perf_summ += "PSS内存均值增加%s%%，" % '{:.2f}'.format(abs(pss_avg_diff) * 100)
                    if mono_heap_max_diff >= 0.1:
                        perf_summ += "mono堆内存峰值增加%s%%，" % (abs(mono_heap_max_diff) * 100)
                    if dc_diff >= 5:
                        perf_summ += "draw call均值增加%s，" % abs(dc_diff)
                    if cpu_diff >= 10:
                        perf_summ += "CPU使用增加%s%%，" % abs(cpu_diff)
                    perf_summ = "<font color=\"red\">" + perf_summ[:-1] \
                                + "。</font>\r"
                else:
                    continue

        if not perf_summ:
            perf_summ += "今日构建包在各级设备下，性能指标均正常。"
        return perf_summ

    def get_benchmark_by_device_id(self, device_id):
        sql = "select * from benchmark_performance_aov where device_id = '%s' and branch_name = '%s' " \
              "order by id desc limit 1;" % (device_id, self.model)
        benchmark_data = MySQLHelper(return_type='dict').execute_query(sql)
        if not benchmark_data:
            sql = "select * from benchmark_performance_aov where device_id = '%s' and branch_name = 'trunk' " \
                  "order by id desc limit 1;" % device_id
            benchmark_data = MySQLHelper(return_type='dict').execute_query(sql)
        if not benchmark_data:
            return None
        return benchmark_data[0]

    def benchmark_compare(self):
        if self.model == '3v3':
            return "各机型性能指标正常"
        kv_all = {'avg_fps': '平均帧率', 'loading_time': 'loading时间',
                  'fps_more_18': '帧率>18比例', 'fps_more_25': '帧率>25比例',
                  'var_fps': '帧率方差', 'ftime_more_100': '单帧>100ms比例',
                  'jank_10m': '卡顿次数(10m)', 'big_jank_10m': '严重卡顿次数(10m)',
                  'avg_memory_MB': 'PSS内存均值(MB)', 'peak_memory_MB': 'PSS内存峰值(MB)',
                  'mono_max_used': 'Mono已用内存峰值(MB)', 'mono_max_heap': 'Mono堆内存峰值(MB)',
                  'gc_count': 'GC次数', 'draw_calls_avg': 'Draw call均值',
                  'tris_avg': '三角形数均值', 'verts_avg': '顶点数均值',
                  'avg_ui_calls': 'UI_dc', 'avg_hud_calls': 'HUD_dc',
                  'avg_scene_calls': 'Secne_dc', 'avg_particle_dcs': 'Particle_dc',
                  'LFrameSynchrTime': 'FrameSync', 'LogicThreadTime': 'LogicThr',
                  'SleepTime': 'SleepTime', 'PostFrameTime': 'PostTime',
                  'avg_cpu': '平均CPU', 'ctemp': '最大温度'}

        kv_bench_check_name = {'avg_fps': '帧率', 'loading_time': 'loading时间',
                               'jank_10m': '卡顿次数(10m)', 'big_jank_10m': '严重卡顿次数(10m)',
                               'avg_memory_MB': 'PSS内存均值', 'peak_memory_MB': 'PSS内存峰值',
                               'mono_max_used': 'Mono已用峰值', 'mono_max_heap': 'Mono堆峰值',
                               'gc_count': 'GC次数', 'draw_calls_avg': 'Draw call均值',
                               # 'tris_avg': '三角形数均值', 'verts_avg': '顶点数均值',
                               'avg_cpu': 'CPU'}

        # 需要监控对比的性能指标
        check_key_list = ['avg_fps', 'loading_time', 'avg_cpu', 'avg_memory_MB',
                          'mono_max_used', 'mono_max_heap', 'gc_count', 'jank_10m', 'big_jank_10m',
                          'draw_calls_avg']
        if self.model == "pub":
            check_key_list.remove("loading_time")

        kv_bench_check_diff = {'avg_fps': -1, 'loading_time': 2,
                               'jank_10m': 5, 'big_jank_10m': 5,
                               'avg_memory_MB': 0.1, 'peak_memory_MB': 0.1,
                               'mono_max_used': 0.1, 'mono_max_heap': 0.1,
                               'gc_count': 3, 'draw_calls_avg': 5,
                               # 'tris_avg': 0.1, 'verts_avg': 0.1,
                               'avg_cpu': 10}

        # # 对比低端机数据
        # ios_6P_benchmark = self.get_benchmark_by_level(11)
        # lowest_benchmark = self.get_benchmark_by_level(1)
        # # print 'lowest_benchmark: %s' % lowest_benchmark
        # low_benchmark = self.get_benchmark_by_level(2)
        # middle_benchmark = self.get_benchmark_by_level(3)
        # high_benchmark = self.get_benchmark_by_level(4)
        # hd_benchmark = self.get_benchmark_by_level(5)
        # bench_device_kv = {'92010e74c4b8c295': lowest_benchmark, '32012153ed2c74d9': lowest_benchmark,
        #                    'SW5TMBBELR4SYLDM': low_benchmark, 'DYN6R20430003422': middle_benchmark,
        #                    'NJ5HS4SS4PCEFESC': high_benchmark, 'f1af3d624c00d5ac1e09aeac90770c5a2344bdd4': ios_6P_benchmark,
        #                    'JAAZGV160485Y83': hd_benchmark, }
        device_name = get_device_name_dict()
        bench_compare_result = ''

        # 对比
        for device in self.device_list:
            print("now handle device: %s" % device)
            device_compare_result = device_name[device] + '：'
            perf_data = self.get_daily_perf_by_device_dict(device, 1)[0]
            print perf_data
            for key in check_key_list:
                print 'handling key: %s' % key
                # time.sleep(3)
                bench_device = self.get_benchmark_by_device_id(device)
                if not bench_device:
                    continue
                bench_data = float(bench_device[key])
                diff = None
                if kv_bench_check_diff[key] >= 1:  # 说明指标增长时是性能下降
                    diff = float(perf_data[key]) - bench_data
                elif kv_bench_check_diff[key] <= -1:  # 说明指标降低时是性能下降
                    diff = perf_data[key] - bench_data
                elif 0 < kv_bench_check_diff[key] < 1:  # 说明按照百分比判断指标增长是否超标
                    diff = (perf_data[key] - bench_data) / bench_data
                elif -1 < kv_bench_check_diff[key] < 0:  # 说明按照百分比判断指标降低是否超标
                    diff = (perf_data[key] - bench_data) / bench_data

                if diff:
                    if kv_bench_check_diff[key] > 0:
                        if diff > kv_bench_check_diff[key]:
                            device_compare_result += '[%s] %s -> <font color=\"red\">%s</font>,' % (
                            kv_bench_check_name[key], bench_data, float(perf_data[key]))
                        elif diff < -kv_bench_check_diff[key]:
                            device_compare_result += '[%s] %s -> <font color=\"green\">%s</font>,' % (
                            kv_bench_check_name[key], bench_data, float(perf_data[key]))
                    elif kv_bench_check_diff[key] < 0:
                        if diff < kv_bench_check_diff[key]:
                            device_compare_result += '[%s] %s -> <font color=\"red\">%s</font>,' % (
                            kv_bench_check_name[key], bench_data, float(perf_data[key]))
                        if diff > -kv_bench_check_diff[key]:
                            device_compare_result += '[%s] %s -> <font color=\"green\">%s</font>,' % (
                            kv_bench_check_name[key], bench_data, float(perf_data[key]))
            if '->' in device_compare_result:
                bench_compare_result += "<li>%s</li>\r\n" % device_compare_result[:-1]

        if bench_compare_result:
            bench_compare_result = "<ul> %s </ul>" % bench_compare_result
        else:
            bench_compare_result = '各机型性能指标正常'
        return bench_compare_result


if __name__ == '__main__':
    compare_result_file_path = "E:\\workspace\\"

    test_model = "pub"  # optimize，battle, warmAI
    gh = GanerateReportHtml(test_model)
    # temp = gh.benchmark_compare()
    perf_picture = gh.draw_picture()
    time.sleep(60)
    # time.sleep(600)
    msg_to_debug = ['anselzhu@tencent.com']
    msg_to_formal = ['g_IEG_TiMi_TMJ6_AoV@tencent.com',
                     'g_IEG_TiMi_TMJ6_CoreTeam@tencent.com',
                     'g_IEG_TiMi_TMJ6_AoV_QATeam@tencent.com',
                     'ansonwu@tencent.com', 'oliverchu@tencent.com']
    # if test_model == "trunk":
    #     compare_filename = [os.path.join(compare_result_file_path, get_dlc_compare_result()[2])]
    # else:
    #     compare_filename = None
    attch_file_list = [
        "E:\\workspace\\aov_profiler_file\\profiler_%s_%s.zip" % (test_model, str(datetime.date.today()))]

    HtmlPath = gh.ganerate_html()

    while True:
        prompt = "please input send mail to who, formal or debug ? "
        message = raw_input(prompt)
        if message == 'formal':
            send_mail(HtmlPath, gh.title, msg_to_formal, perf_picture, attch_file_list)
            break
        elif message == 'debug':
            send_mail(HtmlPath, gh.title, msg_to_debug, perf_picture, attch_file_list)
        elif message == 'stop':
            print("exit.")
            break
        else:
            print ("input error, please input again.")
        # send_tips.send(perf_summ)
