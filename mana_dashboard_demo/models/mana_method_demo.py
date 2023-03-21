
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManaDashboardDemoMethodDemo(models.Model):
    '''
    Model Project
    '''
    _name = 'mana_dashboard_demo.method_demo'
    _description = 'Method Demo For Mana Dashboard'

    name = fields.Char(string='name')
