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

-----
# Descriptive Statistics
Repo containing statistics stuff (improving knowledge from basics).

# Section 2 - Sample of Population Data?

| Object        | Notation           | Numbers obtained  | Definition |
| :------------- |:-------------:| :-----:|:-------:|
| Population     | N | Called parameters | Hard to observe and contact |
| Sample    | n      |   Called statistics | Subset of the Population (easier to observe and contact) |

Almost always we will be working with samples.  
Samples have 2 defining features:

* Randomness: each member of the sample is chosen stricly by chance.
* Representativeness: representative sample is a subset of the population that accurately reflects the members of the entire population.

# Section 3 - The fundamentals of descriptive ststistics

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

## Relationship between Variables

### Categorical
  * Cross-Tables

### Numerical
  * Scatter plots

# Section 4 - Measures of central tendency, asymmetry and variability.

## Measures of central tendency

* Mean
  * Population: &mu;
  * Sample: x&#772;
  * Most commonly used measure of central tendency.
  * Huge downside : easily affected by outliers.

* Median
  * The middle number in an ordered dataset
  * Number in (n+1)/2 position
  * In cases where the sample no is pair, the median is the simple average of
  the two intermediate numbers.

* Mode
  * Value that occurs more often

* There's no *best* central tendency measure. But using only one of them is definitely the worst (they should be used together).

## Measures of asymmetry

* Skewness
    * Indicates wether the data is concentrated on one side
    * Mean > Median -> Positive or right Skew
        * Bigger in lower X, smaller in high X
        * Outliers to the right
        * ![](/udemy_statistics_for_ds/img/PositiveSkew.png?raw=true "Positive Skew")
        * ![](/udemy_statistics_for_ds/img/PositiveSkew-Measures.png?raw=true "Measures of Central Tendency on Positive Skew")
    * Mean = Median = Mode -> Zero Skew
        * Simmetrical Distribution
    * Mean < Median -> Negative or left skew
        * Outliers to the left
        * ![](/udemy_statistics_for_ds/img/NegativeSkew.png?raw=true "Negative Skew")

## Measures of variability

* Sample Statistic is an approximation of the population parameter.
* There's different formulas for calculate population and sample statistics.

* Variance
    * Dispersion of a set of data points around their mean.
    * Large and hard to compare

* Standard Deviation
    * Square root of the variance
    * Most common measure of variability

* Coefficient of variation
    * Relative standard deviation
    * Standard deviation divided by mean
    * Comparing two datasets
    * Universal across datasets.

## Univariate Measures
    * Central tendency
    * Asymmetry
    * variability

## Measures of Relationship between Variables
* Covariance
    * '>' 0, the two variables move together
    * '<' 0, the two variables move in opposite directions
    * = 0, the two variables are independent
    * Problem with the scale -> Can be 0.0001234 or 330000000
* Correlation
    * Adjusts covariance so that the relationship between the two variables becomes easy and intuitive to interpret.
    * -1 <= correlation coefficient <= 1
    * Correlation = 1 -> The entire variability of one variable is explained by the other.
    * Correlation = 0 -> Absolutely independent variables.
    * Correlation = -1 -> Same as 1, but inverted.
    * Correlation (Y,X) == Correlation (X,Y)
    * Correlation does not imply causation.
    * Correlation less than 0.2 is negligible
* Causality
    * Important to understand the direction of causal relationships -> In house pricing, size causes the price.

## Data Analysis example with the content so far
    * Identify Types (Categorical, numerical, etc.)
    * ID
        - Type is Categorical
        - Level of measurement is Qualitative, nominal
    * Age
        - Numerical Discrete
        - Level of measurement is Quantitative Ratio
    * Age Interval
        - Numerical Discrete
        - Level of measurement is Qualitative Ordinal
    * Price
        - Numerical Continuous or Discrete (like age)
        - Level of measurement is Quantitative Ratio
    * Gender
        - Categorical Type
        - Level of measurement is Qualitative Nominal
    * State
        - Categorical type
        - Qualitative Nominal
    * Gender
        - Categorical
        - Qualitative Nominal

# Inferential Statistics

## Distribution
    * Normal, Binomial, Uniform
    * Function that shows the possible values for a variable and how often they occur (probability)
    * Rolling a die = Discrete uniform Distribution
    * Graph is just a representation, not the distribution itself.
    * Rolling two dices - Normal

## Normal and Student distributions
    * They approximate a wide variety of random Variables
    * Distributions of sample means with large enough sample sizes could be approximated to normal
    * All computable statistics are elegant [?]
    * Decisions based on normal distribution insights have a good track record
    * Normal
        * Gaussian distribution or Bell Curve
        * Mean = Median = Mode
        * No skew
        * N ~ (&mu;, &sigma;)
        * Bigger Mean move graph to the right, lower mean move the graph to the left (keeping the same std).
        * Bigger std, more dispersion (fatter tails), lower std, lower dispersion (more data in the middle, thinner tails)

## Standardization
    * Every distribution can be standardized.
    * Standard normal deviation Z ~ N(0,1)
    * Adding or subtracting values from all data points does not change the std.
    * To standardize a normal:
        * Subtract mean from all data points.
        * Divide all data points by std.
        * Useful to make predictions and inferences easier.

## Central Limit Theorem
    * No matter the underlying distribution, the sampling distribution approximates a Normal.
    * Variance - Population Variance / by the sample size
    * Sample size > 30
    * Allow us to performs tests, solve problems and make inferences using the normal distribution, even when the population is not normally distributed.

## Standard Error
    * The Standard deviation of the distribution formed by the sample means.
    * Used in most statistical tests because it shows how well you approximated the true mean.

## Estimators and Estimates
    * Estimate - Approximation Depending solely on sample information.
    * Point Estimate -> Single values
    * Confidence interval estimates -> Interval
    * Estimator properties
        - Efficiency
            - Least Variability of outcomes
            - The most efficient estimator is the unbiased estimator with smallest variance
        - Bias
            - Unbiased estimator -> Expected Value = Population Parameter
    * Statistics vs Estimators
        * Statistics
            Broader Term
        * Estimators
            A Type of Statistic

## Confidence intervals
    * Much more accurate representation of reality
    * 95% CI means there is only 5% chance that the population parameter is outside the range.
    * Confidence Level -> &alpha;
    * 0 < &alpha; < 1
    * CI 95% -> &alpha; = 5%
    * CI 99% -> &alpha; = 1%
    * Confidence intervals can be calculated when the population is known or unknown
        * The calculation method differs from one another.
    * Confidence intervals for a population mean with a known variance.
    * For confidence levels of 90%, 95% and 99%, the common &alpha; is 10%, 5% and 1% or 0.1, 0.05 and 0.01
    * Using the Z-table for CI = 95%
        - &alpha; is 0.05
        - Z&alpha;/2 = 0.025
        - In the table, the value is 1-0.025 -> 0.975
        - The corresponding Z comes from the sum of the row and column that has this value
        - ![](/udemy_statistics_for_ds/img/z_of_normal.png?raw=true "Table showing how to get Z")
        - In this case -> 1.9 + 0.06 = 1,96
        - When the value of 1 - (&alpha;/2) isn't found in the table, round to neares number.
    * Lower the confidence -> Smaller CI, Higher confidence -> Bigger CI
    * CI for normally distributed data have the need of the population variance.

## Students - t
    * Inferences through small Samples with Unknown population Variance
    * Approximates Normal, but with fatter tails
    * CI based on small samples from normally distributed populations are calculated with t-statistic
    * Using T-Table
        - Find the degrees of freedom (n-1) -> that gives us the row.
        - Find &alpha; (1 - CI) -> 95% CI, &alpha; = 0.05
        - Divide &alpha; by 2 and find the column in the t-table.

## Margin or Error
    * Bigger margin of error => Wider confidence interval
    * Smaller margin or error -> Narrower confidence interval
    * Smaller Statistic (Z or T) and Smaller STD will reduce the margin of error.
    * Higher sample sizes decrease the margin of error

## CI with 2 Populations
    * Samples of 2 populations
        - Dependent
            - Same subject over time (ex Weight loss, blood samples)
            - Another example is when researching families
            - Before and after situation
            - Cause and effect
        - Independent
            - 3 Cases
                - Population variance is known
                - Population variance unknown but assumed to be equal
                - Population variance unknown but assumed to be different

## CI 2 Populations with independent samples - Case 1 Known population variances
    * Population are normally distributed
    * Population variances are Known
    * Samples different sizes
    * Choosing statistic
        - Samples are big
        - Population variances are known
        - Populations are assumed to follow Normal distribution
        - Thus, we use the Z statistic.
    * Variance of the difference
        - ![](/udemy_statistics_for_ds/img/var_diff.png?raw=true "Formula of Variance of the difference")
