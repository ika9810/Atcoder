# importing required libraries
import requests
from operator import itemgetter
import csv

# specifying the URL to retrieve the data from
url = 'https://kenkoooo.com/atcoder/resources/problem-models.json'

# creating a session object to handle the HTTP requests
session_obj = requests.Session()

# sending a GET request to the specified URL with the headers to mimic a web browser
response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})

# getting the JSON data from the response
data = requests.get(url).json()

# defining a function to calculate the Kyu rank of a problem based on its difficulty level
def kyu(difficulty):
    # checking the difficulty range of the problem and returning the Kyu rank and its color
    if difficulty <= 399:
        return {"Kyu" : "9 Kyu", "Color" : "lightgrey"}
    elif difficulty >= 400 and difficulty <= 799:
        if difficulty <= 599:
            return {"Kyu" : "8 Kyu", "Color" : "critical"}
        else:
            return {"Kyu" : "7 Kyu", "Color" : "critical"}
    elif difficulty >= 800 and difficulty <= 1199:
        if difficulty <= 999:
            return {"Kyu" : "6 Kyu", "Color" : "brightgreen"}
        else:
            return {"Kyu" : "5 Kyu", "Color" : "brightgreen"}
    elif difficulty >= 1200 and difficulty <= 1599:
        if difficulty <= 1399:
            return {"Kyu" : "4 Kyu", "Color" : "green"}
        else:
            return {"Kyu" : "3 Kyu", "Color" : "green"}
    elif difficulty >= 1600 and difficulty <= 1999:
        if difficulty <= 1799:
            return {"Kyu" : "2 Kyu", "Color" : "blue"}
        else:
            return {"Kyu" : "1 Kyu", "Color" : "blue"}
    elif difficulty >= 2000 and difficulty <= 2399:
        if difficulty <= 2199:
            return {"Kyu" : "1 Dan", "Color" : "yellow"}
        else:
            return {"Kyu" : "2 Dan", "Color" : "yellow"}
    elif difficulty >= 2400 and difficulty <= 2799:
        if difficulty <= 2599:
            return {"Kyu" : "3 Dan", "Color" : "orange"}
        else:
            return {"Kyu" : "4 Dan", "Color" : "orange"}
    elif difficulty >= 2800:
        return {"Kyu" : "5 Dan or higher", "Color" : "red"}
    else:
        return {"Kyu" : "Unknown", "Color" : "black"}

# Extracting the list of problem ID
keys = [key for key in data]

# initialising a list to store the problem data after cleaning
res = []

# iterating over the problem IDs to extract the relevant information
for key in keys:
    try:
        con = ['abc','arc','agc']
        # checking if the problem ID is from a valid contest
        if key[:3] in con:
            pass
        else:
            continue
        # storing the problem data in the res list
        res.append({'Problem': key, 'Difficulty': data[key]["difficulty"], 'Link' : "https://atcoder.jp/contests/" + key.split("_")[0] + "/tasks/" + key, 'Contest' : "https://atcoder.jp/contests/" + key.split("_")[0]})
    except:
        pass
        #print("here",data[key])
data = sorted(res, key=itemgetter('Difficulty'))
f = open('Problem_List.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(["Number",'Problem', 'Difficulty', "Kyu", "Color", "Link", "Contest"])
for i in range(len(data)):
    key = data[i]['Problem'].upper()
    value = data[i]["Difficulty"]
    link = data[i]['Link']
    contest = data[i]["Contest"]
    Kyu = kyu(value)["Kyu"]
    Color = kyu(value)["Color"]

    wr.writerow([i+1,key,value,Kyu,Color,link,contest])
f.close()

num = input("Problem Number : ")
problem = input("Problem Name : ")
link = input("Problem Link : ")
sub = input("Submission  Link : ")


contest = link.split("https://atcoder.jp/contests/")[1].split("/tasks/")[0]
contest_name = ""
if contest[:3] in ["abc","arc","agc"]:
    if contest[:3] == "abc":
        contest_name = "Atcoder Beginner Contest " + str(contest[3:])
    elif contest[:3] == "arc":
        contest_name = "Atcoder Regular Contest " + str(contest[3:])
    elif contest[:3] == "agc":
        contest_name = "Atcoder Grand Contest " + str(contest[3:])
f = open('Problem_List.csv','r')
rdr = csv.reader(f)
diffi = ""
for line in rdr:
    if line[5] == link:
        diffi = line[2]
        break
msg = "|"+ num + "|[" + problem + "](" + link + ")| [Python3](https://github.com/ika9810/Atcoder/blob/main/Boot%20camp%20for%20Beginners/Easy%20100/" + problem.replace(" ","%20") + ".py)|[AC](" + sub + ")|" + diffi + "|[" + contest_name + "](" + link.split("/tasks/")[0]+")|\n"
#|22|[A. Candy Distribution Again](https://atcoder.jp/contests/agc027/tasks/agc027_a)| [Python3](https://github.com/ika9810/Atcoder/blob/main/Boot%20camp%20for%20Beginners/Easy%20100/A.%20Candy%20Distribution%20Again.py)|[AC](https://atcoder.jp/contests/agc027/submissions/39148303)|114|[AtCoder Grand Contest 027](https://atcoder.jp/contests/agc027)|
saveline =[msg]
f = open('README.md')
lines = f.readlines()
f.close()

with open('./README.md', 'a') as f:
    f.writelines(saveline)
    f.close()

#Atcoder Problem List
# I used This Link "https://kenkoooo.com/atcoder/resources/problem-models.json"
# I referred to "https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md"