

def get_connection(type, login, hostname):
    if type == 1:
        url = 'qemu+tcp://%s/system' % hostname
    if type == 2:
        url = 'qemu+ssh://%s@%s/system' % (login, hostname)
    if type == 3:
        url = 'qemu+tls://%s@%s/system' % (login, hostname)
    if type == 4:
        url = 'qemu:///system'
    return [{ "url": url, "type": type}]