# Orbital Mechanics Simulation

A Python program that simulates how planets/objects orbit around a star and calculates the area swept out by the orbit.

## What does this do?

This program:
1. Takes initial conditions for an orbit (position, velocity, etc.)
2. Calculates the orbital path using numerical methods
3. Plots the orbit so you can see what it looks like
4. Calculates the area enclosed by the orbit

## Files

- **`kepler2.py`** - Main file, run this one!
- **`initials_int_plot.py`** - Has the math for calculating orbits and plotting
- **`Area_int.py`** - Has different methods for calculating orbital area

## How to Run

Just run:
```bash
python kepler2.py
```

Then follow the prompts!

## What You'll Be Asked

1. **Which integration method?**
   - Type `0` for RK4 (more accurate, recommended)
   - Type `1` for Euler (faster but less accurate)

2. **Which area calculation method?**
   - Type `0` for Euler
   - Type `1` for Simpson's (most accurate, recommended)
   - Type `2` for Trapezoidal

3. **Orbital parameters:**
   - Step size: how precise the calculation is (try `0.001`)
   - Mass of star: usually `1.0`
   - Initial distance from star: try `1.0`
   - Initial radial velocity: how fast it's moving toward/away from star (try `0.0` for circular orbit)
   - Initial tangential velocity: sideways velocity (try `1.0`)
   - Number of orbits: how many times to go around (try `1`)

## Example Run

```
Integration method? RK4 method [0], Euler method [1]: 0
Area integration method? Euler[0], Simpson's[1], Trapezoidal[2]: 1
integration step size: 0.001
Mass of star: 1.0
initial radial distance: 1.0
initial radial velocity: 0.0
initial tangential velocity: 1.0
number of orbits: 1
```

## What You'll See

- A plot showing the orbital path
- Green dot = where it starts
- Yellow dot = where it ends
- Red dot = the star at the center
- Printed area calculations (your numerical answer vs the exact answer)

## Important: Energy Constraint

For an orbit to be **bound** (closed orbit, object doesn't escape), the total energy must be negative:

```
E = (1/2)(vr² + vθ²) - M/r < 0
```

Where:
- `vr` = radial velocity (toward/away from star)
- `vθ` = tangential velocity (sideways)
- `M` = mass of star
- `r` = distance from star

**What this means:** If your object is moving too fast, it has enough energy to escape the star's gravity and won't orbit!

If you get the error "Energy is unbound", try:
- Lower velocities
- Larger star mass

## What's the Math?

The program solves equations that describe how objects move in orbits. It uses:
- **Euler method**: Simple but not super accurate
- **RK4 method**: More complex but much more accurate
- Different integration methods to calculate the area swept by the orbit

## Requirements

You need these Python libraries:
- `math`
- `matplotlib`
- `numpy`

Install with: `pip install matplotlib numpy`