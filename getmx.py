import dns.resolver


def get_host(domain="google.com"):
    try:
        host = dns.resolver.resolve(domain, 'MX')[0]
    except:
        print("No mail exchange found for domain {}".format(domain))
    return host.to_text().split()[1][:-1]

print(get_host())