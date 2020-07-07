import page_util as page
import rubric_dict as keys
import re


creds = page.get_login()
raw = page.get_page(*creds)

keylist=keys.KEYS()

dict = {}

def regex_gen():
    keys = []
    for key in keylist:
        regex = '(?<=class=\"'+keylist[key]+'\">)(.*?)(?=\<\/)'
        keys.append([key, regex])
    return keys

def rubric(regex_keys):
    title = re.findall(regex_keys[0][1], raw)
    criteria = re.findall(regex_keys[1][1], raw)
    descriptions = re.findall(regex_keys[2][1], raw)
    level_titles = re.findall(regex_keys[3][1], raw)
    point_values = re.findall(regex_keys[4][1], raw)

    dict['title'] = title
    for i, c in enumerate(criteria):
        dict['criteria'+str(i)] = [{}]
        dict['criteria'+str(i)] = c
        print(dict)
    for i, d in enumerate(descriptions):
        dict['criteria'+str(i)]['description'] = d
        for j, lt in enumerate(level_titles):
            dict['criteria'+str(i)][i]['content']['levels'] = [{}]
            dict['criteria'+str(i)][i]['content']['levels'][j]['level title'] = lt
        for j, p in enumerate(point_values):
            dict['criteria'+str(i)][i]['content']['levels'][j]['point value'] = p

    print(dict)
    return dict

    

    

rubric(regex_gen())


