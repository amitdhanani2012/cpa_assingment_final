#!/usr/bin/python

import memcache
from flask import Flask
import time
import os
total_mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') 


rate1=memcache.Client([('127.0.0.1',11211)])

def rates123(rate1):
	h=rate1.get_stats()
#print(h)


########## string perpartion

	str10="<table border=1>"  
	str11="<tr><td>Auth CMDS</td><td>"+str(h[0][1]['auth_cmds'])+"</td></tr>"
	str12="<tr><td>Reclaimed</td><td>"+str(h[0][1]['reclaimed'])+"</td></tr>"
	str13="<tr><td>Curr_items</td><td>"+str(h[0][1]['curr_items'])+"</td></tr>"
	str14="<tr><td>PID</td><td>"+str(h[0][1]['pid'])+"</td></tr>"
	str15="<tr><td>Expired Unfetched</td><td>"+str(h[0][1]['expired_unfetched'])+"</td></tr>"
	str16="<tr><td>Has is Expanding</td><td>"+str(h[0][1]['hash_is_expanding'])+"</td></tr>"
	str17="<tr><td>Cas Hits</td><td>"+str(h[0][1]['cas_hits'])+"</td></tr>"
	str18="<tr><td>Uptime</td><td>"+str(h[0][1]['uptime'])+"</td></tr>"
	str19="<tr><td>Touch Hits</td><td>"+str(h[0][1]['touch_hits'])+"</td></tr>"
	str110="<tr><td>Delete Misses</td><td>"+str(h[0][1]['delete_misses'])+"</td></tr>"
	str111="<tr><td>Listen Disabled Num</td><td>"+str(h[0][1]['listen_disabled_num'])+"</td></tr>"
	str112="<tr><td>Cas Misses</td><td>"+str(h[0][1]['cas_misses'])+"</td></tr>"
	str113="<tr><td>Decr Hits</td><td>"+str(h[0][1]['decr_hits'])+"</td></tr>"
	str114="<tr><td>cmd_touch</td><td>"+str(h[0][1]['cmd_touch'])+"</td></tr>"
	str115="<tr><td>incr_hits</td><td>"+str(h[0][1]['incr_hits'])+"</td></tr>"
	str116="<tr><td>version</td><td>"+str(h[0][1]['version'])+"</td></tr>"
	str117="<tr><td>limit_maxbytes</td><td>"+str(h[0][1]['limit_maxbytes'])+"</td></tr>"
	str118="<tr><td>bytes_written</td><td>"+str(h[0][1]['bytes_written'])+"</td></tr>"
	str119="<tr><td>incr_misses</td><td>"+str(h[0][1]['incr_misses'])+"</td></tr>"
	str120="<tr><td>accepting_conns</td><td>"+str(h[0][1]['accepting_conns'])+"</td></tr>"
	str121="<tr><td>rusage_system</td><td>"+str(h[0][1]['rusage_system'])+"</td></tr>"
	str122="<tr><td>total_items</td><td>"+str(h[0][1]['total_items'])+"</td></tr>"
	str123="<tr><td>cmd_get</td><td>"+str(h[0][1]['cmd_get'])+"</td></tr>"
	str124="<tr><td>curr_connections</td><td>"+str(h[0][1]['curr_connections'])+"</td></tr>"
	str125="<tr><td>touch_misses</td><td>"+str(h[0][1]['touch_misses'])+"</td></tr>"
	str126="<tr><td>threads</td><td>"+str(h[0][1]['threads'])+"</td></tr>"
	str127="<tr><td>total_connections</td><td>"+str(h[0][1]['total_connections'])+"</td></tr>"
	str128="<tr><td>cmd_set</td><td>"+str(h[0][1]['cmd_set'])+"</td></tr>"
	str129="<tr><td>libevent</td><td>"+str(h[0][1]['libevent'])+"</td></tr>"
	str130="<tr><td>conn_yields</td><td>"+str(h[0][1]['conn_yields'])+"</td></tr>"
	str131="<tr><td>get_misses</td><td>"+str(h[0][1]['get_misses'])+"</td></tr>"
	str132="<tr><td>reserved_fds</td><td>"+str(h[0][1]['reserved_fds'])+"</td></tr>"
	str133="<tr><td>bytes_read</td><td>"+str(h[0][1]['bytes_read'])+"</td></tr>"
	str134="<tr><td>hash_bytes</td><td>"+str(h[0][1]['hash_bytes'])+"</td></tr>"
	str135="<tr><td>evicted_unfetched</td><td>"+str(h[0][1]['evicted_unfetched'])+"</td></tr>"
	str136="<tr><td>cas_badval</td><td>"+str(h[0][1]['cas_badval'])+"</td></tr>"
	str137="<tr><td>cmd_flush</td><td>"+str(h[0][1]['cmd_flush'])+"</td></tr>"
	str138="<tr><td>evictions</td><td>"+str(h[0][1]['evictions'])+"</td></tr>"
	str139="<tr><td>bytes</td><td>"+str(h[0][1]['bytes'])+"</td></tr>"
	str140="<tr><td>connection_structures</td><td>"+str(h[0][1]['connection_structures'])+"</td></tr>"
	str142="<tr><td>hash_power_level</td><td>"+str(h[0][1]['hash_power_level'])+"</td></tr>"
	str143="<tr><td>auth_errors</td><td>"+str(h[0][1]['auth_errors'])+"</td></tr>"
	str144="<tr><td>rusage_user</td><td>"+str(h[0][1]['rusage_user'])+"</td></tr>"
	str145="<tr><td>time</td><td>"+str(h[0][1]['time'])+"</td></tr>"
	str146="<tr><td>delete_hits</td><td>"+str(h[0][1]['delete_hits'])+"</td></tr>"
	str147="<tr><td>pointer_size</td><td>"+str(h[0][1]['pointer_size'])+"</td></tr>"
	str148="<tr><td>decr_misses</td><td>"+str(h[0][1]['decr_misses'])+"</td></tr>"
	str149="<tr><td>get_hits</td><td>"+str(h[0][1]['get_hits'])+"</td></tr>"
#############



#	maxlimit=h[0][1]['limit_maxbytes']
	usedmem=float(h[0][1]['bytes_written'])+float(h[0][1]['bytes_read'])
	if float(usedmem)==float(0):
        	percent_usage=0
	else:
		percent_usage=float((float(usedmem)*100)/float(total_mem_bytes))

	str150="<tr><td>Percent Memcache Memory Usage compare to Total RAM</td><td>"+str(percent_usage)+"</td></tr>"
#print("percent used memory: %f" %(percent_usage))
	hits=h[0][1]['get_hits']
	miss=h[0][1]['get_misses']
	hm=float(hits)+float(miss)
	if float(hits)==float(0):
        	percent_hits=0
	else:
                if float(hm)!=0:
			percent_hits=(float(hits)*100)/float(hm)
	str151="<tr><td>Percent Get Hits</td><td>"+str(percent_hits)+"</td></tr>"
########miss######
	if float(miss)==float(0):
                percent_miss=0
        else:
                if float(hm)!=0:
                	percent_miss=(float(miss)*100)/float(hm)
        str151x="<tr><td>Percent Get Miss</td><td>"+str(percent_miss)+"</td></tr>"




#############


	str152="</table>"
#print("percent hits: %f" %(percent_hits))
	strcomp1=str10+str11+str12+str13+str14+str15+str16+str17+str18+str19+str110+str111+str112+str113+str114+str115+str116+str117+str118+str119+str120+str121+str122+str123+str124+str125+str126+str127+str128+str129+str130+str131+str132+str133+str134+str135+str136+str137+str138+str139+str140+str142+str143+str144+str145+str146+str147+str148+str149+str150+str151+str151x+str152
        return strcomp1

#print(strcomp1)

app=Flask(__name__)

@app.route('/app/')
def index():
#        while True:
#               time.sleep(600)
       strcomp1=rates123(rate1)
       return strcomp1

if __name__=='__main__':
   app.run(debug=False,host='0.0.0.0',port=443,ssl_context='adhoc')
