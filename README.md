# Mini Banking System


<p align="center">
<img src="https://imgur.com/2P2PyTL" />
</p>

### [YouTube Explanation with Demonstration](https://youtu.be/lHeVDmgpKy4)

This is a project specified by WGU to solve a package delivery routing problem, which is essentially the traveling salesman problem with a dedicated starting node and a few restrictions/requirements. For my solution, I implemented the nearest neighbor algorithm which operates with a time-complexity of O(n).

## Usage

To get the code run this from the command line:

```commandline
git clone https://github.com/joshmadakor1/C950.git
```

Once that is done, in the main directory where `main.py` is located run:

```commandline
python3 main.py
```

depending on python version^^^

From there you should see the Command Line Interface like this:

```commandline
nnamdimadakor@nnamdis-Mac-mini C950 % python3 Main.py

	What would you like to do?

	d - Begin Delivery Simulation and Package Information Lookup
	q - Quit

>d

	Beginning delivery simulation...

	During deliver, new information has come in about package #9!
	Would you like to correct the address for package #9? Enter 'y' or 'n'
>y
	Package #9's address has been updated to: 410 S State St., Salt Lake City, UT 84111!

