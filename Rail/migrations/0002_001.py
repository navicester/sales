# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'country_province'
        db.create_table('country_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.country'])),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.province'])),
        ))
        db.send_create_signal(u'Rail', ['country_province'])


    def backwards(self, orm):
        # Deleting model 'country_province'
        db.delete_table('country_province')


    models = {
        u'Rail.area': {
            'Meta': {'object_name': 'area', 'db_table': "'area'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.area_country': {
            'Meta': {'object_name': 'area_country', 'db_table': "'area_country'"},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.area']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.biz_year': {
            'Meta': {'object_name': 'Biz_Year', 'db_table': "'biz_year'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.city': {
            'Meta': {'object_name': 'city', 'db_table': "'city'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.country': {
            'Meta': {'object_name': 'country', 'db_table': "'country'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.country_province': {
            'Meta': {'object_name': 'country_province', 'db_table': "'country_province'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.province']"})
        },
        u'Rail.country_region': {
            'Meta': {'object_name': 'country_region', 'db_table': "'country_region'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.region']"})
        },
        u'Rail.currency': {
            'Meta': {'object_name': 'Currency', 'db_table': "'currency'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Rate': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.province': {
            'Meta': {'object_name': 'province', 'db_table': "'province'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.province_city': {
            'Meta': {'object_name': 'province_city', 'db_table': "'province_city'"},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.city']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.province']"})
        },
        u'Rail.rail_bidding': {
            'Bidding_Price_exclude_VAT': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'Bidding_Status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Commercial_Priority': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'Commercial_Status': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'Decision_Maker': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Rail_Bidding', 'db_table': "'rail_bidding'"},
            'OEM_Principle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Rail_Contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Contract']", 'null': 'True'}),
            'Rail_OEM_Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_OEM_Project']", 'null': 'True'}),
            'Reason': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'Ref_No1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Ref_No2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Technical_Priority': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'Technical_Status': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'Voith_Chance': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_business_scope': {
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'Meta': {'object_name': 'Rail_Business_Scope', 'db_table': "'rail_business_scope'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_class': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Class', 'db_table': "'rail_class'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_class_platform_r': {
            'Meta': {'object_name': 'Rail_Class_Platform_r', 'db_table': "'rail_class_platform_r'"},
            'Rail_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Class']"}),
            'Rail_Platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Platform']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_class_type_r': {
            'Meta': {'object_name': 'Rail_Class_Type_r', 'db_table': "'rail_class_type_r'"},
            'Rail_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Class']"}),
            'Rail_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Type']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_competitor': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Competitor', 'db_table': "'rail_competitor'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_competitor_bidding': {
            'Comments': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'Competitor_Price_exclude_VAT': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Currency']"}),
            'Meta': {'object_name': 'Rail_Competitor_Bidding', 'db_table': "'rail_competitor_bidding'"},
            'Rail_Competitor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Competitor']"}),
            'Rail_OEM_Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_OEM_Project']"}),
            'Winner_Flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_configuration': {
            'Based_Price_exclude_VAT': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Configuration', 'db_table': "'rail_configuration'"},
            'Rail_Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product']"}),
            'Rail_Product_Setup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Setup']"}),
            'Rail_Product_Setup_Value': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Setup_Value']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_contract': {
            'Advance_Payment_Bond_Percentage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Contract_Training_Flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '10'}),
            'Currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Currency']"}),
            'Customer_contract_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Delivery_Terms': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Contract', 'db_table': "'rail_contract'"},
            'Percentage_Down_Payment': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Performance_bond': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Quality_Bond_Percentage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Remark': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Sales_Commission_Flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '10'}),
            'Total_Value_DP_exclude_VAT': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Total_Value_exclude_VAT': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'VTA_contract_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Warranty_Period': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_customer': {
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'Location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Customer', 'db_table': "'rail_customer'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Rail_Business_Scope': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Rail.Rail_Business_Scope']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_customer_bidding': {
            'Comments': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Currency']"}),
            'Meta': {'object_name': 'Rail_Customer_Bidding', 'db_table': "'rail_customer_bidding'"},
            'OEM_Chance': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'Rail_Customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Customer']"}),
            'Rail_OEM_Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_OEM_Project']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_customer_business_scope_r': {
            'Meta': {'object_name': 'Rail_Customer_Business_Scope_r', 'db_table': "'rail_customer_business_scope_r'"},
            'Rail_Business_Scope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Business_Scope']"}),
            'Rail_Customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_department': {
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Department', 'db_table': "'rail_department'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_oem_project': {
            'Biz_Year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Biz_Year']"}),
            'Created_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Created_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'Last_modified_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_OEM_Project', 'db_table': "'rail_oem_project'"},
            'Rail_Vehicle_Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Vehicle_Project']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'oem_project_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ts_qty': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'vehicle_project_status': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Rail.rail_package': {
            'Created_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Created_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'Last_modified_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Package', 'db_table': "'rail_package'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Rail_Bidding': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Rail.Rail_Bidding']", 'null': 'True', 'symmetrical': 'False'}),
            'Total_Price_exclude_VAT': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_package_line': {
            'Based_Price_exclude_VAT': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Package_Line', 'db_table': "'rail_package_line'"},
            'Quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'Rail_Configuration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Configuration']", 'null': 'True', 'blank': 'True'}),
            'Rail_Package': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Package']"}),
            'Rail_Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product']"}),
            'Rail_Product_Group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Group']"}),
            'Rail_Product_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Type']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_platform': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Platform', 'db_table': "'rail_platform'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Product', 'db_table': "'rail_product'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_group': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Product_Group', 'db_table': "'rail_product_group'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_group_product_type_r': {
            'Meta': {'object_name': 'Rail_Product_Group_Product_Type_r', 'db_table': "'rail_product_group_product_type_r'"},
            'Rail_Product_Group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Group']"}),
            'Rail_Product_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Type']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_product_setup_r': {
            'Meta': {'object_name': 'Rail_Product_Product_Setup_r', 'db_table': "'rail_product_product_setup_r'"},
            'Rail_Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product']"}),
            'Rail_Product_Setup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Setup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_setup': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Product_Setup', 'db_table': "'rail_product_setup'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_setup_product_setup_value_r': {
            'Meta': {'object_name': 'Rail_Product_Setup_Product_Setup_Value_r', 'db_table': "'rail_product_setup_product_setup_value_r'"},
            'Rail_Product_Setup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Setup']"}),
            'Rail_Product_Setup_Value': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Setup_Value']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_setup_value': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Product_Setup_Value', 'db_table': "'rail_product_setup_value'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_type': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Product_Type', 'db_table': "'rail_product_type'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_product_type_product_r': {
            'Meta': {'object_name': 'Rail_Product_Type_Product_r', 'db_table': "'rail_product_type_product_r'"},
            'Rail_Product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product']"}),
            'Rail_Product_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Product_Type']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_project_in_charge': {
            'Meta': {'object_name': 'Rail_Project_in_Charge', 'db_table': "'rail_project_in_charge'"},
            'Rail_Customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Customer']"}),
            'Rail_Department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Department']"}),
            'Rail_OEM_Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_OEM_Project']"}),
            'Rep_Person': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_tracking': {
            'Comments': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'Contract_Kick_off': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Contract_Sign': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FAI': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'First_Delivery': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'LOI': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'LOI_Kick_off': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Last_Delivery': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Tracking', 'db_table': "'rail_tracking'"},
            'OEM_Bidding': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Rail_OEM_Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_OEM_Project']"}),
            'TA': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'TA_Kick_off': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Tracking_Flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '10'}),
            'Voith_Bidding': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_type': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Type', 'db_table': "'rail_type'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_vehicle_info': {
            'Car_per_TS': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'Currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Currency']", 'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'MCar_per_TS': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'Meta': {'object_name': 'Rail_Vehicle_Info', 'db_table': "'rail_vehicle_info'"},
            'Rail_Class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Class']"}),
            'Rail_Platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Platform']"}),
            'Rail_Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Type']"}),
            'Rail_Vehicle_Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.Rail_Vehicle_Project']", 'null': 'True', 'blank': 'True'}),
            'Speed_From': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'Speed_To': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'TS_Config': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Vehicle_Price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.rail_vehicle_project': {
            'Created_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Created_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'Last_modified_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Line_Length': ('django.db.models.fields.FloatField', [], {'default': '10', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Rail_Vehicle_Project', 'db_table': "'rail_vehicle_project'"},
            'Vehicle_project_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.area']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.city']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.province']", 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.region']", 'null': 'True', 'blank': 'True'})
        },
        u'Rail.region': {
            'Meta': {'object_name': 'region', 'db_table': "'region'"},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Rail.region_province': {
            'Meta': {'object_name': 'region_province', 'db_table': "'region_province'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.province']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rail.region']"})
        }
    }

    complete_apps = ['Rail']