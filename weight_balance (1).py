"""
Weight & Balance Calculator -- starter file

Core idea (statics): every item has a weight and an "arm" (its distance from a
reference datum). Moment = weight x arm. The aircraft's center of gravity (CG)
is the point where all those moments balance:

    CG = total moment / total weight

All numbers below are FICTIONAL. This is a learning project, not real
aircraft data, and must never be used for actual operations.
"""

# Each load item: (name, weight in lb, arm in inches from the datum)
LOADS = [
    ("Basic operating weight", 120_000, 1000),
    ("Forward cargo",            8_000,  600),
    ("Aft cargo",                6_000, 1400),
    ("Passengers (forward)",    10_000,  700),
    ("Passengers (aft)",        12_000, 1300),
    ("Fuel",                    40_000, 1050),
]

# Fictional limits
MAX_WEIGHT = 200_000      # lb
CG_FORWARD_LIMIT = 950    # inches from datum
CG_AFT_LIMIT = 1080       # inches from datum


def moment(weight, arm):
    """Return the moment of a single item."""
    # TODO 1: return weight times arm
    raise NotImplementedError


def total_weight_and_cg(loads):
    """Return (total_weight, cg) for a list of (name, weight, arm) items."""
    # TODO 2: add up all weights, add up all moments, then CG = moments / weight
    raise NotImplementedError


def check_limits(total_weight, cg):
    """Return a list of problem strings. An empty list means within limits."""
    problems = []
    # TODO 3: append a message if total_weight > MAX_WEIGHT
    # TODO 4: append a message if cg is forward of CG_FORWARD_LIMIT or aft of CG_AFT_LIMIT
    return problems


if __name__ == "__main__":
    weight, cg = total_weight_and_cg(LOADS)
    print(f"Total weight: {weight:,.0f} lb")
    print(f"CG: {cg:.2f} in")

    # Self-check: with the numbers above, you should get 196,000 lb and
    # a CG of about 1009.18 in, which is within limits.
    problems = check_limits(weight, cg)
    print("WITHIN LIMITS" if not problems else "OUT OF LIMITS: " + "; ".join(problems))
