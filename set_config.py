import json

def get_config():
    with open("config.json", "r") as config:
        variables = json.load(config)

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
    with open("config.json", "r") as config:
        variables = json.load(config)

    variables["url"] = url

    with open("config.json", "w") as config:
        json.dump(variables, config)

def set_res(res):
    with open("config.json", "r") as config:
        variables = json.load(config)

    variables["resolution"] = res

    with open("config.json", "w") as config:
        json.dump(variables, config)

def set_sym(choice):
    with open("config.json", "r") as config:
        variables = json.load(config)

    variables["incorrect_symbols_remove"] = choice

    with open("config.json", "w") as config:
        json.dump(variables, config)

def set_conv(choice):
    with open("config.json", "r") as config:
        variables = json.load(config)

    variables["convert_to_mp3"] = choice

    with open("config.json", "w") as config:
        json.dump(variables, config)

def set_path(path):
    with open("config.json", "r") as config:
        variables = json.load(config)

    variables["output_path"] = path

    with open("config.json", "w") as config:
        json.dump(variables, config)


