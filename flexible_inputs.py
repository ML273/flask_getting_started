import requests
def main_page():
    r = requests.get("http://vcm-3502.vm.duke.edu:5000/")
    print(r.text)

def see_Marianne_name():
    getname = requests.get("http://vcm-3502.vm.duke.edu:5000/name")
    print(getname.json())

def greet(name):
    hello_name = requests.get("http://vcm-3502.vm.duke.edu:5000/hello/{}".format(name))
    print(hello_name.json())

def pythagorean(pointa, pointb):
    inputs = {"a": pointa, "b": pointb}
    distance = requests.post("http://vcm-3502.vm.duke.edu:5000/distance", inputs)
    print(distance.json())
