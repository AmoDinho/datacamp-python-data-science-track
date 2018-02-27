#--------------------------------------------------------------------------------------------#

#Cahpter 3 - Merging data


#--------------------------------------------------------------------------------------------#
#Merging on a specific column
# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue,managers, on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue,managers, on='branch_id')

# Print merge_by_id
print(merge_by_id)

#--------------------------------------------------------------------------------------------#
#Merging on columns with non-matching labels
# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue,managers,left_on ='city',right_on='branch')

# Print combined
print(combined)


#--------------------------------------------------------------------------------------------#
#Merging on multiple columns
# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue,managers,on=['branch_id','city','state'])

# Print combined
print(combined)

#--------------------------------------------------------------------------------------------#
#Left & right merging on multiple columns


# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales, on=['city','state'], how='right')

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales, managers, left_on=['city','state'], right_on=['branch','state'], how='left')

# Print sales_and_managers
print(sales_and_managers)

#--------------------------------------------------------------------------------------------#
#Merging DataFrames with outer join
# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers,revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers,revenue_and_sales,how='outer')

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers,revenue_and_sales,on=['city','state'],how='outer')

# Print merge_outer_on
print(merge_outer_on)

#--------------------------------------------------------------------------------------------#
#Using merge_ordered()

# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin,houston)

# Print tx_weather
print(tx_weather)

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'])

# Print tx_weather_suff
print(tx_weather_suff)

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'],fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)

#--------------------------------------------------------------------------------------------#
#Using merge_asof()
# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

# Print yearly.corr()
print(yearly.corr())

#--------------------------------------------------------------------------------------------#

