# -*- coding: utf-8 -*-
{
    'name': "employee_bank_approvals",

    'summary': """
    
        """,

    'description': """
        Employee Bank Approvals
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.1.7',

    # any module necessary for this one to work correctly
    'depends': ['hr_approvals'],

    # always loaded
    'data': ['data/bank_changes_data.xml',
             'views/employee_bank_approval_view.xml',
             'views/hr_employee_view.xml',
             'views/employee_bank_change.xml',
             'security/ir.model.access.csv'
             ],
    'installable': True,
    'application': True,
}
