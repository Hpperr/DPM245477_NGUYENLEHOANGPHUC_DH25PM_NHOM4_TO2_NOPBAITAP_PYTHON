"""
 Xử lý JSON File, Chuyển đổi Python Object qua String Json
"""
pythonObject = {
 "ten": "Trần Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}
import json
pythonObject = {
 "ten": "Trần Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}
jsonString = json.dumps(pythonObject)
# the result is a JSON string:
print(jsonString)