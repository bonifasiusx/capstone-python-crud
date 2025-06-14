'''
siswa = [] To-Be --> [Isi data siswa yang ingin ditampilkan by default (Data Siswa + Status Kelulusan)]
'''

siswaDict = [ # List of Dictionary
    {
        'nis': '28LO',
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
        'nis': '19SE',
        'nama': 'Sheril Qonita', 
        'kelas': 'IX-1', 
        'nilai': {
            'Matematika': 86,
            'IPA': 88,
            'IPS': 78,
            'Bahasa IND': 94,
            'English': 90
        }
    },
    {
        'nis': '76EI',
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
        'nis': '31JE',
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
        'nis': '94RY',
        'nama': 'Raymond Murphy', 
        'kelas': 'IX-2', 
        'nilai': {
            'Matematika': 70,
            'IPA': 78,
            'IPS': 65,
            'Bahasa IND': 88,
            'English': 82
        }
    },
    {
        'nis': '46DD',
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
siswa = []
listMapel = list(siswaDict[0]['nilai'].keys()) 
# Akses key dari: SiswaDict -> [] -> {nilai} {keys,value}
siswaColumn = ['NIS', 'Nama', 'Kelas'] + listMapel # Concate listMapel ke column
# print(siswaDict[1])