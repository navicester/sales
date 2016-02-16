
from django import forms
from Rail import models
from django.forms.models import ModelForm

class Rail_PackageForm(ModelForm):
    class Meta:
        model = models.Rail_Package
        verbose_name = 'Rail Package'
        
    id = forms.CharField(max_length=11, widget = forms.TextInput(attrs={'readonly':'readonly','disable':True}), label = 'id') 
    Name = forms.CharField(max_length=11, required=False, label = 'Name', widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Description = forms.CharField(max_length=50, label = 'Description', required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Total_Price_exclude_VAT = forms.CharField(max_length=11, label = 'Total_Price_exclude_VAT', required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

    def __unicode__(self):
        return u'%s %s' % (self.id, self.Name)  

    ''' # why here it doesn't work ?
    def __init__(self, *args, **kwargs):
        super(Rail_PackageForm, self).__init__(*args, **kwargs)
        self.fields['id'].label = "id"
        self.fields['Name'].label = "Name"
        self.fields['Description'].label = "Description"
        self.fields['Total_Price_exclude_VAT'].label = "Total_Price_exclude_VAT"        
    '''
class Rail_BiddingForm(ModelForm):
    class Meta:
        verbose_name = 'Rail Bidding'
        
    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    Reason = forms.CharField(max_length=500, label = "Reason", required=False, widget = 
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


class Rail_OEM_ProjectForm(ModelForm):
    class Meta:
        verbose_name = 'Rail OEM Project'

    id = forms.CharField(max_length=11, label = "id", widget = forms.TextInput(attrs={'readonly':'readonly','disable':True}))         
    oem_project_code = forms.CharField(max_length=11, label = "oem_project_code", required=False, widget = forms.TextInput(attrs={'readonly':'readonly','disable':True})) 
    Description = forms.CharField(max_length=50, label = "Description", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    vehicle_project_status = forms.CharField(max_length=11, label = "vehicle_project_status", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Biz_Year = forms.CharField(max_length=11, label = "Biz_Year", required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    def __unicode__(self):
        return u'%s %s' % (self.oem_project_code, self.Name)  




    
