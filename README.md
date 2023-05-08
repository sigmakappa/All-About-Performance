# All-About-Performance

Hey there, you performance-testing rockstar! Welcome to our awesome repository filled with experiments to test the limits of your apps and systems.

We're all about pushing the boundaries and seeing what these babies can really do, so get ready to unleash some serious testing power.

## Getting Started

To join in on the fun, you'll need a computer running a Linux, macOS, or Windows operating system, Python 3.7 or later, and pip (the package installer for Python). 

If you don't have these already, no worries, you can grab them in a jiffy.

Once you're set up, run this command to install the required Python packages:

```
pip install -r requirements.txt
```

And with that, you're ready to start testing like a boss!

## Running Performance Tests

### Fibonacci Recursion

Want to know how fast your computer can calculate the Fibonacci sequence using recursion? Yeah, we do too! Navigate to the `Fibonacci_Recursion` directory and run this command:

```
python Fibonacci_Recursion.py
```

This will execute the performance test and spit out the results on your screen. If you wanna save the results to a file, you can do that too (though the runtime logs do get saved to the given files too):

```
python Fibonacci_Recursion.py > results.txt
```
Also, check out how fast different platforms can calculate the Fibonacci sequence using recursion [here](https://github.com/sigmakappa/All-About-Performance/blob/main/ProcessorPerformance/Fibonacci_Recursion/README.md).

### Flask API

If you wanna test the performance of a Flask API, head to the `Flask_Application_Performance` directory and start the server with this command:

```
python app.py
```

Once the server is up and running, you can send requests to the API with this command in a separate terminal window:

```
python application.py
```

This will execute the performance test and show you the results. And you guessed it, you can save the results to a file with:

```
python test_api.py > results.txt
```

## Contributing

You think you can make these performance tests even better? You're damn right you can! Fork this repository to your own GitHub account and go nuts! Just follow these steps:

1. Create a new branch for your changes.
2. Make your changes and commit them to your branch.
3. Push your changes to your forked repository.
4. Create a pull request to merge your changes into the main repository.


## License

This repository is licensed under the MIT license, which means you're free to use it, modify it, and distribute it however you want! Just make sure to give us a shoutout, okay?

The MIT license is like a get-out-of-jail-free card for software, so go ahead and get crazy with it! Want to create a Frankenstein's monster of an app using our performance testing experiments? We won't judge. Just make sure you don't blame us if it all goes horribly wrong.

Check out the `LICENSE` file for more info, but trust us, it's pretty straightforward.