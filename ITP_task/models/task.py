# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class Contacts(models.Model):
    _name = "contacts"
    _description = "Contacts"
    
    @api.model
    def create(self, vals):
        if not(re.search(regex,vals['email'])):
            raise ValidationError((_("Please Enter Valid Email Id")))
        
        # creating list        
        contacts_list = []  
        
        # appending instances to list 
        contacts_list.append(vals) 
        
        for obj in contacts_list: 
            if obj['email'] and obj['mobile']:
                existing_rec = self.search(['|', ('email', '=', obj['email']), ('mobile', '=', obj['mobile'])])
                leads_rec = self.env['leads'].search(['|', ('email', '=', obj['email']), ('mobile', '=', obj['mobile'])])
                
            if obj['email'] and not obj['mobile']:
                existing_rec = self.search([('email', '=', obj['email'])])
                leads_rec = self.env['leads'].search([('email', '=', obj['email'])])
                
            if obj['mobile'] and not obj['email']:
                existing_rec = self.search([('mobile', '=', obj['mobile'])])
                leads_rec = self.env['leads'].search([('mobile', '=', obj['mobile'])])
            
            if existing_rec:
                raise ValidationError((_("Record Allready Exists in Contact!")))

            if leads_rec:
                for rec in leads_rec:
                    print("rec",rec)
                    print("leads_rec",leads_rec)
                    l=[]
                    if rec.name:
                        print("rec.name check",rec.name)
                        l.append(rec.name) 
                        vals['name']=rec.name
                    if rec.email:    
                        print("rec.name check",rec.email)
                        l.append(rec.email) 
                        vals['email']=rec.email
                    if rec.mobile:       
                        print("rec.name check",rec.mobile)
                        l.append(rec.mobile) 
                        vals['mobile']=rec.mobile
                    print("------l----",l)    
                    print("last vals",vals)
                    rec.unlink()
                    
            print("Vals-----",vals)    
        result = super(Contacts, self).create(vals)
        return result
    
    name = fields.Char("Name", required=True)
    email = fields.Char("Email", size=128,)
    mobile = fields.Char("Mobile", size=10)
    
#    # function to read the json data and return in list
#    def get_contacts(self, json_data):
#        "return type: contact list"
#        contacts = []
#        
#        # assuming data got from ui (hard coded for now)
#        json_data = ['Alice Brown / None / 1231112223',
#            'Bob Crown / bob@crowns.com / None',
#            'Carlos Drew / carl@drewess.com / 3453334445',
#            'Doug Emerty / None / 4564445556',
#            'Egan Fair / eg@fairness.com / 5675556667']
#
#        # reading the data and storing it in list
#        for row in json_data:
#            name = row.split("/")[0]
#            email = row.split("/")[1] or ''
#            mobile = row.split("/")[2] or ''
#            d = {
#                'name':name,
#                'email':email,
#                'mobile':mobile,
#            }
#            contacts.append(d)
#        return contacts
    

    
    
    