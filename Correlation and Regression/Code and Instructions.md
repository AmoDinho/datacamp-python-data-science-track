Calculating standard Stats

Anscombe %>%
  group_by(set) %>%
  summarize(N = n(), mean(x), sd(x), mean(y), sd(y), cor(x, y))

Correlation between different variables

# Correlation for all baseball players
mlbBat10 %>%
  summarize(N = n(), r = cor(OBP, SLG))

# Correlation for all players with at least 200 ABs
mlbBat10 %>%
  filter(AB >= 200) %>%
  summarize(N = n(), r = cor(OBP, SLG))

# Correlation of body dimensions
bdims %>%
  group_by(sex) %>%
  summarize(N = n(), r = cor(hgt, wgt))

# Correlation among mammals, with and without log
mammals %>%
  summarize(N = n(), 
            r = cor(BodyWt, BrainWt), 
            r_log = cor(log(BodyWt), log(BrainWt)))

spurious_cor

# Create faceted scatterplot
ggplot(data = noise, aes(x = x, y = y)) +
  geom_point() + 
  facet_wrap(~ z)

# Compute correlations for each dataset
noise_summary <- noise %>%
  group_by(z) %>%
  summarize(N = n(), spurious_cor = cor(x, y))

# Isolate sets with correlations above 0.2 in absolute strength
noise_summary %>%
  filter(abs(spurious_cor) > 0.2)

Visualization of linear models
# Scatterplot with regression line
ggplot(data = bdims, aes(x = hgt, y = wgt)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE)


# Estimate optimal value of my_slope
add_line(my_slope = 1)


# Print bdims_summary
bdims_summary

# Add slope and intercept
bdims_summary %>%
  mutate(slope = r * sd_wgt / sd_hgt, 
         intercept = mean_wgt - slope * mean_hgt)

Fitting a linear model "by hand"

# Print bdims_summary
bdims_summary

# Add slope and intercept
bdims_summary %>%
  mutate(slope = r * sd_wgt / sd_hgt, 
         intercept = mean_wgt - slope * mean_hgt)

Regression to the mean
Create a scatterplot of the height of men as a function of their father's height. Add the simple linear regression line and a diagonal line (with slope equal to 1 and intercept equal to 0) to the plot.
Create a scatterplot of the height of women as a function of their mother's height. Add the simple linear regression line and a diagonal line to the plot.

# Height of children vs. height of father
ggplot(data = Galton_men, aes(x = father, y = height)) +
  geom_point() + 
  geom_abline(slope = 1, intercept = 0) + 
  geom_smooth(method = "lm", se = FALSE)

# Height of children vs. height of mother
ggplot(data = Galton_women, aes(x = mother, y = height)) +
  geom_point() + 
  geom_abline(slope = 1, intercept = 0) + 
  geom_smooth(method = "lm", se = FALSE)


Interpreting regression models
Fitting simple linear models
Using the bdims dataset, create a linear model for the weight of people as a function of their height.
Using the mlbBat10 dataset, create a linear model for SLG as a function of OBP.
Using the mammals dataset, create a linear model for the body weight of mammals as a function of their brain weight, after taking the natural log of both variables.
# Linear model for weight as a function of height
lm(wgt ~ hgt, data = bdims)

# Linear model for SLG as a function of OBP
lm(SLG ~ OBP, data = mlbBat10)

# Log-linear model for body weight as a function of brain weight
lm(log(BodyWt) ~ log(BrainWt), data = mammals)

The lm summary output
We have already created the mod object, a linear model for the weight of individuals as a function of their height, using the bdimsdataset and the code
mod <- lm(wgt ~ hgt, data = bdims)


Now, you will:
Use coef() to display the coefficients of mod.
Use summary() to display the full regression output of mod.

# Show the coefficients
coef(mod)

# Show the full output
summary(mod)

Fitted values and residuals
Once you have fit a regression model, you are often interested in the fitted values (y^iy^i) and the residuals (eiei), where ii indexes the observations. Recall that:
ei=yi−y^iei=yi−y^i
The least squares fitting procedure guarantees that the mean of the residuals is zero (n.b., numerical instability may result in the computed values not being exactly zero). At the same time, the mean of the fitted values must equal the mean of the response variable.
In this exercise, we will confirm these two mathematical facts by accessing the fitted values and residuals with the fitted.values() and residuals() functions, respectively, for the following model:
mod <- lm(wgt ~ hgt, data = bdims)

mod (defined above) is available in your workspace.
Confirm that the mean of the body weights equals the mean of the fitted values of mod.
Compute the mean of the residuals of mod.

# Mean of weights equal to mean of fitted values?
mean(bdims$wgt) == mean(fitted.values(mod))

# Mean of the residuals
mean(residuals(mod))

Tidying your linear model
As you fit a regression model, there are some quantities (e.g. R2R2) that apply to the model as a whole, while others apply to each observation (e.g. y^iy^i). If there are several of these per-observation quantities, it is sometimes convenient to attach them to the original data as new variables.
The augment() function from the broompackage does exactly this. It takes a model object as an argument and returns a data frame that contains the data on which the model was fit, along with several quantities specific to the regression model, including the fitted values, residuals, leverage scores, and standardized residuals.
The same linear model from the last exercise, mod, is available in your workspace.
Load the broom package.
Create a new data frame called bdims_tidy that is the augmentation of the mod linear model.
View the bdims_tidy data frame using glimpse()
# Load broom
library(broom)

# Create bdims_tidy
bdims_tidy <- augment(mod)

# Glimpse the resulting data frame
glimpse(bdims_tidy)

Making predictions
The fitted.values() function or the augment()-ed data frame provides us with the fitted values for the observations that were in the original data. However, once we have fit the model, we may want to compute expected values for observations that were not present in the data on which the model was fit. These types of predictions are called out-of-sample.
The ben data frame contains a height and weight observation for one person. The mod object contains the fitted model for weight as a function of height for the observations in the bdims dataset. We can use the predict() function to generate expected values for the weight of new individuals. We must pass the data frame of new observations through the newdata argument.
The same linear model, mod, is defined in your workspace.
Print ben to the console.
Use predict() with the newdataargument to compute the expected height of the individual in the bendata frame.
# Print ben
ben

# Predict the weight of ben
predict(mod, newdata = ben)

Adding a regression line to a plot manually

The geom_smooth() function makes it easy to add a simple linear regression line to a scatterplot of the corresponding variables. And in fact, there are more complicated regression models that can be visualized in the data space with geom_smooth(). However, there may still be times when we will want to add regression lines to our scatterplot manually. To do this, we will use the geom_abline()function, which takes slope and interceptarguments. Naturally, we have to compute those values ahead of time, but we already saw how to do this (e.g. using coef()).
The coefs data frame contains the model estimates retrieved from coef(). Passing this to geom_abline() as the data argument will enable you to draw a straight line on your 

Use geom_abline() to add a line defined in the coefs data frame to a scatterplot of weight vs. height for individuals in the bdims dataset.

# Add the line to the scatterplot
ggplot(data = bdims, aes(x = hgt, y = wgt)) + 
  geom_point() + 
  geom_abline(data = coefs, 
              aes(intercept = `(Intercept)`, slope = hgt),  
              color = "dodgerblue")

5Model Fit
Standard error of residuals
One way to assess strength of fit is to consider how far off the model is for a typical case. That is, for some observations, the fitted value will be very close to the actual value, while for others it will not. The magnitude of a typical residual can give us a sense of generally how close our estimates are.
However, recall that some of the residuals are positive, while others are negative. In fact, it is guaranteed by the least squares fitting procedure that the mean of the residuals is zero. Thus, it makes more sense to compute the square root of the mean squared residual, or root mean squared error (RMSERMSE). R calls this quantity the residual standard error.
To make this estimate unbiased, you have to divide the sum of the squared residuals by the degrees of freedom in the model. Thus,
RMSE=∑ie2id.f.−−−−−√=SSEd.f.−−−−−√RMSE=∑iei2d.f.=SSEd.f.
You can recover the residuals from mod with residuals(), and the degrees of freedom with df.residual().

View a summary() of mod.
Compute the mean of the residuals() and verify that it is approximately zero.
Use residuals() and df.residual() to compute the root mean squared error (RMSE), a.k.a. residual standard error.

# View summary of model
summary(mod)

# Compute the mean of the residuals
mean(residuals(mod))

# Compute RMSE
sqrt(sum(residuals(mod)^2) / df.residual(mod))

Assessing simple linear model fit
Recall that the coefficient of determination (R2R2), can be computed as
R2=1−SSESST=1−Var(e)Var(y),R2=1−SSESST=1−Var(e)Var(y),
where ee is the vector of residuals and yy is the response variable. This gives us the interpretation of R2R2 as the percentage of the variability in the response that is explained by the model, since the residuals are the part of that variability that remains unexplained by the model.
The bdims_tidy data frame is the result of augment()-ing the bdims data frame with the mod for wgt as a function of hgt.
Use the summary() function to view the full results of mod.
Use the bdims_tidy data frame to compute the R2R2 of mod manually using the formula above, by computing the ratio of the variance of the residuals to the variance of the response variable.
# View model summary
summary(mod)

# Compute R-squared
bdims_tidy %>%
  summarize(var_y = var(wgt), var_e = var(.resid)) %>%
  mutate(R_squared = 1 - var_e / var_y)

Interpretation of R^2
The R2R2 reported for the regression model for poverty rate of U.S. counties in terms of high school graduation rate is 0.464.
lm(formula = poverty ~ hs_grad, data = countyComplete) %>%
  summary()


How should this result be interpreted?
46.4% of the variability in poverty rate among U.S. counties can be explained by high school graduation rate.

Linear vs. average
The R2R2 gives us a numerical measurement of the strength of fit relative to a null model based on the average of the response variable:
y^null=y¯y^null=y¯
This model has an R2R2 of zero because SSE=SSTSSE=SST. That is, since the fitted values (y^nully^null) are all equal to the average (y¯y¯), the residual for each observation is the distance between that observation and the mean of the response. Since we can always fit the null model, it serves as a baseline against which all other models will be compared.
In the graphic, we visualize the residuals for the null model (mod_null at left) vs. the simple linear regression model (mod_hgt at right) with height as a single explanatory variable. Try to convince yourself that, if you squared the lengths of the grey arrows on the left and summed them up, you would get a larger value than if you performed the same operation on the grey arrows on the right.
It may be useful to preview these augment()-ed data frames with glimpse():
glimpse(mod_null)
glimpse(mod_hgt)
Compute the sum of the squared residuals (SSE) for the null model mod_null.
Compute the sum of the squared residuals (SSE) for the regression model mod_hgt.
# Compute SSE for null model
mod_null %>%
  summarize(SSE = var(.resid))

# Compute SSE for regression model
mod_hgt %>%
  summarize(SSE = var(.resid))

Leverage
The leverage of an observation in a regression model is defined entirely in terms of the distance of that observation from the mean of the explanatory variable. That is, observations close to the mean of the explanatory variable have low leverage, while observations far from the mean of the explanatory variable have high leverage. Points of high leverage may or may not be influential.
The augment() function from the broom package will add the leverage scores (.hat) to a model data frame.
 
Use augment() to list the top 6 observations by their leverage scores, in descending order.

# Rank points of high leverage
mod %>%
  augment() %>%
  arrange(desc(.hat)) %>%
  head()

Influence
As noted previously, observations of high leverage may or may not be influential. The influence of an observation depends not only on its leverage, but also on the magnitude of its residual. Recall that while leverage only takes into account the explanatory variable (xx), the residual depends on the response variable (yy) and the fitted value (y^y^).
Influential points are likely to have high leverage and deviate from the general relationship between the two variables. We measure influence using Cook's distance, which incorporates both the leverage and residual of each observation.

Use augment() to list the top 6 observations by their Cook's distance (.cooksd), in descending order.

# Rank influential points
mod %>%
  augment() %>%
  arrange(desc(.cooksd)) %>%
  head()


Removing outliers
Observations can be outliers for a number of different reasons. Statisticians must always be careful—and more importantly, transparent—when dealing with outliers. Sometimes, a better model fit can be achieved by simply removing outliers and re-fitting the model. However, one must have strong justification for doing this. A desire to have a higher R2R2 is not a good enough reason!
In the mlbBat10 data, the outlier with an OBP of 0.550 is Bobby Scales, an infielder who had four hits in 13 at-bats for the Chicago Cubs. Scales also walked seven times, resulting in his unusually high OBP. The justification for removing Scales here is weak. While his performance was unusual, there is nothing to suggest that it is not a valid data point, nor is there a good reason to think that somehow we will learn more about Major League Baseball players by excluding him.
Nevertheless, we can demonstrate how removing him will affect our model.
Instructions
Use filter() to create a subset of mlbBat10 called nontrivial_players consisting of only those players with at least 10 at-bats and OBP of below 0.500.
Fit the linear model for SLG as a function of OBP for the nontrivial_players. Save the result as mod_cleaner.
View the summary() of the new model and compare the slope and R2R2 to those of mod, the original model fit to the data on all players.
Visualize the new model with ggplot() and the appropriate geom_*() functions.
# Create nontrivial_players
nontrivial_players <- mlbBat10 %>%
  filter(AB >= 10, OBP < 0.5)

# Fit model to new data
mod_cleaner <- lm(SLG ~ OBP, data = nontrivial_players)

# View model summary
summary(mod_cleaner)

# Visualize new model
ggplot(data = nontrivial_players, aes(x = OBP, y = SLG)) +
  geom_point() + 
  geom_smooth(method = "lm")

High leverage points
Not all points of high leverage are influential. While the high leverage observation corresponding to Bobby Scales in the previous exercise is influential, the three observations for players with OBP and SLG values of 0 are not influential.
This is because they happen to lie right near the regression anyway. Thus, while their extremely low OBP gives them the power to exert influence over the slope of the regression line, their low SLG prevents them from using it.
Instructions
The linear model, mod, is available in your workspace. Use a combination of augment(), arrange() with two arguments, and head() to find the top 6 observations with the highest leverage but the lowest Cook's distance.
# Rank high leverage points
mod %>%
  augment() %>%
  arrange(desc(.hat), .cooksd) %>%
  head()

