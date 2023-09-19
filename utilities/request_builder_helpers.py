def api_params_reformat(link: str, parameters: dict):
    count = 0
    new_link = link + "/?"
    for key, val in parameters.items():
        parameter = f"{key}={val}"
        if count == len(parameters) - 1:
            new_link += parameter
        else:
            new_link += parameter + "&"
        count += 1
    return new_link


def check_api_link(api):
    if not len(api):
        raise "Invalid: Empty API"
    return api


def check_http_method(http_method):
    http_method = http_method.upper()
    constant = ["GET", "POST", "DELETE", "PUT", "PATCH"]
    assert (
        http_method in constant
    ), f"invalid: wrong Http method you entered {http_method}"
    return http_method


def encode_files_base_x64(filepath):
    pass
