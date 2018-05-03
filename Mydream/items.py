# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MydreamItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Form_Factor	 = scrapy.Field()
    M_B_Form_Factor= scrapy.Field()
    CPU = scrapy.Field()
    CPU_Socket = scrapy.Field()
    Chipset = scrapy.Field()
    Memory_Type = scrapy.Field()
    Memory_Capacity = scrapy.Field()
    CPU_Heatsink = scrapy.Field()
    I_O_Modules = scrapy.Field()
    Dimensions_Dx_Wx_H = scrapy.Field()
    TPM_Version = scrapy.Field()
    Drive_Bays = scrapy.Field()
    Ethernet = scrapy.Field()
    PSU_Form_Factor = scrapy.Field()
    Serial_Port = scrapy.Field()
    Video = scrapy.Field()
    Indicators = scrapy.Field()
    USB = scrapy.Field()
    Front_Control = scrapy.Field()
    System_Security = scrapy.Field()
    Cooling_Fans = scrapy.Field()
    Expansion_Slots = scrapy.Field()
    HDD_Backplane = scrapy.Field()
    Net_Weight = scrapy.Field()
    Gross_Weight = scrapy.Field()
    Features_Benefits = scrapy.Field()
    Pictures = scrapy.Field()
    Container_Loading_Single_Packing=scrapy.Field()
    Cubic_Feet=scrapy.Field()
    Front_Bezel=scrapy.Field()
    pass
