from enum import Enum
from datetime import datetime, date
import dateutil


class DateHelper:

    class DateFormats(Enum):
        D_YYMMDD = "yy-MM-dd"
        D_DDMMyy = "dd-MM-yy"
        D_YYMMDD_N = "yy-MMM-dd" 
        D_DDMMyy_N = "dd-MMM-yy"
        D_YYMMDDHHMMA_N = "yy-MMM-dd, hh:mma"
        D_DDMMyyHHMMA_N = "dd-MMM-yy, hh:mma"
        S_YYMMDD = "yy/MM/dd"
        S_DDMMyy = "dd/MM/yy"
        S_YYMMDDHHMMA = "yy/MM/dd, hh:mma"
        S_DDMMyyHHMMA = "dd/MM/yy, hh:mma"
        S_YYMMDDHHMMA_N = "yy/MMM/dd, hh:mma"
        S_DDMMyyHHMMA_N = "dd/MMM/yy, hh:mma"
        D_YYYYMMDD = "yyyy-MM-dd"
        D_DDMMYYYY = "dd-MM-yyyy"
        D_YYYYMMDDHHMMA = "yyyy-MM-dd, hh:mma"
        D_DDMMYYYYHHMMA = "dd-MM-yyyy, hh:mma"
        D_YYYYMMDD_N = "yyyy-MMM-dd"
        D_DDMMYYYY_N = "dd-MMM-yyyy"
        D_YYYYMMDDHHMMA_N = "yyyy-MMM-dd, hh:mma"
        D_DDMMYYYYHHMMA_N = "dd-MMM-yyyy, hh:mma"
        S_YYYYMMDD = "yyyy/MM/dd"
        S_DDMMYYYY = "dd/MM/yyyy"
        S_YYYYMMDDHHMMA = "yyyy/MM/dd, hh:mma"
        S_DDMMYYYYHHMMA = "dd/MM/yyyy, hh:mma"
        S_YYYYMMDDHHMMA_N = "yyyy/MMM/dd, hh:mma"
        S_DDMMYYYYHHMMA_N = "dd/MMM/yyyy, hh:mma"
        D_YYMMDDHHMMSSA_N = "yy-MMM-dd, hh:mm:ssa"
        D_DDMMyyHHMMSSA_N = "dd-MMM-yy, hh:mm:ssa"
        S_YYMMDDHHMMSSA = "yy/MM/dd, hh:mm:ssa"
        S_DDMMyyHHMMSSA = "dd/MM/yy, hh:mm:ssa"
        S_YYMMDDHHMMSSA_N = "yy/MMM/dd, hh:mm:ssa"
        S_DDMMyyHHMMSSA_N = "dd/MMM/yy, hh:mm:ssa"
        D_YYYYMMDDHHMMSSA = "yyyy-MM-dd, hh:mm:ssa"
        D_DDMMYYYYHHMMSSA = "dd-MM-yyyy, hh:mm:ssa"
        D_YYYYMMDDHHMMSSA_N = "yyyy-MMM-dd, hh:mm:ssa"
        D_DDMMYYYYHHMMSSA_N = "dd-MMM-yyyy, hh:mm:ssa"
        S_YYYYMMDDHHMMSSA = "yyyy/MM/dd, hh:mm:ssa"
        S_DDMMYYYYHHMMSSA = "dd/MM/yyyy, hh:mm:ssa"
        S_YYYYMMDDHHMMSSA_N = "yyyy/MMM/dd, hh:mm:ssa"
        S_DDMMYYYYHHMMSSA_N = "dd/MMM/yyyy, hh:mm:ssa"
        HHMMA = "hh:mma"
        HHMM = "hh:mm"
        HHMMSSA = "hh:mm:ssa"
        HHMMSS = "hh:mm:ss"

    @staticmethod
    def prettifyDate(timestamp:int | str) -> str:
        if isinstance(timestamp, int):
            d1 = datetime.fromtimestamp(timestamp)
        elif isinstance(timestamp, str):
            d1 = datetime.strptime(timestamp, "%d %b %I:%M %p")
        else:
            raise ValueError()
        today = date.today()
        if d1.date() == today:
            prettifiedDate = d1.strftime("%I:%M %p")
        else:
            prettifiedDate = d1.strftime("%d %b %I:%M %p")
        return prettifiedDate
    
    @staticmethod
    def getDateOnly(timestamp:int | str) -> str | int:
        if isinstance(timestamp, int):
            return ""
        elif isinstance(timestamp, str):
            return 2
        else:
            raise ValueError()
        
    @staticmethod
    def getDateAndTime(timestamp: int | str) -> str:
        if isinstance(timestamp, int):
            return ""
        elif isinstance(timestamp, str):
            return ""
        else:
            raise ValueError()
        
    @staticmethod
    def getTimeOnly(timestamp: int) -> str:
        return ""
    
    @staticmethod
    def getTodayWithTime() -> str:
        return ""
    
    @staticmethod
    def getToday() -> str:
        return ""
    
    @staticmethod
    def getTomorrow() -> str:
        return ""
    
    @staticmethod
    def getDaysBetweenTwoDate(old:str, new:str, dateFormat:str) -> int:
        return 2
        
    @staticmethod
    def getHoursBetweenTwoDate(old:str, new:str, dateFormat:str) -> int:
        return 2
    
    @staticmethod
    def getMinutesBetweenTwoDate(old:str, new:str, dateFormat:str) -> int:
        return 2
    
    @staticmethod
    def parseAnyDate(date:str) -> int:
        return 2
    
    @staticmethod
    def parseDate(date:str, dateformats:DateFormats) -> int:
        return 2
    
    @staticmethod
    def getDesiredFormat(dataFormats:DateFormats) -> str:
        return ""
    
    @staticmethod
    def getDesiredFormat(dateFormats:DateFormats, date:int) -> str:
        return ""

    


if __name__ == "__main__":
    print(DateHelper.prettifyDate(11000000000))
    print(DateHelper.prettifyDate("12 5 4:23 AM"))
