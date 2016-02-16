# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'area'
        db.create_table('area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Rail', ['area'])

        # Adding model 'country'
        db.create_table('country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Rail', ['country'])

        # Adding model 'region'
        db.create_table('region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Rail', ['region'])

        # Adding model 'province'
        db.create_table('province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Rail', ['province'])

        # Adding model 'city'
        db.create_table('city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Rail', ['city'])

        # Adding model 'area_country'
        db.create_table('area_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.area'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.country'])),
        ))
        db.send_create_signal(u'Rail', ['area_country'])

        # Adding model 'country_region'
        db.create_table('country_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.region'])),
        ))
        db.send_create_signal(u'Rail', ['country_region'])

        # Adding model 'region_province'
        db.create_table('region_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.region'])),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.province'])),
        ))
        db.send_create_signal(u'Rail', ['region_province'])

        # Adding model 'province_city'
        db.create_table('province_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.province'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.city'])),
        ))
        db.send_create_signal(u'Rail', ['province_city'])

        # Adding model 'Biz_Year'
        db.create_table('biz_year', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Biz_Year'])

        # Adding model 'Currency'
        db.create_table('currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Rate', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'Rail', ['Currency'])

        # Adding model 'Rail_Class'
        db.create_table('rail_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Class'])

        # Adding model 'Rail_Platform'
        db.create_table('rail_platform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Platform'])

        # Adding model 'Rail_Type'
        db.create_table('rail_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Type'])

        # Adding model 'Rail_Class_Platform_r'
        db.create_table('rail_class_platform_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Class'])),
            ('Rail_Platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Platform'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Class_Platform_r'])

        # Adding model 'Rail_Class_Type_r'
        db.create_table('rail_class_type_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Class'])),
            ('Rail_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Type'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Class_Type_r'])

        # Adding model 'Rail_Vehicle_Project'
        db.create_table('rail_vehicle_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Vehicle_project_no', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('Line_Length', self.gf('django.db.models.fields.FloatField')(default=10, null=True, blank=True)),
            ('Created_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('Created_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Last_modified_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.area'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.region'], null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.province'], null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.city'], null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Vehicle_Project'])

        # Adding model 'Rail_OEM_Project'
        db.create_table('rail_oem_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('oem_project_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('vehicle_project_status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ts_qty', self.gf('django.db.models.fields.IntegerField')(max_length=11, null=True, blank=True)),
            ('Created_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Created_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Last_modified_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Biz_Year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Biz_Year'])),
            ('Rail_Vehicle_Project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Vehicle_Project'], null=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_OEM_Project'])

        # Adding model 'Rail_Business_Scope'
        db.create_table('rail_business_scope', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=300)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Business_Scope'])

        # Adding model 'Rail_Customer'
        db.create_table('rail_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('Location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Customer'])

        # Adding M2M table for field Rail_Business_Scope on 'Rail_Customer'
        m2m_table_name = db.shorten_name('rail_customer_Rail_Business_Scope')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rail_customer', models.ForeignKey(orm[u'Rail.rail_customer'], null=False)),
            ('rail_business_scope', models.ForeignKey(orm[u'Rail.rail_business_scope'], null=False))
        ))
        db.create_unique(m2m_table_name, ['rail_customer_id', 'rail_business_scope_id'])

        # Adding model 'Rail_Customer_Bidding'
        db.create_table('rail_customer_bidding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('OEM_Chance', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('Comments', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('Rail_Customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Customer'])),
            ('Currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Currency'])),
            ('Rail_OEM_Project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_OEM_Project'], null=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Customer_Bidding'])

        # Adding model 'Rail_Customer_Business_Scope_r'
        db.create_table('rail_customer_business_scope_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Customer'])),
            ('Rail_Business_Scope', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Business_Scope'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Customer_Business_Scope_r'])

        # Adding model 'Rail_Vehicle_Info'
        db.create_table('rail_vehicle_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('Car_per_TS', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('MCar_per_TS', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('Speed_From', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('Speed_To', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('Vehicle_Price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('TS_Config', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Rail_Platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Platform'])),
            ('Currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Currency'], null=True, blank=True)),
            ('Rail_Class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Class'])),
            ('Rail_Vehicle_Project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Vehicle_Project'], null=True, blank=True)),
            ('Rail_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Type'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Vehicle_Info'])

        # Adding model 'Rail_Contract'
        db.create_table('rail_contract', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Delivery_Terms', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('Customer_contract_no', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('VTA_contract_no', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('Total_Value_exclude_VAT', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Sales_Commission_Flag', self.gf('django.db.models.fields.BooleanField')(default=False, max_length=10)),
            ('Percentage_Down_Payment', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Total_Value_DP_exclude_VAT', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Advance_Payment_Bond_Percentage', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Performance_bond', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Contract_Training_Flag', self.gf('django.db.models.fields.BooleanField')(default=False, max_length=10)),
            ('Quality_Bond_Percentage', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Warranty_Period', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('Remark', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('Currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Currency'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Contract'])

        # Adding model 'Rail_Bidding'
        db.create_table('rail_bidding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Reason', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('Voith_Chance', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('Commercial_Priority', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('Commercial_Status', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('Technical_Priority', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('Technical_Status', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('OEM_Principle', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('Bidding_Status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('Ref_No1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('Ref_No2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('Decision_Maker', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Bidding_Price_exclude_VAT', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('Rail_OEM_Project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_OEM_Project'], null=True)),
            ('Rail_Contract', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Contract'], null=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Bidding'])

        # Adding model 'Rail_Competitor'
        db.create_table('rail_competitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Competitor'])

        # Adding model 'Rail_Competitor_Bidding'
        db.create_table('rail_competitor_bidding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Competitor_Price_exclude_VAT', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Winner_Flag', self.gf('django.db.models.fields.BooleanField')(default=False, max_length=10)),
            ('Comments', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
            ('Currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Currency'])),
            ('Rail_Competitor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Competitor'])),
            ('Rail_OEM_Project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_OEM_Project'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Competitor_Bidding'])

        # Adding model 'Rail_Product'
        db.create_table('rail_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product'])

        # Adding model 'Rail_Product_Type'
        db.create_table('rail_product_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Type'])

        # Adding model 'Rail_Product_Setup'
        db.create_table('rail_product_setup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Setup'])

        # Adding model 'Rail_Product_Setup_Value'
        db.create_table('rail_product_setup_value', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Setup_Value'])

        # Adding model 'Rail_Product_Group'
        db.create_table('rail_product_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Group'])

        # Adding model 'Rail_Product_Group_Product_Type_r'
        db.create_table('rail_product_group_product_type_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Product_Group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Group'])),
            ('Rail_Product_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Type'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Group_Product_Type_r'])

        # Adding model 'Rail_Product_Type_Product_r'
        db.create_table('rail_product_type_product_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Product_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Type'])),
            ('Rail_Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Type_Product_r'])

        # Adding model 'Rail_Product_Product_Setup_r'
        db.create_table('rail_product_product_setup_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product'])),
            ('Rail_Product_Setup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Setup'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Product_Setup_r'])

        # Adding model 'Rail_Product_Setup_Product_Setup_Value_r'
        db.create_table('rail_product_setup_product_setup_value_r', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Product_Setup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Setup'])),
            ('Rail_Product_Setup_Value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Setup_Value'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Product_Setup_Product_Setup_Value_r'])

        # Adding model 'Rail_Package'
        db.create_table('rail_package', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('Total_Price_exclude_VAT', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('Created_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('Created_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Last_modified_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Package'])

        # Adding M2M table for field Rail_Bidding on 'Rail_Package'
        m2m_table_name = db.shorten_name('rail_package_Rail_Bidding')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rail_package', models.ForeignKey(orm[u'Rail.rail_package'], null=False)),
            ('rail_bidding', models.ForeignKey(orm[u'Rail.rail_bidding'], null=False))
        ))
        db.create_unique(m2m_table_name, ['rail_package_id', 'rail_bidding_id'])

        # Adding model 'Rail_Configuration'
        db.create_table('rail_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Based_Price_exclude_VAT', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('Rail_Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product'])),
            ('Rail_Product_Setup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Setup'])),
            ('Rail_Product_Setup_Value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Setup_Value'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Configuration'])

        # Adding model 'Rail_Package_Line'
        db.create_table('rail_package_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rail_Package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Package'])),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('Quantity', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('Based_Price_exclude_VAT', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('Rail_Configuration', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Configuration'], null=True, blank=True)),
            ('Rail_Product_Group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Group'])),
            ('Rail_Product_Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product_Type'])),
            ('Rail_Product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Product'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Package_Line'])

        # Adding model 'Rail_Department'
        db.create_table('rail_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Rail', ['Rail_Department'])

        # Adding model 'Rail_Project_in_Charge'
        db.create_table('rail_project_in_charge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rep_Person', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Rail_Department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Department'])),
            ('Rail_Customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_Customer'])),
            ('Rail_OEM_Project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_OEM_Project'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Project_in_Charge'])

        # Adding model 'Rail_Tracking'
        db.create_table('rail_tracking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('OEM_Bidding', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Voith_Bidding', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('LOI', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('LOI_Kick_off', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('TA', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('TA_Kick_off', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Contract_Sign', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Contract_Kick_off', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('FAI', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('First_Delivery', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Last_Delivery', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Comments', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('Tracking_Flag', self.gf('django.db.models.fields.BooleanField')(default=False, max_length=10)),
            ('Rail_OEM_Project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rail.Rail_OEM_Project'])),
        ))
        db.send_create_signal(u'Rail', ['Rail_Tracking'])


    def backwards(self, orm):
        # Deleting model 'area'
        db.delete_table('area')

        # Deleting model 'country'
        db.delete_table('country')

        # Deleting model 'region'
        db.delete_table('region')

        # Deleting model 'province'
        db.delete_table('province')

        # Deleting model 'city'
        db.delete_table('city')

        # Deleting model 'area_country'
        db.delete_table('area_country')

        # Deleting model 'country_region'
        db.delete_table('country_region')

        # Deleting model 'region_province'
        db.delete_table('region_province')

        # Deleting model 'province_city'
        db.delete_table('province_city')

        # Deleting model 'Biz_Year'
        db.delete_table('biz_year')

        # Deleting model 'Currency'
        db.delete_table('currency')

        # Deleting model 'Rail_Class'
        db.delete_table('rail_class')

        # Deleting model 'Rail_Platform'
        db.delete_table('rail_platform')

        # Deleting model 'Rail_Type'
        db.delete_table('rail_type')

        # Deleting model 'Rail_Class_Platform_r'
        db.delete_table('rail_class_platform_r')

        # Deleting model 'Rail_Class_Type_r'
        db.delete_table('rail_class_type_r')

        # Deleting model 'Rail_Vehicle_Project'
        db.delete_table('rail_vehicle_project')

        # Deleting model 'Rail_OEM_Project'
        db.delete_table('rail_oem_project')

        # Deleting model 'Rail_Business_Scope'
        db.delete_table('rail_business_scope')

        # Deleting model 'Rail_Customer'
        db.delete_table('rail_customer')

        # Removing M2M table for field Rail_Business_Scope on 'Rail_Customer'
        db.delete_table(db.shorten_name('rail_customer_Rail_Business_Scope'))

        # Deleting model 'Rail_Customer_Bidding'
        db.delete_table('rail_customer_bidding')

        # Deleting model 'Rail_Customer_Business_Scope_r'
        db.delete_table('rail_customer_business_scope_r')

        # Deleting model 'Rail_Vehicle_Info'
        db.delete_table('rail_vehicle_info')

        # Deleting model 'Rail_Contract'
        db.delete_table('rail_contract')

        # Deleting model 'Rail_Bidding'
        db.delete_table('rail_bidding')

        # Deleting model 'Rail_Competitor'
        db.delete_table('rail_competitor')

        # Deleting model 'Rail_Competitor_Bidding'
        db.delete_table('rail_competitor_bidding')

        # Deleting model 'Rail_Product'
        db.delete_table('rail_product')

        # Deleting model 'Rail_Product_Type'
        db.delete_table('rail_product_type')

        # Deleting model 'Rail_Product_Setup'
        db.delete_table('rail_product_setup')

        # Deleting model 'Rail_Product_Setup_Value'
        db.delete_table('rail_product_setup_value')

        # Deleting model 'Rail_Product_Group'
        db.delete_table('rail_product_group')

        # Deleting model 'Rail_Product_Group_Product_Type_r'
        db.delete_table('rail_product_group_product_type_r')

        # Deleting model 'Rail_Product_Type_Product_r'
        db.delete_table('rail_product_type_product_r')

        # Deleting model 'Rail_Product_Product_Setup_r'
        db.delete_table('rail_product_product_setup_r')

        # Deleting model 'Rail_Product_Setup_Product_Setup_Value_r'
        db.delete_table('rail_product_setup_product_setup_value_r')

        # Deleting model 'Rail_Package'
        db.delete_table('rail_package')

        # Removing M2M table for field Rail_Bidding on 'Rail_Package'
        db.delete_table(db.shorten_name('rail_package_Rail_Bidding'))

        # Deleting model 'Rail_Configuration'
        db.delete_table('rail_configuration')

        # Deleting model 'Rail_Package_Line'
        db.delete_table('rail_package_line')

        # Deleting model 'Rail_Department'
        db.delete_table('rail_department')

        # Deleting model 'Rail_Project_in_Charge'
        db.delete_table('rail_project_in_charge')

        # Deleting model 'Rail_Tracking'
        db.delete_table('rail_tracking')


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