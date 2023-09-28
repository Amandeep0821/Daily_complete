""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2

AMANDEEP SINGH (100893335), TPRG 2131-01

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""

print("Series resonant circuit calculator\n(CTRL-C to quit)")
import math

def get_positive_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def calculate_series_resistance(r1, r2):
    return r1 + r2

def calculate_parallel_resistance(r1, r2):
    return 1 / (1 / r1 + 1 / r2)

def calculate_rc_time_constant(r, c):
    return r * c

def calculate_resonant_frequency(l, c):
    return 1 / (2 * math.pi * math.sqrt(l * c))

def calculate_bandwidth(r, l):
    return r / (2 * math.pi * l)

def calculate_q_factor(r, l, c):
    return (1 / r) * math.sqrt(l / c)

print("Series resonant circuit calculator\n(Type 'q' to quit)")

try:
    while True:
        print("Select the type of calculation:")
        print("1. Series Resistance")
        print("2. Parallel Resistance")
        print("3. RC Time Constant")
        print("4. Resonant Frequency, Bandwidth, and Q Factor")
        print("Type 'q' to quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            r1 = get_positive_value("Enter the first resistance in ohms: ")
            r2 = get_positive_value("Enter the second resistance in ohms: ")
            series_resistance = calculate_series_resistance(r1, r2)
            print(f"Series Resistance: {series_resistance} ohms\n")

        if choice == '2':
            r1 = get_positive_value("Enter the first resistance in ohms: ")
            r2 = get_positive_value("Enter the second resistance in ohms: ")
            parallel_resistance = calculate_parallel_resistance(r1, r2)
            print(f"Parallel Resistance: {parallel_resistance} ohms\n")

        if choice == '3':
            r = get_positive_value("Enter the resistance in ohms: ")
            c = get_positive_value("Enter the capacitance in uF: ")
            rc_time_constant = calculate_rc_time_constant(r, c)
            print(f"RC Time Constant: {rc_time_constant} seconds\n")

        if choice == '4':
            l = get_positive_value("Enter the inductance in henries: ")
            c = get_positive_value("Enter the capacitance in uF: ")
            resonant_frequency = calculate_resonant_frequency(l, c)
            bandwidth = calculate_bandwidth(resonant_frequency, l)
            q_factor = calculate_q_factor(resonant_frequency, l, c)

            print(f"Resonant Frequency: {resonant_frequency} Hz")
            print(f"Bandwidth: {bandwidth} Hz")
            print(f"Q Factor: {q_factor}\n")

        elif choice == 'q':
            break

        else:
            print("Invalid choice. Please try again.\n")

except KeyboardInterrupt:
    print("\nExiting the Series Resonant Circuit Calculator")