import page_util as page
import rubric_dict as keys
import re
import sys
sys.path.insert(1, 'logging-test')
import makelogger as logger

GCLOGGER = logger.get_logger(__name__)

creds = page.get_login()

keylist=keys.KEYS()

dict = {}

def regex_gen():
    keys = []
    i=0
    for key in keylist:
        regex = '(?<=class=\"'+keylist[key]+'\">)(.*?)(?=\<\/)'
        keys.append([key, regex])
        i += 1
    print(str(i)+': '+str(keys))
    return keys

def rubric(regex_keys, url):
    print('URL: '+url+'\n')

    raw = page.get_page(*creds, url)

    if raw != None:
        
        title = re.findall(regex_keys[0][1], raw)
        criteria = re.findall(regex_keys[1][1], raw)
        descriptions = re.findall(regex_keys[2][1], raw)
        level_titles = re.findall(regex_keys[3][1], raw)
        point_values = re.findall(regex_keys[4][1], raw)
    
        criteria = list(dict.fromkeys(criteria))
    
        rubric = {}
        rubric['title'] = title[0]
        print(rubric['title'])
        rubric['criteria'] = []
        for i in range(0, len(criteria)):
            rubric['criteria'].append({'criterion'+str(i): criteria[i], 'content': []})
            for j in range(((i+1)*3)-3, (i+1)*3):
                rubric['criteria'][i]['content'].append({'description': descriptions[j], 'level title': level_titles[j], 'point value': point_values[j]})


    else:
        return None
        
    
    #GCLOGGER.info(rubric)
    return rubric
    






