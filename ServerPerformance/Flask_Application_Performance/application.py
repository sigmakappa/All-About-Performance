from flask import Flask, jsonify

from Fibonacci_using_maps import fib as fib
from Prime_using_SQRT import isPrime

app = Flask(__name__)


@app.route('/fibo/<number>', methods=['GET', 'POST'])
def fibo(number):
    nth_number = fib(int(number))

    # return str(nth_number)
    json = {"index": number,
            "fibonacci_number": nth_number}

    return jsonify(json)


@app.route('/isprime/<number>', methods=['GET', 'POST'])
def prime(number):
    status = isPrime(int(number))

    json = {"number": number,
            "status": status}
    return jsonify(json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
