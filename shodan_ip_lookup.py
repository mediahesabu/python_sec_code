import shodan

SHODAN_API_KEY = "MY_API_KEY"

api = shodan.Shodan(SHODAN_API_KEY)

try:
# Lookup the host
    host = api.host('131.247.182.229')
    
    print "IP Address:", host['ip_str']
    print "Organization:", host.get('org', 'n/a')
    print "Operating System", host.get('os', 'n/a')
    
    for item in host['data']:
        print """
                    Port: %s
                    Banner: %s
    
            """ % (item['port'], item['data'])    
    
except shodan.APIError, e:
    print 'Error: %s' % e