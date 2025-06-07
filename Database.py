'''
Si
'''

siswaDict = [ # List of Dictionary
    {
        'nis': '49LO',
        'nama': 'Leon Kennedy', 
        'kelas': 'IX-1', 
        'nilai': {
            'Matematika': 80,
            'IPA': 78,
            'IPS': 82,
            'Bahasa IND': 88,
            'English': 85
        }
    },
    {
        'nis': '34SEI',
        'nama': 'Sheril Qonita', 
        'kelas': 'IX-1', 
        'nilai': {
            'Matematika': 94,
            'IPA': 88,
            'IPS': 78,
            'Bahasa IND': 86,
            'English': 90
        }
    },
    {
        'nis': '22EIA',
        'nama': 'Elisabeth Rose', 
        'kelas': 'IX-3', 
        'nilai': {
            'Matematika': 72,
            'IPA': 60,
            'IPS': 68,
            'Bahasa IND': 75,
            'English': 62
        }
    },
    {
        'nis': '25JEH',
        'nama': 'Joe Hendrix', 
        'kelas': 'IX-2', 
        'nilai': {
            'Matematika': 80,
            'IPA': 78,
            'IPS': 82,
            'Bahasa IND': 88,
            'English': 85
        }
    },
    {
        'nis': '7RYO',
        'nama': 'Raymond Murphy', 
        'kelas': 'IX-2', 
        'nilai': {
            'Matematika': 88,
            'IPA': 78,
            'IPS': 65,
            'Bahasa IND': 70,
            'English': 82
        }
    },
    {
        'nis': '16DDN',
        'nama': 'Dudung Nalepa', 
        'kelas': 'IX-3', 
        'nilai': {
            'Matematika': 62,
            'IPA': 65,
            'IPS': 65,
            'Bahasa IND': 70,
            'English': 45
        }
    },
]
siswa = [] # To-be --> Nested-list
listMapel = list(siswaDict[0]['nilai'].keys()) 
# Akses key dari: SiswaDict -> [] -> {nilai} {keys,value}
siswaColumn = ['NIS', 'Nama', 'Kelas'] + listMapel # Concate listMapel ke column