#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : anselzhu
import re
import shutil
import sys
import os
import time
import random
import traceback
import datetime
import ConfigParser
from xlrd import open_workbook
from xlutils.copy import copy
from commons.const import *
from tools.gmCommands.gm_manager import *
from libs.wpyscripts.uiautomator import uiautomator_manager

sys.path.append("..\\..\\..\\wpyscripts_upload\\")

# usage = "usage:%prog [options] --qqname= --qqpwd= --engineport= --uiport= --serial="
# parser = optparse.OptionParser(usage)
# parser.add_option("-e", "--engineport", dest="LOCAL_ENGINE_PORT", help="network port forward engine sdk")
# parser.add_option("-u", "--uiport", dest="UIAUTOMATOR_PORT", help="network port forward uiautomator server")
# parser.add_option("-s", "--serial", dest="ANDROID_SERIAL", help="adb devices android mobile serial")
# parser.add_option("-g", "--othername", dest="OTHERNAME", help="upload account")
# parser.add_option("-f", "--otherpwd", dest="OTHERPWD", help="upload password")
# parser.add_option("-a", "--garenaname", dest="GARENANAME", help="garena Account")
# parser.add_option("-d", "--garenapassword", dest="GARENAPASSWORD", help="garena Password")
# (options, args) = parser.parse_args()
# if options.LOCAL_ENGINE_PORT:
#     os.environ["LOCAL_ENGINE_PORT"] = options.LOCAL_ENGINE_PORT
# if options.UIAUTOMATOR_PORT:
#     os.environ["UIAUTOMATOR_PORT"] = options.UIAUTOMATOR_PORT
# if options.ANDROID_SERIAL:
#     os.environ["ANDROID_SERIAL"] = options.ANDROID_SERIAL
# if options.GARENANAME:
#     os.environ["GARENANAME"] = options.GARENANAME
# if options.GARENANAME:
#     os.environ["GARENAPASSWORD"] = options.GARENAPASSWORD
#
# print ("options is: %s" % options)

from libs.wpyscripts import manager
from commons import util, handle_popup_window, loading, handle_game_over
from commons.util import find_elment_wait, find_elment_wait_new
from libs.wpyscripts.tools.baisc_operater import wait_for_scene, screen_shot_click, swipe_and_press_relative
from tools.gmCommands.gm_manager import startHeroLevelChange, startCreditValue, startCoinChange, startAutoAI, \
    setPVEComputerFull, setPVEComputerOption
from perfdog import autotest
from commons import login, env_prepare, select_servers, loading
from tools import data_handle, log
from tools.mysql_helper import MySQLHelper
from commons.const import get_android_device_level_dict, get_model_table_dict


# reload(sys)
# sys.setdefaultencoding('utf8')
logger = log.Logger().logger
engine = manager.get_engine()
report = manager.get_reporter()


def pve_perform(hero_skin_id, perf_data_path, test_round):
    """
    开始测试pve下的性能，进入对战后，开启perfdog录制，需从大厅开始进入
    测试完成后会强制kill游戏进程
    :param gm_comm: 本轮测试需要执行的GM命令列表
    :param perf_data_path:
    :param hero_skin_id: 本轮测试设置的英雄&皮肤id
    :return:
    """
    android_device_level_dict = get_android_device_level_dict()
    model_table_dict = get_model_table_dict()

    logger.debug("pve_5v5 performance test start ...")

    # 大厅-实时对战按钮
    entryPath = "/BootObj/CUIManager/Form_Lobby/BottomLayer/GameEntry/PVPBattle/click"
    # 开房间按钮
    openroomPath = "/BootObj/CUIManager/Form_PvPEntry/panelGroup1/btnGroup/RoomBtn"
    # 开房间-传说战场按钮
    legendPath = "/BootObj/CUIManager/Form_CreateRoom/Main/ScrollRectPanel/btnGroup/Button1"
    # 英雄选择确定按钮
    lockPath = "/BootObj/CUIManager/Form_HeroSelectNormal/btnConfirm/DynamicRes/dynamicHookTemplate/EnableButton"
    # 选择英雄界面-第一个英雄
    # if task_model != 'trunk' and task_model != 'battle':
    #     hero_path = "/BootObj/CUIManager/Form_HeroSelectNormal/PanelLeft/ListHostHeroInfo/ScrollRect/Content/ListElement_0/heroItemCell"
    # else:
    hero_path = "/BootObj/CUIManager/Form_HeroSelectNormal/PanelLeft/Left/ListHostHeroInfo/ScrollRect/Content/ListElement_0/heroItemCell"
    # pve开房间界面-开始游戏按钮
    matchBeginPath = "/BootObj/CUIManager/Form_Room/Panel_Main/Btn_Start/DynamicRes/dynamicHookTemplate" \
                           "/EnableButton"

    # 快速进入开房间
    if task_model == '3v3':
        engine.call_registered_handler("QucikPVERoom", "20002")
    else:
        engine.call_registered_handler("QucikPVERoom", "20011")
        engine.call_registered_handler("WeQucikPVERoom", "20011")  # 部分包可能用这个函数
    # 有超时+重试，等GM最终执行结果
    time.sleep(30)
    # 点击一下，关掉游客登录的提示框
    engine.click_position(300, 300)
    logger.debug("click (300,300)")
    # time.sleep(3)
    # 检测是否进入开房间界面成功
    if engine.find_element("/BootObj/CUIManager/Form_Room/Panel_Main/bg1/LeftRobot_Bg/RobotButton"):
        logger.debug("quick enter room success.")
        # 临时增加，按一下返回键
        # if task_model == "trunk":
        #     time.sleep(5)
        #     cmd = "adb -s %s shell input keyevent 4" % os.environ.get("ANDROID_SERIAL", None)
        #     os.popen(cmd)
    else:
        logger.error("GM QucikPVERoom failed, try enter step by step.")
        time.sleep(30000)
        # 加一个是否正在大厅的判断

        # 点击大厅的实时对战按钮
        i = 0
        while i < 5:
            if util.find_elment_wait(entryPath):
                btn = engine.find_element(entryPath)
                util.click_and_sleep(btn)
                logger.debug("click GameEntry/PVPBattle/click button")
                break
            else:
                i += 1
                # 尝试关闭弹窗
                manager.get_device().back()
                logger.error("cannot find entryPath, task restart !!!")
                if i == 4:
                    return False

        # 关闭首次进入的超魔斗场提示
        btn_right_path = "/BootObj/CUIManager/Form_BannerIntroDialog/Panel/BtnGroup/ButtonRight"
        if engine.find_element(btn_right_path):
            btn = engine.find_element(btn_right_path)
            engine.click(btn)
        chao_mo_path = "/BootObj/CUIManager/Form_BannerIntroDialog/Panel/BtnGroup/ButtonBottom/DynamicRes" \
                       "/dynamicHookTemplate/EnableButton"
        if util.find_elment_wait(chao_mo_path):
            btn = engine.find_element(chao_mo_path)
            util.click_and_sleep(btn)
            logger.debug("close ChaoMoDouChang button")

        # 点击开房间
        if util.find_elment_wait(openroomPath):
            btn1 = util.find_elment_wait(openroomPath)
            util.click_and_sleep(btn1)
            logger.debug("click OpenRoom button")
            # screen_shot_click(btn1)
        else:
            logger.error("cannot find openroomPath, task restart !!!!!!")
            return False

        # report.screenshotNew()
        time.sleep(3)
        # 点击第三层的经典竞技(传说战场)
        if util.find_elment_wait(legendPath):
            btn4 = util.find_elment_wait(legendPath)
            util.click_and_sleep(btn4)
            logger.debug("click legend fight button")
        else:
            logger.error("cannot find legendPath, task restart !!!")
            return False

    # 加入电脑玩家
    setPVEComputerFull()
    time.sleep(3)
    # 确保电脑玩家加入成功
    if engine.find_element("/BootObj/CUIManager/Form_Room/Panel_Main/bg1/LeftRobot_Bg/RobotButton"):
        btn1 = util.find_elment_wait("/BootObj/CUIManager/Form_Room/Panel_Main/bg1/LeftRobot_Bg/RobotButton")
        # util.click_and_sleep(btn1)
        # 多点几次，确保加满电脑玩家
        for x in range(6):
            screen_shot_click(btn1)
            logger.debug("click LeftRobot_Bg/RobotButton button")
    if engine.find_element("/BootObj/CUIManager/Form_Room/Panel_Main/bg2/RightRobot_Bg/RobotButton"):
        logger.debug("#wetest-log: enter the second levelPath success")
        btn1 = util.find_elment_wait("/BootObj/CUIManager/Form_Room/Panel_Main/bg2/RightRobot_Bg/RobotButton")
        # util.click_and_sleep(btn1)
        for x in range(7):
            screen_shot_click(btn1)
            logger.debug("click RightRobot_Bg/RobotButton button")
    # time.sleep(10)

    # 执行指定的局外GM命令
    if gm_comm[0]:
        engine.call_registered_handler(gm_comm[0], None)
        print("outside gm command : %s" % gm_comm[0])
        # time.sleep(60)

    if task_model in ['stateSync_trunk', 'stateSync']:
        set_state = engine.call_registered_handler("WeStateSetGameAcntStateSync", None)
        ds_test = engine.call_registered_handler("WeStateDsTest", None)
        logger.debug("execute stateSync command result: %s, %s" % (set_state, ds_test))

    if task_model in ['system_40']:
        ds_test1 = "系統綫開啓播報主題包"
        set_state1 = engine.call_registered_handler("WeSetBattleSystemVoiceTheme", 3)
        logger.debug("execute stateSync command result: %s, %s" % (set_state1, ds_test1))
        engine.call_registered_handler("WeSetBattleSystemVoiceTheme", "3")

    # 设置英雄&皮肤
    # inParam = "13300 11100 12000 15200 13500 13300 11100 12000 15200 13500"
    hero_skin_id = ' '.join(hero_skin_id.split())
    if len(hero_skin_id.split(" ")) == 10:
        inParam = hero_skin_id
    elif len(hero_skin_id.split(" ")) == 1:
        inParam = ((hero_skin_id + " ") * 10).strip()
        engine.call_registered_handler("StartSingleHero", None)
        logger.debug("has set StartSingleHero")
    else:
        logger.error("skin id param is error: %s" % hero_skin_id)
        return False
    logger.debug("appoint hero&skin id is  '%s'" % inParam)
    setPVEComputerOption(inParam)

    # 设置中路乱斗
    logger.debug("let all heros go middle ...")
    engine.call_registered_handler("FixedHeroRunMid", None)

    # 角色自动战斗
    startAutoAI()

    # 点击开始游戏，进入选择英雄界面
    if util.find_elment_wait(matchBeginPath):
        matchBtn = util.find_elment_wait(matchBeginPath)
        util.click_and_sleep(matchBtn)
        # util.click_and_sleep(matchBtn)
        logger.info("click matchBeginPath button end !!!")
    else:
        logger.error("cannot find matchBeginPath, task restart !!!")
        return False

    time.sleep(5)
    # engine.call_registered_handler("AppointHeroes", inParam)
    # report.screenshotNew()

    # 点击选择英雄，选择第一个就行
    if util.find_elment_wait(hero_path):
        logger.debug("#wetest-log: has enter hero select success")
        btn5 = util.find_elment_wait(hero_path)
        util.click_and_sleep(btn5)
        logger.debug("#wetest-log: has finish hero select %s" % str(util.find_elment_wait(lockPath)))
    # 等待1分钟，确保局内资源预加载完成
    logger.debug("sleep 10s, wait for load battle source")
    time.sleep(10)
    # 英雄选择完毕，点击确认，开始游戏
    if util.find_elment_wait(lockPath):
        logger.debug("#wetest-log: has finish hero select success")
        btn4 = util.find_elment_wait(lockPath)
        screen_shot_click(btn4)
        # util.click_and_sleep(btn4)
    else:
        logger.error("cannot find lockPath, task restart !!!")
        return False

    # 等待加载游戏
    loading_start_time = time.time()
    time.sleep(5)
    wait_N = 0
    # while engine.find_element("Form_Loading") and waitForLoadingN < 100:
    #     waitForLoadingN += 1
    #     logger.debug("#wetest-log: waitForLoadingN = %s" % str(waitForLoadingN))
    #     time.sleep(2)
    logger.debug("find element Form_Battle: %s, current scene: %s, wait_N: %s"
                 % (engine.find_element("Form_Battle"), engine.get_scene(), wait_N))
    while engine.find_element("Form_Battle") is None and wait_N < 100:
        wait_N += 1
        # logger.debug("#wetest-log: waiting for enter battle, wait times= %s" % str(wait_N))
        time.sleep(2)

    # 判断是否已正常进入战场
    atk_path = "/BootObj/CUIManager/Form_Battle_Part_SkillBtn/AtkSkill/AtkBtn"
    if engine.find_element("Form_Battle") and engine.find_element(atk_path):
        loading_end_time = time.time()
        logger.info("had enter battle success")
        loading_time_old = loading_end_time - loading_start_time

        # 获取loading时间
        loading_time_new = get_battle_loading()
        # 如果=-1，则多次尝试获取
        for i in range(10):
            if loading_time_new == '-1':
                logger.debug("get battle loading is -1, try again...")
                time.sleep(0.5)
                loading_time_new = get_battle_loading()
            else:
                break
        if loading_time_new is None or loading_time_new == '-1':
            battle_loading = loading_time_old
        else:
            battle_loading = loading_time_new
        logger.error("loading_time_old: %s, loading_time_new: %s" % (loading_time_old, loading_time_new))

        sql = "update t_time_statistic set loading_time = '%s' " \
              "where task_id = '%s'; " % (battle_loading, task_id)
        MySQLHelper().execute_no_query(sql)
        time.sleep(3)

        # 执行指定局内GM命令
        if gm_comm[1]:
            engine.call_registered_handler(gm_comm[1], None)
            logger.debug("inside gm command: %s, execute success ..." % gm_comm[1])

        # ！！！！！！！开启perfdog
        logger.debug("perfdog start ...")
        # now = int(round(time.time() * 1000))
        # timestamp = time.strftime('%m%d%H%M%S', time.localtime(now / 1000))
        # case_name = "%s_%s_%s" % (task_id, device_uid, timestamp)
        # perfdog 记录性能数据
        case_name = autotest.run(task_id, task_model, perf_data_path, perfdog_token, pve_fighting_time, test_round)
        if not case_name:
            return False  # 本局测试不算
        # 获取战场5分钟状态值
        frame_hash = engine.call_registered_handler("GetLogicFrameHash", None)

        # 生成profiler文件
        engine.call_registered_handler("SetActiveProfiler", "false")

        # 获取单局结束数据
        gc_count = engine.call_registered_handler("GetBattleGCCollectCount", None)
        logger.debug("GetBattleGCCollectCount: %s" % gc_count)

        LogicThreadTime = engine.call_registered_handler("GetLogicFrameTime", "LogicThreadTime")
        logger.debug("LogicThreadTime: %s" % LogicThreadTime)
        SleepTime = engine.call_registered_handler("GetLogicFrameTime", "SleepTime")
        logger.debug("SleepTime: %s" % SleepTime)
        PostFrameTime = engine.call_registered_handler("GetLogicFrameTime", "PostFrameTime")
        logger.debug("PostFrameTime: %s" % PostFrameTime)
        LFrameSynchrTime = engine.call_registered_handler("GetLogicFrameTime", "LFrameSynchrTime")
        logger.debug("LFrameSynchrTime: %s" % LFrameSynchrTime)

        # 数据回写excel并写入数据库
        insert_db("%s%s.xlsx" % (perf_data_path, case_name))

        # 数据自动校验1：检查FPS、卡顿与基准的差值
        try:
            bench_sql = "select avg_fps, jank_10m from benchmark_performance_aov where device_level = '%s' " \
                        "and branch_name='trunk' order by id desc limit 1;" % android_device_level_dict[device_uid]
            res0 = MySQLHelper().execute_query(bench_sql)
            bench_fps, bench_jank = res0[0][0], res0[0][1]
            logger.debug("bench_fps: %s, bench_jank: %s" % (bench_fps, bench_jank))

            get_sql = "select avg_fps, jank_10m from %s where task_id='%s'" % (model_table_dict[task_model], task_id)
            res1 = MySQLHelper().execute_query(get_sql)
            fps, jank = res1[0][0], res1[0][1]
            logger.debug("test result check: fps[%s], jank[%s]" % (fps, jank))

            if float(bench_fps) - float(fps) > 10 or float(jank) > 50:
                sql = "update %s set status = 0 where task_id = '%s'" % (table_name, task_id)
                MySQLHelper().execute_no_query(sql)
        except KeyError:
            logger.debug("there isn't [%s], don't check data. " % device_uid)

        # 更新LogicFrameHash值
        if frame_hash:
            sql = "update %s set LogicFrameHash = '%s' where task_id = '%s'" % (table_name, frame_hash, task_id)
            MySQLHelper().execute_no_query(sql)
        else:
            # 数据自动校验2：检查LogicFrameHash值是否为null
            logger.debug("LogicFrameHash is null, update status=0 ")
            sql = "update %s set status = 0 where task_id = '%s'" % (table_name, task_id)
            MySQLHelper().execute_no_query(sql)
        # 更新逻辑线程开销
        if LogicThreadTime and LFrameSynchrTime:
            sql = "update %s set LogicThreadTime = '%s', SleepTime = '%s'," \
                  "PostFrameTime = '%s', LFrameSynchrTime = '%s' " \
                  "where task_id = '%s'" \
                  % (table_name, LogicThreadTime, SleepTime, PostFrameTime,
                     LFrameSynchrTime, task_id)
            MySQLHelper().execute_no_query(sql)
        # 更新GC次数
        if gc_count:
            sql = "update %s set gc_count = '%s' where task_id = '%s'" % (table_name, gc_count, task_id)
            MySQLHelper().execute_no_query(sql)
        # 手动退出本局，并计算结算时间
        setting_path = "/BootObj/CUIManager/Form_Battle/PanelBtn/MenuBtn"
        exit_path = "/BootObj/CUIManager/Form_Settings_Battle/OpSettingDynamic/OpSetting_Battle/ExitBattle/Button_ExitLog"
        #"/BootObj/CUIManager/Form_Settings_Battle/OpSettingDynamic/OpSetting_Battle/ExitBattle/Button_ExitLog"

        if util.find_elment_wait(setting_path):
            setting_btn = find_elment_wait(setting_path)
            screen_shot_click(setting_btn)
            exit_btn = util.find_elment_wait(exit_path)
            if exit_btn:
                screen_shot_click(exit_btn)
                # exit_start_time = time.time()
                #
                # exit_end_time = time.time()
                # settlement_time = exit_end_time - exit_start_time
                # logger.info("#time#settlement_time: %d " % settlement_time)
                time.sleep(5)
                util.click_and_sleep_relative(0.5, 0.5)
        #device_uid = os.environ["ANDROID_SERIAL"]
        #if device_uid == "92012180ace233c7":
            #click_cmd1 = "adb -s %s shell input tap 706 349" % device_uid
            #os.popen(click_cmd1)
            #logger.debug("@xinhxing: 在點OK1")
        #if device_uid == "33002f67e639c377":
            #click_cmd2 = "adb -s %s shell input tap 1385 661" % device_uid
            #os.popen(click_cmd2)
            #logger.debug("@xinhxing: 在點OK2")
        #if device_uid == "4fbbc3f7":
            #click_cmd3 = "adb -s %s shell input tap 1385 661" % device_uid
            #os.popen(click_cmd3)
            #logger.debug("@xinhxing: 在點OK3")
        #if device_uid == "04945259BT009920":
            #click_cmd4 = "adb -s %s shell input tap 1093 457" % device_uid
            #os.popen(click_cmd4)
            #logger.debug("@xinhxing: 在點OK4")
        #if device_uid == "J9AZGV030205PAG":
            #click_cmd5 = "adb -s %s shell input tap 1512 674" % device_uid
            #os.popen(click_cmd5)
            #logger.debug("@xinhxing: 在點OK5")
                time.sleep(5)

        # perfdog录制完成，清理环境
        device = manager.get_device()
        ngame_package = os.environ.get("PKGNAME", "com.garena.game.kgcn")
        device.force_stop_app(ngame_package)
        device.force_stop_app("com.garena.gas")
        # device._clear_user_info(ngame_package)
        # device._clear_user_info("com.garena.gas")
        logger.debug("complete one round test, clean environment success ...")
        return True
    else:
        logger.error("enter battle failed, please check !!!")
        return False


def do_login():
    try:
        # 环境初始化
        # todo(phi): 检查准备的执行情况
        prepareResult = env_prepare._prepare()
        startup_start_time = time.time()

        if not prepareResult:
            logger.debug("Connect to sdk fail,please config your game contain sdk or not in the first scene")
            return False
        else:
            logger.debug("@phiwu: prepare done~")
            loading_result = loading.waiting_lauching()
            if not loading_result:
                return False
            if loading_result == 2:
                return True
            # 获取启动loading时间
            logger.debug("@phiwu: prepare done~~~")
            for i in range(10):
                if get_startup_loading() == '-1':
                    logger.debug("cannot get startup loading time, %s times retry..." % i)
                    time.sleep(0.5)
                else:
                    break
            startup_time = 0 if get_startup_loading() is None else get_startup_loading()
            logger.info("get_startup_loading time: %s" % startup_time)
            sql = "insert into t_time_statistic (task_id, startup_time) " \
                  "values ('%s', '%s');" % (task_id, startup_time)
            MySQLHelper().execute_no_query(sql)

            for i in range(10):
                env_prepare.check_allow_or_back_button()
            time.sleep(5)
            #uiauto = uiautomator_manager.get_uiautomator()
            #OKByt = uiauto(resourceId="android:id/button1")
            #if OKByt and OKByt.exists:
                #logger.debug("Click OKByt Button")
                #OKByt.click.wait()
            #click_cmd = ""
            #if device_uid == "32012153ed2c74d9":
                #click_cmd = "adb -s %s shell input tap 706 349" % device_uid
            #if device_uid == "92012180ace233c7":
                #click_cmd = "adb -s %s shell input tap 706 349" % device_uid
                #logger.debug("@xinhxing: 在點OK")
            #if device_uid == "92010e74c4b8c295":
                #click_cmd = "adb -s %s shell input tap 690 360" % device_uid
            #os.popen(click_cmd)
            #click_cmd1 = "adb -s 92012180ace233c7 shell input tap 706 349"
            #os.popen(click_cmd1)
            #logger.debug("@xinhxing: 在點OK1")

            # 游客登录
            guest = engine.find_element("/BootObj/CUIManager/Form_Login/pnlGarenaLogin/LoginBtn/GuestLogin")
            if guest:
                login.login_guest()
            logger.debug("guest login end ...")

            # 关闭 公告通知
            close = engine.find_element("/BootObj/CUIManager/Form_EmergencyNotice/Panel_Announcement/CommonButtonTemplate/DynamicRes/dynamicHookTemplate/EnableButton")
            if close:
                screen_shot_click(close)

            # 选择测试服务器
            select_servers.select_sections(task_model)
            login_start_time = time.time()
            logger.debug("select server end ...")
            ok_btn = "/BootObj/CUIManager/Form_LockArea/Panel/Panel/btnGroup/Button_Confirm/DynamicRes/dynamicHookTemplate/EnableButton"
            ok_btn1 = engine.find_element(ok_btn)
            if ok_btn1 and util.is_touchable(ok_btn1):
                logger.debug("@xinhxing: find ok_byt...")
                screen_shot_click(ok_btn)
                time.sleep(5)
                screen_shot_click(ok_btn)
            time.sleep(10)  # 确保进入到下一个界面

            # 如果需要创建角色
            scene = engine.get_scene()
            if scene == "CreateRoleScene":
                logger.info("need create role...")
                while engine.find_element("Form_RoleCreate/startButton"):
                    randomName = engine.find_element("Button_RandomName")
                    if util.is_touchable(randomName):
                        screen_shot_click(randomName)
                        logger.debug("#wetest-log: Click Button %s" % randomName)
                        # a = "/BootObj/CUIManager/Form_RoleCreate/startButton/DynamicRes/dynamicHookTemplate/EnableButton"
                        # startBtn = engine.find_element("Form_RoleCreate/startButton")
                        startBtn = engine.find_element("EnableButton")
                        if util.is_touchable(startBtn):
                            util.click_and_sleep(startBtn)
                            login_start_time = time.time()
                            time.sleep(10)
            # 如果需要过新手
            toggle_element = engine.find_element('/BootObj/CUIManager/Form_GameDifficultSelect/ToggleGroup/Toggle3')
            if toggle_element:
                screen_shot_click(toggle_element)
                time.sleep(3)
                enable_element = engine.find_element('/BootObj/CUIManager/Form_GameDifficultSelect/ConfirmBtn/DynamicRes/dynamicHookTemplate/EnableButton')
                screen_shot_click(enable_element)
            enter_game = wait_for_scene("LobbyScene", 120, 0.5)
            login_end_time = time.time()
            if not enter_game:
                logger.error("enter game failed. please check the server status.")
                return False
            login_time = login_end_time - login_start_time
            logger.info("enter game success! ")
            logger.info("#time statistic# login_time: %d" % login_time)
            sql = "update t_time_statistic set login_time = '%s' " \
                  "where task_id = '%s'; " % (login_time, task_id)
            MySQLHelper().execute_no_query(sql)

            # 退出权限提示
            os.popen("adb -s %s shell input keyevent 4" % device_uid)
            time.sleep(20)

            logger.debug("login end.")
            return True

            # 处理大厅弹窗
            # handle_popup_window.handle_daily_promotion_window()

            # 开始pve测试
            # return pve_perform(hero_skin_id, perf_data_path)
    except Exception as e:
        traceback.print_exc()
        # report.screenshot()
        stack = traceback.format1_exc()
        logger.error(stack)
        return False


def perf_data_sum(source_path, target_path):
    """
    汇总所有perfdog生成的文件
    :param source_path: 原perfdog数据文件存放路径，为上一级路径
    :param target_path: 汇总excel的绝对路径
    :return:
    """
    if os.path.exists(target_path):
        try:
            os.rename(target_path, target_path + ".bak")
        except OSError:
            logger.error("ERROR: file has been opened or bak file is exist")

    sum_file = data_handle.ExcelWrite(target_path)

    files = os.listdir(source_path)
    logger.info("source_path file list is %s" % files)
    if files:
        x = 0
        for f in files:
            # if os.path.splitext(f)[-1] == ".xlsx" or os.path.splitext(f)[-1] == ".xls":
            if str(f).endswith(('.xlsx', '.xls')) and not str(f).startswith('~$'):
                logger.debug("now handling file: %s" % f)
                f_path = source_path + "\\" + f
                perf_data = data_handle.ExcelRead(f_path)
                # task_data = data_handle.ExcelRead(task_excel_path)
                sum_content = []

                # task_id = f.split("_")[0]
                timestamp = perf_data.get_cell_value(0, 0)
                # 获取平均温度
                ctemp = 0
                temp = perf_data.get_col_value(14)
                for y in range(len(temp)):
                    if temp[y] == "CTemp(℃)":
                        ctemp = temp[y + 1]

                # 文件名称即为task_id
                file_name = f.split(".")[0]
                logger.debug("get task_id: %s, timestamp: %s, avg CTemp(℃): %s"
                             % (file_name, timestamp, ctemp))
                # 根据task_id获取task_desc
                sql = "select task_desc from t_task_info where task_id = '%s';" % file_name
                r = MySQLHelper().execute_query(sql)
                if r:
                    task_desc = r[0][0]
                else:
                    task_desc = ""

                value_content = [file_name, task_desc, timestamp, package_name, version,
                                 perf_data.get_cell_value(4, 0), ctemp]
                value_content += perf_data.get_row_value(8)
                # 第一次插入时需要title信息
                if x == 0:
                    title_content = ["taskId", "task_desc", "timestamp", "package_name", "version",
                                     perf_data.get_cell_value(3, 0), "CTemp(℃)"]
                    # title.append(device)
                    title_content += perf_data.get_row_value(7)
                    sum_content.append(title_content)
                    print ("sum content is: %s" % sum_content)
                    x += 1

                sum_content.append(value_content)
                sum_file.add_content(sum_content)
        sum_file.write_now()
    else:
        print ("no files!!!!!")


def insert_db(data_path):
    # task_id = "etPP!weSUFl2@5iwmx4L"
    # write_db = True
    # package_name = "NGame_Garena_Global_Dev_202103230120_Beta31_B0001_dev_CHS_Standard_Global_1.40.1.1_r522810_E2113_AIO.signed.shell.apk"
    # device_uid = "4200f660a884b42d"
    # version = "主干日构建_r522810"
    # table_name = "t_trunk_performance_info"
    try:
        # 先读取excel内容，后面要重命名文件
        perf_excel = data_handle.ExcelRead(data_path)
        # 从DB中获取mono内存
        mono_sql = "select max(used_mem_MB), max(heap_mem_MB) from mono_mem_info " \
                   "where task_id='%s';" % task_id
        mono_info = MySQLHelper().execute_query(mono_sql)

        rendering_sql = "select round(avg(draw_calls),2), max(draw_calls), round(avg(tris),2), " \
                        "max(tris), round(avg(verts),2), max(verts), round(avg(ui_dcs),2)," \
                        "round(avg(hud_dcs),2),round(avg(scene_dcs),2),round(avg(particle_dcs),2)" \
                        "from rendering_statistics_info " \
                        "where task_id ='%s';" % task_id
        rendering_info = MySQLHelper().execute_query(rendering_sql)

        # 将mono数据及渲染指标数据回写到perfdog导出的excel中
        rexcel = open_workbook(data_path)
        excel = copy(rexcel)
        table = excel.get_sheet(0)
        table.write(7, 17, "mono_max_used(MB)")
        table.write(7, 18, "mono_max_heap(MB)")
        table.write(7, 19, "avg_draw_calls")
        table.write(7, 20, "max_draw_calls")
        table.write(7, 21, "avg_tris")
        table.write(7, 22, "max_tris")
        table.write(7, 23, "avg_verts")
        table.write(7, 24, "max_verts")
        table.write(8, 17, mono_info[0][0])
        table.write(8, 18, mono_info[0][1])
        table.write(8, 19, rendering_info[0][0])
        table.write(8, 20, rendering_info[0][1])
        table.write(8, 21, rendering_info[0][2])
        table.write(8, 22, rendering_info[0][3])
        table.write(8, 23, rendering_info[0][4])
        table.write(8, 24, rendering_info[0][5])
        excel.save(data_path[:-1])
        # os.rename(data_path, data_path + ".bak")

        # 判断是否需要写入performance_info表
        if write_db:
            values = [task_id, package_name, device_uid, version.decode('utf-8')]
            perf_values = perf_excel.get_row_value(8)[:23]
            logger.debug("get perf data from excel: %s" % perf_values)
            # perfdog service新加入的一些指标，不需要的先删掉，不然会造成入库数据错乱，后面有时间换成更智能的方式。。。
            del perf_values[7:10]
            del perf_values[15:18]
            logger.debug("delete useless data: %s" % perf_values)

            values += perf_values

            values.append(mono_info[0][0])
            values.append(mono_info[0][1])
            for i in range(10):
                values.append(rendering_info[0][i])

            # 获取平均温度
            ctemp = 0
            max_row = perf_excel.get_max_row()
            summ_row = perf_excel.get_row_value(max_row - 3)
            logger.debug("max row: %s, summ_row: %s" % (max_row, summ_row))
            # temp = perf_excel.get_col_value(14)
            for y in range(len(summ_row)):
                if summ_row[y] == "CTemp(℃)":
                    ctemp = perf_excel.get_cell_value(max_row-1, y)
            values.append(ctemp)

            sql_value = ""
            for v in values:
                v = "'%s'," % v
                sql_value += v

            sql = """insert into %s (task_id, package_name, device_id, version, avg_fps, 
                fps_more_18, fps_more_25, var_fps, drop_fps_h, jank_10m, big_jank_10m, ftime_more_100, 
                delta_ftime_more_100_hour, avg_memory_MB, peak_memory_MB, peak_mem_swap_MB, avg_cpu, cpu_less_60, 
                cpu_less_80, recv_send_s, recv_send_10m, mono_max_used, mono_max_heap, draw_calls_avg, 
                draw_calls_max, tris_avg, tris_max, verts_avg, verts_max, avg_ui_calls, avg_hud_calls, 
                avg_scene_calls, avg_particle_dcs, ctemp, created_time) 
                VALUES (%s CURRENT_TIMESTAMP);""" % (table_name, sql_value)
            logger.info("sql: %s" % sql)

            result = MySQLHelper().execute_no_query(sql)
            if result > 0:
                logger.debug("write DB success!")
            else:
                logger.debug("write DB error!")
    except Exception as e:
        logger.error("insert_db error: %s" % e)


def profiler_file_handle():
    logger.debug("from device [%s] pull profiler file" % device_uid)
    profiler_file_path = "E:\\workspace\\aov_profiler_file\\%s" % device_uid
    if os.path.exists(profiler_file_path):
        shutil.rmtree(profiler_file_path)

    os.makedirs(profiler_file_path)

    if device_uid == "92010545841513cb":
        #pull_cmd = "adb -s %s pull /storage/emulated/0/Android/data/Perf %s" % (device_uid, profiler_file_path)
        pull_cmd = "adb -s %s pull /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf %s" % (device_uid, profiler_file_path)
        #rm_cmd = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/Perf" % device_uid
        rm_cmd = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf" % device_uid
        #pull_cmd = "adb -s %s pull /sdcard/Android/data/Perf %s" % (device_uid, profiler_file_path)
        pull_cmd1 = "adb -s %s pull /sdcard/Android/data/com.garena.game.kgcn/files/Perf %s" % (device_uid, profiler_file_path)
        #rm_cmd = "adb -s %s shell rm -rf //sdcard/Android/data/Perf" % device_uid
        rm_cmd1 = "adb -s %s shell rm -rf sdcard/Android/data/com.garena.game.kgcn/files/Perf" % device_uid
    elif device_uid == "4fbbc3f7":
        #pull_cmd = "adb -s %s pull /storage/emulated/0/Android/data/Perf %s" % (device_uid, profiler_file_path)
        #pull_cmd1 = "adb -s %s pull /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf %s" % (device_uid, profiler_file_path)
        #rm_cmd = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/Perf" % device_uid
        #rm_cmd1 = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf" % device_uid
        pull_cmd = "adb -s %s pull /sdcard/Android/data/Perf %s" % (device_uid, profiler_file_path)
        pull_cmd1 = "adb -s %s pull /sdcard/Android/data/com.garena.game.kgcn/files/Perf %s" % (device_uid, profiler_file_path)
        rm_cmd = "adb -s %s shell rm -rf //sdcard/Android/data/Perf" % device_uid
        rm_cmd1 = "adb -s %s shell rm -rf sdcard/Android/data/com.garena.game.kgcn/files/Perf" % device_uid
    elif device_uid == "04945259BT009920":
        # pull_cmd = "adb -s %s pull /storage/emulated/0/Android/data/Perf %s" % (device_uid, profiler_file_path)
        # pull_cmd1 = "adb -s %s pull /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf %s" % (device_uid, profiler_file_path)
        # rm_cmd = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/Perf" % device_uid
        # rm_cmd1 = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf" % device_uid
        pull_cmd = "adb -s %s pull /sdcard/Android/data/Perf %s" % (device_uid, profiler_file_path)
        pull_cmd1 = "adb -s %s pull /sdcard/Android/data/com.garena.game.kgcn/files/Perf %s" % (device_uid, profiler_file_path)
        rm_cmd = "adb -s %s shell rm -rf //sdcard/Android/data/Perf" % device_uid
        rm_cmd1 = "adb -s %s shell rm -rf sdcard/Android/data/com.garena.game.kgcn/files/Perf" % device_uid
    elif device_uid == "J9AZGV030205PAG":
        pull_cmd = "adb -s %s pull /storage/emulated/0/Android/data/Perf %s" % (device_uid, profiler_file_path)
        pull_cmd1 = "adb -s %s pull /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf %s" % (device_uid, profiler_file_path)
        rm_cmd = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/Perf" % device_uid
        rm_cmd1 = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf" % device_uid
    else:
        pull_cmd = "adb -s %s pull /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf/ %s" % (device_uid, profiler_file_path)
        pull_cmd1 = "adb -s %s pull /storage/sdcard0/Android/data/com.garena.game.kgcn/files/Perf/ %s" % (device_uid, profiler_file_path)
        rm_cmd = "adb -s %s shell rm -rf /storage/emulated/0/Android/data/com.garena.game.kgcn/files/Perf/" % device_uid
        rm_cmd1 = "adb -s %s shell rm -rf /storage/sdcard0/Android/data/com.garena.game.kgcn/files/Perf/" % device_uid

    logger.debug("execute pull cmd: %s" % pull_cmd)
    os.popen(pull_cmd)
    os.popen(pull_cmd1)
    time.sleep(5)
    logger.debug("execute remove cmd: %s" % rm_cmd)
    os.popen(rm_cmd)
    os.popen(rm_cmd1)


def main(task_info):
    model_table_dict = get_model_table_dict()
    # 从pve_performance.ini中读取任务参数
    config = ConfigParser.ConfigParser()
    config.read('pve_performance.ini')
    perfdog_token = config.get("perfdog", "token")
    root_path = config.get("perfdog", "export_path")
    task_excel_path = config.get("path", "task_excel_path")
    print "@phiwu task_excel_path:", task_excel_path
    pve_fighting_time = int(config.get("time", "pve_fighting"))
    logger.debug("task_excel_path: %s, perfdog export path: %s, perfdog account: %s"
                 % (task_excel_path, root_path, perfdog_token))
    if task_info:
        task_model = task_info[1]
        package_name = task_info[3]
        table_name = model_table_dict[task_model]
        version = task_info[5]
    else:
        table_name = "daily_performance_info"
        task_model = "temp"
        package_name = None
        version = ""

    try:
        write_db = True if config.get("mysql", "enable").lower() == "true" else False
        logger.info("get write db config: %s" % write_db)
    except Exception:
        write_db = False
        logger.info("do not write DB !!")

    global table_name, perfdog_token, pve_fighting_time, write_db, version, package_name, task_model

    # 从任务excel中读取任务参数
    if not task_excel_path:
        logger.error("task_excel_path is null")
        sys.exit(0)
    excel = data_handle.ExcelRead(task_excel_path)

    task_descs = excel.get_col_value(0)[2:]
    skin_ids = excel.get_col_value(1)[2:]
    gms_out = excel.get_col_value(2)[2:]
    gms_in = excel.get_col_value(3)[2:]
    count_list = excel.get_col_value(4)[2:]
    status_list = excel.get_col_value(5)[2:]
    task_name = excel.get_cell_value(0, 0)

    # now = int(round(time.time() * 1000))
    # day_sign = time.strftime('%Y%m%d', time.localtime(now / 1000))
    device_uid = os.environ["ANDROID_SERIAL"]
    local_perf_path = root_path + str(datetime.date.today()) + "\\" + device_uid + "\\"
    folder = os.path.exists(local_perf_path)
    if not folder:
        for retry in range(100):
            try:
                os.makedirs(local_perf_path)
                break
            except IOError as e:
                logger.error("IO error: {0}".format(e))
                logger.error("makedir failed, retrying ...")
    # time_sign = time.strftime('%Y%m%d%H%M%S', time.localtime(now / 1000))
    logger.debug("test skin ids is: %s, count is %s" % (skin_ids, len(skin_ids)))

    for x in range(len(skin_ids)):
        # for x in range(3):
        task_desc = str(task_descs[x])
        skin_id = str(skin_ids[x]).replace(u"\xa0", u" ")
        print "@phiwu status:", status_list[x], type(status_list[x])
        status = int(status_list[x])
        count = int(count_list[x])
        gm_comm = [gms_out[x], gms_in[x]]

        global device_uid, gm_comm
        logger.info("%s time(s) test, skin id: %s, gm_comm: %s" % (x, skin_id, gm_comm))
        # time.sleep(10)
        # if False:
        if status == 1:
            logger.info("skinid: %s , test rounds: %s, GM command: %s" % (skin_id, count, gm_comm))
            suc_task_list = []

            for i in range(count):
                task_id = get_random_id()
                logger.info("task id is: %s" % task_id)
                global task_id
                # 入库task详细信息
                sql = "insert into t_task_info (task_id, task_desc, device_id, skin_id, gm_comm, task_status)" \
                      "values ('%s', '%s', '%s', '%s', '%s', 0);" \
                      % (task_id, task_desc, device_uid, skin_id, " ".join(gm_comm))
                MySQLHelper().execute_no_query(sql)

                retry = 0
                while retry < 3:
                    logger.info("%s rounds test, %s times try" % (i + 1, retry + 1))
                    login_result = do_login()
                    if login_result:
                        logger.debug("login success")
                        pve_result = pve_perform(skin_id, local_perf_path, i)
                        if pve_result:
                            suc_task_list.append(task_id)
                            break
                        else:
                            logger.error("pve test failed!!")
                            retry += 1
                    else:
                        logger.error("login failed!! retry")
                        retry += 1
                if i < count - 1:
                    test_interval = int(config.get("time", "pve_interval"))
                    logger.info("pve test one round end, sleep %s seconds" % test_interval)
                    time.sleep(test_interval)
                else:
                    # 这里是否可以加自动校验的
                    logger.info("task test end.")
    # 测试完成，拉取profiler文件到指定位置
    profiler_file_handle()

    # 上报数据到GPM
    from gpm_sdk.gpm_upload import gpm_upload
    new_version = version.split('_')[1]
    #new_version = version.split('_')[1]al_perf_path, suc_task_list)

    #gpm_upload(device_uid, task_model, package_name, new_version, loc)
    gpm_upload(device_uid, task_model, package_name, new_version, local_perf_path, suc_task_list)

# 生成20位随机串
def get_random_id():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&()_+=-"
    sa = []
    for i in range(20):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    # print (salt)
    return salt


if __name__ == '__main__':
    pass
