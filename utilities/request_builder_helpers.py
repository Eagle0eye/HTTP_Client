import base64
import re


def api_params_reformat(link: str, parameters: dict):
    count = 0
    new_link = link.lower() + "/?"
    for key, val in parameters.items():
        parameter = f"{key}={val}"
        if count == len(parameters) - 1:
            new_link += parameter
        else:
            new_link += parameter + "&"
        count += 1
    return new_link


def check_api_link(api: str):
    if not len(api.strip()):
        raise "Invalid: Empty API"
    return api.strip()


def check_http_method(http_method: str):
    http_method = http_method.upper()
    constant = ["GET", "POST", "DELETE", "PUT", "PATCH"]
    assert (
        http_method in constant
    ), f"invalid: wrong Http method you entered {http_method}"
    return http_method


def __manipulate_files(path: str, permission: str):
    file = open(path, permission)
    fetch_data = file.read()
    file.close()
    return fetch_data


def encode_excel_base_x64(filepath):
    __path_pattern = "^(?:[a-zA-Z]:\\|(?:\/|\b\w+\b\/|\w+\/))*[\w.-]+$"
    pattern = re.compile(__path_pattern)
    assert pattern.match(filepath), "Path Not Found"
    data = __manipulate_files(filepath, "rb")
    encoded_data = base64.b64encode(data).decode(encoding="utf-8")
    return encoded_data
