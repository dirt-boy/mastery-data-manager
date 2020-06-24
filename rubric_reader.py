import page_util
import os

def load_file(url):
    name = page_util.make_name(url)
    return name+'.html'

def get_indices(file, opentag, closetag):
    path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(path, 'html-examples/')
    with open(filename+file, 'rt') as rubric:
        html = rubric.read()
        first_index = html.find(opentag)
        last_index = html.rfind(closetag)
        indices = [first_index, last_index]
    return indices

def extract_text(file, first_index, last_index):
    path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(path, 'html-examples/')

    with open(filename+file, 'rt') as rubric:
        html = rubric.read()
        rubric_data = html[first_index:last_index]
    return rubric_data

def write_file(url, opentag, closetag):
    file = load_file(url)
    text = extract_text(file, *get_indices(file, opentag, closetag))
    
    with open(file[:-5]+'-rubric-data.html', 'x') as rubric_data:
        rubric_data.write(text)

write_file('https://classroom.google.com/u/3/c/MTE0NTcxNDk1Mzgz/a/MTE0NTcxNDk1Mzkx/details', '<div class="ZoO8hd uXlBQc">', '<div role="presentation" class="jlfrG C4yF5e R5iLrf bJuVn ">')
    
