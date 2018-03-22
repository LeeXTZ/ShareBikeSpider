import requests
import xlrd
from xlutils.copy import copy
import numpy as np
import time
import multiprocessing
import random
import bd2WGS

global proxies
proxies = []


def data_get(lat, lng, prox):

    proxy_list1 = [{'http': 'http://120.77.182.203:8888'},
                   {'http': 'http://120.77.87.231:8888'},
                  {'http': 'http://112.74.172.125:8888'},
                  {'http': 'http://120.77.144.75:8888'},
                  {'http': 'http://117.33.185.160:8118'},
                  {'http': 'http://121.196.226.246:84'},
                  {'http': 'http://111.13.7.116:80'},
                  {'http': 'http://118.144.54.247:8118'},
                  {'http': 'http://59.38.241.196:808'},
                  {'http': 'http://120.77.145.164:8888'},
                  {'http': 'http://120.77.155.191:8888'},
                  {'http': 'http://119.36.92.47:843'},
                  {'http': 'http://120.77.182.21:8888'},
                  {'http': 'http://221.10.85.149:808'},
                  {'http': 'http://111.13.7.122:80'},
                  {'http': 'http://120.77.154.125:8888'},
                  {'http': 'http://182.18.20.192:8088'},
                  {'http': 'http://124.133.230.254:80'},
                   {'http': 'http://61.152.81.193:9100'},
                   {'http': 'http://61.152.81.193:9100'},
                   {'http': 'http://60.178.4.205:8081'},
                   {'http': 'http://1.82.132.75:8080'},
                   {'http': 'http://122.70.145.49:80'},
                   {'http': 'http://120.77.203.202:8888'},
                   {'http': 'http://125.77.25.124:80'},
                   {'http': 'http://120.83.13.53:8080'},
                   {'http': 'http://101.37.35.17:3128'},
                  {'http': 'http://111.13.7.118:80'},
                  {'http': 'http://111.13.141.99:80'},
                  {'http': 'http://183.222.102.102:8080'},
                  {'http': 'http://121.226.155.51:808'},
                  {'http': 'http://123.207.30.187:3128'},
                  {'http': 'http://110.73.9.238:8123'},
                  {'http': 'http://120.77.174.216:8888'},
                  {'http': 'http://124.206.133.219:3128'},
                  {'http': 'http://166.111.77.32:3128'},
                  {'http': 'http://120.77.152.51:8888'},
                  {'http': 'http://120.77.180.24:8888'},
                  {'http': 'http://118.144.54.247:8118'},
                  {'http': 'http://119.36.92.47:843'},
                  {'http': 'http://120.77.182.203:8888'},
                  {'http': 'http://120.77.155.191:8888'},
                  {'http': 'http://120.77.154.153:8888'},
                  {'http': 'http://125.77.25.123:80'},
                  {'http': 'http://114.215.150.13:3128'},
                  {'http': 'http://121.196.226.246:84'},
                  {'http': 'http://123.206.107.106:8080'},
                  {'http': 'http://61.152.81.193:9100'},
                  {'http': 'http://61.152.81.193:9100'},
                  {'http': 'http://1.82.132.75:8080'},
                  {'http': 'http://60.178.4.205:8081'},
                  {'http': 'http://221.10.85.149:808'},
                  {'http': 'http://111.13.7.122:80'},
                  {'http': 'http://124.133.230.254:80'},
                  {'http': 'http://120.77.144.75:8888'},
                  {'http': 'http://111.13.7.118:80'},
                  {'http': 'http://111.13.7.116:80'},
                  {'http': 'http://111.13.7.42:843'},
                  {'http': 'http://122.70.145.49:80'},
                  {'http': 'http://120.77.203.202:8888'},
                  {'http': 'http://125.77.25.124:80'},
                  {'http': 'http://120.83.13.53:8080'},
                  {'http': 'http://113.58.232.203:808'},
                  {'http': 'http://182.18.20.192:8088'},
                  {'http': 'http://120.77.145.164:8888'},
                  {'http': 'http://120.77.155.249:8888'},
                  {'http': 'http://166.111.77.32:3128'},
                  {'http': 'http://219.129.164.122:3128'},
                  {'http': 'http://219.153.76.77:8080'},
                  {'http': 'http://111.13.141.99:80'},
                  {'http': 'http://120.77.180.24:8888'},
                  {'http': 'http://183.222.102.102:8080'},
                  {'http': 'http://120.77.177.212:8888'},
                  {'http': 'http://123.207.30.187:3128'},
                  {'http': 'http://112.74.189.103:8888'},
                  {'http': 'http://112.84.1.208:808'},
                  {'http': 'http://120.77.152.51:8888'},
                  {'http': 'http://111.13.7.117:80'},
                  {'http': 'http://120.77.182.35:8888'},
                  {'http': 'http://180.96.27.12:88'},
                  {'http': 'http://120.77.174.216:8888'},
                  {'http': 'http://113.243.40.171:80'},
                  {'http': 'http://183.222.102.95:8080'},
                  {'http': 'http://120.27.163.210:3128'},
                  {'http': 'http://111.9.116.145:8080'},
                  {'http': 'http://119.23.133.113:8088'},
                  {'http': 'http://42.81.11.22:8080'},
                  {'http': 'http://220.174.236.211:80'},
                  {'http': 'http://61.160.208.222:8080'},
                  {'http': 'http://120.194.18.90:81'},
                  {'http': 'http://183.222.102.108:80'},
                  {'http': 'http://112.74.59.231:8888'},
                  {'http': 'http://101.37.79.125:3128'},
                  {'http': 'http://120.199.224.78:80'},
                  {'http': 'http://118.190.14.107:3128'},
                  {'http': 'http://120.77.86.173:8888'},
                  {'http': 'http://222.169.193.162:8099'},
                  {'http': 'http://118.178.124.33:3128'},
                  {'http': 'http://42.51.26.79:3128'},
                  {'http': 'http://121.15.220.61:80'},
                  {'http': 'http://120.52.21.132:8082'},
                  {'http': 'http://183.222.102.97:8080'},
                  {'http': 'http://202.85.213.220:3128'},
                  {'http': 'http://58.16.42.140:80'},
                  {'http': 'http://60.178.3.62:8081'},
                  {'http': 'http://119.36.92.42:80'},
                  {'http': 'http://120.77.156.103:8888'},
                  {'http': 'http://120.77.85.115:8888'},
                  {'http': 'http://218.241.131.249:80'},
                  {'http': 'http://183.222.102.98:8080'},
                  {'http': 'http://183.222.102.104:8080'},
                  {'http': 'http://120.77.171.88:8888'},
                  {'http': 'http://120.132.71.212:80'},
                  {'http': 'http://101.201.151.16:8088'},
                  {'http': 'http://113.107.112.210:8101'},
                  {'http': 'http://120.77.176.179:8888'},
                  {'http': 'http://125.77.25.116:80'},
                  {'http': 'http://101.200.44.5:8888'}]

    proxy_list2 = [{'http': 'http://123.206.107.106:8080'},
                   {'http': 'http://123.207.30.187:3128'},
                   {'http': 'http://120.83.13.53:8080'},
                   {'http': 'http://120.77.152.51:8888'},
                   {'http': 'http://111.1.3.38:8000'},
                   {'http': 'http://166.111.77.32:3128'},
                   {'http': 'http://183.222.102.102:8080'},
                   {'http': 'http://120.77.155.249:8888'},
                   {'http': 'http://125.77.25.124:80'},
                   {'http': 'http://211.143.155.172:80'},
                   {'http': 'http://61.139.79.93:8080'},
                   {'http': 'http://183.230.177.170:8081'},
                   {'http': 'http://111.13.7.117:80'},
                   {'http': 'http://120.77.153.53:8888'},
                   {'http': 'http://183.153.29.214:808'},
                   {'http': 'http://171.38.36.78:8123'},
                   {'http': 'http://117.21.234.107:8080'},
                   {'http': 'http://120.77.146.200:8888'},
                   {'http': 'http://111.13.2.138:80'},
                   {'http': 'http://123.59.101.100:80'},
                   {'http': 'http://121.31.86.230:8123'},
                   {'http': 'http://121.31.102.135:8123'},
                   {'http': 'http://111.13.2.131:80'},
                   {'http': 'http://139.129.94.241:3128'},
                   {'http': 'http://221.203.88.202:80'},
                   {'http': 'http://202.195.192.197:3128'},
                   {'http': 'http://211.143.155.167:80'},
                   {'http': 'http://120.77.183.34:8888'},
                   {'http': 'http://114.238.62.25:808'},
                   {'http': 'http://183.153.8.49:808'},
                   {'http': 'http://111.1.3.34:8000'},
                   {'http': 'http://112.74.189.103:8888'},
                   {'http': 'http://112.74.189.103:8888'},
                   {'http': 'http://123.206.107.106:8080'},
                   {'http': 'http://122.70.145.49:80'},
                   {'http': 'http://61.139.79.93:8080'},
                   {'http': 'http://120.77.155.249:8888'},
                   {'http': 'http://61.152.81.193:9100'},
                   {'http': 'http://120.77.174.216:8888'},
                   {'http': 'http://110.157.179.59:8888'},
                   {'http': 'http://120.77.152.51:8888'},
                   {'http': 'http://120.77.180.24:8888'},
                   {'http': 'http://120.77.151.160:8888'},
                   {'http': 'http://183.153.29.214:808'},
                   {'http': 'http://111.13.2.138:80'},
                   {'http': 'http://101.37.79.125:3128'},
                   {'http': 'http://120.199.224.78:80'},
                   {'http': 'http://120.194.18.90:81'},
                   {'http': 'http://120.77.86.173:8888'},
                   {'http': 'http://27.44.160.139:80'},
                   {'http': 'http://120.77.182.21:8888'},
                   {'http': 'http://101.53.101.172:9999'},
                   {'http': 'http://218.241.131.249:80'},
                   {'http': 'http://119.7.81.213:808'},
                   {'http': 'http://119.36.92.42:80'},
                   {'http': 'http://113.107.112.210:8101'},
                   {'http': 'http://120.77.85.115:8888'},
                   {'http': 'http://58.16.42.140:80'},
                   {'http': 'http://120.77.148.161:8888'},
                   {'http': 'http://120.77.87.231:8888'},
                   {'http': 'http://101.201.151.16:8088'},
                   {'http': 'http://120.77.171.88:8888'},
                   {'http': 'http://42.84.202.30:80'},
                   {'http': 'http://182.18.20.192:8088'},
                   {'http': 'http://101.4.136.34:8080'},
                   {'http': 'http://183.248.15.219:80'},
                   {'http': 'http://60.29.226.177:80'},
                   {'http': 'http://121.196.226.246:84'},
                   {'http': 'http://120.77.182.203:8888'},
                   {'http': 'http://125.77.25.123:80'},
                   {'http': 'http://183.153.29.214:808'},
                   {'http': 'http://120.77.174.216:8888'},
                   {'http': 'http://42.59.142.232:80'},
                   {'http': 'http://1.60.61.59:80'},
                   {'http': 'http://166.111.77.32:3128'},
                   {'http': 'http://115.202.180.42:808'},
                   {'http': 'http://120.77.152.51:8888'},
                   {'http': 'http://218.86.200.6:8118'},
                   {'http': 'http://61.139.79.93:8080'},
                   {'http': 'http://60.19.52.152:80'},
                   {'http': 'http://101.200.44.5:8888'},
                   {'http': 'http://111.13.2.138:80'},
                   {'http': 'http://113.123.18.29:808'},
                   {'http': 'http://42.51.26.79:3128'},
                   {'http': 'http://59.38.241.35:808'},
                   {'http': 'http://120.199.224.78:80'},
                   {'http': 'http://119.7.75.28:808'},
                   {'http': 'http://101.53.101.172:9999'},
                   {'http': 'http://119.7.84.98:808'},
                   {'http': 'http://120.77.156.103:8888'},
                   {'http': 'http://114.238.62.25:808'},
                   {'http': 'http://119.7.81.213:808'},
                   {'http': 'http://113.107.112.210:8101'},
                   {'http': 'http://58.16.42.140:80'},
                   {'http': 'http://119.254.84.90:80'},
                   {'http': 'http://1.80.50.199:80'},
                   {'http': 'http://110.72.32.19:8123'},
                   {'http': 'http://122.192.66.50:808'},
                   {'http': 'http://171.39.78.13:8123'},
                   {'http': 'http://101.201.151.16:8088'},
                   {'http': 'http://120.77.171.88:8888'},
                   {'http': 'http://120.77.182.203:8888'},
                   {'http': 'http://111.13.7.119:80'},
                   {'http': 'http://61.130.97.212:8099'},
                   {'http': 'http://139.224.58.46:8088'},
                   {'http': 'http://120.77.85.115:8888'},
                   {'http': 'http://183.133.51.71:80'},
                   {'http': 'http://120.199.64.163:8081'},
                   {'http': 'http://119.36.92.47:843'},
                   {'http': 'http://120.77.182.72:8888'},
                   {'http': 'http://124.206.133.219:3128'},
                   {'http': 'http://120.77.153.69:8888'},
                   {'http': 'http://120.77.145.164:8888'},
                   {'http': 'http://27.184.131.220:8888'},
                   {'http': 'http://114.215.150.13:3128'},
                   {'http': 'http://183.56.177.130:808'},
                   {'http': 'http://125.77.25.116:80'},
                   {'http': 'http://61.143.228.162:3128'},
                   {'http': 'http://180.97.235.30:80'},
                   {'http': 'http://222.204.6.235:8080'},
                   {'http': 'http://115.159.155.42:1080'},
                   {'http': 'http://61.53.65.54:3128'},
                   {'http': 'http://182.18.20.192:8088'},
                   {'http': 'http://222.92.244.40:80'},
                   {'http': 'http://120.77.154.125:8888'},
                   {'http': 'http://113.85.68.97:8081'},
                   {'http': 'http://182.92.64.238:80'},
                   {'http': 'http://60.17.201.89:80'},
                   {'http': 'http://120.77.147.160:8888'},
                   {'http': 'http://183.222.102.106:8080'},
                   {'http': 'http://120.77.146.158:8888'},
                   {'http': 'http://120.77.255.133:8088'},
                   {'http': 'http://120.77.156.16:8888'},
                   {'http': 'http://120.77.145.5:8888'},
                   {'http': 'http://101.251.234.254:51238'},
                   {'http': 'http://120.77.153.4:8888'},
                   {'http': 'http://120.77.154.150:8888'},
                   {'http': 'http://121.42.176.133:3128'},
                   {'http': 'http://110.73.3.152:8123'},
                   {'http': 'http://112.195.140.203:808'},
                   {'http': 'http://101.205.81.38:808'},
                   {'http': 'http://111.13.7.123:80'},
                   {'http': 'http://125.77.25.120:80'},
                   {'http': 'http://121.30.197.38:8080'},
                   {'http': 'http://110.73.35.146:8123'},
                   {'http': 'http://112.192.30.159:8118'},
                   {'http': 'http://222.175.44.23:8081'},
                   {'http': 'http://123.56.67.222:80'},
                   {'http': 'http://111.13.109.27:80'},
                   {'http': 'http://116.62.11.138:3128'},
                   {'http': 'http://120.77.180.24:8888'},
                   {'http': 'http://111.13.2.138:80'},
                   {'http': 'http://61.139.79.93:8080'},
                   {'http': 'http://183.153.29.214:808'},
                   {'http': 'http://221.181.6.35:808'},
                   {'http': 'http://112.194.8.128:80'},
                   {'http': 'http://218.73.105.244:808'},
                   {'http': 'http://1.60.61.59:80'},
                   {'http': 'http://120.77.183.34:8888'},
                   {'http': 'http://120.77.152.51:8888'},
                   {'http': 'http://60.19.52.152:80'},
                   {'http': 'http://111.1.3.38:8000'},
                   {'http': 'http://113.107.112.210:8101'},
                   {'http': 'http://120.77.155.249:8888'},
                   {'http': 'http://101.201.151.16:8088'},
                   {'http': 'http://58.16.42.140:80'},
                   {'http': 'http://120.77.171.88:8888'},
                   {'http': 'http://166.111.77.32:3128'},
                   {'http': 'http://42.202.130.246:3128'},
                   {'http': 'http://120.77.176.179:8888'},
                   {'http': 'http://120.77.85.115:8888'},
                   {'http': 'http://124.206.133.219:3128'},
                   {'http': 'http://120.77.182.72:8888'},
                   {'http': 'http://110.73.4.101:8123'},
                   {'http': 'http://42.51.26.79:3128'},
                   {'http': 'http://125.77.25.116:80'},
                   {'http': 'http://222.204.6.235:8080'},
                   {'http': 'http://115.46.67.42:8123'},
                   {'http': 'http://101.4.136.34:8080'},
                   {'http': 'http://120.77.182.203:8888'},
                   {'http': 'http://61.53.65.54:3128'},
                   {'http': 'http://182.18.20.192:8088'},
                   {'http': 'http://59.38.241.35:808'},
                   {'http': 'http://120.199.224.78:80'},
                   {'http': 'http://171.13.36.69:808'},
                   {'http': 'http://219.139.240.145:8090'},
                   {'http': 'http://120.77.148.161:8888'},
                   {'http': 'http://125.77.25.123:80'},
                   {'http': 'http://60.23.44.71:8118'},
                   {'http': 'http://101.53.101.172:9999'},
                   {'http': 'http://120.199.64.163:8081'},
                   {'http': 'http://183.248.15.219:80'},
                   {'http': 'http://171.39.78.13:8123'},
                   {'http': 'http://113.73.152.38:808'},
                   {'http': 'http://183.222.102.106:8080'},
                   {'http': 'http://61.136.163.245:3128'},
                   {'http': 'http://60.178.0.124:8081'},
                   {'http': 'http://101.251.234.254:51238'},
                   {'http': 'http://116.3.151.170:80'},
                   {'http': 'http://120.77.154.150:8888'},
                   {'http': 'http://115.159.155.42:1080'},
                   {'http': 'http://119.23.129.24:3128'},
                   {'http': 'http://39.174.149.53:80'},
                   {'http': 'http://106.15.177.202:80'},
                   {'http': 'http://120.77.146.158:8888'},
                   {'http': 'http://112.74.62.158:8888'},
                   {'http': 'http://113.85.68.97:8081'},
                   {'http': 'http://111.13.7.119:80'},
                   {'http': 'http://61.130.97.212:8099'},
                   {'http': 'http://120.77.150.239:8888'},
                   {'http': 'http://111.13.7.123:80'},
                   {'http': 'http://125.77.25.120:80'},
                   {'http': 'http://120.77.200.161:8888'},
                   {'http': 'http://120.77.154.127:8888'},
                   {'http': 'http://121.31.86.236:8123'},
                   {'http': 'http://123.56.67.222:80'},
                   {'http': 'http://120.77.147.160:8888'},
                   {'http': 'http://103.37.150.35:8080'},
                   {'http': 'http://222.175.44.23:8081'},
                   {'http': 'http://183.56.177.130:808'},
                   {'http': 'http://116.62.11.138:3128'},
                   {'http': 'http://182.92.64.238:80'},
                   {'http': 'http://111.202.92.115:8080'},
                   {'http': 'http://180.97.235.30:80'},
                   {'http': 'http://120.77.152.53:8888'},
                   {'http': 'http://120.77.145.5:8888'},
                   {'http': 'http://120.77.255.133:8088'},
                   {'http': 'http://120.77.156.16:8888'},
                   {'http': 'http://112.74.50.191:8888'},
                   {'http': 'http://120.77.153.4:8888'},
                   {'http': 'http://101.37.35.17:3128'},
                   {'http': 'http://123.207.30.187:3128'},
                   {'http': 'http://120.77.200.152:8888'},
                   {'http': 'http://121.30.197.38:8080'},
                   {'http': 'http://111.1.3.38:8000'},
                   {'http': 'http://119.254.102.90:8080'},
                   {'http': 'http://110.73.49.158:8123'},
                   {'http': 'http://119.179.193.69:8889'},
                   {'http': 'http://180.110.46.89:8888'},
                   {'http': 'http://121.31.100.34:8123'},
                   {'http': 'http://111.13.109.27:80'},
                   {'http': 'http://110.73.3.232:8123'},
                   {'http': 'http://111.13.7.122:80'},
                   {'http': 'http://120.77.153.201:8888'},
                   {'http': 'http://120.77.155.249:8888'},
                   {'http': 'http://120.77.146.98:8888'},
                   {'http': 'http://166.111.77.32:3128'},
                   {'http': 'http://112.194.8.128:80'},
                   {'http': 'http://60.178.10.35:8081'},
                   {'http': 'http://118.190.14.150:3128'},
                   {'http': 'http://111.13.7.117:80'},
                   {'http': 'http://139.129.94.241:3128'},
                   {'http': 'http://211.143.155.173:80'},
                   {'http': 'http://123.59.101.100:80'},
                   {'http': 'http://61.152.81.193:9100'},
                   {'http': 'http://27.44.160.139:80'},
                   {'http': 'http://211.143.155.172:80'},
                   {'http': 'http://120.77.146.200:8888'},
                   {'http': 'http://101.37.79.125:3128'},
                   {'http': 'http://183.52.12.184:808'},
                   {'http': 'http://118.190.14.150:3128'},
                   {'http': 'http://120.77.146.98:8888'},
                   {'http': 'http://183.222.102.102:8080'},
                   {'http': 'http://110.73.4.101:8123'},
                   {'http': 'http://183.222.102.97:8080'},
                   {'http': 'http://120.83.13.53:8080'},
                   {'http': 'http://119.36.92.42:80'},
                   {'http': 'http://211.143.155.167:80'},
                   {'http': 'http://120.194.18.90:81'},
                   {'http': 'http://125.77.25.124:80'},
                   {'http': 'http://183.222.102.104:8080'},
                   {'http': 'http://120.77.182.21:8888'},
                   {'http': 'http://222.208.83.26:9000'},
                   {'http': 'http://183.248.15.219:80'},
                   {'http': 'http://112.74.50.191:8888'},
                   {'http': 'http://60.29.226.177:80'},
                   {'http': 'http://61.136.163.245:3128'},
                   {'http': 'http://139.224.58.46:8088'},
                   {'http': 'http://42.202.130.246:3128'},
                   {'http': 'http://183.133.51.71:80'},
                   {'http': 'http://120.77.87.231:8888'},
                   {'http': 'http://182.90.121.63:8123'},
                   {'http': 'http://119.23.129.24:3128'},
                   {'http': 'http://106.15.177.202:80'},
                   {'http': 'http://112.74.62.158:8888'},
                   {'http': 'http://120.77.150.239:8888'},
                   {'http': 'http://120.77.156.103:8888'},
                   {'http': 'http://42.84.202.30:80'},
                   {'http': 'http://120.77.146.172:8888'},
                   {'http': 'http://114.215.150.13:3128'},
                   {'http': 'http://120.77.154.127:8888'},
                   {'http': 'http://110.73.7.93:8123'},
                   {'http': 'http://120.77.153.69:8888'},
                   {'http': 'http://106.44.80.252:8118'},
                   {'http': 'http://144.0.53.224:8118'},
                   {'http': 'http://182.92.183.168:3128'}
                   ]

    proxy_list3 = [{'http': 'http://114.95.243.147:8000'},
                   {'http': 'http://42.233.94.247:81'},
                   {'http': 'http://60.191.47.56:81'},
                   {'http': 'http://120.77.182.203:8888'},
                   {'http': 'http://125.77.25.116:80'},
                   {'http': 'http://120.77.145.164:8888'},
                   {'http': 'http://120.77.153.53:8888'},
                   {'http': 'http://123.206.107.106:8080'},
                   {'http': 'http://120.77.86.173:8888'},
                   {'http': 'http://111.13.2.131:80'},
                   {'http': 'http://124.95.44.99:8888'},
                   {'http': '49.73.180.93:81'},
                   {'http': '180.111.184.127:81'},
                   {'http': '120.77.146.158:8888'},
                   {'http': '112.74.36.89:8888'},
                   {'http': '120.77.146.200:8888'},
                   {'http': '139.224.20.210:8080'},
                   {'http': '180.96.27.12:88'},
                   {'http': '120.77.255.133:8088'},
                   {'http': '175.17.1.7:8888'},
                   {'http': '125.77.25.116:80'},
                   {'http': '120.77.200.152:8888'},
                   {'http': '120.25.231.153:80'},
                   {'http': '120.77.176.179:8888'},
                   {'http': '114.95.243.147:8000'},
                   {'http': '125.77.25.124:80'},
                   {'http': '120.77.182.203:8888'},
                   {'http': '120.77.154.125:8888'},
                   {'http': '123.206.107.106:8080'},
                   {'http': '120.77.144.75:8888'},
                   {'http': '120.77.200.161:8888'},
                   {'http': '121.58.8.138:8888'},
                   {'http': '111.202.120.52:8088'},
                   {'http': '125.104.239.166:81'},

                   ]

    global proxies
    url = 'http://www.dancheditu.com:3000/bikes?lat=' \
          + str(lat) + '&lng=' + str(lng) + '&cityid=218&token=demo'
    prcname_in_get = multiprocessing.current_process().name
    try:
        print(prcname_in_get, ':try中的当前IP:', proxies)
        r = requests.get(url, timeout=10, proxies=proxies)
        # r = requests.get(url, timeout=10)
        r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
        result = r.json()
    except:
        print(prcname_in_get, ':请求异常或连接超时或json异常！')

# --------------------------proxy_list在此--------------------------------- #
        for newp in range(2 * len(proxy_list2)):
            proxies = random.choice(proxy_list3)
            try:
                print(prcname_in_get, ':尝试新IP,第', newp, '次')
                r = requests.get(url, timeout=5, proxies=proxies)
                r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
                result = r.json()
            # except (requests.exceptions.ConnectTimeout, requests.RequestException) as e:
            except:
                print(prcname_in_get, ':新IP不可用或连接超时或json异常！')
                isctn = False
                continue
            else:
                print('进程', prcname_in_get, ':新IP可用，已更换')
                isctn = True
                break
    else:
        isctn = True

    if isctn:
        return result["msg"]
    else:
        print(prcname_in_get, ':无可用IP。')
        return

'''
def mobikedata_get(lat, lng):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.5.7 NetType/WIFI Language/zh_CN',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://servicewechat.com/wx80f809371ae33eda/23/page-frame.html',
    }
    url = 'https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
    data = {
        'longitude': str(lng),  # 经度
        'latitude': str(lat),  # 纬度
        'citycode': '218',
        'errMsg': 'getMapCenterLocation:ok'

    }
    # 下面必须加上verify=False,表示不验证ssl，要不然一直报错。。。
    z = requests.post(url, data=data, headers=headers, verify=False)

    print(z.json()['object'])
'''

'''
def data_write(result):
    t = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    if len(result) > 0:
        # print('result：', result)
        print('result：~~')
        print('正在写入...')

        r_xls = xlrd.open_workbook('multiprc_test1.xls')
        r_sheet = r_xls.sheet_by_index(0)  # r_sheet 只读
        rows = r_sheet.nrows
        w_xls = copy(r_xls)
        w_sheet = w_xls.get_sheet(0)  # w_sheet可以写入

        for i in range(0, len(result)):
            if len(result[i]) == 4:
                w_sheet.write(rows + i, 0, result[i]['id'])
                w_sheet.write(rows + i, 1, result[i]['brand'])
                w_sheet.write(rows + i, 2, result[i]['lat'])
                w_sheet.write(rows + i, 3, result[i]['lng'])
                w_sheet.write(rows + i, 4, t)
            else:
                continue
        print('---写入完成。')
        w_xls.save('multiprc_test1.xls ')
        print('---保存成功。')
    else:
        print('当前区域共享单车数量为0。进入下一区域...')
        return
'''

def data_write2txt(result):
    t = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    prcname_in_write = multiprocessing.current_process().name
    if len(result) > 0:
        print(prcname_in_write, ':len of result:',len(result))
        print(prcname_in_write, ':正在写入...')
        with open('datatest1.txt', 'a') as f:
            for i in range(0, len(result)):
                if len(result[i]) == 4:
                    if result[i]['lng'] is None or result[i]['lat'] is None: #过滤经纬度为NONETYPE的数据
                        continue
                    else:                        
                        if 114<result[i]['lng']<115 and 30<result[i]['lat']<31:

                            """---------坐标转换：---------"""
                            trans_result = bd2WGS.bd09_to_wgs84(result[i]['lng'], result[i]['lat'])

                            f.write(str(trans_result[0]) + ',' +
                                    str(trans_result[1]) + ',' +
                                    str(result[i]['id']) + ',' +
                                    str(result[i]['brand']) + ',' +
                                    t + '\n')
                        else:
                            continue
                    
                else:
                    continue
        print(prcname_in_write, ':写入完成。')
    else:
        print(prcname_in_write, ':当前区域共享单车数量为0。进入下一区域...')
        return


def crawl(coor_range):
    regionnum = 0
    datasum = 0
    global proxies
    proxies = {'http': 'http://114.95.243.147:8000'}
    prcname = multiprocessing.current_process().name
    for lat in np.arange(coor_range[0], coor_range[1], 0.004000):
        for lng in np.arange(coor_range[2], coor_range[3], 0.004000):
            regionnum += 1

            print('—--进程', prcname, '第', regionnum, '个区域：')
            data = data_get(lat, lng, proxies)
            datasum += len(data)
            data_write2txt(data)
    print(prcname, ':ALL FINISH')
    print(prcname, ':共爬取区域：', regionnum, '个')
    print(prcname, ':共爬取数据：', datasum, '个')


if __name__ == '__main__':

    #武昌区
    # 114.275874, 30.628952 西北点
    # 114.356901, 30.563269 中心点
    # 114.437928, 30.497586 东南点
    with open('datatest1.txt','w') as myf:
        myf.write('lng,lat,id,brand,time\n')

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # prc(30.462961, 30.702852, 114.164457, 114.470501)
    mycoor_range1 = [30.564269, 30.628952, 114.275874, 114.356901]  # 西北 （第一个+0.001
    mycoor_range2 = [30.564269, 30.628952, 114.357901, 114.437928]  # 东北 （第一个+0.001 第三个+0.001
    mycoor_range3 = [30.497586, 30.563269, 114.275874, 114.356901]  # 西南
    mycoor_range4 = [30.497586, 30.563269, 114.357901, 114.437928]  # 东南 （第三个+0.001
    mycoor_ranges = [mycoor_range1, mycoor_range2, mycoor_range3, mycoor_range4]
    starttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    pool.map(crawl, mycoor_ranges)
    pool.close()
    pool.join()

    endtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('we started from:', starttime)
    print('and ended at:', endtime)
