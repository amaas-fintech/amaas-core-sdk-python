# POTENTIALLY SUPPORT MULTIPLE ENVIRONMENTS

LOCAL = False

if LOCAL:
    ENDPOINTS = {
        'assets': 'http://localhost:8000',
        'books': 'http://localhost:8000',
        'monitor': 'http://localhost:8000',
        'parties': 'http://localhost:8000',
        'transactions': 'http://localhost:8000'
    }
else:
    ENDPOINTS = {
        'assets': 'https://zc6udsq1nb.execute-api.ap-southeast-1.amazonaws.com/dev',
        'books': 'https://smc367plfg.execute-api.ap-southeast-1.amazonaws.com/dev',
        'monitor': 'https://wt50nd7j7l.execute-api.ap-southeast-1.amazonaws.com/dev',
        'parties': 'https://hpihgzmxoc.execute-api.ap-southeast-1.amazonaws.com/dev',
        'transactions': 'https://1w0gb581sl.execute-api.ap-southeast-1.amazonaws.com/dev'
    }
