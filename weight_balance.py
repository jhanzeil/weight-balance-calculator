"""
Weight & Balance Calculator -- starter file
Core idea (statics): every item has a weight and an "arm" (its distance from a reference datum).
Moment = weight x arm. The aircraft's cen\
ter of gravity (CG) is the point where all those moments balance:
     CG = total moment / total weight
All numbers below are FICTIONAL. This is a learning project,
not real aircraft data, and must never be used for actual operations
"""
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
     return weight * arm

def total_weight_and_cg(loads):
    """Return (total_weight, cg) for a list of (name, weight, arm) items."""
    total_weight = 0
    total_moment = 0
    for name, weight, arm in loads:
        total_weight = total_weight + weight
        total_moment = total_moment + moment(weight, arm)
    cg = total_moment / total_weight
    return total_weight, cg

def check_limits(total_weight, cg):
     """Return a list of problem strings. An empty list mean\
s within limits."""
     problems = []
     if total_weight > MAX_WEIGHT:
         problems.append("Over max weight")
     if cg < CG_FORWARD_LIMIT:
         problems.append("CG too far forward")
     if cg > CG_AFT_LIMIT:
         problems.append("CG too far aft")
     return problems

if __name__ == "__main__":
     weight, cg = total_weight_and_cg(LOADS)
     print(f"Total weight: {weight:,.0f} lb")
     print(f"CG: {cg:.2f} in")

problems = check_limits(weight, cg)
print("WITHIN LIMITS" if not problems else "OUT OF LIMITS: " + "\
; ".join(problems))
