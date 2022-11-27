{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'sequence': -100,
    'category':'',
    'summary':'',
    'depends': ['mail','product'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'data/sequence.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application':True,
    'assets':{}
}