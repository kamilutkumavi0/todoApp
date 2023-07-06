from lib.date import Date
import datetime
from termcolor import colored
""" 
Todo girdimis görev ne zaman girdimizi soyler


"""
class Todo:
    priority_select = "priority"
    def __init__(self,
                 mission: str,
                 priority: int
                 ):
        
        self.publish_date: Date = Date(datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
        self.priority = priority
        self.mission = mission
    @classmethod
    def set(cls, priority_select: str):
        """
        todo objesinin sıralama formatını değiştirir
        """
        cls.priority_select = priority_select
    def __gt__(self, other):
        if self.priority_select == "priority":
            if self.priority > other.priority:
                return True
            return False
        if self.priority_select == "priority":
            if self.publish_date > other.publish_date:
                return True
            return False
    def __eq__(self, other):
        if self.priority_select == "priority":
            if self.priority == other.priority:
                return True
            return False
        if self.priority_select == "priority":
            if self.publish_date == other.publish_date:
                return True
            return False
    
    def __str__(self)-> str:
        """
        todo objesi str formatına dönüştürür
        """
        sayi = len(self.mission)
        bosluk_sayisi = 15- sayi
        tarih_sayi = len(str(self.publish_date))
        bosluk_sayisi_tarih = 9-tarih_sayi
        return colored(self.mission, "blue") + " "*bosluk_sayisi +  " | " + colored(str(self.priority), "red") + " | " + colored(str(self.publish_date),"green") + " "*bosluk_sayisi_tarih +" | "