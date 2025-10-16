import json
import os

def get_config():
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
        variables = json.load(config)

    if len(variables["url"]) > 50:
        url = variables["url"][0: 50] + "..."
    else:
        url = variables["url"]
    res = variables["resolution"]
    incorrect_sym = variables["incorrect_symbols_remove"]
    convert_to_mp3 = variables["convert_to_mp3"]
    output_path = variables["output_path"]

    str = f'''Url: {url}
 Resolution: {res}
 Filter title symbols: {incorrect_sym}
 Convert to mp3: {convert_to_mp3}
 Output path: {output_path}
        '''
    return str

def set_url(url):
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
        variables = json.load(config)

    variables["url"] = url

    with open(config_path, "w") as config:
        json.dump(variables, config)

def set_res(res):
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
        variables = json.load(config)

    variables["resolution"] = res

    with open(config_path, "w") as config:
        json.dump(variables, config)

def set_sym(choice):
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
        variables = json.load(config)

    variables["incorrect_symbols_remove"] = choice

    with open(config_path, "w") as config:
        json.dump(variables, config)

def set_conv(choice):
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
        variables = json.load(config)

    variables["convert_to_mp3"] = choice

    with open(config_path, "w") as config:
        json.dump(variables, config)

def set_path(path):
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
        variables = json.load(config)

    variables["output_path"] = path

    with open(config_path, "w") as config:
        json.dump(variables, config)


