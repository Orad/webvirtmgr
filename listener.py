#!/usr/bin/python
import sys
import libvirt
import requests
import threading
from hotqueue import HotQueue
from libvirt import libvirtError

VIR_DOMAIN_EVENT_MAPPING = {
    0: "VIR_DOMAIN_EVENT_DEFINED",
    1: "VIR_DOMAIN_EVENT_UNDEFINED",
    2: "VIR_DOMAIN_EVENT_STARTED",
    3: "VIR_DOMAIN_EVENT_SUSPENDED",
    4: "VIR_DOMAIN_EVENT_RESUMED",
    5: "VIR_DOMAIN_EVENT_STOPPED",
    6: "VIR_DOMAIN_EVENT_SHUTDOWN",
    7: "VIR_DOMAIN_EVENT_PMSUSPENDED",
}
VIR_DOMAIN_STATE_MAPPING = {
    0: "VIR_DOMAIN_NOSTATE",
    1: "VIR_DOMAIN_RUNNING",
    2: "VIR_DOMAIN_BLOCKED",
    3: "VIR_DOMAIN_PAUSED",
    4: "VIR_DOMAIN_SHUTDOWN",
    5: "VIR_DOMAIN_SHUTOFF",
    6: "VIR_DOMAIN_CRASHED",
    7: "VIR_DOMAIN_PMSUSPENDED",
}

libvirt.virEventRegisterDefaultImpl()
queue = HotQueue("ComputeQueue")
ApiDomain = "http://127.0.0.1:8000"

def event_lifecycle_callback(conn, dom, event, detail, opaque):
    url = '%s/api/save_event/'%(ApiDomain)
    data = {"instance_name": dom.name(),"event": VIR_DOMAIN_STATE_MAPPING.get(dom.state()[0], "?")}
    response = requests.post(url, data=data)

def conn_register_event_id_lifecycle(conn, url):
    callback_id = conn.domainEventRegisterAny( None,
        libvirt.VIR_DOMAIN_EVENT_ID_LIFECYCLE,
        event_lifecycle_callback,
        conn)
    for connection in connections:
        if connection['url'] == url:
            connection["callback_id"] = callback_id
            connection["conn"] = conn

def connect_socket():
    try:
        conn = libvirt.open('qemu:///system')
        conn_register_event_id_lifecycle(conn,"qemu:///system")
    except libvirtError as e:
        print 'Connection Failed: ' + str(e)

response = requests.get("%s/api/connections/"%(ApiDomain))
connections = response.json()
for connection in connections:
    if connection['type'] == 4:
        connect_socket()

def register_connection():
    while True:
        connection = queue.get()
        if connection:
            if connection["event"] == "Created":
                append = True
                for conn in connections:
                    if conn['url'] == connection["data"]["url"]:
                        conn['count'] += 1
                        append = False
                if append:
                    if connection["data"]["type"] == 4:
                        connections.append(connection["data"])
                        connect_socket()
            if connection["event"] == "Deleted":
                for conn in connections:
                    if conn['url'] == connection["data"]["url"]:
                        if conn['count'] == 1:
                            conn['conn'].domainEventDeregisterAny(conn['callback_id'])
                            connections.remove(conn) 
                        else:
                            conn['count'] -= 1

def event_listener():
    while True:
        libvirt.virEventRunDefaultImpl()

try:
    sensor_queue = threading.Thread(target=register_connection)        
    sensor_queue.daemon = True        
    sensor_queue.start()

    sensor_queue = threading.Thread(target=event_listener)        
    sensor_queue.daemon = True        
    sensor_queue.start()

    while (True):            
        pass
except (KeyboardInterrupt, SystemExit):
    print "[Exception] ERROR main thread halts"
