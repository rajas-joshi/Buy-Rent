# Buy-Rent

### This model works on data set picked up from kaggle (https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho?select=Car+details+v3.csv). Based on factors such as maitainance cost, fuel charges, one time charges and other miscellaneous costs, I've calculated the effective cost of owning a car. The next step was to determine the expense if the same distance was covered in rented car. This was done by colleting information on cab prices in the particular years. Based on both these values (effective cost of owning a car and cost of renting car), I classified data points. 

### The data generated was used to build different classification models. Based on the accuracies, Decision tree classification algorithm was chosen. In the end, I've built a front end web page that asks for some data from the user regarding the car they wish to buy. Based on the values given, web page displays whether the user should buy a car or consider renting one.
