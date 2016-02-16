from django.contrib.admin.options import *
from django.contrib import admin

from Rail.models import *
from Rail import models
from Rail.my_model_admin import MyModelAdmin
from Rail.link_form_admin import LinkFormAdmin
from Rail.link_model_admin import LinkModelAdmin

from Rail.link_model_forms import Rail_PackageForm,Rail_BiddingForm,Rail_OEM_ProjectForm
from Rail.link_form_forms import RailPackageForm,RailBiddingForm,RailOEMProjectForm

import csv
#from django.http import HttpResponse
#from django.utils.translation import ugettext as _


###########################################################################    
#
#               Form Link
#
###########################################################################

class RailBidingLinkFormAdmin(LinkFormAdmin):

    extra = 1
    
    link_form = RailBiddingForm
    link_obj_class = Rail_Bidding
    link_m2m = False
    link_init_search = False

class RailPackageLinkFormAdmin(LinkFormAdmin):

    extra = 1
    
    link_form = RailPackageForm
    link_obj_class = Rail_Package
    link_m2m = True

class RailOEMProjectLinkFormAdmin(LinkFormAdmin):

    extra = 1
    
    link_form = RailOEMProjectForm
    link_obj_class = Rail_OEM_Project
    link_m2m = False
    link_init_search = True

###########################################################################    
#
#               ModelForm Link
#
###########################################################################

class RailPackageLink(LinkModelAdmin):
    model = Rail_Package
    form = Rail_PackageForm
    extra = 0

    link_m2m = True
    
    fieldsets= [
        (None,{
             'fields':
                ('id',
                 'Name',
                 'Description',
                 'Total_Price_exclude_VAT',
                 )}),
        ]    

    readonly_fields= (
#                 'id',
                 'Name',
                 'Description',
                 'Total_Price_exclude_VAT',
                 )                 

class RailOEMProjectLink(LinkModelAdmin):
    model = Rail_OEM_Project
    form = Rail_OEM_ProjectForm
    extra = 0

    link_m2m = False
    
    fieldsets= [
        (None,{
             'fields':
                ('id',
                 'oem_project_code',
                 #'Description',
                 'vehicle_project_status',
                 'ts_qty',
                 'Biz_Year',
                 )}),
        ]    

    readonly_fields= (
                 'oem_project_code',
                 #'Description',
                 'vehicle_project_status',
                 'ts_qty',
                 'Biz_Year',
                 )                 

class RailBiddingLink(LinkModelAdmin):
    model = Rail_Bidding
    form = Rail_BiddingForm
    extra = 0

    link_m2m = False
  
    fieldsets= [
        (None,{
             'fields':
                (
                 'id',
                 'Reason',
                 'Voith_Chance',
                 'Bidding_Status',                 
                 'Total_Bidding_Price_exclude_VAT',
                 'Decision_Maker',
                 )}),
        ]

    readonly_fields= (
                 'Reason',
                 'Voith_Chance',
                 'Bidding_Status',                 
                 'Total_Bidding_Price_exclude_VAT',
                 'Decision_Maker',
                 )  
    


###########################################################################    
#
#               admin.TabularInline
#
###########################################################################
class RailCompetitorBiddingInline(admin.TabularInline):
    model = Rail_Competitor_Bidding
    extra = 1

class RailBiddingInline(admin.TabularInline):
    model = Rail_Bidding
    extra = 0    

class RailCustomerBiddingInline(admin.TabularInline):
    model = Rail_Customer_Bidding
    extra = 1

class RailVehicleInfoInline(admin.StackedInline):
    model = Rail_Vehicle_Info
    #extra = 0
    extra = 1
    max_num = 1
    
    fieldsets= [
        (None,{
             'fields':
                (
                 'Description',
                 'Car_per_TS',
                 'MCar_per_TS',
                 'Speed_From',
                 'Speed_To',
                 )}),
        (None,{
             'fields':
                 (
                 'Vehicle_Price',                 
                 'TS_Config',                                  
                 'Currency',
                 'Rail_Class',
                 'Rail_Type',
                 'Rail_Platform',
                 'Rail_Vehicle_Project',                 
                 )}),
        ]    

#class Package_LineInline(admin.StackedInline):
class RailPackageLineInline(admin.TabularInline):
    model = Rail_Package_Line
    extra = 1


class RailContractInline(admin.StackedInline):
    model = Rail_Contract
    extra = 0

    fieldsets= [
        (None,{
             'fields':
                (
                 #'id',
                 'Delivery_Terms',
                 'VTA_contract_no',
                 'Warranty_Period',
                 'Remark',
                 'Contract_Training_Flag',                 
                 )}),
        (None,{
             'fields':
                 ('Customer_contract_no',
                 'Sales_Commission_Flag',
                 'Percentage_Down_Payment',
                 'Total_Value_DP_exclude_VAT',
                 'Total_Value_exclude_VAT',
                 'Advance_Payment_Bond_Percentage',
                 'Quality_Bond_Percentage', 
                 'Currency',
                 )}),
        ]

class RailProjectInChargeInline(admin.TabularInline):
    model = Rail_Project_in_Charge
    extra = 1
    
    fieldsets= [
        (None,{
             'fields':
                ('Employee',
                 'Rail_Department',
                 )}),
    ]

#Added by Toni Dong    
class ProductListInline(admin.TabularInline):
    model = Product_lists
    extra = 1

    fieldsets= [
        (None,{'fields':
            ('Rail_Product_Group',
             'Rail_Product_Type',
             'Rail_Product',
             'Based_Price_exclude_VAT',
             'Quantity',
             #'Currency'
            )}),
    ]
    
class RailTrackingInline(admin.StackedInline):
    model = Rail_Tracking
    extra =1
    max_num = 1

    fieldsets= [
        (None,{
             'fields':
                ('Tracking_Flag',
                 'Comments',
                 'OEM_Bidding',
                 'Voith_Bidding',
                 'LOI',
                 'LOI_Kick_off',
                 'TA',
                 'TA_Kick_off',                 
                 )}),
        (None,{
             'fields':
                 ('Contract_Sign',
                 'Contract_Kick_off',
                 'FAI',
                 'First_Delivery',
                 'Last_Delivery',
                 #'Rail_OEM_Project',       
                  'Rail_Bidding',
                 )}),
    ]    


class CustomerInline(admin.TabularInline):
    model = Rail_Customer
    extra = 1
    
class RailCompetitorInline(admin.StackedInline):
    model = Rail_Competitor
    extra = 1
    max_num = 1

class RailPackageInline(admin.TabularInline):
    model = Rail_Package
    extra = 1    
    readonly_fields = ('Name','Description','Total_Price_exclude_VAT')

    fieldsets= [
        (None,{
             'fields':
                (
                 #'id',
                 'Name',
                 'Description',
                 'Total_Price_exclude_VAT',
                 )}),
        ]

#    def get_fieldsets(self, request, obj=None):
#        return [(None, {'fields': ('id','Name','Description','Total_Price_exclude_VAT')})]
        

class RailVehicleProjectAdmin(MyModelAdmin):

    list_display = ('Vehicle_project_no','Description','End_User','Line_Length', 'Created_by') 
    #list_display =  ('Vehicle_project_no', 'Line_Length', 'Created_by', 'Area', 'Country','Region','Province','City') 
    search_fields = ('Vehicle_project_no',)   
    list_filter = ('Vehicle_project_no','Created_by',)  
    ordering = ('Vehicle_project_no',) 

    save_as = True

    inlines = [RailVehicleInfoInline, ]
#    modelform_links = [RailOEMProjectLink,]
    form_links = [RailOEMProjectLinkFormAdmin]
    
    fieldsets= [
        (None,{
             'fields':
                ('Vehicle_project_no',
			    'End_User',
                 'Description',
                 )}),
        (None,{
             'fields':
                 ('Created_by',
                 'Created_date',
#                 'Last_modified_date',
                 'Line_Length',                 
                 )}),
        (None,{
             'fields':
                 (('area','country'),
                 ('region','province','city'),
                 )}),

    ]
    
    @csrf_protect_m
    @transaction.commit_on_success
    def add_view(self, request, form_url='', extra_context=None):

        extra_context = {}
        areas = area.objects.all()
        area_countrys = area_country.objects.all()
        country_regions = country_region.objects.all()
        country_provinces = country_province.objects.all()
        region_provinces = region_province.objects.all()
        province_citys = province_city.objects.all()

        rail_class_types = Rail_Class_Type_r.objects.all()
        rail_class_platforms = Rail_Class_Platform_r.objects.all()
        
        extra_context_cur = {        
            'areas':areas,      
            'area_countrys': area_countrys,
            'country_regions': country_regions,
            'country_provinces': country_provinces,            
            'region_provinces': region_provinces, 
            'province_citys': province_citys,
            'rail_class_types': rail_class_types,
            'rail_class_platforms': rail_class_platforms,
        }

        extra_context.update(extra_context_cur)
        
        return super(RailVehicleProjectAdmin, self).add_view(request,form_url,extra_context)

    @csrf_protect_m
    @transaction.commit_on_success
    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = {}

        areas = area.objects.all()
        area_countrys = area_country.objects.all()
        country_regions = country_region.objects.all()
        country_provinces = country_province.objects.all()        
        region_provinces = region_province.objects.all()
        province_citys = province_city.objects.all()

        obj = self.get_object(request, unquote(object_id))        
        cur_country = obj.country
        cur_region = obj.region
        cur_province = obj.province
        cur_city = obj.city

        rail_class_types = Rail_Class_Type_r.objects.all()
        rail_class_platforms = Rail_Class_Platform_r.objects.all()
        
        extra_context_cur = {        
            'areas':areas,      
            'area_countrys': area_countrys,
            'country_regions': country_regions,
            'country_provinces': country_provinces,                        
            'region_provinces': region_provinces, 
            'province_citys': province_citys,            

            'cur_country': cur_country,    
            'cur_region': cur_region,    
            'cur_province': cur_province,    
            'cur_city': cur_city,                

            'rail_class_types': rail_class_types,
            'rail_class_platforms': rail_class_platforms,
        }

        extra_context.update(extra_context_cur)

        return super(RailVehicleProjectAdmin, self).change_view(request,object_id, form_url,extra_context)

    def _dismiss_popup(self, request, obj):
        return super(MyModelAdmin, self).response_add(request,obj)  

class RailOEMProjectAdmin(MyModelAdmin):
    list_display = ('oem_project_code','Description','ts_qty','vehicle_project_status', 'Rail_Vehicle_Project')
    search_fields = ('oem_project_code',)
    list_filter = ('oem_project_code',)
    ordering = ('-oem_project_code',)

    #inlines = [RailTrackingInline, RailProjectInChargeInline, RailCompetitorBiddingInline, RailCustomerBiddingInline] 
    #inlines = [RailTrackingInline, RailProjectInChargeInline, RailCompetitorBiddingInline] 
    inlines = [RailProjectInChargeInline]
#    modelform_links = [RailBiddingLink]
    form_links = [RailBidingLinkFormAdmin]
    
    fieldsets= [
        (None,{
             'fields':
                (
                 'oem_project_code',
                 'Description',
                 'ts_qty',
                 'Biz_Year',
                 )}),
        (None,{
             'fields':
                 ('Created_by',
                 'Created_date',
                 'vehicle_project_status',  
                 'Rail_Customer',
                 )}),
    ]

    fieldsets_fk= (None,{
             'fields':
                (
                 'Rail_Vehicle_Project',
                 )})


    def _dismiss_popup(self, request, obj):
    
        pk_value = obj._get_pk_val()
        
        array= []
        array.append("oem_project_code")
        array.append(escape(obj.oem_project_code))
        #array.append("Description")
        #array.append(escape(''.join(obj.Description.split('\r\n'))))
        array.append("vehicle_project_status")
        array.append(escape(obj.vehicle_project_status))
        array.append("Biz_Year")
        array.append(escape(obj.Biz_Year))

        from django.shortcuts import render_to_response
        return render_to_response('admin/myprj/linkback.html', 
                                            {'array': array, 
                                            'newId' : escape(pk_value), 
                                            'newRepr' : escape(obj),
                                            })

class RailBiddingAdmin(MyModelAdmin):
    list_display = ('Voith_Chance','Commercial_Priority','Commercial_Status','Technical_Priority','Technical_Status','Bidding_Status')
    search_fields = ('Voith_Chance',)
    list_filter = ('Voith_Chance',) 
    ordering = ('-Technical_Priority',) 

    #inlines = [] 
    #inlines = [ProductListInline] 
    inlines = [ProductListInline,RailTrackingInline,RailCompetitorBiddingInline] 
#    modelform_links = [RailPackageLink]
#    form_links = [RailPackageLinkFormAdmin]    Modified by Toni Dong
    
    fieldsets= [
        (None,{
             'fields':
                (
                 #'id',
                 'Reason',
                 'Commercial_Priority',
                 'Technical_Priority',
                 'Decision_Maker',
                 'Total_Bidding_Price_exclude_VAT',                       
                 )}),
        (None,{
             'fields':
                 ('Voith_Chance',
                 'Commercial_Status',
                 'Technical_Status',
                 'OEM_Principle',
                 'Bidding_Status',
                 'Ref_No1',
                 'Ref_No2',
                 'Rail_Contract',      
                 'Currency',   
                 )}),                 
    ]    

    fieldsets_fk= (None,{
             'fields':
                (
                 'Rail_OEM_Project',
                 )})

    def _dismiss_popup(self, request, obj):
    
        pk_value = obj._get_pk_val()
        
        array= []
        array.append("Reason")
        array.append(escape(''.join(obj.Reason.split('\r\n'))))
        array.append("Package_Name")
        array.append(escape(obj.Bidding_Status))
        array.append("Commercial_Priority")
        array.append(escape(obj.Commercial_Priority))
        array.append("Bidding_Status")
        array.append(escape(obj.Bidding_Status))

        from django.shortcuts import render_to_response
        return render_to_response('admin/myprj/linkback.html', 
                                            {'array': array, 
                                            'newId' : escape(pk_value), 
                                            'newRepr' : escape(obj),
                                            })
    @csrf_protect_m
    @transaction.commit_on_success
    def add_view(self, request, form_url='', extra_context=None):

        extra_context = {}

        Rail_Product_Group_Product_Type_rs = Rail_Product_Group_Product_Type_r.objects.all()
        Rail_Product_Type_Product_rs = Rail_Product_Type_Product_r.objects.all()
        Rail_Product_Product_Setup_rs = Rail_Product_Product_Setup_r.objects.all()
        Rail_Product_Setup_Product_Setup_Value_rs = Rail_Product_Setup_Product_Setup_Value_r.objects.all()
        
        extra_context_cur = {        
            'Rail_Product_Group_Product_Type_rs':Rail_Product_Group_Product_Type_rs,      
            'Rail_Product_Type_Product_rs': Rail_Product_Type_Product_rs,
            'Rail_Product_Product_Setup_rs': Rail_Product_Product_Setup_rs,
            'Rail_Product_Setup_Product_Setup_Value_rs': Rail_Product_Setup_Product_Setup_Value_rs,
        }

        extra_context.update(extra_context_cur)
        
        return super(RailBiddingAdmin, self).add_view(request,form_url,extra_context)

    @csrf_protect_m
    @transaction.commit_on_success
    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = {}

        Rail_Product_Group_Product_Type_rs = Rail_Product_Group_Product_Type_r.objects.all()
        Rail_Product_Type_Product_rs = Rail_Product_Type_Product_r.objects.all()
        Rail_Product_Product_Setup_rs = Rail_Product_Product_Setup_r.objects.all()
        Rail_Product_Setup_Product_Setup_Value_rs = Rail_Product_Setup_Product_Setup_Value_r.objects.all()
        
        extra_context_cur = {        
            'Rail_Product_Group_Product_Type_rs':Rail_Product_Group_Product_Type_rs,      
            'Rail_Product_Type_Product_rs': Rail_Product_Type_Product_rs,
            'Rail_Product_Product_Setup_rs': Rail_Product_Product_Setup_rs,
            'Rail_Product_Setup_Product_Setup_Value_rs': Rail_Product_Setup_Product_Setup_Value_rs,
        }

        extra_context.update(extra_context_cur)

        return super(RailBiddingAdmin, self).change_view(request,object_id, form_url,extra_context)

class RailPackageAdmin(MyModelAdmin):
    list_display = ('Name','Created_by','Created_date','Total_Price_exclude_VAT') #list head in record table
    search_fields = ('Name',)    #search bar in record table
    ordering = ('Name',)    #sort by field    

    inlines = [RailPackageLineInline,]

    
    fieldsets= [
        (None,{
             'fields':
                (
                 #'id',
                 'Name',
                 'Description'
                 )}),    
        (None,{
             'fields':
                (
                 'Total_Price_exclude_VAT',
                 'Created_by',
                 'Created_date',
#                 'Last_modified_date',
                 )}),    
    ]

    fieldsets_fk= (None,{
             'fields':
                (
                 'Rail_Bidding',
                 )})

    def _dismiss_popup(self, request, obj):
    
        pk_value = obj._get_pk_val()
        
        array= []
        array.append("Name")
        array.append(escape(obj.Name))
        array.append("Description")
        array.append(escape(''.join(obj.Description.split('\r\n'))))
        array.append("Total_Price_exclude_VAT")
        array.append(escape(obj.Total_Price_exclude_VAT))

        from django.shortcuts import render_to_response
        return render_to_response('admin/myprj/linkback.html', 
                                            {'array': array, 
                                            'newId' : escape(pk_value), 
                                            'newRepr' : escape(obj),
                                            })    

    @csrf_protect_m
    @transaction.commit_on_success
    def add_view(self, request, form_url='', extra_context=None):

        extra_context = {}

        Rail_Product_Group_Product_Type_rs = Rail_Product_Group_Product_Type_r.objects.all()
        Rail_Product_Type_Product_rs = Rail_Product_Type_Product_r.objects.all()
        Rail_Product_Product_Setup_rs = Rail_Product_Product_Setup_r.objects.all()
        Rail_Product_Setup_Product_Setup_Value_rs = Rail_Product_Setup_Product_Setup_Value_r.objects.all()
        
        extra_context_cur = {        
            'Rail_Product_Group_Product_Type_rs':Rail_Product_Group_Product_Type_rs,      
            'Rail_Product_Type_Product_rs': Rail_Product_Type_Product_rs,
            'Rail_Product_Product_Setup_rs': Rail_Product_Product_Setup_rs,
            'Rail_Product_Setup_Product_Setup_Value_rs': Rail_Product_Setup_Product_Setup_Value_rs,
        }

        extra_context.update(extra_context_cur)
        
        return super(RailPackageAdmin, self).add_view(request,form_url,extra_context)

    @csrf_protect_m
    @transaction.commit_on_success
    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = {}

        Rail_Product_Group_Product_Type_rs = Rail_Product_Group_Product_Type_r.objects.all()
        Rail_Product_Type_Product_rs = Rail_Product_Type_Product_r.objects.all()
        Rail_Product_Product_Setup_rs = Rail_Product_Product_Setup_r.objects.all()
        Rail_Product_Setup_Product_Setup_Value_rs = Rail_Product_Setup_Product_Setup_Value_r.objects.all()
        
        extra_context_cur = {        
            'Rail_Product_Group_Product_Type_rs':Rail_Product_Group_Product_Type_rs,      
            'Rail_Product_Type_Product_rs': Rail_Product_Type_Product_rs,
            'Rail_Product_Product_Setup_rs': Rail_Product_Product_Setup_rs,
            'Rail_Product_Setup_Product_Setup_Value_rs': Rail_Product_Setup_Product_Setup_Value_rs,
        }

        extra_context.update(extra_context_cur)

        return super(RailPackageAdmin, self).change_view(request,object_id, form_url,extra_context)




###########################################################################    
#
#               admin.ModelAdmin
#
###########################################################################

class BizYearAdmin(admin.ModelAdmin):
    list_display = ('Name',) #list head in record table
    search_fields = ('Name',)    #search bar in record table
    ordering = ('Name',)    #sort by field
    
class DetailQuantityAdmin(admin.ModelAdmin):
    list_display = ('Name',) #list head in record table
    search_fields = ('Name',)    #search bar in record table
    ordering = ('Name',)    #sort by field
     
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Rate') #list head in record table
    search_fields = ('Name',)    #search bar in record table
    list_filter = ('Rate',)     #search bar by fields
    ordering = ('Name',)    #sort by field

    
class RailVehicleInfoAdmin(admin.ModelAdmin):
    list_display = ('Description','Speed_From','Speed_To')
    search_fields = ('Description',)
    list_filter = ('TS_Config',)
    ordering = ('TS_Config',)
    raw_id_fields = ('Rail_Class','Rail_Platform','Rail_Type')

            
class RailCompetitorAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Description',)
    list_filter = ('Name','Description')
    ordering = ('Description',) 
    
    context = {}

    def __init__(self, model, admin_site):
        self.model = model
        self.opts = model._meta
        self.admin_site = admin_site
        ''' child admin
        self.b_child_admin = False
        '''
        super(ModelAdmin, self).__init__()
    
class RailCompetitorBiddingAdmin(MyModelAdmin):
    list_display = ('Rail_Competitor','Competitor_Price_exclude_VAT','Winner_Flag')
    search_fields = ('Rail_Competitor__Name',)
    list_filter = ('Rail_Competitor','Winner_Flag')
    ordering = ('Rail_Competitor',) 

    actions = ['export_all']    
    
    fieldsets= [
        (None,{
             'fields':
                ('Rail_Competitor',
                 'Comments',
                 'Winner_Flag',
                 'Competitor_Price_exclude_VAT',
                 'Currency',
                 'Rail_Bidding'
                 )}),
    ]    

    def export_all(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        vehicleproject_all = Rail_Vehicle_Project.objects.all()
        
        writer.writerow(['id', 'Competitor_Price_exclude_VAT','Winner_Flag','Comments', 'Currency', 'Rail_Competitor', 'Rail_OEM_Project'])
        for obj in vehicleproject_all:
            #vehicleinfo_all = Rail_Vehicle_Info.objects.filter(Rail_Vehicle_Project = obj)
            #row.append(obj.Comments)
            #row.append(obj.Currency)
            row = []
            row.append(obj.pk)
            row.append(obj.Competitor_Price_exclude_VAT)
            row.append(obj.Winner_Flag)
            row.append(obj.Rail_Competitor)
            row.append(obj.Rail_OEM_Project)
            writer.writerow(row)    

        obj_all = Rail_Vehicle_Project.objects.all()
        writer.writerow(['id', 'Competitor_Price_exclude_VAT','Winner_Flag','Comments', 'Currency', 'Rail_Competitor', 'Rail_OEM_Project'])
        for obj in obj_all:
            row.append(obj.Comments)
            row.append(obj.Currency)
            row = []
            row.append(obj.pk)
            row.append(obj.Competitor_Price_exclude_VAT)
            row.append(obj.Winner_Flag)
            row.append(obj.Rail_Competitor)
            row.append(obj.Rail_OEM_Project)
            writer.writerow(row)  
        return response
    
class ConfigPackageAdmin(admin.ModelAdmin):
    list_display = ('Name','Quantity','Based_Price_exclude_VAT')
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)
    filter_horizontal = ('Product_Type',) #many2many shown in page
    #filter_vertical = ('Product_Type',)    #another show way in page
    raw_name_fields = ('Rail_Competitor_Bidding',)     #foreign key show function in page
          
class RailContractAdmin(admin.ModelAdmin):
    list_display = ('Delivery_Terms','VTA_contract_no','Total_Value_exclude_VAT')
    search_fields = ('VTA_contract_no',)
    list_filter = ('Total_Value_exclude_VAT',)
    ordering = ('VTA_contract_no',)

    fieldsets= [
        (None,{
             'fields':
                (
                 #'id',
                 'Delivery_Terms',
                 'Customer_contract_no',
                 'VTA_contract_no',
                 'Warranty_Period',
                 'Remark',
                 'Currency',                 
                 )}),
        (None,{
             'fields':
                 ('Sales_Commission_Flag',
                 'Percentage_Down_Payment',
                 'Total_Value_DP_exclude_VAT',
                 'Total_Value_exclude_VAT',
                 'Advance_Payment_Bond_Percentage',
                 'Quality_Bond_Percentage',
                 'Contract_Training_Flag',                        
                 )}),
    ]    

             
class RailCustomerBiddingAdmin(admin.ModelAdmin):
    list_display = ('OEM_Chance','Comments', 'Rail_Customer', )
    search_fields = ('OEM_Chance',)
    list_filter = ('OEM_Chance',)
    ordering = ('-OEM_Chance',)
            
class RailProductTypeAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)
#    raw_id_fields = ('Rail_Product',)
            
class RailProductSetupAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    ordering = ('Description',)
#    raw_id_fields = ('Rail_Product_Setup_Value',)
        
class RailProductSetupValueAdim(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    list_filter = ('Name',)    
    ordering = ('Name',)
#   raw_id_fields = ('Rail_Product_Setup_Value',)
        
class RailProductGroupAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    ordering = ('Name',)
#   raw_id_fields = ('Rail_Product',)
        
class RailProductAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    list_filter = ('Name',) 
    ordering = ('Name',)
#    raw_id_fields = ('Rail_Product_Setup',)
            
class RailProjectinChargeAdmin(admin.ModelAdmin):
    list_display = ('Employee','Rail_Department')
    list_filter = ('Employee',) 
    ordering = ('Employee',) 
      
           
class RailPlatformAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    list_filter = ('Name',)   
    ordering = ('Name',)   
         
class RailClassAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    list_filter = ('Name',)   
    ordering = ('Name',)  
            
class RailTrackingAdmin(admin.ModelAdmin):
    list_display = ('Comments','Tracking_Flag')  
    search_fields = ('Comments',)
    list_filter = ('Tracking_Flag',)
    ordering = ('Tracking_Flag',)
                 
class RailTypeAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')  
    search_fields = ('Name',)
    list_filter = ('Name',)   
    ordering = ('Name',)  
         
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('Tutor','Date','Description','Type') 
    search_fields = ('Tutor',)
    list_filter = ('Date',)   
    ordering = ('-Date',) 


class RailBusinessScopeAdmin(admin.ModelAdmin):
    list_display = ('Name','Description')
    search_fields = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)
    
class RailCustomerAdmin(admin.ModelAdmin):
    list_display = ('Number','Name','Description')
    search_fields = ('Number',)
    list_filter = ('Number',)   
    ordering = ('Name',)
    
    #inlines = [RailProjectInChargeInline,]
    context = {}
                    
class RailPackageLineAdmin(admin.ModelAdmin):
    list_display = ('Rail_Package',) #list head in record table
    search_fields = ('Rail_Package__Name',)    #search bar in record table
    ordering = ('Rail_Package',)    #sort by field    
#    fields = ('Rail_Package','Quantity','Based_Price_exclude_VAT','Configuration',)
#    exclude =('Product_Type_r','Product_Group_Type_r',)    

#Added by Toni Dong                   
class ProductListsAdmin(admin.ModelAdmin):
    list_display = ('Rail_Bidding','Rail_Product_Group','Rail_Product_Type','Rail_Product','Quantity','Based_Price_exclude_VAT') 
    #list_display = ('getbidding','Rail_Product_Group','Rail_Product_Type','Rail_Product','Quantity','Based_Price_exclude_VAT')
    search_fields = ('Rail_Bidding',)    #search bar in record table
    ordering = ('Rail_Bidding',)    #sort by field    
    
class EndUserAdmin(admin.ModelAdmin):
    list_display = ('Name',) #list head in record table
    search_fields = ('Name',)    #search bar in record table
    ordering = ('Name',)    #sort by field 
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Name',) #list head in record table
    search_fields = ('Name',)    #search bar in record table
    ordering = ('Name',)    #sort by field     
    
class DecisionMakerAdmin(admin.ModelAdmin):
    list_display = ('Name',) #list head in record table
    search_fields = ('Name',)    #search bar in record table
    ordering = ('Name',)    #sort by field 
    
class AreaAdmin(admin.ModelAdmin):
    list_display = ('Name',) #list head in record table
    search_fields = ('Name',)    #search bar in record table
    ordering = ('Name',)    #sort by field    
    
class CountryAdmin(admin.ModelAdmin):
    list_display = ('Name',) 
    search_fields = ('Name',)   
    list_filter = ('Name',)  
    ordering = ('Name',) 
    
class RegionAdmin(admin.ModelAdmin):
    list_display = ('Name',) 
    search_fields = ('Name',)   
    list_filter = ('Name',)  
    ordering = ('Name',) 
    
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('Name',) 
    search_fields = ('Name',)   
    list_filter = ('Name',)  
    ordering = ('Name',) 
    
class CityAdmin(admin.ModelAdmin):
    list_display = ('Name',) 
    search_fields = ('Name',)   
    list_filter = ('Name',)  
    ordering = ('Name',) 


class AreaCountryAdmin(admin.ModelAdmin):
    list_display = ('area','country') #list head in record table
    search_fields = ('area',)    #search bar in record table
    ordering = ('area',)    #sort by field    

class CountryRegionAdmin(admin.ModelAdmin):
    list_display = ('country','region') #list head in record table
    search_fields = ('country',)    #search bar in record table
    ordering = ('country',)    #sort by field    

class CountryProvinceAdmin(admin.ModelAdmin):
    list_display = ('country','province') #list head in record table
    search_fields = ('country',)    #search bar in record table
    ordering = ('country',)    #sort by field    
    
class RegionProvinceAdmin(admin.ModelAdmin):
    list_display = ('region','province') #list head in record table
    search_fields = ('region',)    #search bar in record table
    ordering = ('region',)    #sort by field    

class ProvinceCityAdmin(admin.ModelAdmin):
    list_display = ('province','city') #list head in record table
    search_fields = ('city',)    #search bar in record table
    ordering = ('city',)    #sort by field    

class RailDepartmentAdmin(admin.ModelAdmin):
    list_display = ('Name','Description') 
    search_fields = ('Name',)   
    list_filter = ('Name',)  
    ordering = ('Name',) 

class RailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('Rail_Product','Based_Price_exclude_VAT') 
    search_fields = ('Rail_Product__Name',)   
    list_filter = ('Rail_Product',)  
    ordering = ('Rail_Product',) 

    @csrf_protect_m
    @transaction.commit_on_success
    def add_view(self, request, form_url='', extra_context=None):

        extra_context = {}

        Rail_Product_Product_Setup_rs = Rail_Product_Product_Setup_r.objects.all()
        Rail_Product_Setup_Product_Setup_Value_rs = Rail_Product_Setup_Product_Setup_Value_r.objects.all()
        
        extra_context_cur = {        
            'Rail_Product_Product_Setup_rs': Rail_Product_Product_Setup_rs,
            'Rail_Product_Setup_Product_Setup_Value_rs': Rail_Product_Setup_Product_Setup_Value_rs,
        }

        extra_context.update(extra_context_cur)
        
        return super(RailConfigurationAdmin, self).add_view(request,form_url,extra_context)

    @csrf_protect_m
    @transaction.commit_on_success
    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = {}

        Rail_Product_Product_Setup_rs = Rail_Product_Product_Setup_r.objects.all()
        Rail_Product_Setup_Product_Setup_Value_rs = Rail_Product_Setup_Product_Setup_Value_r.objects.all()
        
        extra_context_cur = {        
            'Rail_Product_Product_Setup_rs': Rail_Product_Product_Setup_rs,
            'Rail_Product_Setup_Product_Setup_Value_rs': Rail_Product_Setup_Product_Setup_Value_rs,
        }

        extra_context.update(extra_context_cur)

        return super(RailConfigurationAdmin, self).change_view(request,object_id, form_url,extra_context)


class RailProductGroupProductTypeAdmin(admin.ModelAdmin):
    list_display = ('Rail_Product_Group','Rail_Product_Type')
    search_fields = ('Rail_Product_Group__Name','Rail_Product_Type__Name')
    ordering = ('Rail_Product_Group','Rail_Product_Type') 

class RailProductTypeProductAdmin(admin.ModelAdmin):
    list_display = ('Rail_Product_Type','Rail_Product')
    search_fields = ('Rail_Product_Type__Name','Rail_Product__Name')
    ordering = ('Rail_Product_Type','Rail_Product') 

class RailProductProductSetupAdmin(admin.ModelAdmin):
    list_display = ('Rail_Product','Rail_Product_Setup')
    search_fields = ('Rail_Product__Name','Rail_Product_Setup__Name')
    ordering = ('Rail_Product','Rail_Product_Setup') 

class RailProductSetupProductSetupValueAdmin(admin.ModelAdmin):
    list_display = ('Rail_Product_Setup','Rail_Product_Setup_Value')
    search_fields = ('Rail_Product_Setup__Name','Rail_Product_Setup_Value__Name')
    ordering = ('Rail_Product_Setup','Rail_Product_Setup_Value') 

class RailClassTypeAdmin(admin.ModelAdmin):
    list_display = ('Rail_Class','Rail_Type')
    search_fields = ('Rail_Class__Name','Rail_Type__Name')
    ordering = ('Rail_Class','Rail_Type') 

class RailClassPlatformAdmin(admin.ModelAdmin):
    list_display = ('Rail_Class','Rail_Platform')
    search_fields = ('Rail_Class__Name','Rail_Platform__Name')
    ordering = ('Rail_Class','Rail_Platform') 

class RailCustomerBusinessScopeAdmin(admin.ModelAdmin):
    list_display = ('Rail_Customer','Rail_Business_Scope')
    search_fields = ('Rail_Customer__Name','Rail_Business_Scope__Name')
    ordering = ('Rail_Customer','Rail_Business_Scope') 


###########################################################################    
#
#               admin.AdminSite
#
###########################################################################

# to customize site object
#from django.db.models.base import ModelBase
from django.views.decorators.cache import never_cache



class AdminSiteExtend(admin.AdminSite):

    @never_cache
    def index(self, request, extra_context=None):
        rail_list = ['Rail OEM Projects', 'Product lists', 'End User projects','Rail Biddings']
        product_list = ['Rail Product Groups', "Rail Product Types", 'Rail Products', 'Rail Product Setups', 'Rail Product Setup Values', 'Rel Rail Product Group - Product Types', 'Rel Rail Product Type - Products', 'Rel Rail Product - Product Setups', 'Rel Rail Product Setup - Setup Types' ]
        location_list = ['Areas', "Countrys", 'Regions', 'Provinces', 'Citys', 'Rel Area Countrys', 'Rel Country Regions',  'Rel Country Provinces', 'Rel Province Citys']        
        class_list = ['Rail Classes', 'Rail Types', 'Rail Platforms', 'Rel Rail Class - Rail Platforms','Rel Rail Class - Rail Types'] 
        other_list = ['Rail Competitors', 'Rail_Business Scopes', 'Rail Customers', 'Rel Rail Customer - Rail Business Scopes'  ]   
        
        extra_context = {
            'rail_list' : rail_list,
            'product_list' : product_list,
            'location_list' : location_list,
            'class_list' : class_list,
            'other_list' : other_list, 
        }

        return super(AdminSiteExtend, self).index(request, extra_context)

    def app_index(self, request, app_label, extra_context=None):
        rail_list = ['Rail OEM Projects', 'Product lists', 'End User projects', 'Rail Biddings']
        product_list = ['Rail Product Groups', "Rail Product Types", 'Rail Products', 'Rail Product Setups', 'Rail Product Setup Values', 'Rel Rail Product Group - Product Types', 'Rel Rail Product Type - Products', 'Rel Rail Product - Product Setups', 'Rel Rail Product Setup - Setup Types' ]
        location_list = ['Areas', "Countrys", 'Regions', 'Provinces', 'Citys', 'Rel Area Countrys', 'Rel Country Regions',  'Rel Country Provinces', 'Rel Province Citys']        
        class_list = ['Rail Classes', 'Rail Types', 'Rail Platforms', 'Rel Rail Class - Rail Platforms','Rel Rail Class - Rail Types'] 
        other_list = ['Rail Competitors', 'Rail_Business Scopes', 'Rail Customers', 'Rel Rail Customer - Rail Business Scopes'  ]        
        
        extra_context = {
            'rail_list' : rail_list,
            'product_list' : product_list,
            'location_list' : location_list,
            'class_list' : class_list,
            'other_list' : other_list, 
        }

        return super(AdminSiteExtend, self).app_index(request, app_label, extra_context)
        

mysite = AdminSiteExtend()

mysite.register(models.Biz_Year, BizYearAdmin)   
#mysite.register(models.Vehicle_Project,VehicleProjectAdmin, RailBiddingForm, Vehicle_Project, Rail_Bidding)
mysite.register(models.Rail_Vehicle_Project,RailVehicleProjectAdmin)
mysite.register(models.Rail_Vehicle_Info,RailVehicleInfoAdmin)
mysite.register(models.Rail_Business_Scope,RailBusinessScopeAdmin)
mysite.register(models.Rail_Competitor,RailCompetitorAdmin)
mysite.register(models.Rail_Competitor_Bidding,RailCompetitorBiddingAdmin)
mysite.register(models.Rail_Contract,RailContractAdmin)
mysite.register(models.Currency,CurrencyAdmin)
mysite.register(models.Rail_Customer,RailCustomerAdmin)
#mysite.register(models.Rail_Customer_Bidding,RailCustomerBiddingAdmin) Modified by Toni Dong
mysite.register(models.Rail_Product,RailProductAdmin)
mysite.register(models.Rail_Product_Setup,RailProductSetupAdmin)
mysite.register(models.Rail_Product_Setup_Value,RailProductSetupValueAdim)
mysite.register(models.Rail_Product_Group,RailProductGroupAdmin)
mysite.register(models.Rail_Product_Type,RailProductTypeAdmin)
mysite.register(models.Rail_Project_in_Charge,RailProjectinChargeAdmin)
mysite.register(models.Rail_Bidding,RailBiddingAdmin)
mysite.register(models.Rail_Platform,RailPlatformAdmin)
mysite.register(models.Rail_Class,RailClassAdmin)
mysite.register(models.Rail_Tracking,RailTrackingAdmin)
mysite.register(models.Rail_Type,RailTypeAdmin)
mysite.register(models.Rail_Department,RailDepartmentAdmin)
#mysite.register(models.Rail_Package,RailPackageAdmin) Modified by Toni Dong
#mysite.register(models.Rail_Package_Line,RailPackageLineAdmin) Modified by Toni Dong
mysite.register(models.Product_lists,ProductListsAdmin) #Added by Toni Dong
mysite.register(models.Rail_Configuration,RailConfigurationAdmin)
mysite.register(models.Rail_OEM_Project,RailOEMProjectAdmin)

mysite.register(models.End_User,EndUserAdmin)
mysite.register(models.Employee,EmployeeAdmin)
mysite.register(models.Decision_Maker,DecisionMakerAdmin)
mysite.register(models.area,AreaAdmin)
mysite.register(models.country,CountryAdmin)
mysite.register(models.region,RegionAdmin)
mysite.register(models.province,ProvinceAdmin)
mysite.register(models.city,CityAdmin)
mysite.register(models.area_country,AreaCountryAdmin)
mysite.register(models.country_region,CountryRegionAdmin)
mysite.register(models.country_province,CountryProvinceAdmin)
mysite.register(models.region_province,RegionProvinceAdmin)
mysite.register(models.province_city,ProvinceCityAdmin)

mysite.register(models.Rail_Product_Group_Product_Type_r,RailProductGroupProductTypeAdmin)
mysite.register(models.Rail_Product_Type_Product_r,RailProductTypeProductAdmin)
mysite.register(models.Rail_Product_Product_Setup_r,RailProductProductSetupAdmin)
mysite.register(models.Rail_Product_Setup_Product_Setup_Value_r,RailProductSetupProductSetupValueAdmin)

mysite.register(models.Rail_Class_Type_r,RailClassTypeAdmin)
mysite.register(models.Rail_Class_Platform_r,RailClassPlatformAdmin)
mysite.register(models.Rail_Customer_Business_Scope_r,RailCustomerBusinessScopeAdmin)

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
mysite.register(Group, GroupAdmin)
mysite.register(User, UserAdmin)



'''
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin
mysite.register(Site, SiteAdmin)

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
mysite.register(FlatPage, FlatPageAdmin)

mysite.register(Comment, CommentsAdmin)
mysite.register(Redirect, RedirectAdmin)
'''

