def parse(file):
    data = []

    with open(file, 'r') as f:
        all_lines = f.readlines()
    
    
    for i, l in enumerate(all_lines):
        #FOR TESTING
        #print("line_"+str(i)+":\n")
        #print(str(l)+"\n")
        data.append(l)
    return data
    #print(data[2])
    





parse("sample-gclassroom-output.json")
        


        


