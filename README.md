# Aircraft Weight & Balance Calculator

A Python program that calculates the total weight and center of gravity (CG) of an aircraft load configuration and checks it against weight and CG limits.

**All aircraft data in this project is fictional.** This is a learning project and must never be used for real flight or load planning.

## How it works

Every item on the aircraft has a weight (lb) and an arm (inches from a reference datum).

- Moment = weight x arm
- CG = total moment / total weight

The program loops through a list of six load items (basic operating weight, forward and aft cargo, forward and aft passengers, and fuel), adds up the weights and moments, and calculates the CG. It then checks three limits:

- Total weight must not exceed the maximum weight
- CG must not be forward of the forward limit
- CG must not be aft of the aft limit

If any limit is exceeded, the program prints which one.

## How to run it

1. Install Python 3
2. Download `weight_balance.py`
3. Run: `python weight_balance.py`

Expected output with the default numbers:

    Total weight: 196,000 lb
    CG: 1009.18 in
    WITHIN LIMITS

## Testing

I verified the limit checks by changing the data on purpose:

- Raised the fuel weight to push the total over the maximum weight, and confirmed the overweight warning appeared
- Moved the aft cargo arm far aft, and confirmed the "CG too far aft" warning appeared

## What I learned

- How to retrace back into the code and solve my own errors
- How CG calculations connect to statics
- How to apply my real-life experience into a well-put project

## Possible next steps

- Take weights as user input
- Plot the weight and CG against an allowable envelope
- Model CG shift as fuel burns off during a flight

## Author

Jhanzeil Pena, Mechanical Engineering Technology, University of North Texas
