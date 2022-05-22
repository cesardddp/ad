import logging
from flask import Flask, jsonify,request,render_template
from flask_cors import CORS,cross_origin
from flask_pymongo import PyMongo,ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/portifolio"
logging.getLogger('flask_cors').level = logging.DEBUG

mongo = PyMongo(app)
# mongo - conection
# mongo.db - db
# mongo.db.Collection - Collection
teste = mongo.db.teste
atividades = mongo.db.atividades
CORS(app)#,resources={r"/*": {"origins": "*"}})

@app.post("/salva")
def salva():
    print(
        request.get_data()
    )
    result = atividades.insert_one(
        {"html":request.data.decode()}
    )
    # import pdb;pdb.set_trace()
    return jsonify({"id":str(result.inserted_id)}),200

@app.get("/")
def index()->str:
    atvs = []
    for atv in atividades.find():
        # import pdb;pdb.set_trace()
        atvs.append(atv)

    return render_template("doc.html",atividades=atvs)

@app.get("/face")
def face()->str:
    # atvs = [a for a in atividades.find()]
    # import pdb;pdb.set_trace()

    return render_template("post2.html")

@app.patch("/update/<pk>")
def atualiza(pk):
    # atividades.delete_one({'_id':ObjectId(pk)})
    # import pdb;pdb.set_trace()
    return ""

@app.delete("/<pk>")
def delete(pk):
    result = atividades.delete_one({'_id':ObjectId(pk)})
    # import pdb;pdb.set_trace()
    return f"deletados: "+str(result.deleted_count)



# {"atividades":[
#     {
#         "id":1,
#         "html":"<p>oi</p>"
#     }
# ]
# }
# update(
#     "id":"6159d46fa41929e64660446c",

# )


