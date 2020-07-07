import page_util
import os

def get_indices(file, opentag, closetag):
    path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(path, 'html-examples/')
    with open(file.name, 'rt') as rubric:
        html = rubric.read()
        first_index = html.find(opentag)
        last_index = html.rfind(closetag)
        indices = [first_index, last_index]
    return indices

def extract_text(file, first_index, last_index):
    path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(path, 'html-examples/')

    with open(file.name, 'rt') as rubric:
        html = rubric.read()
        rubric_data = html[first_index:last_index]
    return rubric_data

def write_file(file, opentag, closetag):
    text = extract_text(file, *get_indices(file, opentag, closetag))
    
    with open(file.name[:-5]+'-rubric-data.html', 'x') as rubric_data:
        rubric_data.write(text)


    
