import json

class boy:
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age

boy1 = boy('Will', 20)

#default method for decode
def boydefault(obj):
    if isinstance(obj, boy):
        return {'name': obj.name, 'age': obj.age}
    return obj;

def boyhook(dic):
    print('test')
    if dic['name']:
        return boy(dic['name'], dic['age'])
    return dic

boy_encode_str = json.dumps(boy1, default=boydefault)
new_boy = json.loads(boy_encode_str, object_hook=boyhook)
print(boy_encode_str)
print(new_boy)

class BoyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, boy):
            return {'name': o.name, 'age': o.age}
        return json.JSONEncoder.default(o);

#override decode method
class BoyDecoder(json.JSONDecoder):
    def decode(self, s):
        dic = super().decode(s);
        return boy(dic['name'], dic['age']);

#override __init__ method
class BoyDecoder2(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self)
        self.object_hook = boyhook

boy_encode_str = json.dumps(boy1, cls=BoyEncoder)
new_boy = json.loads(boy_encode_str, cls=BoyDecoder)
new_boy2 = json.loads(boy_encode_str, cls=BoyDecoder2)
print(boy_encode_str)
print(new_boy)
print(new_boy2)