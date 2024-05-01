# SIS Model Simulation

This repository contains Python code to simulate the Susceptible-Infectious-Susceptible (SIS) model, a simple epidemiological model used to study the dynamics of infectious diseases within a population. The simulation is implemented using Euler's numerical methods (Explicit - Implicit - Mid Point)

![SIS](/assets/img/SIS.png)


## Introduction

The SIS model divides the population into two groups: Susceptible individuals (those who can contract the disease) and Infectious individuals (those who are currently infected and can spread the disease). This model does not account for recovered individuals; instead, infectious individuals return to the susceptible population after recovering from the disease.

## Contents

- `euler.py` Python module containing the implementation of  Euler's methods.
- `sis.py` Python script containing the implementation of the SIS model and its simulation.

## Dependencies

- `numpy`
- `scipy`
- `matplotlib`


## Usage

To run the SIS model simulation, make sure to have the required dependencies installed.

1. Clone the repository:

```bash
git clone https://github.com/choukrani/Euler-methods-SIS-model-simulation.git
```

2. Navigate to the project directory:

```bash
cd Euler-methods-SIS-model-simulation
```

3. Run the desired Python script:

```bash
python3 sis.py
```


## Results

The simulation produces plots showing the population dynamics of susceptible and infectious individuals over time. These plots provide insights into the spread and control of infectious diseases within a population.

![Population Dynamics](/assets/img/100indv1infectious20days.png)



## References

- [Wikipedia - Compartmental models in epidemiology](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)


## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contact

If you have any questions or inquiries about this repository, please contact [omar.choukrani@insa-rouen.fr](mailto:omar.choukrani@insa-rouen.fr).
