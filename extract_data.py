"""Read data from rubric/submissions html."""
import re
import sys

import page_util as page
import rubric_dict as keys

sys.path.insert(1, 'logging-test')




creds = page.get_login()

page_title_regex = '(?<=<title>).*(?=<\/title>)'

keylist=keys.KEYS()

dict = {}


def regex_gen(index):
    keys = []
    i=0
    if index==0:
        for key in keylist[index]:
            regex = '(?<=class=\"'+keylist[index][key]+'\">)(.*?)(?=<)'
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
    #print('GETTING RUBRIC...')
    #print(url)
    #page.prt_scr('error')

    if raw != None:
        #print("\nRAW:\n"+raw)
        #print(regex_keys[0][1])

        try:
            #page.get_src('title-blank')
            #page.prt_scr('title-blank')
            title = re.findall(page_title_regex, raw)
            criteria = re.findall(regex_keys[1][1], raw)
            descriptions = re.findall(regex_keys[2][1], raw)
            level_titles = re.findall(regex_keys[3][1], raw)
            point_values = re.findall(regex_keys[4][1], raw)

            criteria = list(dict.fromkeys(criteria))

            rubric = {}
            #print(title)
            rubric['title'] = title[0]
            rubric['criteria'] = []
            for i in range(0, len(criteria)):
                rubric['criteria'].append({'criterion'+str(i): criteria[i], 'content': []})
                for j in range(((i+1)*3)-3, (i+1)*3):
                    rubric['criteria'][i]['content'].append({'description': descriptions[j], 'level title': level_titles[j], 'point value': point_values[j]})
        except:
            print('Rubric not found.')
    else:
        return None


    #GCLOGGER.info(rubric)
    return rubric

def submission(regex_keys, url, cw_id, ref, uid, c_id):
    #print('URL: '+url+'\n')
    #print('GETTING GRADE... URL is: '+url+'\n')
    print('\nREGEX KEYS:\n'+str(regex_keys))
    try:
        title = ref['courseWork'][cw_id]
    except:
        title = "Unknown CourseworkId "
    try:
        user = ref['roster']['students'][uid]
    except:
        user = "Unkown UID"
    try:
        course = ref['courses'][c_id]
    except:
        course = "Unknown CourseId"
    #print(title)

    #page_title = re.findall(page_title_regex, raw)
    #print(page_title)


    if 'Project' in title:
        raw = page.get_page(*creds, url)
        criterion_grade = re.findall(regex_keys[1][1], raw)
        criterion_title = re.findall('(?<=class=\"K0lUWd\">)(.*?)(?=<)', raw)
        #print(criterion_grade)
        #print('\n')
        #print('...')
    else:
        return "Non-Project"


    #GCLOGGER.info(rubric)
    #print("user: " + str(user) +'\n'+"grades: "+ str(criterion_grade))
    return {'course' : course, 'courseWork' : title, 'user' : user,  'grades' : criterion_grade, 'titles': criterion_title}
