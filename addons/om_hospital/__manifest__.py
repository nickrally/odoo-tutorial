{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'sequence': -100,
    'category':'',
    'summary':'',
    'depends': ['mail','product'],
    'data':[
        'security/ir.model.access.csv',
        'wizard/cancel_appointement_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'data/sequence.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application':True,
    'assets':{}
}