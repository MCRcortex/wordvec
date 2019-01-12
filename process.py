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
    f.write(requests.get("https://storage.googleapis.com/takeafile/AEnB2Ur8am-HA0q-qeXMeQbEgQqCFwlhzdMuicT74nxA9EaKZTxjioDmQ9Uw-P68tBDBWEjCYR5O1gf2DuEEv9LydPmNXK2U_QVyewpjNVPR_56qRK5g5BA.TM_7CrU1buayfDmN?GoogleAccessId=download@tyris-transfast.iam.gserviceaccount.com&Expires=1547252365&Signature=lVrI8KFlI52%2FbUaDu%2BJN55SIoLEeEn21ot3N2LwQ9ZY%2FkNLJkQMmTxIhHHcgapBj8Y8kXGJQ7WkXsRRcqW7vmZfldakh1h73QKEP8J8DhRlO68quvgFCT0AusejsXUXOxeAoGs%2FJrYhE%2FcTW6CYR0uEPLQB1TdGPBicExd2OSvVFFbNIhuAPmYboJESZW5ISIENB7syegQqhG2q0pBQsrk5kS%2Fti3%2FR4nZq5yGNsn1IvxTp7RR1ZrKtemcJT6gaGRu6y4YSd3SC9nZ0VlgVCrj%2BNYKiEboYRsFwT7LKl%2BIpy0cmVwEeS71O2QDAcwBHwc%2Bdr3IgKpE1oFAEIa3naRw%3D%3D&response-content-disposition=attachment;filename=%22data.npz%22", allow_redirects=True).content)
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
    out={}
    for i in sorted[1:15]:
        out[words[i]]=temp[i]
    return str(out)

if __name__ == '__main__':
    # Start the web server!
    app.run()


