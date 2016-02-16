from django.db import models

from django.forms import IntegerField
from django.forms.widgets import Input
from django.forms.util import ValidationError
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
from django.utils.safestring import mark_safe 
 
class PercentInput(Input):
    """ A simple form input for a percentage """
    input_type = 'text'

    def _format_value(self, value):
        if value is None or value == '':
            return ''
        return str(int(value * 100))

    def render(self, name, value, attrs=None):
        value = self._format_value(value)
        return super(PercentInput, self).render(name, value, attrs) #+ mark_safe(u'%')

    def _has_changed(self, initial, data):
        return super(PercentInput, self)._has_changed(self._format_value(initial), data)

class PercentField(models.IntegerField):
    """ A field that gets a value between 0 and 1 and displays as a value between 0 and 100"""
    widget = PercentInput(attrs={"class": "percentInput", "size": 4})

    default_error_messages = {
        'positive': _(u'Must be a positive number.'),
    }

    def clean(self, value):
        """
        Validates that the input can be converted to a value between 0 and 1.
        Returns a Decimal
        """
        value = super(PercentField, self).clean(value)
        if value is None:
            return None
        if (value < 0):
            raise ValidationError(self.error_messages['positive'])
        return Decimal("%.2f" % (value / 100.0))
        
#-----    Location part------

class area(models.Model):
    Name = models.CharField(max_length=50,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'area'
        db_table = 'area'    

class country(models.Model):
    Name = models.CharField(max_length=50,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'country'
        db_table = 'country'

class region(models.Model):
    Name = models.CharField(max_length=50,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'region'
        db_table = 'region'
        
class province(models.Model):
    Name = models.CharField(max_length=50,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        verbose_name = 'province'
        db_table = 'province'
        
class city(models.Model):
    Name = models.CharField(max_length=50,verbose_name='Name')
    def __unicode__(self):
        return u'%s' % (self.Name)
    
    class Meta:
        verbose_name = 'city'
        db_table = 'city'

class area_country(models.Model):
    area = models.ForeignKey(area,verbose_name='Area')
    country = models.ForeignKey(country,verbose_name='Country')

    def __unicode__(self):
        return u'%s %s' % (self.area.Name, self.country.Name)

    class Meta:
        verbose_name = 'rel area country'
        db_table = 'area_country'

class country_region(models.Model):
    country = models.ForeignKey(country,verbose_name='Country')
    region = models.ForeignKey(region,verbose_name='Region')
    
    def __unicode__(self):
        return u'%s %s' % (self.country.Name, self.region.Name)

    class Meta:
        verbose_name = 'rel country region'
        db_table = 'country_region'

class region_province(models.Model):
    region = models.ForeignKey(region,verbose_name='Region')
    province = models.ForeignKey(province,verbose_name='Province')

    def __unicode__(self):
        return u'%s %s' % (self.region.Name, self.province.Name)

    class Meta:
        verbose_name = 'rel region province'
        db_table = 'region_province'

class province_city(models.Model):
    province = models.ForeignKey(province,verbose_name='Province')
    city = models.ForeignKey(city,verbose_name='City')

    def __unicode__(self):
        return u'%s %s' % (self.province.Name, self.city.Name)

    class Meta:
        verbose_name = 'rel province city'
        db_table = 'province_city'


#-----    Bidding part------

class Biz_Year(models.Model):
    Name = models.CharField(max_length=45,verbose_name='BIZ Year',blank=True, null=True,help_text="Format likes '2012/13'")
    
    class Meta:
        verbose_name = 'Business Year'
        db_table = 'biz_year'
        
    def __unicode__(self):
        return self.Name     

class Currency(models.Model):
    Name = models.CharField(max_length=10,verbose_name='Currency')
    Rate = models.FloatField(verbose_name='Rate')
    
    class Meta:
        verbose_name = 'Currency'  
        db_table = 'currency'        
          
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Rate)
        
class Rail_Class(models.Model):
    Name = models.CharField(max_length=100,
                                           choices=(
                                                            ('EMU','EMU'),
                                                            ('CITY RAIL','CITY RAIL'),
                                                            ('LOCO','LOCO'),
                                                            ('S.P.V','S.P.V'),
                                                            ('DMU','DMU')),
                                           verbose_name='Rail Class')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
        
    class Meta:
        verbose_name = "Rail Classe"     #show name for module
        db_table = 'rail_class'        
        
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description) 
        

class Rail_Platform(models.Model):
    Name = models.CharField(max_length=100,verbose_name='Platform')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Platform'
        db_table = 'rail_platform'

    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)
        

class Rail_Type(models.Model):
    Name = models.CharField(max_length=20,verbose_name='Type')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Type'
        db_table = 'rail_type'

    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)

class Rail_Class_Platform_r(models.Model): 
    Rail_Class = models.ForeignKey(Rail_Class)
    Rail_Platform = models.ForeignKey(Rail_Platform)    
        
    class Meta:
        verbose_name = 'rel Rail Class - Rail Platform'  
        db_table = 'rail_class_platform_r'        

class Rail_Class_Type_r(models.Model): 
    Rail_Class = models.ForeignKey(Rail_Class)
    Rail_Type = models.ForeignKey(Rail_Type)    
        
    class Meta:
        verbose_name = 'rel Rail Class - Rail Type'  
        db_table = 'rail_class_type_r'        


class Rail_Vehicle_Project(models.Model):
    Vehicle_project_no = models.CharField(max_length=100,verbose_name='Vehicle Project No')
    Description = models.TextField(max_length=300,blank = True, null=True, verbose_name='Description')
    Line_Length = models.FloatField(default=10,blank=True, null=True,verbose_name='Line Length')
    Created_by = models.CharField(max_length=100,blank=True, null=True,verbose_name='Created By')
    Created_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='Created Date')
    Last_modified_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='Last Modified Date')

    area = models.ForeignKey(area,verbose_name='Area')
    country = models.ForeignKey(country,verbose_name='Country')
    region = models.ForeignKey(region,blank=True, null=True,verbose_name='Region')
    province = models.ForeignKey(province,blank=True, null=True,verbose_name='Province')
    city = models.ForeignKey(city,blank=True, null=True,verbose_name='City')

    class Meta:
        verbose_name = 'Rail Vehicle project'
        db_table = 'rail_vehicle_project'        
            
    def __unicode__(self):
        return u'%s %s' % (self.Vehicle_project_no, self.Created_by)  

class Rail_OEM_Project(models.Model):
#    id = models.IntegerField(max_length=11,verbose_name='ID (OEM Project Code)',  primary_key=True)  
    oem_project_code = models.CharField(max_length=100,verbose_name='OEM Project Code') # here "oem_project_code" can be replaced by "id", just change verbose_name
    name = models.CharField(max_length=50,blank=True, null=True,verbose_name='OEM Project Name')
    Description = models.TextField(max_length=300)
    vehicle_project_status = models.CharField(max_length=50,choices=
                                                                                            (('Initial','Initial'),
                                                                                            ('Closed','Closed'),
                                                                                            ('OEM Bidding','OEM Bidding'),
                                                                                            ('OEM Producing','OEM Producing'),
                                                                                            ('OEM Lost','OEM Lost'),
                                                                                            ('In Operation','In Operation')),
                                                                                            verbose_name='Vehicle Project Status')
    ts_qty = models.IntegerField(max_length=11,blank=True, null=True)
    Created_by = models.CharField(max_length=50,blank=True, null=True,verbose_name='Created by')
    Created_date = models.DateTimeField(blank=True, null=True, verbose_name='Created date')
    Last_modified_date = models.DateTimeField(blank=True, null=True, verbose_name='Last modified date')

    Biz_Year = models.ForeignKey(Biz_Year)
    Rail_Vehicle_Project = models.ForeignKey(Rail_Vehicle_Project, null=True) 
    
    class Meta:
        verbose_name = 'Rail OEM Project'
        db_table = 'rail_oem_project'        
            
    def __unicode__(self):
        return u'%s %s %s' % (self.oem_project_code, self.name, self.vehicle_project_status)  

    def getitems(self):
        return {'id':self.pk, "oem_project_code":self.oem_project_code, "Description":self.Description, "vehicle_project_status":self.vehicle_project_status, "Biz_Year":self.Biz_Year}


class Rail_Business_Scope(models.Model):
    Name = models.CharField(max_length=100,verbose_name='Business Scope')
    Description = models.TextField(max_length=300,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Business Scope'
        db_table = 'rail_business_scope'        
            
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)
    
class Rail_Customer(models.Model):
    Number = models.CharField(max_length=100,verbose_name='Customer NO')
    Name = models.CharField(max_length=100,verbose_name='Customer Name')
    Description = models.TextField(max_length=300,verbose_name='Description')
    Location = models.CharField(max_length=100,blank=True, null=True,verbose_name='Location')
    Rail_Business_Scope = models.ManyToManyField(Rail_Business_Scope, verbose_name='Rail Business Scope')
    
    class Meta:
        verbose_name = 'Rail Customer'
        db_table = 'rail_customer'
        
    def __unicode__(self):
        return u'Number: %s Name : %s' % (self.Number, self.Name)

class Rail_Customer_Bidding(models.Model):
    OEM_Chance = models.CharField(max_length=5,choices=(('0%','0%'),('20%','20%'),('40%','40%'),('50%','50%'),('60%','60%'),('80%','80%'),('100%','100%')),verbose_name='OEM Chance Rate')
#    OEM_Chance = PercentField(max_length=5,choices=(('0%','0'),('20%','20'),('40%','40'),('50%','50'),('60%','60'),('80%','80'),('100%','100')),verbose_name='OEM Chance Rate')    
    Comments = models.CharField(max_length=500,blank=True, null=True,verbose_name='Comments')
    
    Rail_Customer = models.ForeignKey(Rail_Customer)
    Currency = models.ForeignKey(Currency)
    Rail_OEM_Project = models.ForeignKey(Rail_OEM_Project, verbose_name='Rail OEM Project', null = True)    
#    Rail_Business_Scope = models.ForeignKey(Rail_Business_Scope, null = True, verbose_name='Rail Business Scope')
    
    class Meta:
        verbose_name = 'Rail Customer Bidding'
        db_table = 'rail_customer_bidding'        
            
    def __unicode__(self):
        return u'%s %s' % (self.OEM_Chance, self.Rail_Customer.Name)

class Rail_Customer_Business_Scope_r(models.Model): 
    Rail_Customer = models.ForeignKey(Rail_Customer)
    Rail_Business_Scope = models.ForeignKey(Rail_Business_Scope)    
        
    class Meta:
        verbose_name = 'rel Rail Customer - Rail Business Scope'  
        db_table = 'rail_customer_business_scope_r'        

    
class Rail_Vehicle_Info(models.Model):
    Description = models.TextField(max_length=300,verbose_name='Description')
    Car_per_TS = models.DecimalField(max_digits=2, decimal_places=0,verbose_name='Car per Transit')
    MCar_per_TS = models.DecimalField(max_digits=2, decimal_places=0,verbose_name='Motive Car per Transit')
    Speed_From = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Speed From')
    Speed_To = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Speed To')
    Vehicle_Price = models.FloatField(blank=True, null=True,verbose_name='Vehicle Price')
    TS_Config = models.CharField(max_length=100,verbose_name='Transit Configure')

    Rail_Platform = models.ForeignKey(Rail_Platform)
    Currency = models.ForeignKey(Currency,blank=True, null=True)
    
    Rail_Class = models.ForeignKey(Rail_Class)
    Rail_Vehicle_Project = models.ForeignKey(Rail_Vehicle_Project, blank=True, null=True)
    Rail_Type = models.ForeignKey(Rail_Type)

    class Meta:
        verbose_name = 'Rail Vehicle Info'
        db_table = 'rail_vehicle_info'
        
            
    def __unicode__(self):
        return u'%s %s %s %s' % (self.Car_per_TS,  self.Rail_Class.Name,self.Rail_Platform.Name,self.Rail_Type.Name)

#-----    Contract part------
class Rail_Contract(models.Model):
#    id = models.IntegerField(max_length=11,verbose_name='ID',  primary_key=True)
    Delivery_Terms = models.CharField(max_length=500,blank=True, null=True,verbose_name='Contract Delivery Terms')
    Customer_contract_no = models.CharField(max_length=100,blank=True, null=True,verbose_name='Customer Contract NO')
    VTA_contract_no = models.CharField(max_length=100,blank=True, null=True,verbose_name='VTA Contract NO')
    Total_Value_exclude_VAT = models.FloatField(blank=True, null=True,verbose_name='Total Value Exclude VAT')
    Sales_Commission_Flag = models.BooleanField(max_length=10,verbose_name='Sales Commission Flag')
    Percentage_Down_Payment = models.FloatField(blank=True, null=True,verbose_name='Percentage of Down Payment')
    Total_Value_DP_exclude_VAT = models.FloatField(blank=True, null=True,verbose_name='Total value of Down Payment Exclude VTA')
    Advance_Payment_Bond_Percentage = models.FloatField(blank=True, null=True,verbose_name='Advance Payment Bond Percentage')
    Performance_bond = models.FloatField(blank=True, null=True,verbose_name='Performance Bond')
#    Contract_Training_Flag = models.NullBooleanField(max_length=10,blank=True, null=True)    
    Contract_Training_Flag = models.BooleanField(max_length=10)        
    Quality_Bond_Percentage = models.FloatField(blank=True, null=True,verbose_name='Quality Bond Percentage')
    Warranty_Period = models.IntegerField(max_length=3,help_text="(Month)")
    Remark = models.CharField(max_length=500,blank=True, null=True)

    Currency = models.ForeignKey(Currency)
    
    class Meta:
        verbose_name = 'Rail Contract'
        db_table = 'rail_contract'        
            
    def __unicode__(self):
        return u'%s customer contract no : %s' % (self.pk, self.Customer_contract_no) #must opertion 

class Rail_Bidding(models.Model):
#    id = models.IntegerField(max_length=11,verbose_name='ID',  primary_key=True)
    Reason = models.TextField(max_length=500)    
    Voith_Chance = models.CharField(max_length=5,choices=(('0%','0%'),('20%','20%'),('40%','40%'),('50%','50%'),('60%','60%'),('80%','80%'),('100%','100%')),verbose_name='VOITH Chance') #default is 0
    Commercial_Priority = models.CharField(max_length=1,choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')),blank=True, null=True,help_text="1 is highest priority")
    Commercial_Status = models.CharField(max_length=300,blank=True, null=True,verbose_name='Commercial KeyPoint')
    Technical_Priority = models.CharField(max_length=1,choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), blank=True, null=True,help_text="1 is highest priority")
    Technical_Status = models.CharField(max_length=300,blank=True, null=True,verbose_name='Technical KeyPoint')
    OEM_Principle = models.CharField(max_length=100,blank=True, null=True)
    Bidding_Status  = models.CharField(max_length=20,choices=(('Won','Won'),('Closed','Closed'),('Lost','Lost'),('Delivered','Delivered'),('Tracking','Tracking'),('LOI Signed','LOI Signed'),('Contract Signed','Contract Signed'),('TBD','TBD')),blank=True, null=True)
    Ref_No1= models.CharField(max_length=100,blank=True, null=True)
    Ref_No2= models.CharField(max_length=100,blank=True, null=True)
    Decision_Maker= models.CharField(max_length=100)    
    Bidding_Price_exclude_VAT = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True,verbose_name='Bidding Price Exclude VAT')    

    Rail_OEM_Project = models.ForeignKey( Rail_OEM_Project, to_field = 'id',  null=True)    
    Rail_Contract = models.ForeignKey( Rail_Contract, null=True)    
    
    class Meta:
        verbose_name = 'Rail Bidding'
        db_table = 'rail_bidding'        
            
    def __unicode__(self):
        return u'%s %s' % (self.pk, self.Voith_Chance)  

    def getitems(self):
        return {'id':self.pk, "Reason":self.Reason, "Commercial_Priority":self.Commercial_Priority, "Bidding_Status":self.Bidding_Status,"Package_Name":self.Bidding_Status}

class Rail_Competitor(models.Model):
    Name = models.CharField(max_length=100,verbose_name='Competitor')
    Description = models.CharField(max_length=300,blank=True, null=True,verbose_name='Description')

    class Meta:
        verbose_name = 'Rail Competitor'    
        db_table = 'rail_competitor'        
        
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)


class Rail_Competitor_Bidding(models.Model):
    
    Competitor_Price_exclude_VAT = models.FloatField(blank=True, null=True,verbose_name='Competitor Price Exclude VAT')
#    Winner_Flag = models.NullBooleanField(max_length=10,blank=True, null=True,verbose_name='Winner Flag')
    Winner_Flag = models.BooleanField(max_length=10,verbose_name='Winner Flag')    
    Comments = models.TextField(max_length=1000,blank=True, null=True,verbose_name='Comments')

    Currency = models.ForeignKey(Currency)
    Rail_Competitor = models.ForeignKey(Rail_Competitor)
    Rail_OEM_Project = models.ForeignKey(Rail_OEM_Project)
        
    class Meta:
        verbose_name = 'Rail Competitor Bidding'    
        db_table = 'rail_competitor_bidding'        
        
    def __unicode__(self):
        return u'%s %s' % (self.Rail_Competitor.Name, self.Winner_Flag)          

#-----    Contract part------

class Rail_Product(models.Model):
    Name = models.CharField(max_length=50,choices=(('AC','AC'),('SAC','SAC'),('SPC','SPC'),('AAR','AAR'),('FN','FN'),('FHM','FHM'),('Hydraulic Buffer','Hydraulic Buffer'),('Gas Hydraulic Buffer','Gas Hydraulic Buffer'),('Side Buffer','Side Buffer')),verbose_name='Product')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Product'
        db_table = 'rail_product'        
            
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)
      
class Rail_Product_Type(models.Model):
    Name = models.CharField(max_length=50,
                                            choices=(
                                                 ('Coupler','Coupler'),
                                                 ('FN/FHM','FN/FHM'),
                                                 ('Adaptor','Adaptor'),
                                                 ('Buffer','Buffer'),
                                                 ('Gearbox','Gearbox'),
                                                 ('Coupling','Coupling'),
                                                 ('Powerpack','Powerpack'),
                                                 ('Transmission','Transmission'),
                                                 ('Cooling','Cooling'),
                                                 ('Converter','Converter')),
                                            verbose_name='Type')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Product Type'  
        db_table = 'rail_product_type'
        
          
    def __unicode__(self):
        return u'%s' % (self.Name)

class Rail_Product_Setup(models.Model):
    Name = models.CharField(max_length=50,choices=(('Head Type','Head Type'),('E-Coupler','E-Coupler'),('Shank','Shank'),('EFG','EFG'),('Head','Head'),('Blank','Blank')),verbose_name='SETUP')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Product Setup'
        db_table = 'rail_product_setup'        
    
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)
    
class Rail_Product_Setup_Value(models.Model):
    Name = models.CharField(max_length=50,choices=(('Type 10','Type 10'),('Type 35','Type 35'),('Type 330','Type 330'),('Other','Other'),('N/A','N/A'),('20-Point','20-Point'),('30-Point','30-Point'),('100-Point','100-Point'),('GH','GH'),('HY','HY'),('DT','DT'),('Rigid','Rigid'),('Yes','Yes'),('No','No')),verbose_name='SETUP Value')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Product Setup Value'  
        db_table = 'rail_product_setup_value'        
          
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)

class Rail_Product_Group(models.Model):
    Name = models.CharField(max_length=50,choices=(('ATE','ATE'),('ATM','ATM'),('ATH','ATH'),('ATK','ATK'),('VTAS','VTAS')),verbose_name='Rail Product Group')
    Description = models.CharField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Product Group'
        db_table = 'rail_product_group'        
            
    def __unicode__(self):
        return u'%s %s' % (self.Name, self.Description)

class Rail_Product_Group_Product_Type_r(models.Model): 
    Rail_Product_Group = models.ForeignKey(Rail_Product_Group)    
    Rail_Product_Type = models.ForeignKey(Rail_Product_Type)
        
    class Meta:
        verbose_name = 'rel Rail Product Group - Product Type'  
        db_table = 'rail_product_group_product_type_r'        
        
class Rail_Product_Type_Product_r(models.Model): 
    Rail_Product_Type = models.ForeignKey(Rail_Product_Type)
    Rail_Product = models.ForeignKey(Rail_Product)    

    class Meta:
        verbose_name = 'rel Rail Product Type - Product'  
        db_table = 'rail_product_type_product_r'        

class Rail_Product_Product_Setup_r(models.Model): 
    Rail_Product = models.ForeignKey(Rail_Product)
    Rail_Product_Setup = models.ForeignKey(Rail_Product_Setup)

    class Meta:
        verbose_name = 'rel Rail Product - Product Setup'  
        db_table = 'rail_product_product_setup_r'        
    
class Rail_Product_Setup_Product_Setup_Value_r(models.Model): 
    Rail_Product_Setup = models.ForeignKey(Rail_Product_Setup)
    Rail_Product_Setup_Value = models.ForeignKey(Rail_Product_Setup_Value)    
        
    class Meta:
        verbose_name = 'rel Rail Product Setup - Product Setup Type'  
        db_table = 'rail_product_setup_product_setup_value_r'        
        
#-----    Package part------
class Rail_Package(models.Model):
#    id = models.IntegerField(max_length=11,verbose_name='ID',  primary_key=True)
    Name = models.CharField(max_length=100,verbose_name='Name')
    Description = models.TextField(max_length=500, verbose_name='Description')    
    Total_Price_exclude_VAT = models.DecimalField(max_digits=12, decimal_places=2,verbose_name='Total Price exclude VAT')
    Created_by = models.CharField(max_length=100,blank=True, null=True,verbose_name='Created By')
    Created_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='Created Date')
    Last_modified_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='Last Modified Date')

    Rail_Bidding = models.ManyToManyField(Rail_Bidding, null=True)    
    
    class Meta:
        verbose_name = 'Rail Package'
        db_table = 'rail_package'
        
    def __unicode__(self):
        return u'%s %s' % (self.pk, self.Name)  
        

    def getitems(self):
        return {'id':self.pk, "Name":self.Name, "Description":self.Description, "Total_Price_exclude_VAT":self.Total_Price_exclude_VAT,}

class Rail_Configuration(models.Model):
    Based_Price_exclude_VAT = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True,verbose_name='Based Price Exclude VAT')
    Rail_Product = models.ForeignKey(Rail_Product, verbose_name='Rail Product')
    Rail_Product_Setup = models.ForeignKey(Rail_Product_Setup, verbose_name='Rail Product Setup')    
    Rail_Product_Setup_Value = models.ForeignKey(Rail_Product_Setup_Value, verbose_name='Rail Product Setup value')        

    class Meta:
        verbose_name = 'Rail Configuration'
        db_table = 'rail_configuration'
        
    def __unicode__(self):
        return u'%s' % (self.Based_Price_exclude_VAT)  


class Rail_Package_Line(models.Model): 
    Rail_Package = models.ForeignKey(Rail_Package)    
    Description = models.TextField(max_length=300,blank=True, null=True,verbose_name='Description')
    Quantity = models.IntegerField(max_length=5,verbose_name='Quantity')
    Based_Price_exclude_VAT = models.DecimalField(max_digits=12, decimal_places=2,verbose_name='Price')

    Rail_Configuration = models.ForeignKey(Rail_Configuration, blank=True, null=True, verbose_name='Rail Configuration')    
    
    Rail_Product_Group = models.ForeignKey(Rail_Product_Group, verbose_name='Rail Product Group')    
    Rail_Product_Type = models.ForeignKey(Rail_Product_Type, verbose_name='Rail Product Type')
    Rail_Product = models.ForeignKey(Rail_Product, verbose_name='Rail Product')

    class Meta:
        verbose_name = 'Rail Package Line'
        db_table = 'rail_package_line'
        
    def __unicode__(self):
        return u'%s %s' % (self.Quantity,self.Based_Price_exclude_VAT)  


#-----    Project Tracking part------
class Rail_Department(models.Model):
    Name = models.CharField(max_length=50,verbose_name='Rail Department')
    Description = models.TextField(max_length=100,blank=True, null=True,verbose_name='Description')
    
    class Meta:
        verbose_name = 'Rail Department'  
        db_table = 'rail_department'
        
    def __unicode__(self):
        return self.Name 

class Rail_Project_in_Charge(models.Model):
    Rep_Person = models.CharField(max_length=50,verbose_name='In Charge Person')
#    Rail_Department = models.OneToOneField(Rail_Department)
    Rail_Department = models.ForeignKey(Rail_Department)    
    Rail_Customer = models.ForeignKey(Rail_Customer)
    Rail_OEM_Project = models.ForeignKey(Rail_OEM_Project)
    
    class Meta:
        verbose_name = 'Rail Project in Charge'  
        db_table = 'rail_project_in_charge'
        
    def __unicode__(self):
        return u'%s Dpt : %s  Customer : %s' % (self.Rep_Person, self.Rail_Department.Name, self.Rail_Customer.Name)

'''
class Rail_Tracking(models.Model):
    OEM_Bidding = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='OEM Bidding Time')
    Voith_Bidding = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='VOITH Bidding Time') 
    LOI = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    LOI_Kick_off = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='LOI Kick Off')
    TA = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    TA_Kick_off = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='TA Kick off')
    Contract_Sign = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    Contract_Kick_off = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='Contract Kick Off') 
    FAI = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    First_Delivery = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    Last_Delivery = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name='Last Delivery')
    Comments = models.CharField(max_length=100,blank=True, null=True)   
    Tracking_Flag = models.BooleanField(max_length=10)

    Rail_OEM_Project = models.ForeignKey(Rail_OEM_Project)
#    Rail_OEM_Project = models.OneToOneField(Rail_OEM_Project)
    
    class Meta:
        verbose_name = 'Rail Tracking'
        db_table = 'rail_tracking'
        
    def __unicode__(self):
        return u'%s %s %s %s %s %s' % ( self.OEM_Bidding, self.Voith_Bidding, self.LOI_Kick_off,self.TA_Kick_off,self.Contract_Kick_off,self.Last_Delivery)  
'''

