import requests
from bs4 import BeautifulSoup
import json
import os
import shutil
import sys
import datetime
import time
import math
import copy
import re
from logging.handlers import TimedRotatingFileHandler
import logging
from QtDailyReportMainWindow import Ui_MainWindow  # 導入轉換後的 UI 類
from QtCreateProjectDialog import Ui_Dialog as Ui_CreateProjectDialog
from QtDailyReportPerDayDialog import Ui_Dialog as Ui_DailyReportPerDayDialog
from QtSelectEditProjectDialog import Ui_Dialog as Ui_SelectEditProjectDialog
from QtHolidaySettingDialog import Ui_Dialog as Ui_HolidaySettingDialog
from QtVariableConditionSettingDialog import Ui_Dialog as Ui_VariableConditionSettingDialog
from QtExtendWorkingDaysSettingDialog import Ui_Dialog as Ui_ExtendWorkingDaysSettingDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QButtonGroup, QMessageBox, QStyledItemDelegate, QFileDialog, QHeaderView, QVBoxLayout, QHBoxLayout, \
                              QLabel, QLineEdit, QDialogButtonBox, QTabBar, QWidget, QTableView, QComboBox, QPushButton, QSizePolicy, QSpacerItem, QCheckBox, QDoubleSpinBox, \
                              QProgressBar, QTabWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon, QBrush
from PySide6.QtCore import Qt, QModelIndex, QRect, QSignalBlocker, QSize, QThread, QObject, Signal, QSettings
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, PatternFill, Font, Border, Side
from enum import Enum, IntEnum, auto
from decimal import Decimal
from scipy.optimize import newton


#打包指令
# cd D:\_2.code\HuachunDailyReport2024\Python
# pyinstaller --hidden-import "babel.numbers" --add-data "resources;./resources" --onefile --noconsole StockPriceMainWindow.py
# pyinstaller --hidden-import "babel.numbers" --add-data "resources;./resources" --onefile --console StockPriceMainWindow.py
# pyinstaller --hidden-import "babel.numbers" --add-data "resources;./resources" --noconsole StockPriceMainWindow.py
# pyinstaller --hidden-import "babel.numbers" --add-data "resources;./resources" --add-data "StockInventory/Dividend;./StockInventory/Dividend" --noconsole StockPriceMainWindow.py

# 要把.ui檔變成.py
# cd D:\_2.code\HuachunDailyReport2024\Python
# pyside6-uic QtDailyReportMainWindow.ui -o QtDailyReportMainWindow.py
# pyside6-uic QtCreateProjectDialog.ui -o QtCreateProjectDialog.py
# pyside6-uic QtHolidaySettingDialog.ui -o QtHolidaySettingDialog.py
# pyside6-uic QtVariableConditionSettingDialog.ui -o QtVariableConditionSettingDialog.py
# pyside6-uic QtExtendWorkingDaysSettingDialog.ui -o QtExtendWorkingDaysSettingDialog.py
# pyside6-uic QtSelectEditProjectDialog.ui -o QtSelectEditProjectDialog.py
# pyside6-uic QtDailyReportPerDayDialog.ui -o QtDailyReportPerDayDialog.py

# 靜態掃描
# pylint --disable=all --enable=E1120,E1121 StockPriceMainWindow.py 只顯示參數數量錯誤
# pylint -E StockPriceMainWindow.py 只顯示錯誤級別的資訊


# region 設定 錯誤資訊 logging
# 設定日誌
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

current_date = datetime.datetime.today().strftime("%Y-%m-%d")
log_filename = f"log_{current_date}.txt"
# 日誌檔案處理器
file_handler = TimedRotatingFileHandler(
    filename = log_filename,  # 基本文件名
    when = "midnight",  # 依據每天午夜分割日誌
    interval = 1,  # 每 1 天生成一個新檔案
    backupCount = 7,  # 保留最近 7 天的日誌檔案
    encoding = "utf-8"  # 確保支援 UTF-8 編碼
)
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# 終端處理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# 添加處理器到 logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 自定義未處理例外的鉤子
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # 如果是鍵盤中斷，保持預設行為
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    # 記錄例外
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
# 將自定義的鉤子設定為全局的未處理例外處理器
sys.excepthook = handle_exception
# endregion

g_user_dir = os.path.expanduser("~")  #開發模式跟打包模式下都是C:\Users\foxki
g_exe_dir = os.path.dirname(__file__) #開發模式下是D:\_2.code\PythonStockPrice #打包模式後是C:\Users\foxki\AppData\Local\Temp\_MEI60962 最後那個資料夾是暫時性的隨機名稱
g_exe2_dir = os.path.dirname( sys.executable ) #開發模式下是C:\Users\foxki\AppData\Local\Programs\Python\Python312 #打包模式後是:D:\_2.code\PythonStockPrice\dist
g_abs_dir = os.path.dirname( os.path.abspath(__file__) ) #開發模式下是D:\_2.code\PythonStockPrice #打包模式後是C:\Users\foxki\AppData\Local\Temp\_MEI60962 最後那個資料夾是暫時性的隨機名稱
print( "g_user_dir :" + g_user_dir ) #開發模式下是C:\Users\foxki
print( "g_exe_dir :" + g_exe_dir ) #開發模式下是D:\_2.code\PythonStockPrice #打包模式後是C:\Users\foxki\AppData\Local\Temp\_MEI60962 最後那個資料夾是暫時性的隨機名稱
print( "g_exe2_dir :" + g_exe2_dir ) #開發模式下是C:\Users\foxki\AppData\Local\Programs\Python\Python312 #打包模式後是:D:\_2.code\PythonStockPrice\dist
print( "g_abs_dir :" + g_abs_dir ) #開發模式下是D:\_2.code\PythonStockPrice #打包模式後是C:\Users\foxki\AppData\Local\Temp\_MEI60962 最後那個資料夾是暫時性的隨機名稱

reg_settings = QSettings( "FoxInfo", "DailyReport" )

if getattr( sys, 'frozen', False ):
    # PyInstaller 打包後執行時
    g_exe_root_dir = os.path.dirname(__file__) #C:\Users\foxki\AppData\Local\Temp\_MEI60962
    g_data_dir = os.path.join( g_user_dir, "AppData", "Local", "FoxInfo" ) #C:\Users\foxki\AppData\Local\FoxInfo
else:
    # VSCode執行 Python 腳本時
    g_exe_root_dir = os.path.dirname( os.path.abspath(__file__) )
    g_data_dir = g_exe_root_dir

#region 設定 icon path
window_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\FoxInfo.png' ) 
edit_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\Edit.svg' ) 
edit_icon = QIcon( edit_icon_file_path ) 
delete_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\Delete.svg' ) 
delete_icon = QIcon( delete_icon_file_path ) 
export_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\Export.svg' ) 
export_icon = QIcon( export_icon_file_path )
check_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\CheckOn.svg' ) 
check_icon = QIcon( check_icon_file_path )
uncheck_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\CheckOff.svg' ) 
uncheck_icon = QIcon( uncheck_icon_file_path )
down_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\MoveDown.svg' ) 
down_icon = QIcon( down_icon_file_path )
up_icon_file_path = os.path.join( g_exe_root_dir, 'resources\\MoveUp.svg' ) 
up_icon = QIcon( up_icon_file_path )
styles_css_path = os.path.join( g_exe_root_dir, 'resources\\styles.css' ) 
#endregion

class ProjectData( Enum ):
    STR_PROJECT_NUMBER = 0
    STR_PROJECT_NAME = auto()
    STR_CONTRACT_NUMBER = auto() #合約號碼
    STR_PROJECT_LOCATION = auto()
    N_CONTRACT_VALUE = auto() #合約金額
    STR_OWNER = auto() #業主
    STR_SUPERSIOR = auto() #監造
    STR_DESIGNER = auto() #設計
    STR_CONTRACTOR = auto() #承包商
    STR_BID_DATE = auto() #決標日期
    STR_START_DATE = auto() #開工日期
    E_CONTRACT_CONDITION = auto() #工期條件
    F_INITIAL_CONTRACT_WORKING_DAYS = auto() #契約工期
    STR_INITIAL_CONTRACT_FINISH_DATE = auto() #合約完工日期
    N_INITIAL_CONTRACT_CALENDAR_DAYS = auto() #合約日曆天數
    DICT_HOLIDAY_DATA = auto() #專案假日資料
    DICT_MORNING_WEATHER_CONDITION_DATA = auto() #變動天候條件資料
    DICT_AFTERNOON_WEATHER_CONDITION_DATA = auto() #變動天候條件資料
    DICT_MORNING_HUMAN_CONDITION_DATA = auto() #變動人為條件資料
    DICT_AFTERNOON_HUMAN_CONDITION_DATA = auto() #變動人為條件資料
    DICT_EXTENSION_DATA = auto() #追加工期資料

class Weekday( Enum ):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class DailyReportData( Enum ):
    STR_DATE = 0
    E_MORNING_WEATHER = auto()
    E_AFTERNOON_WEATHER = auto()
    E_MORNING_HUMAN = auto()
    E_AFTERNOON_HUMAN = auto()

class Weather( Enum ):
    SUN = 0
    RAIN = 1
    HEAVY_RAIN = 2
    TYPHOON = 3
    HOT = 4
    MUDDY = 5
    WEATHER_OTHER = 6

class Human( Enum ):
    NONE = 0
    SUSPENSION = 1
    POWER_OFF = 2
    HUMAN_OTHER = 3

class HolidayData( Enum ):
    REASON = 0
    HOLIDAY = 1

class ExtensionData( Enum ):
    EXTENSION_DAYS = 0
    EXTENSION_REASON = 1

class ContractCondition( Enum ):
    WORKING_DAY_NO_DAYOFF = 0
    WORKING_DAY_ONE_DAYOFF = 1
    WORKING_DAY_TWO_DAYOFF = 2
    CALENDAR_DAY = 3
    FIXED_DEADLINE = 4

class VariableConditionNoCount( Enum ):
    COUNT_ZERO_DAY_OFF = 0
    COUNT_HALF_DAY_OFF = 0.5
    COUNT_ONE_DAY_OFF = 1

class CenterIconDelegate( QStyledItemDelegate ):
    def paint( self, painter, option, index ):
        # 获取单元格数据
        icon = index.data( Qt.DecorationRole )  # 获取图标
        
        # 如果有图标
        if icon:
            rect = option.rect  # 单元格的绘制区域
            size = icon.actualSize( rect.size() ) * 0.7  # 图标实际尺寸
            
            # 计算居中位置
            x = rect.x() + ( rect.width() - size.width() ) // 2
            y = rect.y() + ( rect.height() - size.height() ) // 2
            target_rect = QRect( x, y, size.width(), size.height() )
            
            # 绘制图标
            icon.paint( painter, target_rect, Qt.AlignCenter )
        else:
            # 如果没有图标，使用默认绘制方法
            super().paint( painter, option, index )

class Utility():
    def create_project_data( str_project_number, 
                             str_project_name, 
                             str_contract_number,
                             str_project_location,
                             i_contract_value,
                             str_owner,
                             str_supersior,
                             str_designer,
                             str_contractor,
                             str_bid_date,
                             str_start_date,
                             e_contract_condition,
                             f_contract_duration,
                             str_contract_finish_date,
                             dict_project_holiday_data,
                             dict_morning_weather_condition_data,
                             dict_afternoon_weather_condition_data,
                             dict_morning_human_condition_data,
                             dict_afternoon_human_condition_data,
                             dict_extension_data ):
        dict_per_project_data = {}
        dict_per_project_data[ ProjectData.STR_PROJECT_NUMBER ] = str_project_number
        dict_per_project_data[ ProjectData.STR_PROJECT_NAME ] = str_project_name
        dict_per_project_data[ ProjectData.STR_CONTRACT_NUMBER ] = str_contract_number
        dict_per_project_data[ ProjectData.STR_PROJECT_LOCATION ] = str_project_location
        dict_per_project_data[ ProjectData.N_CONTRACT_VALUE ] = i_contract_value
        dict_per_project_data[ ProjectData.STR_OWNER ] = str_owner
        dict_per_project_data[ ProjectData.STR_SUPERSIOR ] = str_supersior
        dict_per_project_data[ ProjectData.STR_DESIGNER ] = str_designer
        dict_per_project_data[ ProjectData.STR_CONTRACTOR ] = str_contractor
        dict_per_project_data[ ProjectData.STR_BID_DATE ] = str_bid_date
        dict_per_project_data[ ProjectData.STR_START_DATE ] = str_start_date
        dict_per_project_data[ ProjectData.E_CONTRACT_CONDITION ] = e_contract_condition
        dict_per_project_data[ ProjectData.F_INITIAL_CONTRACT_WORKING_DAYS ] = f_contract_duration
        dict_per_project_data[ ProjectData.STR_INITIAL_CONTRACT_FINISH_DATE ] = str_contract_finish_date
        dict_per_project_data[ ProjectData.DICT_HOLIDAY_DATA ] = dict_project_holiday_data
        dict_per_project_data[ ProjectData.DICT_MORNING_WEATHER_CONDITION_DATA ] = dict_morning_weather_condition_data
        dict_per_project_data[ ProjectData.DICT_AFTERNOON_WEATHER_CONDITION_DATA ] = dict_afternoon_weather_condition_data
        dict_per_project_data[ ProjectData.DICT_MORNING_HUMAN_CONDITION_DATA ] = dict_morning_human_condition_data
        dict_per_project_data[ ProjectData.DICT_AFTERNOON_HUMAN_CONDITION_DATA ] = dict_afternoon_human_condition_data
        dict_per_project_data[ ProjectData.DICT_EXTENSION_DATA ] = dict_extension_data
        return dict_per_project_data

    def is_valid_english_number_string( s ):
        pattern = r'^[a-zA-Z0-9_-]+$'  # 允許的字元: 英文(a-zA-Z)、數字(0-9)、下劃線(_)、減號(-)
        return bool( re.fullmatch( pattern, s ) )
    
    def is_valid_english_chinese_number_string( s ):
        pattern = r'^[a-zA-Z0-9_\-\u4e00-\u9fff]+$'  # 允許: 英文、數字、中文、_、-
        return bool( re.fullmatch( pattern, s ) )

    def get_qt_weekday_text( n_weekday ):
        if n_weekday == 0:
            return "(日)"
        elif n_weekday == 1:
            return "(一)"
        elif n_weekday == 2:    
            return "(二)"
        elif n_weekday == 3:
            return "(三)"
        elif n_weekday == 4:
            return "(四)"
        elif n_weekday == 5:
            return "(五)"
        elif n_weekday == 6:
            return "(六)"
        else:
            return ""
    
    def get_obj_datetime_weekday_text( n_weekday ):
        if n_weekday == 0:
            return "(一)"
        elif n_weekday == 1:
            return "(二)"
        elif n_weekday == 2:
            return "(三)"
        elif n_weekday == 3:
            return "(四)"
        elif n_weekday == 4:
            return "(五)"
        elif n_weekday == 5:
            return "(六)"
        else:
            return "(日)"

    def get_concatenate_date_and_weekday_text( str_date ):
        obj_date = datetime.datetime.strptime( str_date, "%Y-%m-%d" )
        n_weekday = obj_date.weekday()
        str_weekday = Utility.get_obj_datetime_weekday_text( n_weekday )
        return str_date + " " + str_weekday

    def get_contract_condition_text( e_contract_condition ):
        if e_contract_condition == ContractCondition.WORKING_DAY_NO_DAYOFF:
            return "工作天_無週休"
        elif e_contract_condition == ContractCondition.WORKING_DAY_ONE_DAYOFF:
            return "工作天_週休一日"
        elif e_contract_condition == ContractCondition.WORKING_DAY_TWO_DAYOFF:
            return "工作天_週休二日"
        elif e_contract_condition == ContractCondition.CALENDAR_DAY:
            return "日曆天"
        elif e_contract_condition == ContractCondition.FIXED_DEADLINE:
            return "限期完工"
        else:
            return ""

    def get_is_work_day( list_const_holiday, list_const_workday, obj_date, e_contract_condition, ret_b_is_weekend, ret_b_is_holiday, ret_b_is_makeup_workday ):
        ret_b_is_weekend[0] = False
        ret_b_is_holiday[0] = False
        ret_b_is_makeup_workday[0] = False
        n_weekday = obj_date.weekday()
        if n_weekday == Weekday.SUNDAY.value:
            if ( e_contract_condition == ContractCondition.WORKING_DAY_ONE_DAYOFF or 
                 e_contract_condition == ContractCondition.WORKING_DAY_TWO_DAYOFF ):
                if obj_date in list_const_workday:
                    ret_b_is_makeup_workday[0] = True
                    return True
                else:
                    ret_b_is_weekend[0] = True
                    return False
            elif obj_date in list_const_holiday:
                ret_b_is_holiday[0] = True
                return False
            else:
                return True
        elif n_weekday == Weekday.SATURDAY.value:
            if e_contract_condition == ContractCondition.WORKING_DAY_TWO_DAYOFF:
                if obj_date in list_const_workday:
                    ret_b_is_makeup_workday[0] = True
                    return True
                else:
                    ret_b_is_weekend[0] = True
                    return False
            elif obj_date in list_const_holiday:
                ret_b_is_holiday[0] = True
                return False
            else:
                return True
        else:
            if obj_date in list_const_holiday:
                ret_b_is_holiday[0] = True
                return False
            else:
                return True
        
    def get_expect_finish_date( e_contract_condition, n_contract_working_days, obj_start_date, list_const_holiday, list_const_workday ):
        obj_expect_end_date = obj_start_date
        while( True ):
            
            b_is_weekend = [False]
            b_is_holiday = [False]
            b_is_make_up_workday = [False]
            if Utility.get_is_work_day( list_const_holiday, list_const_workday, obj_expect_end_date, e_contract_condition, b_is_weekend, b_is_holiday, b_is_make_up_workday ):
                n_contract_working_days -= 1
            if( n_contract_working_days <= 0 ):
                break
            obj_expect_end_date += datetime.timedelta( days = 1 )
        obj_return_value = {}
        obj_return_value[ 'ExpectFinishDate' ] = obj_expect_end_date
        obj_return_value[ 'ExpectTotalCalendarDays' ] = ( obj_expect_end_date - obj_start_date ).days + 1

        return obj_return_value

    # e_count_type 工期計算方式 0:周休一日  1:周休二日  2:日曆天
    # n_expect_total_workdays 工期天數
    # obj_start_date 開工日，如 '2023-01-01'
    # obj_today_date 今天日期，如 '2023-01-01'
    # arr_const_holiday 固定因素放假日
    # arr_const_workday 固定因素補班日
    # dict_weather_and_human_related_holiday 因為天氣停工資料
    # dict_extend_data 追加工期資料
    def get_real_finish_date( e_contract_condition, 
                              n_contract_working_days, 
                              obj_start_date, 
                              obj_today_date, 
                              list_const_holiday, 
                              list_const_workday, 
                              dict_weather_and_human_related_holiday, 
                              dict_extend_data ):
        obj_real_end_date = obj_start_date 
        obj_expect_end_date = obj_start_date
        n_real_rest_workdays = n_contract_working_days
        n_expect_rest_workdays = n_contract_working_days
        n_past_workdays = 0
        n_total_extend_days = 0

        #讀入追加工期資料
        for key, value in dict_extend_data.items():
            obj_extend_start_date = key
            if obj_today_date >= obj_extend_start_date:
                n_total_extend_days += value

        n_real_rest_workdays += n_total_extend_days

        while( True ):
            b_is_weekend = [False]
            b_is_holiday = [False]
            b_is_make_up_workday = [False]
            if Utility.get_is_work_day( list_const_holiday, list_const_workday, obj_real_end_date, e_contract_condition, b_is_weekend, b_is_holiday, b_is_make_up_workday ):
                if obj_real_end_date <= obj_today_date:
                    if obj_real_end_date in dict_weather_and_human_related_holiday:
                        if dict_weather_and_human_related_holiday[ obj_real_end_date ] == CountWorkingDay.NO_COUNT:
                            pass
                        elif dict_weather_and_human_related_holiday[ obj_real_end_date ] == CountWorkingDay.COUNT_HALF_DAY:
                            n_past_workdays += 0.5
                            n_real_rest_workdays -= 0.5
                        else:
                            n_past_workdays += 1
                            n_real_rest_workdays -= 1
                    else:
                        n_past_workdays += 1
                        n_real_rest_workdays -= 1#沒填日報表就當作一般晴天
                else:
                    n_real_rest_workdays -= 1#未來的日子還沒有日報表
                n_expect_rest_workdays -= 1

            if n_real_rest_workdays <= 0:
                break

            if n_expect_rest_workdays > 0:
                obj_expect_end_date += datetime.timedelta( days = 1 )

            obj_real_end_date += datetime.timedelta( days = 1 )

        obj_return_value = {}
        obj_return_value['ExpectFinishDate']        = obj_expect_end_date
        obj_return_value['ExpectTotalCalendarDays'] = ( obj_expect_end_date - obj_start_date ).days + 1
        obj_return_value['RealFinishDate']          = obj_real_end_date
        obj_return_value['RealTotalCalendarDays']   = ( obj_real_end_date - obj_start_date ).days + 1
        obj_return_value['FromStartCalendarDays']   = ( obj_today_date - obj_start_date ).days + 1
        obj_return_value['FromStartWorkDays']       = n_past_workdays
        obj_return_value['ExpectRestWorkDays']      = n_contract_working_days - n_past_workdays
        obj_return_value['ExpectRestCalendarkDays'] = ( obj_expect_end_date - obj_today_date ).days
        obj_return_value['RealRestWorkDays']        = n_contract_working_days + n_total_extend_days - n_past_workdays
        obj_return_value['RealRestCalendarkDays']   = ( obj_real_end_date - obj_today_date ).days 
        #契約工期         合約給定
        #契約完工日       ExpectFinishDate
        #契約天數         ExpectTotalCalendarDays

        #開工迄今工作天數  FromStartWorkDays
        #開工迄今日曆天數  FromStartCalendarDays
        #變動完工日       RealFinishDate
        #變動完工天數     RealTotalCalendarDays
        #預計剩餘工期     ExpectRestWorkDays
        #預計剩餘天數     ExpectRestCalendarkDays
        #實際剩餘工期     RealRestWorkDays
        #實際剩餘天數     RealRestCalendarkDays


        return obj_return_value

    def get_real_finish_date2( e_contract_condition, 
                              n_contract_working_days, 
                              obj_start_date, 
                              obj_today_date, 
                              list_const_holiday, 
                              list_const_workday, 
                              dict_weather_and_human_related_holiday, 
                              dict_extend_data ):
        obj_real_end_date = obj_start_date 
        obj_expect_end_date = obj_start_date
        n_real_rest_workdays = n_contract_working_days
        n_expect_rest_workdays = n_contract_working_days
        n_past_workdays = 0
        n_total_extend_days = 0

        #讀入追加工期資料
        for key, value in dict_extend_data.items():
            obj_extend_start_date = key
            if obj_today_date >= obj_extend_start_date:
                n_total_extend_days += value

        n_real_rest_workdays += n_total_extend_days

        while( True ):
            b_is_weekend = [False]
            b_is_holiday = [False]
            b_is_make_up_workday = [False]
            if Utility.get_is_work_day( list_const_holiday, list_const_workday, obj_real_end_date, e_contract_condition, b_is_weekend, b_is_holiday, b_is_make_up_workday ):
                if obj_real_end_date <= obj_today_date:
                    if obj_real_end_date in dict_weather_and_human_related_holiday:
                        if dict_weather_and_human_related_holiday[ obj_real_end_date ] == CountWorkingDay.NO_COUNT:
                            pass
                        elif dict_weather_and_human_related_holiday[ obj_real_end_date ] == CountWorkingDay.COUNT_HALF_DAY:
                            n_past_workdays += 0.5
                            n_real_rest_workdays -= 0.5
                        else:
                            n_past_workdays += 1
                            n_real_rest_workdays -= 1
                    else:
                        n_past_workdays += 1
                        n_real_rest_workdays -= 1#沒填日報表就當作一般晴天
                else:
                    n_real_rest_workdays -= 1#未來的日子還沒有日報表
                n_expect_rest_workdays -= 1

            if n_real_rest_workdays <= 0:
                break

            if n_expect_rest_workdays > 0:
                obj_expect_end_date += datetime.timedelta( days = 1 )

            obj_real_end_date += datetime.timedelta( days = 1 )

        obj_return_value = {}
        obj_return_value['ExpectFinishDate']        = obj_expect_end_date
        obj_return_value['ExpectTotalCalendarDays'] = ( obj_expect_end_date - obj_start_date ).days + 1
        obj_return_value['RealFinishDate']          = obj_real_end_date
        obj_return_value['RealTotalCalendarDays']   = ( obj_real_end_date - obj_start_date ).days + 1
        obj_return_value['FromStartCalendarDays']   = ( obj_today_date - obj_start_date ).days + 1
        obj_return_value['FromStartWorkDays']       = n_past_workdays
        obj_return_value['ExpectRestWorkDays']      = n_contract_working_days - n_past_workdays
        obj_return_value['ExpectRestCalendarkDays'] = ( obj_expect_end_date - obj_today_date ).days
        obj_return_value['RealRestWorkDays']        = n_contract_working_days + n_total_extend_days - n_past_workdays
        obj_return_value['RealRestCalendarkDays']   = ( obj_real_end_date - obj_today_date ).days 
        #契約工期         合約給定
        #契約完工日       ExpectFinishDate
        #契約天數         ExpectTotalCalendarDays

        #開工迄今工作天數  FromStartWorkDays
        #開工迄今日曆天數  FromStartCalendarDays
        #變動完工日       RealFinishDate
        #變動完工天數     RealTotalCalendarDays
        #預計剩餘工期     ExpectRestWorkDays
        #預計剩餘天數     ExpectRestCalendarkDays
        #實際剩餘工期     RealRestWorkDays
        #實際剩餘天數     RealRestCalendarkDays


        return obj_return_value

class CreateProjectDialog( QDialog ):
    def __init__( self, parent, dict_global_holiday_data, b_edit_mode, dict_single_project_data ):
        super().__init__( parent )

        self.ui = Ui_CreateProjectDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

        self.ui.qtProjectNumberWarningLabel.setVisible( False )
        self.ui.qtProjectNameWarningLabel.setVisible( False )
        self.ui.qtContractNumberWarningLabel.setVisible( False )
        self.obj_current_date = datetime.datetime.today()

        self.ui.qtBidDateEdit.dateChanged.connect( lambda: self.on_date_changed( self.ui.qtBidDateEdit, self.ui.qtBidWeekdayLabel ) )
        self.ui.qtStartDateEdit.dateChanged.connect( self.compute_contract_finish_date )
        self.ui.qtContractFinishDateEdit.dateChanged.connect( lambda: self.on_date_changed( self.ui.qtContractFinishDateEdit, self.ui.qtFinishWeekdayLabel ) )
        self.ui.qtWorkingDayRadioButton.toggled.connect( self.compute_contract_finish_date )
        self.ui.qtCalendarDayRadioButton.toggled.connect( self.compute_contract_finish_date )
        self.ui.qtFixedDeadlineRadioButton.toggled.connect( self.compute_contract_finish_date )
        self.ui.qtNoDayOffRadioButton.toggled.connect( self.compute_contract_finish_date )
        self.ui.qtOneDayOffRadioButton.toggled.connect( self.compute_contract_finish_date )
        self.ui.qtTwoDayOffRadioButton.toggled.connect( self.compute_contract_finish_date )
        self.ui.qtContractWorkingDaysDoubleSpinBox.valueChanged.connect( self.compute_contract_finish_date )

        self.ui.qtConstantConditionSettingPushButton.clicked.connect( self.constant_condition_setting )
        self.ui.qtVariableConditionSettingPushButton.clicked.connect( self.variable_condition_setting )
        self.ui.qtExtendPushButton.clicked.connect( self.extend_working_days_setting )
        self.ui.qtOkPushButton.clicked.connect( self.accept_data )
        self.ui.qtCancelPushButton.clicked.connect( self.cancel )

        self.dict_global_holiday_data = copy.deepcopy( dict_global_holiday_data )

        if b_edit_mode:
            self.ui.qtProjectNumberLineEdit.setEnabled( False )
            self.ui.qtProjectNumberLineEdit.setText( dict_single_project_data[ ProjectData.STR_PROJECT_NUMBER ] )
            self.ui.qtProjectNameLineEdit.setText( dict_single_project_data[ ProjectData.STR_PROJECT_NAME ] )
            self.ui.qtContractNumberLineEdit.setText( dict_single_project_data[ ProjectData.STR_CONTRACT_NUMBER ] )
            self.ui.qtProjectLocationLineEdit.setText( dict_single_project_data[ ProjectData.STR_PROJECT_LOCATION ] )
            self.ui.qtOwnerLineEdit.setText( dict_single_project_data[ ProjectData.STR_OWNER ] )
            self.ui.qtSupervisorLineEdit.setText( dict_single_project_data[ ProjectData.STR_SUPERSIOR ] )
            self.ui.qtDesignerLineEdit.setText( dict_single_project_data[ ProjectData.STR_DESIGNER ] )
            self.ui.qtContractorLineEdit.setText( dict_single_project_data[ ProjectData.STR_CONTRACTOR ] )
            self.ui.qtContractValueSpinBox.setValue( dict_single_project_data[ ProjectData.N_CONTRACT_VALUE ] )
            with ( QSignalBlocker( self.ui.qtBidDateEdit ),
                   QSignalBlocker( self.ui.qtStartDateEdit ),
                   QSignalBlocker( self.ui.qtWorkingDayRadioButton ),
                   QSignalBlocker( self.ui.qtCalendarDayRadioButton ),
                   QSignalBlocker( self.ui.qtFixedDeadlineRadioButton ),
                   QSignalBlocker( self.ui.qtNoDayOffRadioButton ),
                   QSignalBlocker( self.ui.qtOneDayOffRadioButton ),
                   QSignalBlocker( self.ui.qtTwoDayOffRadioButton ),
                   QSignalBlocker( self.ui.qtContractWorkingDaysDoubleSpinBox ),
                   QSignalBlocker( self.ui.qtContractFinishDateEdit ) ):
                self.ui.qtBidDateEdit.setDate( datetime.datetime.strptime( dict_single_project_data[ ProjectData.STR_BID_DATE ], "%Y-%m-%d" ).date() )
                self.ui.qtStartDateEdit.setDate( datetime.datetime.strptime( dict_single_project_data[ ProjectData.STR_START_DATE ], "%Y-%m-%d" ).date() )
                self.ui.qtContractWorkingDaysDoubleSpinBox.setValue( dict_single_project_data[ ProjectData.F_INITIAL_CONTRACT_WORKING_DAYS ] )
                self.ui.qtContractFinishDateEdit.setDate( datetime.datetime.strptime( dict_single_project_data[ ProjectData.STR_INITIAL_CONTRACT_FINISH_DATE ], "%Y-%m-%d" ).date() )

                e_contract_condition = dict_single_project_data[ ProjectData.E_CONTRACT_CONDITION ]
                if e_contract_condition == ContractCondition.WORKING_DAY_NO_DAYOFF:
                    self.ui.qtWorkingDayRadioButton.setChecked( True )
                    self.ui.qtNoDayOffRadioButton.setChecked( True )
                elif e_contract_condition == ContractCondition.WORKING_DAY_ONE_DAYOFF:
                    self.ui.qtWorkingDayRadioButton.setChecked( True )
                    self.ui.qtOneDayOffRadioButton.setChecked( True )
                elif e_contract_condition == ContractCondition.WORKING_DAY_TWO_DAYOFF:
                    self.ui.qtWorkingDayRadioButton.setChecked( True )
                    self.ui.qtTwoDayOffRadioButton.setChecked( True )
                elif e_contract_condition == ContractCondition.CALENDAR_DAY:
                    self.ui.qtCalendarDayRadioButton.setChecked( True )
                elif e_contract_condition == ContractCondition.FIXED_DEADLINE:
                    self.ui.qtFixedDeadlineRadioButton.setChecked( True )

            self.dict_morning_weather_condition_data = dict_single_project_data[ ProjectData.DICT_MORNING_WEATHER_CONDITION_DATA ]
            self.dict_afternoon_weather_condition_data = dict_single_project_data[ ProjectData.DICT_AFTERNOON_WEATHER_CONDITION_DATA ]
            self.dict_morning_human_condition_data = dict_single_project_data[ ProjectData.DICT_MORNING_HUMAN_CONDITION_DATA ]
            self.dict_afternoon_human_condition_data = dict_single_project_data[ ProjectData.DICT_AFTERNOON_HUMAN_CONDITION_DATA ]
            self.dict_project_holiday_data = dict_single_project_data[ ProjectData.DICT_HOLIDAY_DATA ]
            self.dict_extension_data = dict_single_project_data[ ProjectData.DICT_EXTENSION_DATA ]
        else:
            self.ui.qtBidDateEdit.setDate( self.obj_current_date.date() )
            self.ui.qtStartDateEdit.setDate( self.obj_current_date.date() )
            self.ui.qtContractFinishDateEdit.setDate( self.obj_current_date.date() )
            self.ui.qtProjectNumberLineEdit.setEnabled( True ) 
            self.dict_morning_weather_condition_data = { Weather.RAIN :          VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                         Weather.HEAVY_RAIN :    VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                         Weather.TYPHOON :       VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                         Weather.HOT :           VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                         Weather.MUDDY :         VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                         Weather.WEATHER_OTHER : VariableConditionNoCount.COUNT_HALF_DAY_OFF }
            self.dict_afternoon_weather_condition_data = { Weather.RAIN :          VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                           Weather.HEAVY_RAIN :    VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                           Weather.TYPHOON :       VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                           Weather.HOT :           VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                           Weather.MUDDY :         VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                           Weather.WEATHER_OTHER : VariableConditionNoCount.COUNT_HALF_DAY_OFF }
            self.dict_morning_human_condition_data = { Human.SUSPENSION :  VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                       Human.POWER_OFF :   VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                       Human.HUMAN_OTHER : VariableConditionNoCount.COUNT_HALF_DAY_OFF }
            self.dict_afternoon_human_condition_data = { Human.SUSPENSION : VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                         Human.POWER_OFF :  VariableConditionNoCount.COUNT_HALF_DAY_OFF,
                                                         Human.HUMAN_OTHER :VariableConditionNoCount.COUNT_HALF_DAY_OFF }
            self.dict_project_holiday_data = {}
            self.dict_extension_data = {}
        
        self.dict_single_project_data = {}
        self.update_weekday_text()
        self.compute_contract_finish_date()

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")
        
    def on_date_changed( self, qt_date_edit, qt_weekday_label ):
        obj_date = qt_date_edit.date()
        n_weekday = obj_date.dayOfWeek()
        str_weekday = Utility.get_qt_weekday_text( n_weekday )
        qt_weekday_label.setText( str_weekday )

    def update_weekday_text( self ):
        self.on_date_changed( self.ui.qtBidDateEdit, self.ui.qtBidWeekdayLabel )
        self.on_date_changed( self.ui.qtStartDateEdit, self.ui.qtStartWeekdayLabel )
        self.on_date_changed( self.ui.qtContractFinishDateEdit, self.ui.qtFinishWeekdayLabel )

    def constant_condition_setting( self ):
        dialog = HolidaySettingDialog( self, False, self.dict_global_holiday_data, self.dict_project_holiday_data )
        if dialog.exec():
            self.compute_contract_finish_date()

    def variable_condition_setting( self ):
        dialog = VariableConditionSettingDialog( self, self.dict_morning_weather_condition_data,
                                                       self.dict_afternoon_weather_condition_data, 
                                                       self.dict_morning_human_condition_data,
                                                       self.dict_afternoon_human_condition_data )
        if dialog.exec():
            pass
    
    def extend_working_days_setting( self ):
        dialog = ExtendWorkingDaysSettingDialog( self, self.dict_extension_data )
        if dialog.exec():
            pass

    def update_ui( self ):
        if self.ui.qtWorkingDayRadioButton.isChecked():
            self.ui.qtWorkingDayGroupBox.setEnabled( True )
            self.ui.qtContractWorkingDaysDoubleSpinBox.setEnabled( True )
            self.ui.qtContractFinishDateEdit.setEnabled( False )
            self.ui.qtContractCalendarDaysDoubleSpinBox.setEnabled( False )
        elif self.ui.qtCalendarDayRadioButton.isChecked():
            self.ui.qtWorkingDayGroupBox.setEnabled( False )
            self.ui.qtContractWorkingDaysDoubleSpinBox.setEnabled( True )
            self.ui.qtContractFinishDateEdit.setEnabled( False )
            self.ui.qtContractCalendarDaysDoubleSpinBox.setEnabled( False )
        elif self.ui.qtFixedDeadlineRadioButton.isChecked():
            self.ui.qtWorkingDayGroupBox.setEnabled( False )
            self.ui.qtContractWorkingDaysDoubleSpinBox.setEnabled( False )
            self.ui.qtContractFinishDateEdit.setEnabled( True )
            self.ui.qtContractCalendarDaysDoubleSpinBox.setEnabled( False )

    def compute_contract_finish_date( self ):
        self.update_ui()

        e_contract_condition = self.get_contract_condition()
        f_contract_working_days = self.ui.qtContractWorkingDaysDoubleSpinBox.value()
        obj_start_date = datetime.datetime.strptime( self.ui.qtStartDateEdit.date().toString( "yyyy-MM-dd" ), "%Y-%m-%d" )

        list_const_holiday = []
        list_const_workday = []
        for key_str_date, value in self.dict_project_holiday_data.items():
            if value[ HolidayData.HOLIDAY ]:
                list_const_holiday.append( datetime.datetime.strptime( key_str_date, "%Y-%m-%d") )
            else:
                list_const_workday.append( datetime.datetime.strptime( key_str_date, "%Y-%m-%d") )

        returnValue = Utility.get_real_finish_date( e_contract_condition, 
                                                    f_contract_working_days, 
                                                    obj_start_date, 
                                                    self.obj_current_date, 
                                                    list_const_holiday, 
                                                    list_const_workday, 
                                                    {}, 
                                                    {} )
        
        self.ui.qtContractCalendarDaysDoubleSpinBox.setValue( returnValue['ExpectTotalCalendarDays'] )
        self.ui.qtContractFinishDateEdit.setDate( returnValue['ExpectFinishDate'] )

    def get_contract_condition( self ):
        if self.ui.qtWorkingDayRadioButton.isChecked():
            if self.ui.qtNoDayOffRadioButton.isChecked():
                e_contract_condition = ContractCondition.WORKING_DAY_NO_DAYOFF
            elif self.ui.qtOneDayOffRadioButton.isChecked():
                e_contract_condition = ContractCondition.WORKING_DAY_ONE_DAYOFF
            else:
                e_contract_condition = ContractCondition.WORKING_DAY_TWO_DAYOFF
        elif self.ui.qtCalendarDayRadioButton.isChecked():
            e_contract_condition = ContractCondition.CALENDAR_DAY
        else:
            e_contract_condition = ContractCondition.FIXED_DEADLINE

        return e_contract_condition

    def accept_data( self ):
        str_project_number = self.ui.qtProjectNumberLineEdit.text()
        str_project_name = self.ui.qtProjectNameLineEdit.text()
        str_contract_number = self.ui.qtContractNumberLineEdit.text()
        str_project_location = self.ui.qtProjectLocationLineEdit.text()
        f_contract_value = self.ui.qtContractValueSpinBox.value()
        str_owner = self.ui.qtOwnerLineEdit.text()
        str_supersior = self.ui.qtSupervisorLineEdit.text()
        str_designer = self.ui.qtDesignerLineEdit.text()
        str_contractor = self.ui.qtContractorLineEdit.text()
        str_bid_date = self.ui.qtBidDateEdit.date().toString( "yyyy-MM-dd" )
        str_start_date = self.ui.qtStartDateEdit.date().toString( "yyyy-MM-dd" )

        e_contract_condition = self.get_contract_condition()
        f_contract_duration = self.ui.qtContractWorkingDaysDoubleSpinBox.value()
        str_contract_finish_date = self.ui.qtContractFinishDateEdit.date().toString( "yyyy-MM-dd" )
        
        self.dict_single_project_data[ str_project_number ] = Utility.create_project_data( str_project_number, 
                                                                                           str_project_name, 
                                                                                           str_contract_number,
                                                                                           str_project_location,
                                                                                           f_contract_value,
                                                                                           str_owner,
                                                                                           str_supersior,
                                                                                           str_designer,
                                                                                           str_contractor,
                                                                                           str_bid_date,
                                                                                           str_start_date,
                                                                                           e_contract_condition,
                                                                                           f_contract_duration,
                                                                                           str_contract_finish_date,
                                                                                           self.dict_project_holiday_data,
                                                                                           self.dict_morning_weather_condition_data,
                                                                                           self.dict_afternoon_weather_condition_data,
                                                                                           self.dict_morning_human_condition_data,
                                                                                           self.dict_afternoon_human_condition_data,
                                                                                           self.dict_extension_data )

        self.accept()
    
    def cancel( self ):
        self.reject()

class HolidaySettingDialog( QDialog ):
    def __init__( self, parent, b_main_db, dict_global_holiday_data, dict_project_holiday_data ):
        super().__init__( parent )

        self.ui = Ui_HolidaySettingDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

        obj_current_date = datetime.datetime.today()
        self.ui.qtDateEdit.setDate( obj_current_date.date() )
        self.ui.qtDateEdit.setCalendarPopup( True )

        delegate = CenterIconDelegate()

        self.list_table_horizontal_header = [ '日期', '理由', '放假/補班', '刪除' ]
        self.holiday_data_model = QStandardItemModel( 0, 0 ) 
        self.holiday_data_model.setHorizontalHeaderLabels( self.list_table_horizontal_header )
        self.ui.qtTableView.setModel( self.holiday_data_model )
        self.ui.qtTableView.setItemDelegate( delegate )
        self.ui.qtTableView.verticalHeader().hide()
        self.ui.qtTableView.clicked.connect( lambda index: self.on_table_item_clicked( index, self.holiday_data_model ) )

        self.ui.qtImportFromMainDBPushButton.clicked.connect( self.import_from_main_db_override )
        self.ui.qtAddPushButton.clicked.connect( self.add_data )
        self.ui.qtExportFilePushButton.clicked.connect( self.on_export_push_button_clicked )
        self.ui.qtImportFilePushButton.clicked.connect( self.on_import_push_button_clicked )
        self.ui.qtExitPushButton.clicked.connect( self.accept )

        self.dict_global_holiday_data = dict_global_holiday_data
        self.dict_project_holiday_data = dict_project_holiday_data

        if b_main_db:
            self.ui.qtImportFromMainDBPushButton.setVisible( False )
            self.setWindowTitle("主資料庫假日設定")
            self.dict_used_holiday_data = self.dict_global_holiday_data
        else:
            self.ui.qtImportFromMainDBPushButton.setVisible( True )
            self.setWindowTitle("專案假日設定")
            self.dict_used_holiday_data = self.dict_project_holiday_data

        self.refresh_table()

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def import_from_main_db_override( self ):
        self.dict_used_holiday_data.update( self.dict_global_holiday_data )
        self.refresh_table()

    def add_data( self ):
        str_date = self.ui.qtDateEdit.date().toString( "yyyy-MM-dd" )
        str_reason = self.ui.qtReasonLineEdit.text()
        b_holiday = self.ui.qtHolidayRadioButton.isChecked()

        if str_date in self.dict_used_holiday_data:
            QMessageBox.warning( self, "警告", "該日期已經存在", QMessageBox.Ok )
            return
        else:
            self.dict_used_holiday_data[ str_date ] = {}
            self.dict_used_holiday_data[ str_date ][ HolidayData.REASON ] = str_reason
            self.dict_used_holiday_data[ str_date ][ HolidayData.HOLIDAY ] = b_holiday
            self.process_data()

        self.refresh_table()

    def refresh_table( self ):
        for index_row,( key_date, value_dict_holiday_data ) in enumerate( self.dict_used_holiday_data.items() ):
            date_item = QStandardItem( Utility.get_concatenate_date_and_weekday_text( key_date ) )
            date_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            date_item.setFlags( date_item.flags() & ~Qt.ItemIsEditable )
            self.holiday_data_model.setItem( index_row, 0, date_item ) 

            reason_item = QStandardItem( value_dict_holiday_data[ HolidayData.REASON ] )
            reason_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            reason_item.setFlags( reason_item.flags() & ~Qt.ItemIsEditable )
            self.holiday_data_model.setItem( index_row, 1, reason_item ) 

            if value_dict_holiday_data[ HolidayData.HOLIDAY ]:
                is_holiday_item = QStandardItem( "放假" )
                is_holiday_item.setForeground( QBrush( QBrush( '#FF0000' ) ) )
            else:
                is_holiday_item = QStandardItem( "補班" )
                is_holiday_item.setForeground( QBrush( QBrush( '#00AA00' ) ) )
            is_holiday_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            is_holiday_item.setFlags( is_holiday_item.flags() & ~Qt.ItemIsEditable )
            self.holiday_data_model.setItem( index_row, 2, is_holiday_item ) 

            delete_icon_item = QStandardItem("")
            delete_icon_item.setIcon( delete_icon )
            delete_icon_item.setFlags( delete_icon_item.flags() & ~Qt.ItemIsEditable )
            self.holiday_data_model.setItem( index_row, len( self.list_table_horizontal_header ) - 1, delete_icon_item ) 

    def on_table_item_clicked( self, index, stock_list_model ):
        if index.column() == len( self.list_table_horizontal_header ) - 1:
            result = self.show_warning_message_box_with_ok_cancel_button( "警告", f"確定要刪掉這筆假日/補班資料嗎?" )
            if result:
                # delete icon
                date_item = self.holiday_data_model.item( index.row(), 0 )
                str_date = date_item.text().split(" ")[0]
                del self.dict_used_holiday_data[ str_date ]
                self.holiday_data_model.removeRow( index.row() )

    def show_warning_message_box_with_ok_cancel_button( self, str_title, str_message ): 
        message_box = QMessageBox( self )
        message_box.setIcon( QMessageBox.Warning )  # 設置為警告圖示
        message_box.setWindowTitle( str_title )
        message_box.setText( str_message )

        # 添加自訂按鈕
        button_ok = message_box.addButton("確定", QMessageBox.AcceptRole)
        button_cancel = message_box.addButton("取消", QMessageBox.RejectRole)

        message_box.exec()

        if message_box.clickedButton() == button_ok:
            return True
        elif message_box.clickedButton() == button_cancel:
            return False

    def open_load_json_file_dialog( self ): 
        # 彈出讀取檔案對話框
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "匯入假日資料",     # 對話框標題
            "",                # 預設路徑
            "JSON (*.json);;"  # 檔案類型過濾
        )
        return file_path

    def open_save_json_file_dialog( self ): 
        # 彈出儲存檔案對話框
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "匯出假日資料",     # 對話框標題
            "",                # 預設路徑
            "JSON (*.json);;"  # 檔案類型過濾
        )
        return file_path 

    def on_export_push_button_clicked( self ):
        file_path = self.open_save_json_file_dialog()
        if file_path:
            dict_save_holiday_data = {}
            for key, value in self.dict_used_holiday_data.items():
                dict_save_holiday_data[ key ] = { "reason" : str( value[ HolidayData.REASON ] ), 
                                                  "holiday" : bool( value[ HolidayData.HOLIDAY ] ) }

            with open( file_path, 'w', encoding='utf-8' ) as f:
                f.write( "v1.0.0" '\n' )
                json.dump( dict_save_holiday_data, f, ensure_ascii=False, indent=4 )

    def on_import_push_button_clicked( self ):
        file_path = self.open_load_json_file_dialog()
        if file_path:
            with open( file_path, 'r', encoding='utf-8' ) as f:
                str_version = f.readline().strip()
                if str_version == "v1.0.0":
                    dict_load_holiday_data = json.load( f )
                    for key,value in dict_load_holiday_data.items():
                        self.dict_used_holiday_data[ key ] = { HolidayData.REASON : value[ "reason" ], 
                                                               HolidayData.HOLIDAY : value[ "holiday" ] }
                self.process_data()
            self.refresh_table()
    
    def process_data( self ):
        for key in sorted( self.dict_used_holiday_data.keys() ):
            self.dict_used_holiday_data[ key ] = self.dict_used_holiday_data.pop( key )

    def accept_data( self ):
        self.accept()
    
    def cancel( self ):
        self.reject()

class VariableConditionSettingDialog( QDialog ):
    def __init__( self, parent, dict_morning_weather_condition_data, 
                                dict_afternoon_weather_condition_data,
                                dict_morning_human_condition_data,
                                dict_afternoon_human_condition_data ):
        super().__init__( parent )

        self.ui = Ui_VariableConditionSettingDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )
        self.ui.qtOkPushButton.clicked.connect( self.accept_data )
        self.ui.qtCancelPushButton.clicked.connect( self.cancel )

        self.dict_morning_weather_condition_data = dict_morning_weather_condition_data
        self.dict_afternoon_weather_condition_data = dict_afternoon_weather_condition_data
        self.dict_morning_human_condition_data = dict_morning_human_condition_data
        self.dict_afternoon_human_condition_data = dict_afternoon_human_condition_data
        self.update_ui()

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def update_ui( self ):
        self.update_radio_button( self.ui.qtMorningRainOneDayOffRadioButton,           self.ui.qtMorningRainHalfDayOffRadioButton,           self.ui.qtMorningRainNoDayOffRadioButton,           self.dict_morning_weather_condition_data, Weather.RAIN )
        self.update_radio_button( self.ui.qtMorningHeavyRainOneDayOffRadioButton,      self.ui.qtMorningHeavyRainHalfDayOffRadioButton,      self.ui.qtMorningHeavyRainNoDayOffRadioButton,      self.dict_morning_weather_condition_data, Weather.HEAVY_RAIN )
        self.update_radio_button( self.ui.qtMorningTyphoonOneDayOffRadioButton,        self.ui.qtMorningTyphoonHalfDayOffRadioButton,        self.ui.qtMorningTyphoonNoDayOffRadioButton,        self.dict_morning_weather_condition_data, Weather.TYPHOON )
        self.update_radio_button( self.ui.qtMorningHotOneDayOffRadioButton,            self.ui.qtMorningHotHalfDayOffRadioButton,            self.ui.qtMorningHotNoDayOffRadioButton,            self.dict_morning_weather_condition_data, Weather.HOT )
        self.update_radio_button( self.ui.qtMorningMuddyOneDayOffRadioButton,          self.ui.qtMorningMuddyHalfDayOffRadioButton,          self.ui.qtMorningMuddyNoDayOffRadioButton,          self.dict_morning_weather_condition_data, Weather.MUDDY )
        self.update_radio_button( self.ui.qtMorningWeatherOtherOneDayOffRadioButton,   self.ui.qtMorningWeatherOtherHalfDayOffRadioButton,   self.ui.qtMorningWeatherOtherNoDayOffRadioButton,   self.dict_morning_weather_condition_data, Weather.WEATHER_OTHER )
        self.update_radio_button( self.ui.qtAfternoonRainOneDayOffRadioButton,         self.ui.qtAfternoonRainHalfDayOffRadioButton,         self.ui.qtAfternoonRainNoDayOffRadioButton,         self.dict_afternoon_weather_condition_data, Weather.RAIN )
        self.update_radio_button( self.ui.qtAfternoonHeavyRainOneDayOffRadioButton,    self.ui.qtAfternoonHeavyRainHalfDayOffRadioButton,    self.ui.qtAfternoonHeavyRainNoDayOffRadioButton,    self.dict_afternoon_weather_condition_data, Weather.HEAVY_RAIN )
        self.update_radio_button( self.ui.qtAfternoonTyphoonOneDayOffRadioButton,      self.ui.qtAfternoonTyphoonHalfDayOffRadioButton,      self.ui.qtAfternoonTyphoonNoDayOffRadioButton,      self.dict_afternoon_weather_condition_data, Weather.TYPHOON )
        self.update_radio_button( self.ui.qtAfternoonHotOneDayOffRadioButton,          self.ui.qtAfternoonHotHalfDayOffRadioButton,          self.ui.qtAfternoonHotNoDayOffRadioButton,          self.dict_afternoon_weather_condition_data, Weather.HOT )
        self.update_radio_button( self.ui.qtAfternoonMuddyOneDayOffRadioButton,        self.ui.qtAfternoonMuddyHalfDayOffRadioButton,        self.ui.qtAfternoonMuddyNoDayOffRadioButton,        self.dict_afternoon_weather_condition_data, Weather.MUDDY )
        self.update_radio_button( self.ui.qtAfternoonWeatherOtherOneDayOffRadioButton, self.ui.qtAfternoonWeatherOtherHalfDayOffRadioButton, self.ui.qtAfternoonWeatherOtherNoDayOffRadioButton, self.dict_afternoon_weather_condition_data, Weather.WEATHER_OTHER )

        self.update_radio_button( self.ui.qtMorningSuspendOneDayOffRadioButton,      self.ui.qtMorningSuspendHalfDayOffRadioButton,      self.ui.qtMorningSuspendNoDayOffRadioButton,           self.dict_morning_human_condition_data, Human.SUSPENSION )
        self.update_radio_button( self.ui.qtMorningPowerOffOneDayOffRadioButton,     self.ui.qtMorningPowerOffHalfDayOffRadioButton,     self.ui.qtMorningPowerOffNoDayOffRadioButton,          self.dict_morning_human_condition_data, Human.POWER_OFF )
        self.update_radio_button( self.ui.qtMorningHumanOtherOneDayOffRadioButton,   self.ui.qtMorningHumanOtherHalfDayOffRadioButton,   self.ui.qtMorningHumanOtherNoDayOffRadioButton,        self.dict_morning_human_condition_data, Human.HUMAN_OTHER )
        self.update_radio_button( self.ui.qtAfternoonSuspendOneDayOffRadioButton,    self.ui.qtAfternoonSuspendHalfDayOffRadioButton,    self.ui.qtAfternoonSuspendNoDayOffRadioButton,         self.dict_afternoon_human_condition_data, Human.SUSPENSION )
        self.update_radio_button( self.ui.qtAfternoonPowerOffOneDayOffRadioButton,   self.ui.qtAfternoonPowerOffHalfDayOffRadioButton,   self.ui.qtAfternoonPowerOffNoDayOffRadioButton,        self.dict_afternoon_human_condition_data, Human.POWER_OFF )
        self.update_radio_button( self.ui.qtAfternoonHumanOtherOneDayOffRadioButton, self.ui.qtAfternoonHumanOtherHalfDayOffRadioButton, self.ui.qtAfternoonHumanOtherNoDayOffRadioButton,      self.dict_afternoon_human_condition_data, Human.HUMAN_OTHER )

    def update_radio_button( self, qtOneDayOffRadioButton, qtHalfDayOffRadioButton, qtNoDayOffRadioButton, dict_condition_data, e_condition ):
        with ( QSignalBlocker( qtOneDayOffRadioButton ),
               QSignalBlocker( qtHalfDayOffRadioButton ),
               QSignalBlocker( qtNoDayOffRadioButton ) ):
            if dict_condition_data[ e_condition ] == VariableConditionNoCount.COUNT_ONE_DAY_OFF:
                qtOneDayOffRadioButton.setChecked( True )
            elif dict_condition_data[ e_condition ] == VariableConditionNoCount.COUNT_HALF_DAY_OFF:
                qtHalfDayOffRadioButton.setChecked( True )
            else:
                qtNoDayOffRadioButton.setChecked( True )

    def get_day_off( self, qtOneDayOffRadioButton, qtHalfDayOffRadioButton ):
        if qtOneDayOffRadioButton.isChecked():
            return VariableConditionNoCount.COUNT_ONE_DAY_OFF
        elif qtHalfDayOffRadioButton.isChecked():
            return VariableConditionNoCount.COUNT_HALF_DAY_OFF
        else:
            return VariableConditionNoCount.COUNT_ZERO_DAY_OFF

    def accept_data( self ):
        e_morning_rain          = self.get_day_off( self.ui.qtMorningRainOneDayOffRadioButton,         self.ui.qtMorningRainHalfDayOffRadioButton )
        e_morning_heavyrain     = self.get_day_off( self.ui.qtMorningHeavyRainOneDayOffRadioButton,    self.ui.qtMorningHeavyRainHalfDayOffRadioButton )
        e_morning_typhoon       = self.get_day_off( self.ui.qtMorningTyphoonOneDayOffRadioButton,      self.ui.qtMorningTyphoonHalfDayOffRadioButton )
        e_morning_hot           = self.get_day_off( self.ui.qtMorningHotOneDayOffRadioButton,          self.ui.qtMorningHotHalfDayOffRadioButton )
        e_morning_muddy         = self.get_day_off( self.ui.qtMorningMuddyOneDayOffRadioButton,        self.ui.qtMorningMuddyHalfDayOffRadioButton )
        e_morning_weather_other = self.get_day_off( self.ui.qtMorningWeatherOtherOneDayOffRadioButton, self.ui.qtMorningWeatherOtherHalfDayOffRadioButton )

        self.dict_morning_weather_condition_data[ Weather.SUN ]           = VariableConditionNoCount.COUNT_ZERO_DAY_OFF
        self.dict_morning_weather_condition_data[ Weather.RAIN ]          = e_morning_rain
        self.dict_morning_weather_condition_data[ Weather.HEAVY_RAIN ]    = e_morning_heavyrain
        self.dict_morning_weather_condition_data[ Weather.TYPHOON ]       = e_morning_typhoon
        self.dict_morning_weather_condition_data[ Weather.HOT ]           = e_morning_hot
        self.dict_morning_weather_condition_data[ Weather.MUDDY ]         = e_morning_muddy
        self.dict_morning_weather_condition_data[ Weather.WEATHER_OTHER ] = e_morning_weather_other

        e_afternoon_rain          = self.get_day_off( self.ui.qtAfternoonRainOneDayOffRadioButton,         self.ui.qtAfternoonRainHalfDayOffRadioButton )
        e_afternoon_heavyrain     = self.get_day_off( self.ui.qtAfternoonHeavyRainOneDayOffRadioButton,    self.ui.qtAfternoonHeavyRainHalfDayOffRadioButton )
        e_afternoon_typhoon       = self.get_day_off( self.ui.qtAfternoonTyphoonOneDayOffRadioButton,      self.ui.qtAfternoonTyphoonHalfDayOffRadioButton )
        e_afternoon_hot           = self.get_day_off( self.ui.qtAfternoonHotOneDayOffRadioButton,          self.ui.qtAfternoonHotHalfDayOffRadioButton )
        e_afternoon_muddy         = self.get_day_off( self.ui.qtAfternoonMuddyOneDayOffRadioButton,        self.ui.qtAfternoonMuddyHalfDayOffRadioButton )
        e_afternoon_weather_other = self.get_day_off( self.ui.qtAfternoonWeatherOtherOneDayOffRadioButton, self.ui.qtAfternoonWeatherOtherHalfDayOffRadioButton )

        self.dict_afternoon_weather_condition_data[ Weather.SUN ]           = VariableConditionNoCount.COUNT_ZERO_DAY_OFF
        self.dict_afternoon_weather_condition_data[ Weather.RAIN ]          = e_afternoon_rain
        self.dict_afternoon_weather_condition_data[ Weather.HEAVY_RAIN ]    = e_afternoon_heavyrain
        self.dict_afternoon_weather_condition_data[ Weather.TYPHOON ]       = e_afternoon_typhoon
        self.dict_afternoon_weather_condition_data[ Weather.HOT ]           = e_afternoon_hot
        self.dict_afternoon_weather_condition_data[ Weather.MUDDY ]         = e_afternoon_muddy
        self.dict_afternoon_weather_condition_data[ Weather.WEATHER_OTHER ] = e_afternoon_weather_other

        e_morning_suspension  = self.get_day_off( self.ui.qtMorningSuspendOneDayOffRadioButton,    self.ui.qtMorningSuspendHalfDayOffRadioButton )
        e_morning_power_off   = self.get_day_off( self.ui.qtMorningPowerOffOneDayOffRadioButton,   self.ui.qtMorningPowerOffHalfDayOffRadioButton )
        e_morning_human_other = self.get_day_off( self.ui.qtMorningHumanOtherOneDayOffRadioButton, self.ui.qtMorningHumanOtherHalfDayOffRadioButton )
        
        self.dict_morning_human_condition_data[ Human.SUSPENSION ]  = e_morning_suspension
        self.dict_morning_human_condition_data[ Human.POWER_OFF ]   = e_morning_power_off
        self.dict_morning_human_condition_data[ Human.HUMAN_OTHER ] = e_morning_human_other

        e_afternoon_suspension  = self.get_day_off( self.ui.qtAfternoonSuspendOneDayOffRadioButton,    self.ui.qtAfternoonSuspendHalfDayOffRadioButton )
        e_afternoon_power_off   = self.get_day_off( self.ui.qtAfternoonPowerOffOneDayOffRadioButton,   self.ui.qtAfternoonPowerOffHalfDayOffRadioButton )
        e_afternoon_human_other = self.get_day_off( self.ui.qtAfternoonHumanOtherOneDayOffRadioButton, self.ui.qtAfternoonHumanOtherHalfDayOffRadioButton )

        self.dict_afternoon_human_condition_data[ Human.SUSPENSION ]  = e_afternoon_suspension
        self.dict_afternoon_human_condition_data[ Human.POWER_OFF ]   = e_afternoon_power_off
        self.dict_afternoon_human_condition_data[ Human.HUMAN_OTHER ] = e_afternoon_human_other
        
        self.accept()

    def cancel( self ):
        self.reject()

class ExtendWorkingDaysSettingDialog( QDialog ):
    def __init__( self, parent, dict_project_extension_data ):
        super().__init__( parent )

        self.ui = Ui_ExtendWorkingDaysSettingDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

        obj_current_date = datetime.datetime.today()
        self.ui.qtDateEdit.setDate( obj_current_date.date() )
        self.ui.qtDateEdit.setCalendarPopup( True )

        delegate = CenterIconDelegate()

        self.list_table_horizontal_header = [ '追加起始日', '追加天數', '理由', '刪除' ]
        self.extension_data_model = QStandardItemModel( 0, 0 ) 
        self.extension_data_model.setHorizontalHeaderLabels( self.list_table_horizontal_header )
        self.ui.qtTableView.setModel( self.extension_data_model )
        self.ui.qtTableView.setItemDelegate( delegate )
        self.ui.qtTableView.verticalHeader().hide()
        self.ui.qtTableView.clicked.connect( lambda index: self.on_table_item_clicked( index, self.extension_data_model ) )

        self.ui.qtAddPushButton.clicked.connect( self.add_data )
        self.ui.qtExitPushButton.clicked.connect( self.accept )

        self.dict_project_extension_data = dict_project_extension_data

        self.refresh_table()

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def add_data( self ):
        str_date = self.ui.qtDateEdit.date().toString( "yyyy-MM-dd" )
        str_reason = self.ui.qtReasonLineEdit.text()
        n_extension_days = self.ui.qtExtensionDaysSpinBox.value()

        if str_date in self.dict_project_extension_data:
            QMessageBox.warning( self, "警告", "該日期已經存在", QMessageBox.Ok )
            return
        else:
            self.dict_project_extension_data[ str_date ] = {}
            self.dict_project_extension_data[ str_date ][ ExtensionData.EXTENSION_DAYS ] = n_extension_days
            self.dict_project_extension_data[ str_date ][ ExtensionData.EXTENSION_REASON ] = str_reason
            self.process_data()

        self.refresh_table()

    def refresh_table( self ):
        for index_row,( key_date, value_dict_extension_data ) in enumerate( self.dict_project_extension_data.items() ):
            date_item = QStandardItem( Utility.get_concatenate_date_and_weekday_text( key_date ) )
            date_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            date_item.setFlags( date_item.flags() & ~Qt.ItemIsEditable )
            self.extension_data_model.setItem( index_row, 0, date_item ) 

            extension_days_item = QStandardItem( str( value_dict_extension_data[ ExtensionData.EXTENSION_DAYS ] ) )
            extension_days_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            extension_days_item.setFlags( extension_days_item.flags() & ~Qt.ItemIsEditable )
            self.extension_data_model.setItem( index_row, 1, extension_days_item ) 

            reason_item = QStandardItem( value_dict_extension_data[ ExtensionData.EXTENSION_REASON ] )
            reason_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            reason_item.setFlags( reason_item.flags() & ~Qt.ItemIsEditable )
            self.extension_data_model.setItem( index_row, 2, reason_item ) 

            delete_icon_item = QStandardItem("")
            delete_icon_item.setIcon( delete_icon )
            delete_icon_item.setFlags( delete_icon_item.flags() & ~Qt.ItemIsEditable )
            self.extension_data_model.setItem( index_row, len( self.list_table_horizontal_header ) - 1, delete_icon_item ) 

    def on_table_item_clicked( self, index, stock_list_model ):
        if index.column() == len( self.list_table_horizontal_header ) - 1:
            result = self.show_warning_message_box_with_ok_cancel_button( "警告", f"確定要刪掉這筆追加工期資料嗎?" )
            if result:
                # delete icon
                date_item = self.extension_data_model.item( index.row(), 0 )
                str_date = date_item.text().split(" ")[0]
                del self.dict_project_extension_data[ str_date ]
                self.extension_data_model.removeRow( index.row() )

    def show_warning_message_box_with_ok_cancel_button( self, str_title, str_message ): 
        message_box = QMessageBox( self )
        message_box.setIcon( QMessageBox.Warning )  # 設置為警告圖示
        message_box.setWindowTitle( str_title )
        message_box.setText( str_message )

        # 添加自訂按鈕
        button_ok = message_box.addButton("確定", QMessageBox.AcceptRole)
        button_cancel = message_box.addButton("取消", QMessageBox.RejectRole)

        message_box.exec()

        if message_box.clickedButton() == button_ok:
            return True
        elif message_box.clickedButton() == button_cancel:
            return False
    
    def process_data( self ):
        for key in sorted( self.dict_project_extension_data.keys() ):
            self.dict_project_extension_data[ key ] = self.dict_project_extension_data.pop( key )

    def accept_data( self ):
        self.accept()
    
    def cancel( self ):
        self.reject()

class DailyReportPerDayDialog( QDialog ):
    def __init__( self, parent, dict_per_project_data, dict_per_project_dailyreport_data ):
        super().__init__( parent )

        self.ui = Ui_DailyReportPerDayDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

        obj_current_date = datetime.datetime.today()
        self.ui.qtTodayDateEdit.setDate( obj_current_date.date() )
        self.ui.qtTodayDateEdit.setCalendarPopup( True )

        self.ui.qtOkPushButton.clicked.connect( self.accept_data )
        self.ui.qtCancelPushButton.clicked.connect( self.cancel )

        self.dict_all_project_data = dict_per_project_data
        self.dict_all_project_dailyreport_data = dict_per_project_dailyreport_data

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def accept_data( self ):
        e_morning_weather = Weather( self.ui.qtMorningWeatherComboBox.currentIndex() )
        e_afternoon_weather = Weather( self.ui.qtAfternoonWeatherComboBox.currentIndex() )

        e_morning_human = Human( self.ui.qtMorningHumanComboBox.currentIndex() )
        e_afternoon_human = Human( self.ui.qtAfternoonHumanComboBox.currentIndex() )
        str_today_date = self.ui.qtTodayDateEdit.date().toString( "yyyy-MM-dd" )
        self.dict_all_project_dailyreport_data[ str_today_date ] = { DailyReportData.E_MORNING_WEATHER: e_morning_weather,
                                                                     DailyReportData.E_AFTERNOON_WEATHER: e_afternoon_weather,
                                                                     DailyReportData.E_MORNING_HUMAN: e_morning_human,
                                                                     DailyReportData.E_AFTERNOON_HUMAN: e_afternoon_human}

        self.accept()
    
    def cancel( self ):
        self.reject()

class Worker( QObject ):
    progress = Signal( int )  # Signal to emit progress updates
    finished = Signal( dict )  # Signal to emit the result when done

    def __init__( self, main_window ):
        super().__init__()
        self.main_window = main_window  # 傳入 MainWindow 的實例

    def run( self ):
        # Perform the time-consuming operation (e.g. loading stock data)
        self.main_window.initialize( False, self.update_progress )
        self.finished.emit({})  # Emit the result when done

    def update_progress( self, value ):
        self.progress.emit( value )  # Emit progress updates

class MainWindow( QMainWindow ):
    def __init__( self, b_unit_test = False, 
                  str_UI_setting_file = 'UISetting.config',
                  str_global_holiday_file = 'GlobalHoliday.txt',
                  str_global_project_file = 'ProjectData.txt',
                  str_global_dailyreport_file = 'DailyReportData.txt' ):
        super( MainWindow, self ).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )  # 設置 UI
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )
        size = reg_settings.value( "window_size", QSize( 1250, 893 ) )
        self.resize(size)
        
        self.global_holiday_file_path = os.path.join( g_data_dir, 'DailyReport', str_global_holiday_file )
        self.global_project_data_file_path = os.path.join( g_data_dir, 'DailyReport', str_global_project_file )
        self.global_dialyreport_data_file_path = os.path.join( g_data_dir, 'DailyReport', str_global_dailyreport_file )
        self.UISetting_file_path = os.path.join( g_data_dir, 'DailyReport', 'UISetting.config' )

        if not b_unit_test:
            self.progress_bar = QProgressBar( self )
            self.progress_bar.setGeometry( 400, 350, 300, 25 )  # Adjust position and size as needed
            self.progress_bar.setMaximum( 100 )
            self.progress_bar.setVisible( False )
        
        delegate = CenterIconDelegate()
        self.list_project_list_table_horizontal_header = [ '工程編號', '工程名稱', '案號及契約號', '工程地點', '業主', '設計單位', '工期條件', '開工日期', '契約工期', '預計完工日', '預計完工天數', '編輯', '刪除' ]
        self.project_data_model = QStandardItemModel( 0, 0 ) 
        self.project_data_model.setHorizontalHeaderLabels( self.list_project_list_table_horizontal_header )
        self.ui.qtProjectListTableView.setModel( self.project_data_model )
        self.ui.qtProjectListTableView.setItemDelegate( delegate )
        self.ui.qtProjectListTableView.horizontalHeader().sectionResized.connect( self.on_project_list_table_horizontal_section_resized )
        self.ui.qtProjectListTableView.verticalHeader().setSectionsMovable( True )
        self.ui.qtProjectListTableView.verticalHeader().sectionMoved.connect( self.on_project_list_table_vertical_header_section_moved )
        self.ui.qtProjectListTableView.verticalHeader().sectionClicked.connect( self.on_project_list_table_vertical_section_clicked )
        self.ui.qtProjectListTableView.clicked.connect( lambda index: self.on_project_list_table_item_clicked( index, self.project_data_model ) )
        self.pick_up_project( None )

        self.list_dailyreport_list_table_horizontal_header = [ '日期', '上午天氣', '下午天氣', '上午人為', '下午人為', '今日不計', '工期總計','開工迄今天數', '編輯', '刪除' ]
        self.dailyreport_data_model = QStandardItemModel( 0, 0 ) 
        self.dailyreport_data_model.setHorizontalHeaderLabels( self.list_dailyreport_list_table_horizontal_header )
        self.ui.qtDailyReportListTableView.setModel( self.dailyreport_data_model )
        self.ui.qtDailyReportListTableView.setItemDelegate( delegate )
        self.ui.qtDailyReportListTableView.verticalHeader().hide()
        self.ui.qtDailyReportListTableView.horizontalHeader().sectionResized.connect( self.on_dailyreport_list_table_horizontal_section_resized )
        self.ui.qtDailyReportListTableView.clicked.connect( lambda index: self.on_dailyreport_list_table_item_clicked( index, self.dailyreport_data_model ) )

        self.ui.qtMainHolidayDBSettingAction.triggered.connect( self.on_trigger_main_holiday_db_setting )
        self.ui.qtCreateNewProjectAction.triggered.connect( self.on_trigger_create_new_project )

        self.ui.qtAddDailyReportPushButton.clicked.connect( self.on_add_daily_report_data_push_button_clicked )

        self.list_project_list_column_width = [ 85 ] * len( self.list_project_list_table_horizontal_header )
        self.list_project_list_column_width[ len( self.list_project_list_table_horizontal_header ) - 2 ] = 40
        self.list_project_list_column_width[ len( self.list_project_list_table_horizontal_header ) - 1 ] = 40

        self.list_dailyreport_list_column_width = [ 85 ] * len( self.list_dailyreport_list_table_horizontal_header )
        self.list_dailyreport_list_column_width[ len( self.list_dailyreport_list_table_horizontal_header ) - 2 ] = 40
        self.list_dailyreport_list_column_width[ len( self.list_dailyreport_list_table_horizontal_header ) - 1 ] = 40
        
        self.str_picked_project_number = ""
        self.dict_global_holiday_data = {}
        self.dict_all_project_data = {}
        self.dict_all_project_dailyreport_data = {}

        self.load_stylesheet( styles_css_path )
        if b_unit_test:
            self.initialize( True, None )
            self.load_initialize_data()
        else:
            self.start_loading_stock_data()

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def closeEvent( self, event ):
        """當視窗關閉時，儲存當前大小"""
        reg_settings.setValue( "window_size", self.size() )
        super().closeEvent( event )

    def initialize( self, b_unit_test, update_progress_callback ):
        self.setEnabled( False ) # 資料下載前先Disable整個視窗
        
        # if not b_unit_test:
        #     self.download_all_required_data( update_progress_callback )
        
        self.set_progress_value( update_progress_callback, 100 )
        # self.load_initialize_data()
        self.setEnabled( True ) # 資料下載完後就會Enable

    def set_progress_value( self, update_progress_callback, f_progress ):
        if update_progress_callback:
            update_progress_callback( f_progress )

    def start_loading_stock_data( self ):
        # Show the progress bar
        self.progress_bar.setVisible( True )

        # Create and start a QThread for the worker
        self.thread = QThread()
        self.worker = Worker(self)

        # Move the worker to the new thread
        self.worker.moveToThread( self.thread )

        # Connect signals and slots
        self.worker.progress.connect( self.update_progress )
        self.worker.finished.connect( self.on_loading_finished )
        self.thread.started.connect( self.worker.run )
        self.worker.finished.connect( self.thread.quit )

        # Start the thread
        self.thread.start()

    def update_progress( self, value ):
        self.progress_bar.setValue( value )

    def on_loading_finished( self ):
        self.progress_bar.setVisible( False )
        self.load_initialize_data()

    def load_initialize_data( self ):
        self.manual_load_global_holiday_data( self.global_holiday_file_path )
        self.manual_load_project_data( self.global_project_data_file_path )
        self.load_UI_state()
        self.process_all_dailyreport_data()
        self.refresh_project_list_table()

    def on_trigger_main_holiday_db_setting( self ):
        dialog = HolidaySettingDialog( self, True, self.dict_global_holiday_data, {} )
        if dialog.exec():
            self.auto_save_global_holiday_data()

    def on_trigger_create_new_project( self ):
        dialog = CreateProjectDialog( self, self.dict_global_holiday_data, False, {} )
        if dialog.exec():
            self.dict_all_project_data.update( dialog.dict_single_project_data )
            self.dict_all_project_dailyreport_data[ dialog.dict_single_project_data[ ProjectData.STR_PROJECT_NUMBER ] ] = {}
            self.auto_save_project_data()
            self.refresh_project_list_table()

    def refresh_project_list_table( self ):
        # [ '工程編號', '工程名稱', '案號及契約號', '工程地點', '業主', '設計單位', '工期條件', '開工日期', '契約工期', '預計完工日', '預計完工天數', '編輯', '刪除' ]
        list_vertical_labels = ["   "] * len( self.dict_all_project_data )
        for index_row,( key_project_number, value_dict_project_data ) in enumerate( self.dict_all_project_data.items() ):
            list_item_value = []
            list_item_value.append( key_project_number ) #工程編號
            list_item_value.append( value_dict_project_data[ ProjectData.STR_PROJECT_NAME ] ) #工程名稱
            list_item_value.append( value_dict_project_data[ ProjectData.STR_CONTRACT_NUMBER ] ) #案號及契約號
            list_item_value.append( value_dict_project_data[ ProjectData.STR_PROJECT_LOCATION ] ) #工程地點
            list_item_value.append( value_dict_project_data[ ProjectData.STR_OWNER ] ) #業主
            list_item_value.append( value_dict_project_data[ ProjectData.STR_DESIGNER ] ) #設計單位
            list_item_value.append( Utility.get_contract_condition_text( value_dict_project_data[ ProjectData.E_CONTRACT_CONDITION ] ) ) #工期條件
            list_item_value.append( Utility.get_concatenate_date_and_weekday_text( value_dict_project_data[ ProjectData.STR_START_DATE ] ) ) #開工日期
            list_item_value.append( str( value_dict_project_data[ ProjectData.F_INITIAL_CONTRACT_WORKING_DAYS ] ) ) #契約工期
            list_item_value.append( Utility.get_concatenate_date_and_weekday_text( value_dict_project_data[ ProjectData.STR_INITIAL_CONTRACT_FINISH_DATE ] ) ) #預計完工日

            for index_column, str_item_value in enumerate( list_item_value ):
                item = QStandardItem( str_item_value )
                item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
                item.setFlags( item.flags() & ~Qt.ItemIsEditable )
                self.project_data_model.setItem( index_row, index_column, item )
            

            edit_icon_item = QStandardItem("")
            edit_icon_item.setIcon( edit_icon )
            edit_icon_item.setFlags( edit_icon_item.flags() & ~Qt.ItemIsEditable )
            self.project_data_model.setItem( index_row, len( self.list_project_list_table_horizontal_header ) - 2, edit_icon_item ) 

            delete_icon_item = QStandardItem("")
            delete_icon_item.setIcon( delete_icon )
            delete_icon_item.setFlags( delete_icon_item.flags() & ~Qt.ItemIsEditable )
            self.project_data_model.setItem( index_row, len( self.list_project_list_table_horizontal_header ) - 1, delete_icon_item ) 
        
        for column in range( len( self.list_project_list_table_horizontal_header ) ):
            if column < len( self.list_project_list_column_width ):
                self.ui.qtProjectListTableView.setColumnWidth( column, self.list_project_list_column_width[ column ] )
            else:
                self.ui.qtProjectListTableView.setColumnWidth( column, 85 )
                self.list_project_list_column_width.append( 85 )
        
        self.project_data_model.setVerticalHeaderLabels( list_vertical_labels )

    def on_project_list_table_horizontal_section_resized( self, n_logical_index, n_old_size, n_new_size ): 
        self.list_project_list_column_width[ n_logical_index ] = n_new_size
        self.save_UI_state()

    def on_project_list_table_vertical_header_section_moved( self, n_logical_index, n_old_visual_index, n_new_visual_index ):
        pass

    def on_project_list_table_vertical_section_clicked( self, n_logical_index ):
        pass

    def on_project_list_table_item_clicked( self, index, stock_list_model ):
        project_number_item = self.project_data_model.item( index.row(), 0 )
        str_project_number = project_number_item.text()
        if index.column() == len( self.list_project_list_table_horizontal_header ) - 2:# edit
            dict_single_project_data = self.dict_all_project_data[ str_project_number ]
            edit_dialog = CreateProjectDialog( self, self.dict_global_holiday_data, True, dict_single_project_data )
            if edit_dialog.exec():
                self.dict_all_project_data.update( edit_dialog.dict_single_project_data )
                self.auto_save_project_data()
                self.refresh_project_list_table()
                self.pick_up_project( str_project_number )
                self.refresh_dailyreport_list_table()
        elif index.column() == len( self.list_project_list_table_horizontal_header ) - 1:# delete
            result = self.show_warning_message_box_with_ok_cancel_button( "警告", f"確定要刪掉這筆專案資料嗎?" )
            if result:
                del self.dict_all_project_data[ str_project_number ]
                self.project_data_model.removeRow( index.row() )
        else:
            if str_project_number != self.str_picked_project_number:
                self.pick_up_project( str_project_number )
                self.refresh_dailyreport_list_table()

    def pick_up_project( self, str_project_number ):
        self.str_picked_project_number = str_project_number
        if str_project_number is not None:
            str_stock_name = 'Test'# self.dict_all_project_data[ str_project_number ][ 0 ]
            self.ui.qtCurrentSelectProjectLabel.setText( f"目前選擇專案：{ str_project_number } { str_stock_name }" )
            self.ui.qtCurrentSelectProjectLabel.setStyleSheet("color: yellow; ")
        else:
            self.ui.qtCurrentSelectProjectLabel.setText( "" )

    def refresh_dailyreport_list_table( self ):
        dict_per_project_dailyreport_data = self.dict_all_project_dailyreport_data[ self.str_picked_project_number ]
        
        for index_row,( key_date, value_dict_dailyreport_data ) in enumerate( dict_per_project_dailyreport_data.items() ):
            date_item = QStandardItem( Utility.get_concatenate_date_and_weekday_text( key_date ) )
            date_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            date_item.setFlags( date_item.flags() & ~Qt.ItemIsEditable )
            self.dailyreport_data_model.setItem( index_row, 0, date_item ) 

            e_morning_weather = value_dict_dailyreport_data[ DailyReportData.E_MORNING_WEATHER ]
            e_afternoon_weather = value_dict_dailyreport_data[ DailyReportData.E_AFTERNOON_WEATHER ]
            e_morning_human = value_dict_dailyreport_data[ DailyReportData.E_MORNING_HUMAN ]
            e_afternoon_human = value_dict_dailyreport_data[ DailyReportData.E_AFTERNOON_HUMAN ]

            morning_weather_item = QStandardItem( self.get_weather_text( e_morning_weather ) )
            morning_weather_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            morning_weather_item.setFlags( morning_weather_item.flags() & ~Qt.ItemIsEditable )
            self.dailyreport_data_model.setItem( index_row, 1, morning_weather_item ) 

            afternoon_weather_item = QStandardItem( self.get_weather_text( e_afternoon_weather ) )
            afternoon_weather_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            afternoon_weather_item.setFlags( afternoon_weather_item.flags() & ~Qt.ItemIsEditable )
            self.dailyreport_data_model.setItem( index_row, 2, afternoon_weather_item ) 

            morning_human_item = QStandardItem( self.get_human_text( e_morning_human ) )
            morning_human_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            morning_human_item.setFlags( morning_human_item.flags() & ~Qt.ItemIsEditable )
            self.dailyreport_data_model.setItem( index_row, 3, morning_human_item ) 

            afternoon_human_item = QStandardItem( self.get_human_text( e_afternoon_human ) )
            afternoon_human_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            afternoon_human_item.setFlags( afternoon_human_item.flags() & ~Qt.ItemIsEditable )
            self.dailyreport_data_model.setItem( index_row, 4, afternoon_human_item ) 

            edit_icon_item = QStandardItem("")
            edit_icon_item.setIcon( edit_icon )
            edit_icon_item.setFlags( edit_icon_item.flags() & ~Qt.ItemIsEditable )
            self.dailyreport_data_model.setItem( index_row, len( self.list_dailyreport_list_table_horizontal_header ) - 2, edit_icon_item ) 

            delete_icon_item = QStandardItem("")
            delete_icon_item.setIcon( delete_icon )
            delete_icon_item.setFlags( delete_icon_item.flags() & ~Qt.ItemIsEditable )
            self.dailyreport_data_model.setItem( index_row, len( self.list_dailyreport_list_table_horizontal_header ) - 1, delete_icon_item ) 
        
        for column in range( len( self.list_dailyreport_list_table_horizontal_header ) ):
            if column < len( self.list_dailyreport_list_column_width ):
                self.ui.qtDailyReportListTableView.setColumnWidth( column, self.list_dailyreport_list_column_width[ column ] )
            else:
                self.ui.qtDailyReportListTableView.setColumnWidth( column, 85 )
                self.list_dailyreport_list_column_width.append( 85 )

    def get_weather_text( self, e_weather ):
        if e_weather == Weather.SUN:
            return "晴"
        elif e_weather == Weather.RAIN:
            return "雨"
        elif e_weather == Weather.HEAVY_RAIN:
            return "豪雨"
        elif e_weather == Weather.TYPHOON:
            return "颱風"
        elif e_weather == Weather.HOT:
            return "酷熱"
        elif e_weather == Weather.MUDDY:
            return "泥濘"
        elif e_weather == Weather.OTHER:
            return "其他"

    def get_human_text( self, e_human ):
        if e_human == Human.NONE:
            return "無"
        elif e_human == Human.SUSPENSION:
            return "停工"
        elif e_human == Human.POWER_OFF:
            return "停電"
        elif e_human == Human.OTHER:
            return "其他"

    def on_dailyreport_list_table_horizontal_section_resized( self, n_logical_index, n_old_size, n_new_size ): 
        self.list_dailyreport_list_column_width[ n_logical_index ] = n_new_size
        self.save_UI_state()

    def on_dailyreport_list_table_item_clicked( self, index, stock_list_model ):
        pass

    def on_add_daily_report_data_push_button_clicked( self ):
        dict_per_project_data = self.dict_all_project_data[ self.str_picked_project_number ]
        dict_per_project_dailyreport_data = self.dict_all_project_dailyreport_data[ self.str_picked_project_number ]

        dialog = DailyReportPerDayDialog( self, dict_per_project_data, dict_per_project_dailyreport_data )
        if dialog.exec():
            self.auto_save_project_data()
            self.refresh_dailyreport_list_table()

    def process_all_dailyreport_data( self ): 
        for key_project_number, value_dict_per_project_dailyreport_data in self.dict_all_project_dailyreport_data.items():
            self.process_dailyreport_data( key_project_number )

    def process_dailyreport_data( self, project_number ):
        dict_per_project_data = self.dict_all_project_data[ project_number ]
        dict_per_project_dailyreport_data = self.dict_all_project_dailyreport_data[ project_number ]
        for key in sorted( dict_per_project_dailyreport_data.keys() ):
            dict_per_project_dailyreport_data[ key ] = dict_per_project_dailyreport_data.pop( key )

        e_contract_condition = dict_per_project_data[ ProjectData.E_CONTRACT_CONDITION ]
        n_contract_working_days = dict_per_project_data[ ProjectData.F_INITIAL_CONTRACT_WORKING_DAYS ]
        dict_morning_weather_condition = dict_per_project_data[ ProjectData.DICT_MORNING_WEATHER_CONDITION_DATA ]
        dict_afternoon_weather_condition = dict_per_project_data[ ProjectData.DICT_AFTERNOON_WEATHER_CONDITION_DATA ]
        dict_morning_human_condition = dict_per_project_data[ ProjectData.DICT_MORNING_HUMAN_CONDITION_DATA ]
        dict_afternoon_human_condition = dict_per_project_data[ ProjectData.DICT_AFTERNOON_HUMAN_CONDITION_DATA ]
        obj_date = datetime.datetime.strptime( dict_per_project_data[ ProjectData.STR_START_DATE ], "%Y-%m-%d" )
        dict_holiday_data = dict_per_project_data[ ProjectData.DICT_HOLIDAY_DATA ]
        list_const_holiday = []
        list_const_workday = []
        for key_str_date, value in dict_holiday_data.items():
            if value[ HolidayData.HOLIDAY ]:
                list_const_holiday.append( datetime.datetime.strptime( key_str_date, "%Y-%m-%d") )
            else:
                list_const_workday.append( datetime.datetime.strptime( key_str_date, "%Y-%m-%d") )

        # while( True ):
        #     if n_contract_working_days <= 0:
        #         break
        #     str_date = obj_date.strftime( "%Y-%m-%d" )
        #     e_morning_weather = Weather.SUN
        #     e_afternoon_weather = Weather.SUN
        #     e_morning_human = Human.NONE
        #     e_afternoon_human = Human.NONE
        #     if str_date in dict_per_project_dailyreport_data:
        #         e_morning_weather = dict_per_project_dailyreport_data[ str_date ][ DailyReportData.E_MORNING_WEATHER ]
        #         e_afternoon_weather = dict_per_project_dailyreport_data[ str_date ][ DailyReportData.E_AFTERNOON_WEATHER ]
        #         e_morning_human = dict_per_project_dailyreport_data[ str_date ][ DailyReportData.E_MORNING_HUMAN ]
        #         e_afternoon_human = dict_per_project_dailyreport_data[ str_date ][ DailyReportData.E_AFTERNOON_HUMAN ]

        #     if( e_morning_weather != Weather.SUN or e_morning_human != Human.NONE ):
        #         f_morning_weather_nocount = dict_weather_condition[ e_morning_weather ]
        #         f_morning_human_nocount = dict_human_condition[ e_morning_human ]
        #         pass

        #     b_is_weekend = [False]
        #     b_is_holiday = [False]
        #     b_is_make_up_workday = [False]
        #     if Utility.get_is_work_day( list_const_holiday, list_const_workday, str_date, e_contract_condition, b_is_weekend, b_is_holiday, b_is_make_up_workday ):
                
                
        #         if str_date in dict_per_project_dailyreport_data: #有填日報表
        #             pass
                
        #         pass
        #     else: #非工作日
        #         if str_date in dict_per_project_dailyreport_data: #非工作日，但有填日報表
        #             pass
        #         else:#非工作日，沒填日報表
        #             pass
        #     obj_date += datetime.timedelta( days = 1 )

    def save_UI_state( self ): 
        # 確保目錄存在，若不存在則遞歸創建
        os.makedirs( os.path.dirname( self.UISetting_file_path ), exist_ok = True )

        with open( self.UISetting_file_path, 'w', encoding='utf-8' ) as f:
            f.write( "版本," + 'v1.0.0' + '\n' )
            f.write( "顯示排序," + str( self.ui.qtFromNewToOldAction.isChecked() ) + '\n' )
            f.write( "年度顯示," + str( self.ui.qtADYearAction.isChecked() ) + '\n' )
            f.write( "工程列表欄寬" )
            for i in range( len( self.list_project_list_column_width ) ):
                f.write( f",{ self.list_project_list_column_width[ i ] }" )
            f.write( "\n" )
            f.write( "日報列表欄寬" )
            for i in range( len( self.list_dailyreport_list_column_width ) ):
                f.write( f",{ self.list_dailyreport_list_column_width[ i ] }" )
            f.write( "\n" )

    def load_UI_state( self ): 
        with ( QSignalBlocker( self.ui.qtFromNewToOldAction ),
               QSignalBlocker( self.ui.qtFromOldToNewAction ), 
               QSignalBlocker( self.ui.qtADYearAction ), 
               QSignalBlocker( self.ui.qtROCYearAction )
               ):

            if os.path.exists( self.UISetting_file_path ):
                with open( self.UISetting_file_path, 'r', encoding='utf-8' ) as f:
                    data = f.readlines()
                    for i, row in enumerate( data ):
                        row = row.strip().split( ',' )
                        if row[0] == "版本":
                            continue
                        elif row[0] == "顯示排序":
                            if row[ 1 ] == 'True':
                                self.ui.qtFromNewToOldAction.setChecked( True )
                                self.ui.qtFromOldToNewAction.setChecked( False )
                            else:
                                self.ui.qtFromNewToOldAction.setChecked( False )
                                self.ui.qtFromOldToNewAction.setChecked( True )
                        elif row[0] == "年度顯示":
                            if row[ 1 ] == 'True':
                                self.ui.qtADYearAction.setChecked( True )
                                self.ui.qtROCYearAction.setChecked( False )
                            else:
                                self.ui.qtADYearAction.setChecked( False )
                                self.ui.qtROCYearAction.setChecked( True )
                        elif row[0] == '工程列表欄寬':
                            self.list_project_list_column_width = []
                            for i in range( 1, len( row ) ):
                                self.list_project_list_column_width.append( int( row[ i ] ) )
                        elif row[0] == '日報列表欄寬':
                            self.list_dailyreport_list_column_width = []
                            for i in range( 1, len( row ) ):
                                self.list_dailyreport_list_column_width.append( int( row[ i ] ) )

    def auto_save_project_data( self ): 
        self.manual_save_project_data( self.global_project_data_file_path )

    def manual_save_project_data( self, file_path ): 
        export_json_data = {}
        for key_project_number, value in self.dict_all_project_data.items():
            dict_per_project_data = {}
            dict_per_project_data[ "project_name" ] = value[ ProjectData.STR_PROJECT_NAME ]
            dict_per_project_data[ "contract_number" ] = value[ ProjectData.STR_CONTRACT_NUMBER ]
            dict_per_project_data[ "project_location" ] = value[ ProjectData.STR_PROJECT_LOCATION ]
            dict_per_project_data[ "contract_value" ] = value[ ProjectData.N_CONTRACT_VALUE ]
            dict_per_project_data[ "owner" ] = value[ ProjectData.STR_OWNER ]
            dict_per_project_data[ "supervisor" ] = value[ ProjectData.STR_SUPERSIOR ]
            dict_per_project_data[ "designer" ] = value[ ProjectData.STR_DESIGNER ]
            dict_per_project_data[ "contractor" ] = value[ ProjectData.STR_CONTRACTOR ]
            dict_per_project_data[ "bid_date" ] = value[ ProjectData.STR_BID_DATE ]
            dict_per_project_data[ "start_date" ] = value[ ProjectData.STR_START_DATE ]
            dict_per_project_data[ "contract_condition" ] = int( value[ ProjectData.E_CONTRACT_CONDITION ].value )
            dict_per_project_data[ "contract_working_days" ] = value[ ProjectData.F_INITIAL_CONTRACT_WORKING_DAYS ]
            dict_per_project_data[ "contract_finish_date" ] = value[ ProjectData.STR_INITIAL_CONTRACT_FINISH_DATE ]
            dict_holiday_data = value[ ProjectData.DICT_HOLIDAY_DATA ]
            json_holiday_data = {}
            for key_holiday, value_holiday in dict_holiday_data.items():
                json_holiday_data[ key_holiday ] = { "reason" : value_holiday[ HolidayData.REASON ], 
                                                     "holiday" : bool( value_holiday[ HolidayData.HOLIDAY ] ) }
            dict_per_project_data[ "holiday_data" ] = json_holiday_data

            dict_morning_weather_condition_data = value[ ProjectData.DICT_MORNING_WEATHER_CONDITION_DATA ]
            export_json_morning_weather_condition_data = {}
            export_json_morning_weather_condition_data[ "rain" ]          = float( dict_morning_weather_condition_data[ Weather.RAIN].value )
            export_json_morning_weather_condition_data[ "heavyrain" ]     = float( dict_morning_weather_condition_data[ Weather.HEAVY_RAIN].value )
            export_json_morning_weather_condition_data[ "typhoon" ]       = float( dict_morning_weather_condition_data[ Weather.TYPHOON].value )
            export_json_morning_weather_condition_data[ "hot" ]           = float( dict_morning_weather_condition_data[ Weather.HOT].value )
            export_json_morning_weather_condition_data[ "muddy" ]         = float( dict_morning_weather_condition_data[ Weather.MUDDY].value )
            export_json_morning_weather_condition_data[ "weather_other" ] = float( dict_morning_weather_condition_data[ Weather.WEATHER_OTHER].value )
            dict_per_project_data[ "morning_weather_condition_data" ] = export_json_morning_weather_condition_data

            dict_afternoon_weather_condition_data = value[ ProjectData.DICT_AFTERNOON_WEATHER_CONDITION_DATA ]
            export_json_afternoon_weather_condition_data = {}
            export_json_afternoon_weather_condition_data[ "rain" ]          = float( dict_afternoon_weather_condition_data[ Weather.RAIN].value )
            export_json_afternoon_weather_condition_data[ "heavyrain" ]     = float( dict_afternoon_weather_condition_data[ Weather.HEAVY_RAIN].value )
            export_json_afternoon_weather_condition_data[ "typhoon" ]       = float( dict_afternoon_weather_condition_data[ Weather.TYPHOON].value )
            export_json_afternoon_weather_condition_data[ "hot" ]           = float( dict_afternoon_weather_condition_data[ Weather.HOT].value )
            export_json_afternoon_weather_condition_data[ "muddy" ]         = float( dict_afternoon_weather_condition_data[ Weather.MUDDY].value )
            export_json_afternoon_weather_condition_data[ "weather_other" ] = float( dict_afternoon_weather_condition_data[ Weather.WEATHER_OTHER].value )
            dict_per_project_data[ "afternoon_weather_condition_data" ] = export_json_afternoon_weather_condition_data

            dict_morning_human_condition_data = value[ ProjectData.DICT_MORNING_HUMAN_CONDITION_DATA ]
            export_json_morning_human_condition_data = {}
            export_json_morning_human_condition_data[ "suspension" ]  = float( dict_morning_human_condition_data[ Human.SUSPENSION].value )
            export_json_morning_human_condition_data[ "poweroff" ]    = float( dict_morning_human_condition_data[ Human.POWER_OFF].value )
            export_json_morning_human_condition_data[ "human_other" ] = float( dict_morning_human_condition_data[ Human.HUMAN_OTHER].value )
            dict_per_project_data[ "morning_human_condition_data" ] = export_json_morning_human_condition_data

            dict_afternoon_human_condition_data = value[ ProjectData.DICT_AFTERNOON_HUMAN_CONDITION_DATA ]
            export_json_afternoon_human_condition_data = {}
            export_json_afternoon_human_condition_data[ "suspension" ]  = float( dict_afternoon_human_condition_data[ Human.SUSPENSION].value )
            export_json_afternoon_human_condition_data[ "poweroff" ]    = float( dict_afternoon_human_condition_data[ Human.POWER_OFF].value )
            export_json_afternoon_human_condition_data[ "human_other" ] = float( dict_afternoon_human_condition_data[ Human.HUMAN_OTHER].value )
            dict_per_project_data[ "afternoon_human_condition_data" ] = export_json_afternoon_human_condition_data

            dict_extension_data = value[ ProjectData.DICT_EXTENSION_DATA ]
            json_extension_data = {}
            for key_extension_start_date, value_extension in dict_extension_data.items():
                json_extension_data[ key_extension_start_date ] = { "extension_days" : value_extension[ ExtensionData.EXTENSION_DAYS ], 
                                                                    "reason" : value_extension[ ExtensionData.EXTENSION_REASON ] }
            dict_per_project_data[ "extension_data" ] = json_extension_data
            
            export_json_dailyreport_data = {}
            dict_daily_report = self.dict_all_project_dailyreport_data[ key_project_number ]
            for key_date, value_dailyreport_data in dict_daily_report.items():
                export_json_dailyreport_data[ key_date ] = { "morning_weather": int( value_dailyreport_data[ DailyReportData.E_MORNING_WEATHER ].value ),
                                                             "afternoon_weather": int( value_dailyreport_data[ DailyReportData.E_AFTERNOON_WEATHER ].value ),
                                                             "morning_human": int( value_dailyreport_data[ DailyReportData.E_MORNING_HUMAN ].value ),
                                                             "afternoon_human": int( value_dailyreport_data[ DailyReportData.E_AFTERNOON_HUMAN ].value ) }
            dict_per_project_data[ "dailyreport_data" ] = export_json_dailyreport_data

            export_json_data[ key_project_number ] = dict_per_project_data

        with open( file_path, 'w', encoding='utf-8' ) as f:
            f.write( "v1.0.0" '\n' )
            json.dump( export_json_data, f, ensure_ascii=False, indent=4 )

    def manual_load_project_data( self, file_path ):
        try:
            with open( file_path, 'r', encoding='utf-8' ) as f:
                str_version = f.readline().strip()
                if str_version == "v1.0.0":
                    dict_load_project_data = json.load( f )
                    for key_project_number, value in dict_load_project_data.items():
                        import_json_holiday_data = value[ "holiday_data" ]
                        dict_holiday_data = {}
                        for key_holiday, value_holiday in import_json_holiday_data.items():
                            dict_holiday_data[ key_holiday ] = { HolidayData.REASON : value_holiday[ "reason" ], 
                                                                 HolidayData.HOLIDAY : value_holiday[ "holiday" ] }
                        import_json_morning_weather_condition_data = value[ "morning_weather_condition_data" ]
                        dict_morning_weather_condition_data = {}
                        dict_morning_weather_condition_data[ Weather.RAIN ]          = VariableConditionNoCount( import_json_morning_weather_condition_data[ "rain" ] )
                        dict_morning_weather_condition_data[ Weather.HEAVY_RAIN ]    = VariableConditionNoCount( import_json_morning_weather_condition_data[ "heavyrain" ] )
                        dict_morning_weather_condition_data[ Weather.TYPHOON ]       = VariableConditionNoCount( import_json_morning_weather_condition_data[ "typhoon" ] )
                        dict_morning_weather_condition_data[ Weather.HOT ]           = VariableConditionNoCount( import_json_morning_weather_condition_data[ "hot" ] )
                        dict_morning_weather_condition_data[ Weather.MUDDY ]         = VariableConditionNoCount( import_json_morning_weather_condition_data[ "muddy" ] )
                        dict_morning_weather_condition_data[ Weather.WEATHER_OTHER ] = VariableConditionNoCount( import_json_morning_weather_condition_data[ "weather_other" ] )
                        
                        import_json_afternoon_weather_condition_data = value[ "afternoon_weather_condition_data" ]
                        dict_afternoon_weather_condition_data = {}
                        dict_afternoon_weather_condition_data[ Weather.RAIN ]          = VariableConditionNoCount( import_json_afternoon_weather_condition_data[ "rain" ] )
                        dict_afternoon_weather_condition_data[ Weather.HEAVY_RAIN ]    = VariableConditionNoCount( import_json_afternoon_weather_condition_data[ "heavyrain" ] )
                        dict_afternoon_weather_condition_data[ Weather.TYPHOON ]       = VariableConditionNoCount( import_json_afternoon_weather_condition_data[ "typhoon" ] )
                        dict_afternoon_weather_condition_data[ Weather.HOT ]           = VariableConditionNoCount( import_json_afternoon_weather_condition_data[ "hot" ] )
                        dict_afternoon_weather_condition_data[ Weather.MUDDY ]         = VariableConditionNoCount( import_json_afternoon_weather_condition_data[ "muddy" ] )
                        dict_afternoon_weather_condition_data[ Weather.WEATHER_OTHER ] = VariableConditionNoCount( import_json_afternoon_weather_condition_data[ "weather_other" ] )

                        import_json_morning_human_condition_data = value[ "morning_human_condition_data" ]
                        dict_morning_human_condition_data = {}
                        dict_morning_human_condition_data[ Human.SUSPENSION ]  = VariableConditionNoCount( import_json_morning_human_condition_data[ "suspension" ] )
                        dict_morning_human_condition_data[ Human.POWER_OFF ]   = VariableConditionNoCount( import_json_morning_human_condition_data[ "poweroff" ] )
                        dict_morning_human_condition_data[ Human.HUMAN_OTHER ] = VariableConditionNoCount( import_json_morning_human_condition_data[ "human_other" ] )

                        import_json_afternoon_human_condition_data = value[ "afternoon_human_condition_data" ]
                        dict_afternoon_human_condition_data = {}
                        dict_afternoon_human_condition_data[ Human.SUSPENSION ]  = VariableConditionNoCount( import_json_afternoon_human_condition_data[ "suspension" ] )
                        dict_afternoon_human_condition_data[ Human.POWER_OFF ]   = VariableConditionNoCount( import_json_afternoon_human_condition_data[ "poweroff" ] )
                        dict_afternoon_human_condition_data[ Human.HUMAN_OTHER ] = VariableConditionNoCount( import_json_afternoon_human_condition_data[ "human_other" ] )


                        dict_extension_data = {}
                        import_json_extension_data = value[ "extension_data" ]
                        for key_extension_start_date, value_extension in import_json_extension_data.items():
                            dict_extension_data[ key_extension_start_date ] = { ExtensionData.EXTENSION_DAYS : value_extension[ "extension_days" ], 
                                                                                ExtensionData.EXTENSION_REASON : value_extension[ "reason" ] }

                        self.dict_all_project_data[ key_project_number ] = Utility.create_project_data( key_project_number,
                                                                                                        value[ "project_name" ],
                                                                                                        value[ "contract_number" ],
                                                                                                        value[ "project_location" ],
                                                                                                        value[ "contract_value" ],
                                                                                                        value[ "owner" ],
                                                                                                        value[ "supervisor" ],
                                                                                                        value[ "designer" ],
                                                                                                        value[ "contractor" ],
                                                                                                        value[ "bid_date" ],
                                                                                                        value[ "start_date" ],
                                                                                                        ContractCondition( value[ "contract_condition" ] ),
                                                                                                        value[ "contract_working_days" ],
                                                                                                        value[ "contract_finish_date" ],
                                                                                                        dict_holiday_data,
                                                                                                        dict_morning_weather_condition_data,
                                                                                                        dict_afternoon_weather_condition_data,
                                                                                                        dict_morning_human_condition_data,
                                                                                                        dict_afternoon_human_condition_data,
                                                                                                        dict_extension_data )
                        export_json_dailyreport_data = {}
                        import_json_daily_report = value[ "dailyreport_data" ]
                        for key_date, value_dailyreport_data in import_json_daily_report.items():
                            export_json_dailyreport_data[ key_date ] = { DailyReportData.E_MORNING_WEATHER : Weather( value_dailyreport_data[ "morning_weather" ] ),
                                                                         DailyReportData.E_AFTERNOON_WEATHER : Weather( value_dailyreport_data[ "afternoon_weather" ] ),
                                                                         DailyReportData.E_MORNING_HUMAN : Human( value_dailyreport_data[ "morning_human" ] ),
                                                                         DailyReportData.E_AFTERNOON_HUMAN : Human( value_dailyreport_data[ "afternoon_human" ] ) }

                        self.dict_all_project_dailyreport_data[ key_project_number ] = export_json_dailyreport_data
        except FileNotFoundError:
            print(f"檔案 {file_path} 找不到")

    def auto_save_global_holiday_data( self ): 
        self.manual_save_global_holiday_data( self.global_holiday_file_path )

    def manual_save_global_holiday_data( self, file_path ): 
        dict_save_holiday_data = {}
        for key,value in self.dict_global_holiday_data.items():
            dict_save_holiday_data[ key ] = { "reason" : str( value[ HolidayData.REASON ] ), 
                                              "holiday" : bool( value[ HolidayData.HOLIDAY ] ) }

        with open( file_path, 'w', encoding='utf-8' ) as f:
            f.write( "v1.0.0" '\n' )
            json.dump( dict_save_holiday_data, f, ensure_ascii=False, indent=4 )

    def manual_load_global_holiday_data( self, file_path ):
        try:
            with open( file_path, 'r', encoding='utf-8' ) as f:
                str_version = f.readline().strip()
                if str_version == "v1.0.0":
                    dict_load_holiday_data = json.load( f )
                    for key,value in dict_load_holiday_data.items():
                        self.dict_global_holiday_data[ key ] = { HolidayData.REASON : value[ "reason" ], 
                                                                 HolidayData.HOLIDAY : value[ "holiday" ] }
        except FileNotFoundError:
            print(f"檔案 {file_path} 找不到")

    def show_warning_message_box_with_ok_cancel_button( self, str_title, str_message ): 
        message_box = QMessageBox( self )
        message_box.setIcon( QMessageBox.Warning )  # 設置為警告圖示
        message_box.setWindowTitle( str_title )
        message_box.setText( str_message )

        # 添加自訂按鈕
        button_ok = message_box.addButton("確定", QMessageBox.AcceptRole)
        button_cancel = message_box.addButton("取消", QMessageBox.RejectRole)

        message_box.exec()

        if message_box.clickedButton() == button_ok:
            return True
        elif message_box.clickedButton() == button_cancel:
            return False

def run_app():
    app = QApplication( sys.argv )
    app.setStyle('Fusion')
    window = MainWindow( False, 
                        'UISetting.config',
                        'GlobalHoliday.txt' )

    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit( run_app() )

