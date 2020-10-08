import page_util as page
import rubric_dict as keys
import re
import sys
sys.path.insert(1, 'logging-test')
import makelogger as logger



GCLOGGER = logger.get_logger(__name__)

creds = page.get_login()

page_title_regex = '(?<=<title>).*(?=<\/title>)'

keylist=keys.KEYS()

dict = {}


def regex_gen(index):
    keys = []
    i=0
    if index==0:
        for key in keylist[index]:
            regex = '(?<=class=\"'+keylist[index][key]+'\">)(.*?)(?=\<\/)'
            keys.append([key, regex])
            i += 1
    else:
        for key in keylist[index]:
            regex = '(?<=class=\"'+keylist[index][key]+' \" tabindex="0" aria-label=")(.*?)(?=data-tooltip=)'
            keys.append([key, regex])
            i += 1
    return keys

def rubric(regex_keys, url):

    raw = page.get_page(*creds, url)
    print('GETTING RUBRIC...')
    print(url)
    #page.prt_scr('error')

    if raw != None:
        

        title = re.findall(regex_keys[0][1], raw)
        criteria = re.findall(regex_keys[1][1], raw)
        descriptions = re.findall(regex_keys[2][1], raw)
        level_titles = re.findall(regex_keys[3][1], raw)
        point_values = re.findall(regex_keys[4][1], raw)
    
        criteria = list(dict.fromkeys(criteria))
    
        rubric = {}
        print(title)
        rubric['title'] = title[0]
        rubric['criteria'] = []
        for i in range(0, len(criteria)):
            rubric['criteria'].append({'criterion'+str(i): criteria[i], 'content': []})
            for j in range(((i+1)*3)-3, (i+1)*3):
                rubric['criteria'][i]['content'].append({'description': descriptions[j], 'level title': level_titles[j], 'point value': point_values[j]})


    else:
        return None
        
    
    #GCLOGGER.info(rubric)
    return rubric

def submission(regex_keys, url, cw_id, ref):
    #print('URL: '+url+'\n')
    print('GETTING GRADE... URL is: '+url+'\n')

    print(ref)
    title = ref['courseWork']['cw_id']
    print(title)
    raw = page.get_page(*creds, url)
    #page_title = re.findall(page_title_regex, raw)
    print(page_title)


    if raw != None and 'Project' in page_title:
        
        criterion_grade = re.findall(regex_keys[1][1], raw)
        print(criterion_grade)
        print('\n')
        print('...')

    else:
        return None
        
    
    #GCLOGGER.info(rubric)
    return criterion_grade

    




