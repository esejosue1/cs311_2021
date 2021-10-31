import argparse
import random
import json

filename="last_opponent_moves.json"
#add confess to data
def add_data_confess():
    item_data={}
    with open(filename, "r") as f:
        temp=json.load(f)
        data_length=len(temp)
    item_data["last_opponent_move"]="confess"
    temp.append(item_data)
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
       


#add silent to data

def add_data_silent():
    item_data={}
    with open(filename, "r") as f:
        temp=json.load(f)
        data_length=len(temp)
    item_data["last_opponent_move"]="silent"
    temp.append(item_data)
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
       

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args=parser.parse_args()

    #first game iteration/play nice
    if(args.last_opponent_move == "zero"):
        print("silent")

    #opponent stays silent
    if(args.last_opponent_move == "silent"):
        add_data_silent()
        with open(filename, "r") as f:
            temp1=json.load(f)
            data_length1=len(temp1)

        #once 3 straight silent from opp, confess
        if(data_length1>3):
            if(temp1[data_length1-1]["last_opponent_move"] == "silent" and temp1[data_length1-2]["last_opponent_move"] == "silent" and temp1[data_length2-3]["last_opponent_move"] == "silent"):
                print("confess")

        else:
            print("silent")
    #opponent confess, choose random
    elif(args.last_opponent_move == "confess"):
        add_data_confess()
        print(random.choice(['silent','confess'])
