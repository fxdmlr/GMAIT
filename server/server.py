from flask import Flask, request, jsonify
from flask_cors import CORS
import importlib.util

import sys
import os

# Add the GMait directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../GMait')))

import gamerunner as gr
import gamehandler as gh


app = Flask(__name__)
CORS(app)

def regMul(ls):
    md = int(ls[0])
    rounds = int(ls[1])
    a, b = ls[2],ls[3]
    ranges = [int(a), int(b)]

    float_mode = int(ls[4])
    a_fl = 0
    # if float_mode:
    #     a_fl = int(input("Digits after floating point : "))
    inpt_dict = {"nranges": ranges, "float_mode": float_mode, "ndigits": a_fl}
    stats = gr.general_runner(gh.regMul, rounds, inpt_dict,md)  # multgame.regMulGame(number_of_rounds=rounds, nrange=ranges, float_mode=float_mode, after_float_point=a_fl)
    print(str(stats))
    return str(stats)

def regMulII(*argc, **arkw):
    pass

def divGame(*argc, **arkw):
    pass

def divGameII(*argc, **arkw):
    pass

def MixedArr(*argc, **arkw):
    pass

def MixedArrII(*argc, **arkw):
    pass

def polyEval(*argc, **arkw):
    pass

def DetGame(*argc, **arkw):
    pass

def EigenValGame(*argc, **arkw):
    pass

def DiscGame(*argc, **arkw):
    pass

def rootGame(*argc, **arkw):
    pass

def PFD(*argc, **arkw):
    pass

def IntegralGame(*argc, **arkw):
    pass

def regMulDig(*argc, **arkw):
    pass

def FourierSeries(*argc, **arkw):
    pass

def EquationSystem(*argc, **arkw):
    pass

def Mean(*argc, **arkw):
    pass

def Stdev(*argc, **arkw):
    pass

def diffeq(*argc, **arkw):
    pass

def PolyDet(*argc, **arkw):
    pass

def PolyDetFourier(*argc, **arkw):
    pass

def curvatureGame(*argc, **arkw):
    pass

def TGame(*argc, **arkw):
    pass

def LineIntegralGame(*argc, **arkw):
    pass

def DiverganceGame(*argc, **arkw):
    pass

def LineIntegralSc(*argc, **arkw):
    pass

# when anything was going wrong, use these two for test
# def function1(inputs):
#
#     return sum(map(int, inputs))
#
# def function2(inputs):
#     return min(map(int, inputs))

function_map = {
    "regMul": regMul,
    "regMulII": regMulII,
    "divGame": divGame,
    "divGameII": divGameII,
    "MixedArr": MixedArr,
    "MixedArrII": MixedArrII,
    "polyEval": polyEval,
    "DetGame": DetGame,
    "EigenValGame": EigenValGame,
    "DiscGame": DiscGame,
    "rootGame": rootGame,
    "PFD": PFD,
    "IntegralGame": IntegralGame,
    "regMulDig": regMulDig,
    "FourierSeries": FourierSeries,
    "EquationSystem": EquationSystem,
    "Mean": Mean,
    "Stdev": Stdev,
    "diffeq": diffeq,
    "PolyDet": PolyDet,
    "PolyDetFourier": PolyDetFourier,
    "curvatureGame": curvatureGame,
    "TGame": TGame,
    "LineIntegralGame": LineIntegralGame,
    "DiverganceGame": DiverganceGame,
    "LineIntegralSc": LineIntegralSc
}


@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()  # Get the incoming JSON data
    function_name = str(data.get('name'))
    inputs = list(data.get('inputs'))
    print(function_name)
    # Call the appropriate function based on the name
    if function_name in function_map:
        result = function_map[function_name](inputs)
        return jsonify(result=result)  # Return result as JSON
    else:
        return jsonify(result="Function not found"), 404  # Handle unknown functions

if __name__ == '__main__':
    app.run(port=5000)  # Run server on localhost:5000