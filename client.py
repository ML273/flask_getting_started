from flask import Flask, jsonify, request
import requests
# import requests
r = requests.get("http://vcm-3502.vm.duke.edu:5000/")
print(r)
