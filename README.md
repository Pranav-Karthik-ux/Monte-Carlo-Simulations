# README

## Overview

This repository contains two Python programs that use **Monte Carlo methods**:

1. **Radioactive Decay Simulation** – A probabilistic model of nucleon decay.
2. **Estimation of $\pi$ (Pi)** – A Monte Carlo approximation using random sampling in a unit square.

Both examples show how randomness can approximate deterministic quantities or simulate stochastic processes.

---

## 1. Radioactive Decay Monte Carlo Simulation

### Description

This simulation models the decay of $N$ unstable particles. Each particle has a fixed probability $p$ of decaying during each time interval $\Delta t$. The program tracks:

- Number of particles remaining  
- Number decayed  
- Time evolution  

A decay curve is plotted using `matplotlib`.

### How It Works

1. Initial values:
   - $N_0$: initial number of particles  
   - $D_0$: initial decayed count  
   - $p$: probability of decay per time step  
   - $t_{\max}$: maximum simulation time  

2. For each time step:
   - Generate $N$ random numbers in $[0,1]$
   - A particle decays if its random value satisfies $r_i \le p$
   - Update  
     - $N \leftarrow N - \Delta N$  
     - $D \leftarrow D + \Delta N$  
   - Increase time by $\Delta t = 0.5$

3. Stop when:
   - $N = 0$, or  
   - $t = t_{\max}$  

The analytic decay law that this process approximates is:

$$
N(t) = N_0 e^{-\lambda t},
$$

with the connection:

$$
p \approx 1 - e^{-\lambda \Delta t}.
$$

---

## 2. Monte Carlo Estimation of $\pi$

### Description

The script estimates $\pi$ using the **quarter-circle sampling method**.  
A point $(x, y)$ randomly chosen in the unit square lies inside the quarter circle if:

$$
x^2 + y^2 < 1.
$$

The ratio of points inside the quarter circle to total points approximates $\pi/4$:

$$
\frac{N_{\text{circle}}}{N_{\text{samples}}} \approx \frac{\pi}{4}.
$$

Thus,

$$
\pi \approx 4 \cdot \frac{N_{\text{circle}}}{N_{\text{samples}}}.
$$

### How It Works

1. Generate $n_s$ random points $(x, y)$ in $[0,1] \times [0,1]$.
2. Count points satisfying $x^2 + y^2 < 1$.
3. Compute  
   $$
   \pi_{\text{est}} = 4 \frac{n_c}{n_s}.
   $$
4. Print the final estimate.

---

## Requirements

Both scripts require:

- Python 3.x  
- `matplotlib` (only for the decay plot)

Install dependencies:

```bash
pip install matplotlib
