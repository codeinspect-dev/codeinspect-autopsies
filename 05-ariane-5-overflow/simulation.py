"""
CodeInspect Forensic Autopsy - Episode 05
Incident: Ariane 5 Flight 501 Disaster (June 4, 1996)
Flaw: Unhandled 64-bit float to 16-bit signed integer conversion overflow.
"""

import time

INT16_MIN = -32768
INT16_MAX = 32767

def simulate_ariane4_flight():
    """Ariane 4 trajectory: lower horizontal velocity, fits within 16-bit bounds."""
    print("[SIMULATION] Ariane 4 Trajectory Profile: Normal Flight")
    for sec in range(0, 40, 5):
        horizontal_bias_64 = 520.0 + (sec * 210.5)
        converted_16 = int(horizontal_bias_64)
        assert INT16_MIN <= converted_16 <= INT16_MAX
        print(f"  T+{sec:02d}s | Raw Float64: {horizontal_bias_64:10.2f} -> Int16: {converted_16:6d} [NOMINAL]")
    print("[RESULT] Ariane 4 completed alignment safely.\n")

def simulate_ariane5_flight():
    """Ariane 5 trajectory: 5x higher horizontal velocity, exceeding 32,767."""
    print("[SIMULATION] Ariane 5 Trajectory Profile: Flight 501")
    time.sleep(0.5)

    for sec in range(0, 45, 3):
        horizontal_bias_64 = 850.0 + (sec ** 2 * 24.2)
        print(f"  T+{sec:02d}s | Horizontal Bias (Float64): {horizontal_bias_64:10.2f}", end=" ")

        raw_int = int(horizontal_bias_64)
        if raw_int > INT16_MAX or raw_int < INT16_MIN:
            print("\n" + "=" * 65)
            print("[FATAL EXCEPTION] Ada Numerical_Error (Overflow)")
            print(f"Value {raw_int} exceeds 16-bit signed integer maximum ({INT16_MAX})")
            print("Flight Control Computer (SRI 1) halts output.")
            print("Diagnostic telemetry data dumped into control bus as flight commands.")
            print("Nozzles swivel to mechanical limit -> 90-degree pitch -> AERODYNAMIC BREAKUP.")
            print("=" * 65)
            raise OverflowError(f"16-bit integer overflow: {raw_int} > {INT16_MAX}")
        else:
            print(f"-> Int16: {raw_int:6d} [NOMINAL]")
        time.sleep(0.1)

if __name__ == "__main__":
    print("=" * 65)
    print("CODEINSPECT AUTOPSY: ARIANE 5 FLIGHT 501 INTEGER OVERFLOW")
    print("=" * 65 + "\n")
    
    simulate_ariane4_flight()
    try:
        simulate_ariane5_flight()
    except OverflowError as e:
        print(f"\n[SYSTEM CRASH CONFIRMED]: {e}")
