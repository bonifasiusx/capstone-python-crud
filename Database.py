# List of Dictionary
siswaDict = [ 
    {
        'nis': '28LO',
        'nama': 'Leon Kennedy', 
        'kelas': 'IX-1', 
        'nilai': {
            'MTK': 80,
            'IPA': 78,
            'IPS': 82,
            'B.IND': 88,
            'B.ING': 85
        }
    },
    {
        'nis': '19SE',
        'nama': 'Sheril Qonita', 
        'kelas': 'IX-1', 
        'nilai': {
            'MTK': 86,
            'IPA': 88,
            'IPS': 78,
            'B.IND': 94,
            'B.ING': 90
        }
    },
    {
        'nis': '76EI',
        'nama': 'Elisabeth Rose', 
        'kelas': 'IX-3', 
        'nilai': {
            'MTK': 72,
            'IPA': 60,
            'IPS': 68,
            'B.IND': 75,
            'B.ING': 62
        }
    },
    {
        'nis': '31JE',
        'nama': 'Joe Hendrix', 
        'kelas': 'IX-2', 
        'nilai': {
            'MTK': 80,
            'IPA': 78,
            'IPS': 82,
            'B.IND': 88,
            'B.ING': 85
        }
    },
    {
        'nis': '94RY',
        'nama': 'Raymond Murphy', 
        'kelas': 'IX-2', 
        'nilai': {
            'MTK': 70,
            'IPA': 78,
            'IPS': 65,
            'B.IND': 88,
            'B.ING': 82
        }
    },
    {
        'nis': '46DD',
        'nama': 'Dudung Nalepa', 
        'kelas': 'IX-3', 
        'nilai': {
            'MTK': 62,
            'IPA': 65,
            'IPS': 65,
            'B.IND': 70,
            'B.ING': 45
        }
    },
]
siswa = [] # Lokasi tampilan default (Data Siswa & Status Kelulusan)
bin = [] # Lokasi penampungan soft-delete
listMapel = list(siswaDict[0]['nilai'].keys()) 
siswaColumn = ['NIS', 'Nama', 'Kelas'] + listMapel # Concate listMapel ke column
