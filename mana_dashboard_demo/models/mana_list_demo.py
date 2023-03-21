
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManaDashboardDemoListDemo(models.Model):
    '''
    Model Project
    '''
    _name = 'mana_dashboard_demo.list_demo'
    _description = 'Mana List Demo'

    name = fields.Char(string='name')
    image = fields.Char(string='image')
    increased = fields.Float(string='increased')
    status = fields.Char(string='status')
    author = fields.Char(string='author')
    price = fields.Float(string='price')
    progress = fields.Float(string='progress')


