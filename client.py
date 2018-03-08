import requests
r = requests.get("http://vcm-3502.vm.duke.edu:5000/")
print(r.text)

getname = requests.get("http://vcm-3502.vm.duke.edu:5000/name")
print(getname.json())

hello_name = requests.get("http://vcm-3502.vm.duke.edu:5000/hello/Marianne")
print(hello_name.json())

distance = requests.post("http://vcm-3502.vm.duke.edu:5000/distance",json={"a": [0, 5], "b": [4, 0]})
print(distance.json())
