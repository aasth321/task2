import packages-
  pandas - data handling
  seaborn -statistical plotting
  matplotlib - general plotting
  plotly.express - interactive plots
Loads Titanic dataset directly from Seaborn to load dataset
Extracts numeric columns using select_dtypes()
Histograms-
    Creates histograms for all numeric columns in one grid with hist() and tight_layout() respectively
    Saves the figure as histograms.png using savefig()
Correlation-
     Computes correlations between numeric columns.
     Plots a heatmap with values annotated using heatmap()
     Saves as correlation.png
Print 5 rows of dataset
Scatter plot -
    Creates an interactive scatter plot of age vs fare.
    Points are colored by survival status.
    Hover shows extra info
    Saves as an HTML file (interactive.html)
Insights :Average age of passengers,Median fare,Overall survival rate,Survival rates broken down by passenger class and Survival rates broken down by sex
