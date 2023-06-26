# Python Flask Web Server Performance Testing

🚀 Welcome to the Python Flask Web Server Performance Testing repository!

📈 This repository is dedicated to measuring and analyzing the performance of web servers built with Python Flask. Get
ready to test your server's performance based on the hardware you are using!

## Table of Contents

- [Understanding Web Server Performance](#understanding-web-server-performance)
- [What is Flask](#what-is-flask)
- [Getting Started](#getting-started)
- [What happens when the test is run?](#what-happens-when-the-test-is-run)
- [Analyzing Performance Results](#analyzing-performance-results)
- [Contributing](#contributing)
- [License](#license)

## Understanding Web Server Performance

API server performance measures how effectively a machine can process requests and provide timely and accurate
responses. Strong performance indicates swift and dependable answers, akin to a superhero's rapid actions.

In contrast, poor performance results in sluggish and uncertain replies, akin to a lethargic and uncertain snail's
movements (resulting in frustrated and dissatisfied users).

## What is Flask?

[Flask](https://flask.palletsprojects.com) is a popular web framework in Python that allows you to build web
applications. It utilizes the WSGI (Web Server
Gateway Interface) protocol to handle incoming requests and generate appropriate responses. Here's a simplified overview
of how Flask servers work:

1. **Setting up routes**: In Flask, you define routes that map URLs to specific functions in your Python code. Each
   route specifies a URL pattern and the corresponding function that should be executed when that URL is accessed.

2. **Handling requests**: When a client sends a request to the Flask server, the server receives the request and
   examines its URL. It then matches the URL to the appropriate route that you defined.

3. **Executing the view function**: Once the route is matched, the server calls the associated view function, passing
   any relevant data from the request (such as form data or query parameters) as function arguments.

4. **Processing the request**: Inside the view function, you can perform various tasks such as accessing databases,
   interacting with external APIs, or manipulating data. You typically write the logic to process the incoming request,
   retrieve or modify data, and prepare the response.

5. **Generating the response**: After processing the request, you construct a response object that will be sent back to
   the client. The response can include HTML content, JSON data, or any other format depending on the requirements of
   your application.

6. **Sending the response**: The Flask server sends the response back to the client, which can be a web browser or any
   other type of client making HTTP requests. The client receives the response and renders it accordingly.

7. **Repeat for subsequent requests**: Flask servers are designed to handle multiple requests simultaneously. They can
   handle requests from different clients concurrently, allowing for efficient and scalable web applications.

It's important to note that Flask is a lightweight framework and does not come with a built-in web server. In
development, you can use Flask's built-in development server. However, for production environments, you would typically
deploy your Flask application on a production-ready web server such as Apache or Nginx using the WSGI protocol.

This is a high-level overview of how Flask servers work. Flask provides a flexible and extensible framework for building
web applications in Python, allowing you to define routes, handle requests, and generate responses with ease.

## Getting Started

🔧 To get started with web server performance testing using Python Flask, follow below steps.

You need **2 machines** (laptops or desktops) and a **router** to which these 2 machines are connected to perform this
test (one
as the Flask Application Server under test and the other as JMeter testing machine which spawns test users).

### A. On the Server machine:

1. Clone this repository to the server
   machine: `git clone https://github.com/sigmakappa/All-About-Performance.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask
   application [file here](https://github.com/sigmakappa/All-About-Performance/Flask_Application_Performance/application.py) as:<br><br>
   ```
   python application.py > logs.txt
   ```
   This above would run the application as below:<br><br>
   ![running the application](https://github.com/sigmakappa/All-About-Performance/blob/main/ServerPerformance/Flask_Application_Performance/files/running_application.png)

### B. On the Testing machine:

1. All you need to do is:
    * Have Java 11+ installed.
    * Download JMeter [here](https://jmeter.apache.org/download_jmeter.cgi)).
    * Load the
      given [jmx file](https://github.com/sigmakappa/All-About-Performance/blob/main/ServerPerformance/Flask_Application_Performance/Test_Scripts/JMeter/JMeter_Test_Script.jmx)
      in JMeter.
    * Change the target IP address here (as obtained in A.3 above):<br><br>
      ![changing address and port](https://github.com/sigmakappa/All-About-Performance/blob/main/ServerPerformance/Flask_Application_Performance/files/changing_address_port.png)<br>

2. The test details and benchmarked load in this test are as below:
    1. Pre-configured in the attached
       JMeter [jmx file](https://github.com/sigmakappa/All-About-Performance/blob/main/ServerPerformance/Flask_Application_Performance/Test_Scripts/JMeter/JMeter_Test_Script.jmx) along-with as in the screenshot below:<br><br>
       
       ![setting up test threads](https://github.com/sigmakappa/All-About-Performance/blob/main/ServerPerformance/Flask_Application_Performance/files/jmx_setting_up_threads.png)<br>

    2. APIs already configured:
        * **Fibonacci**: Takes a random number between 10 and 1000 as input and returns its corresponding Fibonacci
          Number (
          calculating Fibonacci number
          using [Dictionaries](https://github.com/sigmakappa/All-About-Performance/blob/main/ServerPerformance/Flask_Application_Performance/Fibonacci_using_maps.py))
        * **isPrime**: Takes a random number between 1000 and 10000000 and returns whether the number is prime or not.

    3. 20,000 Users to start with.
    4. Ramp Up of 500 seconds (means the test would have spawned all 20K users in time of 500 seconds or 8 minutes 2
       seconds).
    5. Loop Count of 5 (i.e. we'd have a 5X the above users in 500 seconds i.e. 100,000 users total in 500 seconds).

## What happens when the test is run?

![Request_Response](https://github.com/sigmakappa/All-About-Performance/blob/main/ServerPerformance/Flask_Application_Performance/files/Request_Response.jpg)<br>

Make sure to monitor system resource utilization during testing to identify any potential bottlenecks or resource
limitations.

## Analyzing Performance Results

📊 Once you have completed the performance tests, it's time to dive into the data! Use the gathered information,
including response times, throughput, and error rates, to assess the performance of your flask web server. Unleash the power
of visualization tools like graphs and charts to uncover hidden insights, spot performance patterns, and optimize your
server like a true champion!

## Observations on different platforms
:mag: Now here is the most interseting part: the observed numbers on different platforms.

|              | **Details**                                                   |
|--------------|---------------------------------------------------------------|
| **Platform** | Intel i7 1165G7 11th Generation 32G RAM Windows 10 Enterprise |
| **Python**   | Python 3.9                                                    |
| **Flask**    | 1.1.2                                                         |


| **Label** | **# Samples** | **Average** | **Median** | **90% Line** | **95% Line** | **99% Line** | **Min** | **Max** | **Error %** | **Throughput** | **Received KB/sec** | **Sent KB/sec** |
|-----------|---------------|-------------|------------|--------------|--------------|--------------|---------|---------|-------------|----------------|---------------------|-----------------|
| Fibonacci | 100000        | 12          | 9          | 18           | 24           | 59           | 4       | 1270    | 0.000%      | 199.97440      | 56.32               | 62.47           |
| IsPrime   | 100000        | 11          | 9          | 18           | 24           | 56           | 4       | 1076    | 0.000%      | 199.97480      | 38.96               | 63.84           |
| **TOTAL** | 200000        | 11          | 9          | 18           | 24           | 57           | 4       | 1270    | 0.000%      | 399.94401      | 95.29               | 126.31          |

***************************************************************************************************************************

|              | **Details**                                                   |
|--------------|---------------------------------------------------------------|
| **Platform** | Intel i7 1165G7 11th Generation 32G RAM Windows 10 Enterprise |
| **Python**   | Python 3.11.3                                                 |
| **Flask**    | 2.3.2                                                         |


| **Label** | **# Samples** | **Average** | **Median** | **90% Line** | **95% Line** | **99% Line** | **Min** | **Max** | **Error %** | **Throughput** | **Received KB/sec** | **Sent KB/sec** |
|-----------|---------------|-------------|------------|--------------|--------------|--------------|---------|---------|-------------|----------------|---------------------|-----------------|
| Fibonacci | 100000        | 30          | 30         | 34           | 42           | 59           | 15      | 391     | 0.000%      | 199.90564      | 59.96               | 62.45           |
| IsPrime   | 100000        | 31          | 31         | 34           | 43           | 60           | 15      | 390     | 0.000%      | 199.91084      | 42.66               | 63.82           |
| **TOTAL** | 200000        | 31          | 31         | 34           | 43           | 60           | 15      | 391     | 0.000%      | 399.79850      | 102.62              | 126.26          |

***************************************************************************************************************************

|              | **Details**                                                   |
|--------------|---------------------------------------------------------------|
| **Platform** | More to come... |
| **Python**   |                                                |
| **Flask**    |                                                       |


## Contributing

🤝 Contributions are more than welcome! If you have any new **ideas**, **enhancements**, or bug fixes, don't hesitate to
open an issue or submit a pull request. Let's collaborate and elevate this repository to the next level, together!

## License

📜 This repository is licensed under
the [MIT License](https://github.com/sigmakappa/All-About-Performance/blob/56ecd708b5c022b966697e1e03971decca957fb2/LICENSE).
<br>You're free to use, modify, and distribute the code and
associated documentation for your own web server performance testing needs.🚀🔥

