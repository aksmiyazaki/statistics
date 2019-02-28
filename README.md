# Anaconda Stuff

* Creating environment
    * conda create -n yourenvname python=x.x anaconda

* Activating/Deactivating specific environment
    * conda activate yourenvname
    * conda deactivate

* Installing packages into environment
    * conda install -n yourenvname [package]

* Delete a no longer needed env.
    * conda remove -n yourenvname -all

* List Packages
    * conda list

* List environments
    * conda info --envs

# Statistics
Repo containing statistics stuff (improving knowledge from basics).

# Section 2

| Object        | Notation           | Numbers obtained  | Definition |
| :------------- |:-------------:| :-----:|:-------:|
| Population     | N | Called parameters | Hard to observe and contact |
| Sample    | n      |   Called statistics | Subset of the Population (easier to observe and contact) |
 
Almost always we will be working with samples.  
Samples have 2 defining features:

* Randomness: each member of the sample is chosen stricly by chance.
* Representativeness: representative sample is a subset of the population that accurately reflects the members of the entire population.

# Section 3

Data Classification in two ways: **Types of Data** and **Measurement Levels**

By Type:
| Type        | Description           |  Examples  |
| :------------- |:-------------:| :-----:|
| Categorical     | Categories or groups | Car brands (Mercedes, VW, Renault), Answers to Yes/No questions  |
| Numerical Discrete    | Represents numbers (usually integers, entire range can be imagined) | Number of children, Exam Score, Grades, Number of objects |
| Numerical Continuous    | Represents numbers (infinite, impossible to count and imagine) | Weight, Height, Area, Time, Distance |

By Levels of Measurement:
| Type        | Description           |  Examples  |
| :------------- |:-------------:| :-----:|
| Qualitative Nominal | Aren't numbers and cannot be ordered | Car brands, Seasons |
| Qualitative Ordinal | Groups that follows a strict order | Classification of women in Ugly, OK, HOT|
| Quantitative Interval | Numbers, that doesn't have a true 0 | Temperature (Celsius, Fahrenheit). |
| Quantitative Ratio | Numbers, that have a true 0 (most common) | Number of objects, distance, time, Temperature (Kelvin)  |

## Data Visualization - Categorical Variables

Representation of Categorical Variables:
* Frequency Distribution Tables
* Bar Charts
* Pie Charts
* Pareto Diagrams

## Data Visualization - Numerical Variables

Representation of Numerical Variables:

* Frequency Distribution Tables
    * Divide range in intervals and then count the frequency.
* Histograms
    * Possibility to create unequal intervals