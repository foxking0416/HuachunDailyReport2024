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
from logging.handlers import TimedRotatingFileHandler
import logging
from QtDailyReportMainWindow import Ui_MainWindow  # 導入轉換後的 UI 類
from QtCreateProjectPage1Dialog import Ui_Dialog as Ui_CreateProjectPage1Dialog
from QtCreateProjectPage2Dialog import Ui_Dialog as Ui_CreateProjectPage2Dialog
from QtDailyReportPerDayDialog import Ui_Dialog as Ui_DailyReportPerDayDialog
from QtSelectEditProjectDialog import Ui_Dialog as Ui_SelectEditProjectDialog
from QtMainDBHolidaySettingDialog import Ui_Dialog as Ui_MainDBHolidaySettingDialog
from QtVariableConditionSettingDialog import Ui_Dialog as Ui_VariableConditionSettingDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QButtonGroup, QMessageBox, QStyledItemDelegate, QFileDialog, QHeaderView, QVBoxLayout, QHBoxLayout, \
                              QLabel, QLineEdit, QDialogButtonBox, QTabBar, QWidget, QTableView, QComboBox, QPushButton, QSizePolicy, QSpacerItem, QCheckBox, QDoubleSpinBox, \
                              QProgressBar, QTabWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon, QBrush
from PySide6.QtCore import Qt, QModelIndex, QRect, QSignalBlocker, QSize, QThread, QObject, Signal
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, PatternFill, Font, Border, Side
from enum import Enum, IntEnum
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
# pyside6-uic QtCreateProjectPage1Dialog.ui -o QtCreateProjectPage1Dialog.py
# pyside6-uic QtCreateProjectPage2Dialog.ui -o QtCreateProjectPage2Dialog.py
# pyside6-uic QtMainDBHolidaySettingDialog.ui -o QtMainDBHolidaySettingDialog.py
# pyside6-uic QtVariableConditionSettingDialog.ui -o QtVariableConditionSettingDialog.py
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


class HolidayData( Enum ):
    REASON = 0
    HOLIDAY = 1

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

class CreateProjectPage1Dialog( QDialog ):
    def __init__( self, parent = None ):
        super().__init__( parent )

        self.ui = Ui_CreateProjectPage1Dialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )
        self.ui.qtNextStepPushButton.clicked.connect( self.next_step )
        self.ui.qtCancelPushButton.clicked.connect( self.cancel )

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def next_step( self ):
        if True:
            self.accept()
            dialog = CreateProjectPage2Dialog(  self )
            if dialog.exec():
                pass
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

class CreateProjectPage2Dialog( QDialog ):
    def __init__( self, parent = None ):
        super().__init__( parent )

        self.ui = Ui_CreateProjectPage2Dialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )
        self.ui.qtOkPushButton.clicked.connect( self.accept_data )
        self.ui.qtCancelPushButton.clicked.connect( self.cancel )
        self.ui.qtConstantConditionSettingPushButton.clicked.connect( self.constant_condition_setting )
        self.ui.qtVariableConditionSettingPushButton.clicked.connect( self.variable_condition_setting )

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def constant_condition_setting( self ):
        dialog = VariableConditionSettingDialog(  self )
        if dialog.exec():
            pass

    def variable_condition_setting( self ):
        dialog = VariableConditionSettingDialog(  self )
        if dialog.exec():
            pass

    def accept_data( self ):
        if True:
            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

class MainDBHolidaySettingDialog( QDialog ):
    def __init__( self, dict_global_holiday_data, parent = None ):
        super().__init__( parent )

        self.ui = Ui_MainDBHolidaySettingDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

        obj_current_date = datetime.datetime.today()
        self.ui.qtDateEdit.setDate( obj_current_date.date() )

        delegate = CenterIconDelegate()

        self.list_table_horizontal_header = [ '日期', '星期', '理由', '放假/補班', '刪除' ]
        self.holiday_data_model = QStandardItemModel( 0, 0 ) 
        self.holiday_data_model.setHorizontalHeaderLabels( self.list_table_horizontal_header )
        # self.holiday_data_model.setHorizontalHeaderLabels( self.get_trading_data_header() )
        self.ui.qtTableView.setModel( self.holiday_data_model )
        self.ui.qtTableView.setItemDelegate( delegate )
        self.ui.qtTableView.verticalHeader().hide()
        self.ui.qtTableView.clicked.connect( lambda index: self.on_table_item_clicked( index, self.holiday_data_model ) )

        self.ui.qtAddPushButton.clicked.connect( self.add_data )
        self.ui.qtExitPushButton.clicked.connect( self.accept )
        self.dict_global_holiday_data = dict_global_holiday_data
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
        b_holiday = self.ui.qtHolidayRadioButton.isChecked()

        if str_date in self.dict_global_holiday_data:
            # TODO: show error message
            return
        else:
            self.dict_global_holiday_data[ str_date ] = {}
            self.dict_global_holiday_data[ str_date ][ HolidayData.REASON ] = str_reason
            self.dict_global_holiday_data[ str_date ][ HolidayData.HOLIDAY ] = b_holiday

        self.refresh_table()

    def on_table_item_clicked( self, index, stock_list_model ):
        if index.column() == 4:
            result = self.show_warning_message_box_with_ok_cancel_button( "警告", f"確定要刪掉這筆假日/補班資料嗎?" )
            if result:
                # delete icon
                date_item = self.holiday_data_model.item( index.row(), 0 )
                str_date = date_item.text()
                del self.dict_global_holiday_data[ str_date ]
                self.holiday_data_model.removeRow( index.row() )

    def refresh_table( self ):
        for index_row,( key_date, value_dict_holiday_data ) in enumerate( self.dict_global_holiday_data.items() ):
            date_item = QStandardItem( key_date )
            date_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            date_item.setFlags( date_item.flags() & ~Qt.ItemIsEditable )
            # standard_item.setData( key_stock_number, Qt.UserRole )
            self.holiday_data_model.setItem( index_row, 0, date_item ) 

            obj_date = datetime.datetime.strptime( key_date, "%Y-%m-%d")
            n_weekday = obj_date.weekday()
            if n_weekday == 0:
                str_weekday = "(一)"
            elif n_weekday == 1:
                str_weekday = "(二)"
            elif n_weekday == 2:
                str_weekday = "(三)"
            elif n_weekday == 3:
                str_weekday = "(四)"
            elif n_weekday == 4:
                str_weekday = "(五)"
            elif n_weekday == 5:
                str_weekday = "(六)"
            else:
                str_weekday = "(日)"

            weekday_item = QStandardItem( str_weekday )
            weekday_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            weekday_item.setFlags( weekday_item.flags() & ~Qt.ItemIsEditable )
            # standard_item.setData( key_stock_number, Qt.UserRole )
            self.holiday_data_model.setItem( index_row, 1, weekday_item ) 

            reason_item = QStandardItem( value_dict_holiday_data[ HolidayData.REASON ] )
            reason_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            reason_item.setFlags( reason_item.flags() & ~Qt.ItemIsEditable )
            # standard_item.setData( key_stock_number, Qt.UserRole )
            self.holiday_data_model.setItem( index_row, 2, reason_item ) 

            if value_dict_holiday_data[ HolidayData.HOLIDAY ]:
                is_holiday_item = QStandardItem( "放假" )
            else:
                is_holiday_item = QStandardItem( "補班" )
            is_holiday_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            is_holiday_item.setFlags( is_holiday_item.flags() & ~Qt.ItemIsEditable )
            # standard_item.setData( key_stock_number, Qt.UserRole )
            self.holiday_data_model.setItem( index_row, 3, is_holiday_item ) 

            delete_icon_item = QStandardItem("")
            delete_icon_item.setIcon( delete_icon )
            delete_icon_item.setFlags( delete_icon_item.flags() & ~Qt.ItemIsEditable )
            # standard_item.setData( key_stock_number, Qt.UserRole )
            self.holiday_data_model.setItem( index_row, 4, delete_icon_item ) 

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
        
    def accept_data( self ):
        if True:
            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

class VariableConditionSettingDialog( QDialog ):
    def __init__( self, parent = None ):
        super().__init__( parent )

        self.ui = Ui_VariableConditionSettingDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )
        self.ui.qtOkPushButton.clicked.connect( self.accept_data )
        self.ui.qtCancelPushButton.clicked.connect( self.cancel )

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
        if True:
            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

class SelectEditProjectDialog( QDialog ):
    def __init__( self, parent = None ):
        super().__init__( parent )

        self.ui = Ui_SelectEditProjectDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

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
        if True:
            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

class DailyReportPerDayDialog( QDialog ):
    def __init__( self, parent = None ):
        super().__init__( parent )

        self.ui = Ui_DailyReportPerDayDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

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
        if True:
            self.accept()
        else:
            self.reject()
    
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
                  str_global_holiday_file = 'GlobalHoliday.txt'  ):
        super( MainWindow, self ).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )  # 設置 UI
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )
        
        if not b_unit_test:
            self.progress_bar = QProgressBar( self )
            self.progress_bar.setGeometry( 400, 350, 300, 25 )  # Adjust position and size as needed
            self.progress_bar.setMaximum( 100 )
            self.progress_bar.setVisible( False )
        
        delegate = CenterIconDelegate()

        self.ui.qtMainHolidayDBSettingAction.triggered.connect( self.on_trigger_main_holiday_db_setting )
        self.ui.qtCreateNewProjectAction.triggered.connect( self.on_trigger_create_new_project )
        self.ui.qtEditProjectAction.triggered.connect( self.on_trigger_edit_project )
        self.ui.qtSelectProjectAction.triggered.connect( self.on_trigger_select_project )
        self.ui.qtCreateNewDailyReportAction.triggered.connect( self.on_trigger_create_new_daily_report )
        self.ui.qtEditDailyReportAction.triggered.connect( self.on_trigger_edit_daily_report )

        self.global_holiday_file_path = os.path.join( g_data_dir, 'DailyReport', str_global_holiday_file )

        self.global_holiday_data = {}

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
        self.manual_load_data( self.global_holiday_file_path )

    def on_trigger_main_holiday_db_setting( self ):
        dialog = MainDBHolidaySettingDialog( self.global_holiday_data, self )
        if dialog.exec():
            self.auto_save_data()

    def on_trigger_create_new_project( self ):
        dialog = CreateProjectPage1Dialog(  self )
        if dialog.exec():
            pass

    def on_trigger_edit_project( self ):
        dialog = SelectEditProjectDialog(  self )
        if dialog.exec():
            pass

    def on_trigger_select_project( self ):
        pass

    def on_trigger_create_new_daily_report( self ):
        pass

    def on_trigger_edit_daily_report( self ):   
        pass

    def auto_save_data( self ): 
        self.manual_save_data( self.global_holiday_file_path )
        pass

    def manual_save_data( self, file_path ): 
        dict_save_holiday_data = {}
        for key,value in self.global_holiday_data.items():
            dict_save_holiday_data[ key ] = { "reason" : str( value[ HolidayData.REASON ] ), "holiday" : bool( value[ HolidayData.HOLIDAY ] ) }

        with open( file_path, 'w', encoding='utf-8' ) as f:
            f.write( "v1.0.0" '\n' )
            json.dump( dict_save_holiday_data, f, ensure_ascii=False, indent=4 )

    def manual_load_data( self, file_path ):
        try:
            with open( file_path, 'r', encoding='utf-8' ) as f:
                str_version = f.readline().strip()
                if str_version == "v1.0.0":
                    dict_load_holiday_data = json.load( f )
                    for key,value in dict_load_holiday_data.items():
                        self.global_holiday_data[ key ] = { HolidayData.REASON : value[ "reason" ], HolidayData.HOLIDAY : value[ "holiday" ] }
        except FileNotFoundError:
            print(f"檔案 {file_path} 找不到")

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

