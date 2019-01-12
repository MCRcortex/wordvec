# Import flask
from flask import Flask,request,jsonify
import requests
import math
import numpy as np
from collections import OrderedDict

try:
    data=np.load("data.npz")
except:
    f=open("data.npz",'wb')
    f.write(requests.get("http://search.iclr2018.smerity.com/static/ncss-data.npz", allow_redirects=True).content)
    f.close()
    data=np.load("data.npz")
vectors=data["vectors"]
words=data["words"].tolist()
del data

app = Flask(__name__)


@app.route('/get_similar',methods=["GET","POST"])
def main():
    self_vector=vectors[words.index(request.values["word"])]
    temp=np.sum(((vectors-self_vector)**2),axis=1)
    sorted=np.argsort(temp)
    out=[]
    for i in sorted[1:15]:
        out.append((words[i],temp[i]))
    return jsonify(out)

if __name__ == '__main__':
    # Start the web server!
    app.run()


