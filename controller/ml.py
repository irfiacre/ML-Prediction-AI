import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split


DATA_FRAME=pd.read_csv("data/yield_df.csv")
DATA_FRAME.drop("Unnamed: 0", axis=1,inplace=True)
DATA_FRAME

country_counts =DATA_FRAME['Area'].value_counts()
countries_to_drop = country_counts[country_counts < 100].index.tolist()
df_filtered = DATA_FRAME[~DATA_FRAME['Area'].isin(countries_to_drop)]
DATA_FRAME = df_filtered.reset_index(drop=True)

COPY_DF=DATA_FRAME.copy()


categorical_columns = COPY_DF.select_dtypes(include=['object']).columns.tolist()
label_encoder = LabelEncoder()
for column in categorical_columns:
    COPY_DF[column] = label_encoder.fit_transform(COPY_DF[column])

COPY_DF


# Learning with the Model
X, y = COPY_DF.drop(labels='hg/ha_yield', axis=1), COPY_DF['hg/ha_yield']

X, y = COPY_DF.drop(labels='hg/ha_yield', axis=1), COPY_DF['hg/ha_yield']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(scaler, 'controller/model/standard-scaler.joblib')


model= BaggingRegressor(n_estimators=150, random_state=42)
model.fit(X.values, y)

#Create a Persisting Model
joblib.dump(model, 'controller/model/crop-predictor.joblib')

scaler = joblib.load('controller/model/standard-scaler.joblib')

scaled_inputs = [[100,5,2013,657.0,2550.07,19.76]]

model=joblib.load('controller/model/crop-predictor.joblib')
predictions = model.predict(scaled_inputs)

print("Prediction:",predictions)
