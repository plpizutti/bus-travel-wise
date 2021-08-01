# Bus-Travel-Wise
Bus Tickets Sales Forecast with Machine Learning


## Bus Ticket Problem

I often visit my parents travelling from Porto Alegre to a city called Ijuí, located in the country-side of the state of Rio Grande do Sul, Brazil. 
I'm afraid sometimes I forget to buy bus tickets early and I end up not travelling because the tickets are sold out too fast, specially during holiday.
Or I end up travelling in a not so comfortable seat, because the best ones are already sold by the time I try to buy it.
I need to use Machine Learning algorithms like Time Series to forecast when the tickets are going to be sold out and then I can buy it earlier. 

This solution has 3 main tasks:

- Monitoring the amount of ticket available to buy 1 ticket every hour 30 month before the day to travel
- Building a Time Series algorithm to predict the day and hour that the bus will be packed and no tickets are available to buy
- Send a recommendation message to mobile phone informing the best day to buy the tickets

## Business Question
- What is the best time to buy a bus ticket?
- How close of the the departure time the buses get full with passengenrs?


## Feature engineering

Finding the best representation for a process is a hard task, but it usually comes down to highlighting informative relations and removing noise. Besides, the feature engineering process has a clear target: turning the raw data into a **numeric table without missing values**. That's it! Other concept to keep in mind is that of [end-to-end learning](https://www.youtube.com/watch?v=ImUoubi_t7s). Some deep learning models are able to make good data representations themselves, killing two birds with
one stone: feature engineering and modeling. Now, let's check out some techniques:

### Table

The table is the most common data structure in data science. Even when you are working with the other data type you may have a data table at the end. Your 4 main concerns are:

- **Missing values**: when facing missing values you can either delete them, and lose information, or impute them **carefully**!
    - Deletion:
        - Listwise.
        - Pairwise.
        - Columns.
    - Imputation:
        - Categorical: mode; use NA as a level; logistic or multinomial regression with other variables; multiple imputation.
        - Continuous: mean, median, mode; regression; multiple imputation.
- **Outliers**.
- **Categorical encoding**: depends on the number of categories present in a variable (*cardinality*):
    - Low cardinality: one-hot encoding.
    - High cardinality: hashing; bucketing; embeddings.
    - Ciclic variables: circular encoding.
- **Dimensionality reduction**:
    - Feature selection:
        - Filter.
        - Wrapper.
        - Embedded.
    - Feature extraction:
        - Linear: [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis).
        - Non-linear: [t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding); [UMAP](https://arxiv.org/abs/1802.03426); [autoencoder](https://en.wikipedia.org/wiki/Autoencoder).

### Text

The feature engineering on text is usually done in five steps:

- **Cleaning**: removing unused characters, spaces and punctuation.
- **Tokenization**: separate the text into information units, usually words.
- **Remove stop words**: remove frequent and usuless words.
- **Stemming** or **lemmatization**: both aim to reduce inflexional forms. In other words, they try to reduce words to its morphological root.
- **Encoding**: after the aforementioned steps you have a list of words. The enconding is where you transform it into a data table.
    - [Bag-of-words](https://en.wikipedia.org/wiki/Bag-of-words_model).
    - [Tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).
    - [Word embedding](https://en.wikipedia.org/wiki/Word_embedding).

After this process you will have a data table. Now you can still apply all those techniques used on tables.

### Time series

With time series you have two concerns: missing values and creating features to represent the series as a table:

- **Missing values**: contraty to tables, deletion is not really an option here. Besides, imputation here has some particularities:
    - Last Observation Carried Forward (LOCF).
    - Next Observation Carried Backward (NOCB).
    - Linear interpolation.
    - Seasonal Adjustment + Linear Interpolation.
- **Encoding**:
    - Lag features: all time series models deal with autocorrelation in some way.
    - Date-time features.
    - Window features:
        - Rolling window statistics.
        - Expanding window statistcs.

Again, having a data table at the end, you can still apply all those techniques used on tables.

### Image

*To do*.

## Modeling

> "All model are wrong, but some are useful." - George Box

Before exploring the models, let's define our metric. Almost certainly, the project will fall into one of two categories: classification or regression. There are many
[metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) to choose from, but the usual suspects are:

- **Classification**
    - Binary: [recall](https://en.wikipedia.org/wiki/Precision_and_recall); [precision](https://en.wikipedia.org/wiki/Precision_and_recall); [F1-Score](https://en.wikipedia.org/wiki/F1_score); [AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic).
    - Multilabel: micro and macro averaging of the above-mentioned metrics. Other approach is transforming the multilabel into a binary problem (one-vs-all or one-vs-one).
- **Regression**: some sort of agreggation around the error, like [MAE](https://en.wikipedia.org/wiki/Mean_absolute_error) or [RMSE](https://en.wikipedia.org/wiki/Root-mean-square_deviation).

One last point about it, unless it's strictly necessary, **do not change the evaluation metric during the project**. So far, so good: the data guided the feature engineering process, the problem told me which metric I should use. What about the model? Bad news, there is no right model. The silver lining is that we are not looking for the right model, we are looking for a useful one.

Choosing the model for a phenomenom is like opening a [Pandora's box](https://leandromineti.github.io/ml-knowledge-graph/). The rule of thumb here is: start with the basics and move from there. Linear and logistic regression are two good starting candidates. While assessing many different models, and [combinations of them](https://mlwave.com/kaggle-ensembling-guide/), keep three concepts in mind:

- **Interpretation or acuracy?**: if you need to explain the predictions of your model, you may want to avoid the more complex ones.
- **Computational resources**: the hardware available for development and deployment will set some limits on the models you should try.
- **How much data do you have?**: some models require a fair amount of training data to perform well.

As ~~data~~ scientists, we have an Aristotelian urge to classify things. If
that is your thing, good news! There are a lot of labels you can attach to
modeling techniques: generative, discriminative, parametric, nonparametric,
semiparametric, bayesian *et al*. When choosing your path here, remember Vapnik's advice favoring discriminative models: "*when solving a problem of interest, do not solve a more general problem as an intermediate step.*".


The choice between the parametric and nonparametric will be based on
your need for interpretability and/or prediction power and the available
hardware. Technicalities aside, the golden rule in modeling is: **build a basic model as fast as you can and move from there**. You can only improve what you already have!

Now we are good to go. **Where is the data?**

### References

- Albon, C. (2018). Machine learning with Python cookbook: practical solutions from preprocessing to deep learning (First edition). Sebastopol, CA: O’Reilly Media.
- Kuhn, M., & Johnson, K. (2013). Applied predictive modeling (Vol. 26). New York: Springer.
- Swalin, A. (2018, January 31). How to Handle Missing Data. Retrieved December 15, 2018, from https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4
- Zheng, A., & Casari, A. (2018). Feature engineering for machine learning: principles and techniques for data scientists (First edition). Beijing : Boston: O’Reilly.

- This repo is an adaptation of the repo created by Meigarom, from https://github.com/Meigarom/Bus-Travel-Wise. 
