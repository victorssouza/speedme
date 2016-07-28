#!/usr/bin/env python
#Version: 2.0

from influxdb import InfluxDBClient
import datetime
import os

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")
    return current_time

def getting_env_container_hosts():
    if os.system('echo $SPEEDME_INFLUXDB_PORT_8086_TCP_ADDR') == '':
        influxdb_host="localhost"
    elif os.system('echo $SPEEDME_INFLUXDB_PORT_8086_TCP_ADDR') != '':
        #Getting the ip from influxdb container using /etc/hosts file
        #os.system("cat /etc/hosts | awk '($2==\"speedme_influxdb\") {print}' | awk '{print $1}' > influx_db_container_ip.txt")
        os.system('echo $SPEEDME_INFLUXDB_PORT_8086_TCP_ADDR > influx_db_container_ip.txt')
        file = open('influx_db_container_ip.txt', 'r')
        influxdb_host = file.readline().rstrip()
        file.close()

    return influxdb_host

def get_internet_measure():
    with os.popen('speedtest --simple') as speedtest_output:
        for line in speedtest_output:
            label, value, unit = line.split()
            if 'Ping' in label:
                ping = float(value)
            elif 'Download' in label:
                download = float(value)
            elif 'Upload' in label:
                upload = float(value)
        return ping, download, upload


def public_metrics_into_influxdb():
    ping, download, upload = get_internet_measure()
    current_time = get_time()

    net_json_body = [
        {
        "measurement": "internet_measure",
        "tags": {
            "host": "desktop-lab",
            "contract": "Vivo Fibra"
            },
        "time": str(current_time),
        "fields": {
            "ping": ping,
            "download":download,
            "upload": upload
            }
        }
    ]

    print ("\n=========" )
    print ("Inserting: \n" + str(net_json_body))

    influxdb_host = getting_env_container_hosts()
    client = InfluxDBClient(influxdb_host, 8086, 'root', 'root', 'internet_measure')
    client.create_database('internet_measure')
    client.write_points(net_json_body)
    print ("=========\n")   

public_metrics_into_influxdb()