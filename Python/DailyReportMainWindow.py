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
from QtDailyReportMainWindow import Ui_MainWindow  # 導入轉換後的 UI 類
import logging
# from QtStockCapitalIncreaseEditDialog import Ui_Dialog as Ui_StockCapitalIncreaseDialog
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

class TradingType( IntEnum ):
    TEMPLATE = 0
    SELL = 1
    BUY = 2
    REGULAR_BUY = 3
    CAPITAL_INCREASE = 4
    DIVIDEND = 5
    CAPITAL_REDUCTION = 6

class TradingFeeType( Enum ):
    VARIABLE = 0
    CONSTANT = 1

class EditTabTitleDialog( QDialog ):
    """一個小對話框用於編輯 Tab 標題"""
    def __init__( self, current_title, parent = None ):
        super().__init__( parent )
        self.setWindowTitle( "修改名稱" )
        self.resize( 300, 100 )

        self.layout = QVBoxLayout( self )

        self.label = QLabel("輸入名稱:")
        self.layout.addWidget( self.label )

        self.line_edit = QLineEdit( self )
        self.line_edit.setText( current_title )
        self.line_edit.selectAll()
        self.layout.addWidget( self.line_edit )

        self.horizontalLayout_4 = QHBoxLayout()
        self.qtOkPushButton = QPushButton( self )
        self.qtOkPushButton.setText( "確認" )
        self.qtCancelPushButton = QPushButton( self )
        self.qtCancelPushButton.setText( "取消" )

        self.horizontalLayout_4.addWidget(self.qtOkPushButton)
        self.horizontalLayout_4.addWidget(self.qtCancelPushButton)

        self.qtOkPushButton.clicked.connect( self.accept )
        self.qtCancelPushButton.clicked.connect( self.reject )

        self.layout.addLayout( self.horizontalLayout_4 )

    def get_new_title(self):
        """返回用戶輸入的標題"""
        return self.line_edit.text()

class StockTradingEditDialog( QDialog ):
    def __init__( self, str_stock_number, str_stock_name, b_etf, b_discount, f_discount_value, parent = None ):
        super().__init__( parent )

        self.ui = Ui_StockTradingDialog()
        self.ui.setupUi( self )
        
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

        self.ui.qtStockNumberLabel.setText( str_stock_number )
        self.ui.qtStockNameLabel.setText( str_stock_name )
        obj_current_date = datetime.datetime.today()
        self.ui.qtDateEdit.setDate( obj_current_date.date() )
        self.ui.qtDateEdit.setCalendarPopup( True )
        self.ui.qtDiscountCheckBox.setChecked( b_discount )
        self.ui.qtDiscountRateDoubleSpinBox.setValue( f_discount_value * 10 )
        self.ui.qtDiscountRateDoubleSpinBox.setEnabled( b_discount )

        self.ui.qtDiscountCheckBox.stateChanged.connect( self.on_discount_check_box_state_changed )
        self.ui.qtDiscountRateDoubleSpinBox.valueChanged.connect( self.compute_cost )
        self.ui.qtBuyRadioButton.toggled.connect( self.compute_cost )
        self.ui.qtSellRadioButton.toggled.connect( self.compute_cost )
        self.ui.qtCommonTradeRadioButton.toggled.connect( self.on_trading_type_changed )
        self.ui.qtOddTradeRadioButton.toggled.connect( self.on_trading_type_changed )
        self.ui.qtPriceDoubleSpinBox.valueChanged.connect( self.compute_cost )
        self.ui.qtCommonTradeCountSpinBox.valueChanged.connect( self.compute_cost )
        self.ui.qtOddTradeCountSpinBox.valueChanged.connect( self.compute_cost )
        self.ui.qtOkPushButton.clicked.connect( self.accept_data )
        self.ui.qtCancelPushButton.clicked.connect( self.cancel )
        self.b_etf = b_etf
        self.str_stock_name = str_stock_name
        # self.load_stylesheet("style.css")
        self.dict_trading_data = {}

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def on_discount_check_box_state_changed( self, state ):
        if state == 2:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( True )
        else:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( False )

        self.compute_cost()

    def setup_trading_date( self, str_date ):
        self.ui.qtDateEdit.setDate( datetime.datetime.strptime( str_date, "%Y-%m-%d" ).date() )

    def setup_trading_type( self, e_trading_type ):
        if e_trading_type == TradingType.BUY:
            self.ui.qtBuyRadioButton.setChecked( True )
        else:
            self.ui.qtSellRadioButton.setChecked( True )

    def setup_trading_discount( self, f_discount_value ):
        if f_discount_value != 1:
            self.ui.qtDiscountCheckBox.setChecked( True )
            self.ui.qtDiscountRateDoubleSpinBox.setValue( f_discount_value * 10 )
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( True )
        else:
            self.ui.qtDiscountCheckBox.setChecked( False )
            self.ui.qtDiscountRateDoubleSpinBox.setValue( 6 )
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( False )

    def setup_trading_price( self, f_price ):
        self.ui.qtPriceDoubleSpinBox.setValue( f_price )

    def setup_trading_count( self, f_count ):
        if f_count % 1000 == 0:
            self.ui.qtCommonTradeRadioButton.setChecked( True )
            self.ui.qtCommonTradeCountSpinBox.setValue( f_count / 1000 )
            self.ui.qtOddTradeCountSpinBox.setValue( 0 )
        else:
            self.ui.qtOddTradeRadioButton.setChecked( True )
            self.ui.qtCommonTradeCountSpinBox.setValue( 0 )
            self.ui.qtOddTradeCountSpinBox.setValue( f_count )

    def setup_daying_trading( self, b_daying_trading ):
        if b_daying_trading:
            self.ui.qtDayingTradingCheckBox.setChecked( True )
        else:
            self.ui.qtDayingTradingCheckBox.setChecked( False )

    def accept_data( self ):

        if float( self.ui.qtTotalCostLineEdit.text().replace( ',', '' ) ) != 0:
            
            self.dict_trading_data = Utility.generate_trading_data( self.ui.qtDateEdit.date().toString( "yyyy-MM-dd" ), #交易日期
                                                                    self.get_trading_type(),                            #交易種類
                                                                    self.ui.qtPriceDoubleSpinBox.value(),               #交易價格
                                                                    self.get_trading_count(),                           #交易股數
                                                                    TradingFeeType.VARIABLE,                            #手續費種類
                                                                    self.get_trading_fee_discount(),                    #手續費折扣
                                                                    0,                                                  #手續費最低金額
                                                                    0,                                                  #手續費固定金額
                                                                    0,                                                  #每股股票股利
                                                                    0,                                                  #每股現金股利
                                                                    0,                                                  #每股減資金額
                                                                    self.ui.qtDayingTradingCheckBox.isChecked() )       #是否為當沖交易                                          
            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

    def on_trading_type_changed( self ):
        if self.ui.qtCommonTradeRadioButton.isChecked():
            self.ui.qtCommonTradeCountSpinBox.setEnabled( True )
            self.ui.qtOddTradeCountSpinBox.setEnabled( False )
        else:
            self.ui.qtCommonTradeCountSpinBox.setEnabled( False )
            self.ui.qtOddTradeCountSpinBox.setEnabled( True )

        self.compute_cost()

    def get_trading_type( self ):
        if self.ui.qtBuyRadioButton.isChecked():
            return TradingType.BUY
        else:
            return TradingType.SELL

    def get_trading_count( self ):
        if self.ui.qtCommonTradeRadioButton.isChecked():
            return self.ui.qtCommonTradeCountSpinBox.value() * 1000
        else:
            return self.ui.qtOddTradeCountSpinBox.value()
        
    def get_trading_fee_discount( self ):
        if self.ui.qtDiscountCheckBox.isChecked():
            return self.ui.qtDiscountRateDoubleSpinBox.value() / 10
        else:
            return 1

    def compute_cost( self ):
        e_trading_type = self.get_trading_type()
        f_trading_price = self.ui.qtPriceDoubleSpinBox.value()
        n_trading_count = self.get_trading_count()
        f_trading_fee_discount = self.get_trading_fee_discount() 
        b_bond = True if '債' in self.str_stock_name else False
        dict_result = Utility.compute_cost( e_trading_type, f_trading_price, n_trading_count, f_trading_fee_discount, self.b_etf, False, b_bond )

        if e_trading_type == TradingType.BUY:
            self.ui.qtTradingValueLineEdit.setText( format( dict_result[ TradingCost.TRADING_VALUE ], ',' ) )
            self.ui.qtTotalCostLineEdit.setText( format( dict_result[ TradingCost.TRADING_TOTAL_COST ], ',' ) )
        elif e_trading_type == TradingType.SELL:
            self.ui.qtTradingValueLineEdit.setText( format( -dict_result[ TradingCost.TRADING_VALUE ], ',' ) )
            self.ui.qtTotalCostLineEdit.setText( format( -dict_result[ TradingCost.TRADING_TOTAL_COST ], ',' ) )
        self.ui.qtFeeLineEdit.setText( format( dict_result[ TradingCost.TRADING_FEE ], ',' ) )
        self.ui.qtTaxLineEdit.setText( format( dict_result[ TradingCost.TRADING_TAX ], ',' ) )

class SaveCheckDialog( QDialog ):
    def __init__( self, str_title = '', parent = None ):
        super().__init__( parent )

        self.ui = Ui_SaveCheckDialog()
        self.ui.setupUi( self )
        self.setWindowTitle( str_title )
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )

        self.ui.qtSavePushButton.clicked.connect( self.save )
        self.ui.qtNoSavePushButton.clicked.connect( self.no_save )
        self.ui.qtAbortPushButton.clicked.connect( self.abort )
        self.n_return = 0

    def save( self ):
        self.n_return = 1
        self.accept()

    def no_save( self ):
        self.n_return = 2
        self.accept()
    
    def abort( self ):
        self.n_return = 3
        self.accept()

class MainWindow( QMainWindow ):
    def __init__( self, b_unit_test = False, 
                  str_initial_data_file = 'TradingData.json', 
                  str_UI_setting_file = 'UISetting.config', 
                  str_stock_number_file = 'StockNumber.txt',
                  str_stock_price_file = 'StockPrice.txt'  ):
        super( MainWindow, self ).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )  # 設置 UI
        window_icon = QIcon( window_icon_file_path ) 
        self.setWindowIcon( window_icon )
        
        delegate = CenterIconDelegate()

        self.ui.qtMainHolidayDBSettingAction.triggered.connect( self.on_trigger_show_all )

        self.load_stylesheet( styles_css_path )
        # if b_unit_test:
        #     self.initialize( True, None )
        #     self.load_initialize_data()
        # else:
        #     self.start_loading_stock_data()

    def load_stylesheet( self, file_path ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # 指定 UTF-8 編碼
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS 檔案 {file_path} 找不到")
        except Exception as e:
            print(f"讀取 CSS 檔案時發生錯誤: {e}")

    def on_trigger_show_all( self ):
        pass


def run_app():
    app = QApplication( sys.argv )
    app.setStyle('Fusion')
    window = MainWindow( False, 
                        'TradingData.json',
                        'UISetting.config',
                        'StockNumber.txt',
                        'StockPrice.txt' )

    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit( run_app() )

