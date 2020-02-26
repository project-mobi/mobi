import whois


domain = whois.query('fabianvolkers.com')


print(domain.__dict__)
'''
Expected output for google.com:
{
        'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
        'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
        'registrar': 'MARKMONITOR INC.',
        'name': 'google.com',
        'creation_date': datetime.datetime(1997, 9, 15, 0, 0)

}
'''