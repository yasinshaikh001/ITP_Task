# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class Leads(models.Model):
    _name = "leads"
    _description = "Leads"
    
    @api.model
    def create(self, vals):
        if not(re.search(regex,vals['email'])):
            raise ValidationError((_("Please Enter Valid Email Id")))
        
        # creating list        
        lead_list = []  
        
        # appending instances to list 
        lead_list.append(vals) 
        
        print(lead_list)
        print(vals)
        for obj in lead_list: 
            print(obj['name'])
            
            if obj['email']:
                if self.env['leads'].search([('email', '=', obj['email'])]):
                    print("Email Found Add to contact")
                if self.env['leads'].search([('mobile', '=', obj['mobile'])]):
                    print("Mobile Found Add to contact") 
                    
        result = super(Leads, self).create(vals)
        return result
    
#    def write(self, values):
#        if not(re.search(regex,values['email'])):
#            raise ValidationError((_("Please Enter Valid Email Id")))
#            
#        result = super(Leads, self).write(values)
#        return result

        
        
    
    name = fields.Char("Name")
    email = fields.Char("Email")
    mobile = fields.Char("Mobile", size=10)

    