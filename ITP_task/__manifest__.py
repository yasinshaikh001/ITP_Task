# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'ITP TASK',
    'version': '1.1',
    'category': 'Extra Tools',
    'sequence': 1,
    'summary': 'ITP TASK',
    'description': """ITP""",
    'website': 'https://www.odoo.com/page/accounting',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/task.xml',
        'views/leads.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'uninstall_hook': "uninstall_hook",
    'license': 'OEEL-1',
}
