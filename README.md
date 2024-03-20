---

# HTTP Client Request Builder

## Introduction
HTTP Client Request Builder is a Python module designed to simplify the process of constructing and sending HTTP requests. It provides a flexible and intuitive interface for building requests with various HTTP methods, headers, parameters, and authentication tokens. The module follows the Builder Pattern, allowing for fluent and expressive request construction, while also leveraging object-oriented principles for modularity and extensibility.

## Features
- Support for common HTTP methods: GET, POST, PUT, PATCH, DELETE.
- Automatic validation of API links and HTTP methods.
- Easy addition of authentication tokens and custom headers.
- Support for file uploads.
- Flexible handling of request parameters and body data.

## Installation
You can install HTTP Client Request Builder using pip:

```
pip install HTTP_Client
```

## Usage
Here's a basic example demonstrating how to use the HTTP Client Request Builder:

```python
from HTTP_Client.request_builder import RequestBuilder

# Instantiate RequestBuilder with HTTP method and API endpoint
request_builder = RequestBuilder(http_method='GET', api='https://api.example.com/resource')

# Add headers
request_builder.headers({'Content-Type': 'application/json'})

# Add parameters
request_builder.parameters({'param1': 'value1', 'param2': 'value2'})

# Add authentication token
request_builder.bearer_token('your_access_token')

# Send the request
response = request_builder.send()

# Print the response status code and status description
print(response.status_code, response.reason)
```

## Builder Pattern
HTTP Client Request Builder utilizes the Builder Pattern to construct complex HTTP requests. This pattern allows for the step-by-step construction of objects with different configurations, making the code more readable and maintainable. Each method call on the RequestBuilder object returns a reference to itself, enabling method chaining and fluent API design.

## Object-Oriented Approach
The HTTP Client Request Builder module adopts an object-oriented approach to encapsulate request building logic into modular and reusable components. Each HTTP method (GET, POST, PUT, PATCH, DELETE) is implemented as a separate class, following the principles of abstraction, encapsulation, and inheritance. This design promotes code organization, scalability, and code reusability.

## Dependencies
This module depends on the following Python packages:
- requests

## Acknowledgments
Special thanks to [Hossam Hamdy](https://github.com/0xGhazy) for their support and contribution to this project.

## License
This project is licensed under the __Joe-0xRoot__. See the LICENSE file for details.

---

Feel free to adjust the README as needed based on your project requirements and preferences.
