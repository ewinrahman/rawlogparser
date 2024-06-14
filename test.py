import re


''' Raw log splitter information/template (Important fields only):
    end,2562,2024/06/05 19:27:40,165.154.129.130,123.51.190.204,165.154.129.130,10.1.31.77,BI-NAT-Internal System_Style.me Gitlab,,,ssl,vsys1,sdwan,vlan31,ethernet1/2,vlan.31,panorama,2024/06/05 19:27:40,1009045,1,34206,443,34206,443,0x400c1a,tcp,allow,4154,739,3415,11,2024/06/05 19:27:25,1,allurl,,7358049596824040546,0x8000000000000000,United Kingdom,Taiwan,,6,5,tcp-rst-from-client,11,0,0,0,,Xinyi-3220,from-policy,,,0,,0,,N/A,0,0,0,0,4b99d56e-8f04-4ef4-8567-03a392f02d9e,0,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2024-06-05T19:27:41.583+08:00,,,encrypted-tunnel,networking,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,ssl,no,no,0 
    - [1]  -> Event Timestamp (2024/06/05 19:27:48)
    - [3]  -> Event Type (TRAFFIC)
    - [4]  -> 
    - [7]  -> Source IP 
    - [8]  -> Destination IP
    - [9]  -> NAT Source IP 
    - [10] -> NAT Destination IP
    - [11] -> Rule Policy
    - [12] -> Application
    - [22] -> Source Port
    - [23] -> Destination Port
    - [24] -> NAT Source Port
    - [25] -> NAT Destination Port
ref: 
- Traffic: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/traffic-log-fields#idbe18d2d4-9eb8-4966-bec8-df3a6de70e66
- Threat: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/threat-log-fields#id83052cb2-4798-4f9c-abf8-e0b929ce7a3b
'''
t = '<190>Jun  5 19:27:48 Panorama.nogle.com 1,2024/06/05 19:27:48,016201041583,TRAFFIC,end,2562,2024/06/05 19:27:40,165.154.129.130,123.51.190.204,165.154.129.130,10.1.31.77,BI-NAT-Internal System_Style.me Gitlab,,,ssl,vsys1,sdwan,vlan31,ethernet1/2,vlan.31,panorama,2024/06/05 19:27:40,1009045,1,34206,443,34206,443,0x400c1a,tcp,allow,4154,739,3415,11,2024/06/05 19:27:25,1,allurl,,7358049596824040546,0x8000000000000000,United Kingdom,Taiwan,,6,5,tcp-rst-from-client,11,0,0,0,,Xinyi-3220,from-policy,,,0,,0,,N/A,0,0,0,0,4b99d56e-8f04-4ef4-8567-03a392f02d9e,0,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2024-06-05T19:27:41.583+08:00,,,encrypted-tunnel,networking,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,ssl,no,no,0 <190>Jun  5 19:26:05 Panorama.nogle.com 1,2024/06/05 19:26:04,016201041583,THREAT,vulnerability,2562,2024/06/05 19:26:01,165.154.129.130,123.51.190.195,165.154.129.130,10.1.10.108,BI-NAT-Internal System_BTSE-NOGLE Nginx aging.oa.btse.io,,,ssl,vsys1,sdwan,vlan10,ethernet1/2,vlan,panorama,2024/06/05 19:26:01,232941,1,60786,443,60786,443,0x402c00,tcp,alert,"123.51.190.195/",SSL TLS CBC Cipher Suite Detection(59323),allurl,informational,server-to-client,7358049594332318818,0x8000000000000000,United Kingdom,Taiwan,,,0,,,0,,,,,,,,0,11,0,0,0,,Xinyi-3220,,,,,0,,0,,N/A,info-leak,AppThreat-8855-8761,0x0,0,4294967295,,,d6652faf-d1e7-4b12-87c4-a72848aa3161,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0,2024-06-05T19:26:01.785+08:00,,,,encrypted-tunnel,networking,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,ssl,no,no,'

pattern = '\<190\>'
second_pattern = '\,'

ab = re.split(pattern, t)
try:
    dd = ab[1]
    ee = ab[2]
    ff = ab[3]
except:
    pass
cd = re.split(second_pattern, dd)
asd = list(filter(None, cd))

source_ip = 'Source IP: '+ asd[7]
source_ip_NAT = 'NAT Source IP: '+ asd[9]
destination_ip = 'Dst IP: '+asd[8]
destination_ip_NAT = 'NAT Dst IP: '+asd[10]

agawq = asd[4]
print(agawq)
# for bdd in afa:
#     print(bdd)


