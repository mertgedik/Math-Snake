
def high_score_reader():
    with open("high_scores.csv","r") as file:
        rows = [i.strip("\n").split(",") for i in file.readlines()]
        return rows

def high_score_writer(current_name,current_score):
    rows = high_score_reader()
    new = True
    for index,(name,score) in enumerate(rows):
        if current_name == name:
            new = False
            if score < current_score:
                rows[index][1] = current_score
    if new:
        rows.append([current_name,current_score])
    rows = sorted(rows,key = lambda x:x[1],reverse=True)

    with open("high_scores.csv","w") as file:
        file.write("")
    with open("high_scores.csv","a") as file:
        for row in rows:
            file.writelines([",".join(row),"\n"])


