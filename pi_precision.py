from decimal import Decimal, getcontext, ROUND_HALF_UP

# Set the precision high enough to handle 100 decimals
getcontext().prec = 150

PI_STRING = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128"
TRUE_PI = Decimal(PI_STRING)

# --- THE FORMULA: Volume of a Cylinder ---
# V = pi * r^2 * h
def cylinder_volume(pi_val, radius, height):
    return pi_val * (Decimal(radius)**2) * Decimal(height)

# --- SETTINGS ---
RADIUS = 15
HEIGHT = 50
TEST_POINTS = [20, 40, 60, 100]

true_vol = cylinder_volume(TRUE_PI, RADIUS, HEIGHT)

print("--- COMPU LAB: PI PRECISION TEST ---")
print(f"Testing Cylinder Volume with Radius {RADIUS} and Height {HEIGHT}")
print("-" * 60)
print(f"{'Digits':<8} | {'Method':<10} | {'Error Amount'}")
print("-" * 60)

for d in TEST_POINTS:
    dot = PI_STRING.find('.')
    pi_trunc = Decimal(PI_STRING[:dot + 1 + d])
    
    vol_trunc = cylinder_volume(pi_trunc, RADIUS, HEIGHT)
    error_trunc = abs(true_vol - vol_trunc)

    pi_round = TRUE_PI.quantize(Decimal(f"1e-{d}"), rounding=ROUND_HALF_UP)
    
    vol_round = cylinder_volume(pi_round, RADIUS, HEIGHT)
    error_round = abs(true_vol - vol_round)

    # Output the results
    print(f"{d:<8} | Truncate   | {error_trunc:.2e}")
    print(f"{d:<8} | Rounding   | {error_round:.2e}")
    print("." * 60)

print("\nConclusion: Rounding is usually more accurate than truncation.")
