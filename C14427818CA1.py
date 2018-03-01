import pandas as pd
from pandas import DataFrame, read_csv
import datetime
from pandas_datareader import data as web
import matplotlib
#import matplotlib.pylot as plt
from matplotlib import style

#PRATICE
#get_ipython().magic('matplotlib inline')
#style.use('ggplot')

#start = datetime.datetime(2010, 1, 1)
#end = datetime.datetime(2015, 1, 1)

#df = web.DataReader("XOM", 'yahoo', start, end)

#print(df.head())

#df['Adj Close'].plot()

#plt.show()

#Getting Info
Location = r'/home/corourke/Documents/AI/CA1/DataSet.txt'
df = pd.read_csv(Location)

#Getting Info
Location2 = r'/home/corourke/Documents/AI/CA1/featureNames.txt'
df2 = pd.read_csv(Location2,names=['Names'])

#.iloc[] is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array
#**TOTAL IS 16
sort1 = df2.iloc[0]
sort2 = df2.iloc[1]
sort3 = df2.iloc[2]
sort4 = df2.iloc[3]
sort5 = df2.iloc[4]
sort6 = df2.iloc[5]
sort7 = df2.iloc[6]
sort8 = df2.iloc[7]
sort9 = df2.iloc[8]
sort10 = df2.iloc[9]
sort11 = df2.iloc[10]
sort12 = df2.iloc[11]
sort13 = df2.iloc[12]
sort14 = df2.iloc[13]
sort15 = df2.iloc[14]
sort16 = df2.iloc[15]

#**TOTAL IS 16
p1 = sort1['Names']
p2 = sort2['Names']
p3 = sort3['Names']
p4 = sort4['Names']
p5 = sort5['Names']
p6 = sort6['Names']
p7 = sort7['Names']
p8 = sort8['Names']
p9 = sort9['Names']
p10 = sort10['Names']
p11 = sort11['Names']
p12 = sort12['Names']
p13 = sort13['Names']
p14 = sort14['Names']
p15 = sort15['Names']
p16 = sort16['Names']

Location = r'/home/corourke/Documents/AI/CA1/DataSet.txt'
df = pd.read_csv(Location, names=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16])

#AGE
age1 = df["age"].min()
age2 = df["age"].mean()
age3 = df["age"].median()
age4 = df["age"].max()
age5 = df["age"].std()
age6 = df["age"].quantile(.25)
age7 = df["age"].quantile(.75)
age8 = df["age"].count()
age9 = df["age"].unique()

#SAMPLEWEIGHT
sampleWgt1 = df["fnlwgt"].min()
sampleWgt2 = df["fnlwgt"].mean()
sampleWgt3 = df["fnlwgt"].median()
sampleWgt4 = df["fnlwgt"].max()
sampleWgt5 = df["fnlwgt"].std()
sampleWgt6 = df["fnlwgt"].quantile(.25)
sampleWgt7 = df["fnlwgt"].quantile(.75)
sampleWgt8 = df["fnlwgt"].count()
sampleWgt9 = df["fnlwgt"].unique()

#CAPITAL GAIN
capGain1 = df["capital-gain"].min()
capGain2 = df["capital-gain"].mean()
capGain3 = df["capital-gain"].median()
capGain4 = df["capital-gain"].max()
capGain5 = df["capital-gain"].std()
capGain6 = df["capital-gain"].quantile(.25)
capGain7 = df["capital-gain"].quantile(.75)
capGain8 = df["capital-gain"].count()
capGain9 = df["capital-gain"].unique()

#CAPITAL LOSS
capLoss1 = df["capital-loss"].min()
capLoss2 = df["capital-loss"].mean()
capLoss3 = df["capital-loss"].median()
capLoss4 = df["capital-loss"].max()
capLoss5 = df["capital-loss"].std()
capLoss6 = df["capital-loss"].quantile(.25)
capLoss7 = df["capital-loss"].quantile(.75)
capLoss8 = df["capital-loss"].count()
capLoss9 = df["capital-loss"].unique()

#HOURS PER WEEK
hours1 = df[ "hours-per-week"].min()
hours2 = df[ "hours-per-week"].mean()
hours3 = df[ "hours-per-week"].median()
hours4 = df[ "hours-per-week"].max()
hours5 = df[ "hours-per-week"].std()
hours6 = df["hours-per-week"].quantile(.25)
hours7 = df["hours-per-week"].quantile(.75)
hours8 = df["hours-per-week"].count()
hours9 = df["hours-per-week"].unique()

features = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]
minimum = ['string',age1, 'string', sampleWgt1, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain1, capLoss1, hours1, 'string', 'string']
mean = ['string', age2, 'string', sampleWgt2, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain2, capLoss2, hours2, 'string', 'string']
median = ['string',age3, 'string', sampleWgt3 , 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain3, capLoss3, hours3, 'string', 'string']
Max = ['string',age4, 'string', sampleWgt4, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain4, capLoss4, hours4, 'string', 'string']
std = ['string',age5, 'string', sampleWgt5, 'string', 'string', 'string', 'string', 'string', 'string', 'string',  capGain5, capLoss5, hours5, 'string', 'string']
first_quartile = ['string',age6, 'string', sampleWgt6, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain6, capLoss6, hours6, 'string', 'string']
third_quartile = ['string',age7, 'string', sampleWgt7, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain7, capLoss7, hours7, 'string', 'string']
instances = ['string',age8, 'string', sampleWgt8, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain8, capLoss8, hours8, 'string', 'string' ]
unique = ['string',age9, 'string', sampleWgt9, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain9, capLoss9, hours9, 'string', 'string' ]

ca = list(zip(features,minimum, mean,median, Max, std, first_quartile, third_quartile, instances, unique))

df = pd.DataFrame(data = ca, columns=['features', 'minimum', 'mean','median', 'Max', 'std', 'first_quartile', 'third_quartile', 'instances', 'unique'])

df.to_csv('./data/C14427818CONT.csv')

features = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]
catmin = ['string',age1, 'string', sampleWgt1, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain1, capLoss1, hours1, 'string', 'string']
catmean = ['string', age2, 'string', sampleWgt2, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain2, capLoss2, hours2, 'string', 'string']
catmedian = ['string',age3, 'string', sampleWgt3 , 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain3, capLoss3, hours3, 'string', 'string']
catmax = ['string',age4, 'string', sampleWgt4, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain4, capLoss4, hours4, 'string', 'string']
catstd =['string',age5, 'string', sampleWgt5, 'string', 'string', 'string', 'string', 'string', 'string', 'string',  capGain5, capLoss5, hours5, 'string', 'string']
instances = ['string',age8, 'string', sampleWgt8, 'string', 'string', 'string', 'string', 'string', 'string', 'string', capGain8, capLoss8, hours8, 'string', 'string' ]

ca2 = list(zip(features, catmin, catmean, catmedian, catmax, catstd, instances))

df = pd.DataFrame(data = ca2, columns=['features', 'catmin', 'catmean', 'catmedian', 'catmax', 'catstd', 'instances'])

df.to_csv('./data/C14427818CAT.csv')
