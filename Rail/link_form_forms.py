from Rail.link_form_admin import LinkFormAdminForm
from django import forms

class RailPackageForm(LinkFormAdminForm):
    class Meta:
#        model = models.Rail_Package
        verbose_name = 'Rail Package'
        class_name = "rail_package"
        
    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    Name = forms.CharField(max_length=11, label = "Name", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Description = forms.CharField(max_length=50, label = "Description", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Total_Price_exclude_VAT = forms.CharField(max_length=11, label = "Total Price exclude VAT", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

#    readonly_fields = ('Name','Description','Total_Price_exclude_VAT')
    
#    prefix = "__prefix__"

    def __unicode__(self):
        return u'%s %s' % (self.id, self.Name)  

    def is_valid(self):
        return super(RailPackageForm, self).is_valid()            

class RailBiddingForm(LinkFormAdminForm):
    class Meta:
        verbose_name = 'Rail Bidding'
        class_name = "rail_bidding"
        
    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 

    Reason = forms.CharField(max_length=500, label = "Description", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Voith_Chance = forms.CharField(max_length=50, label = "Voith Chance", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Bidding_Status = forms.CharField(max_length=11, label = "Bidding Status", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Total_Bidding_Price_exclude_VAT = forms.CharField(max_length=21, label = "Total Bidding Price exclude VAT", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    Decision_Maker =  forms.CharField(max_length=21, label = "Decision Maker", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))                            

    def __unicode__(self):
        return u'%s %s' % (self.id, self.Name)  

    def is_valid(self):
        return super(RailBiddingForm, self).is_valid() 

class RailOEMProjectForm(LinkFormAdminForm):
    class Meta:
        verbose_name = 'Rail OEM Project'
        class_name = "rail_oem_project"

    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True}))         
    oem_project_code = forms.CharField(max_length=11, label = "oem_project_code", required=False, widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    #Description = forms.CharField(max_length=50, label = "Description", required=False, widget = 
    #                         forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    vehicle_project_status = forms.CharField(max_length=11, label = "vehicle_project_status", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    ts_qty = forms.CharField(max_length=11, label = "Ts_qty", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))
    Biz_Year = forms.CharField(max_length=11, label = "Biz_Year", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    def __unicode__(self):
        return u'%s %s' % (self.id, self.oem_project_code)  

    def is_valid(self):
        return super(RailOEMProjectForm, self).is_valid() 
