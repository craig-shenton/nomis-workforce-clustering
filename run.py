import pandas as pd
import numpy as np

# County / Unitary Authorities Apr-2021

# NOMIS API - Population estimates - local authority based by five year age band
url = "https://www.nomisweb.co.uk/api/v01/dataset/NM_31_1.data.csv?geography=1807745025...1807745028,1807745030...1807745032,1807745034...1807745083,1807745085,1807745282,1807745283,1807745086...1807745155,1807745157...1807745164,1807745166...1807745170,1807745172...1807745177,1807745179...1807745194,1807745196,1807745197,1807745199,1807745201...1807745218,1807745221,1807745222,1807745224,1807745226...1807745231,1807745233,1807745234,1807745236...1807745244,1807745271...1807745281&date=latest&sex=7&age=0,24,22,25&measures=20100,20301&signature=NPK-be81606366125733ff591b:0x55c28d4f3b15b3d94ea6f86d2ba90f4e761c43c3"

df_population = pd.read_csv(url)
df_population = df_population[
    [
        "DATE",
        "GEOGRAPHY_NAME",
        "GEOGRAPHY_CODE",
        "GEOGRAPHY_TYPE",
        "AGE_NAME",
        "MEASURES_NAME",
        "OBS_VALUE",
    ]
]
df_population = df_population[df_population["GEOGRAPHY_CODE"].str.contains("E")]
df_population_pivot = df_population.pivot_table(
    index=["GEOGRAPHY_CODE"], columns=["AGE_NAME", "MEASURES_NAME"], values="OBS_VALUE"
).reset_index()
df_population_pivot.columns = df_population_pivot.columns.map("|".join).str.strip("|")

# NOMIS - annual population survey
url = "https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5.data.csv?geography=1807745025...1807745028,1807745030...1807745032,1807745034...1807745083,1807745085,1807745282,1807745283,1807745086...1807745155,1807745157...1807745164,1807745166...1807745170,1807745172...1807745177,1807745179...1807745194,1807745196,1807745197,1807745199,1807745201...1807745218,1807745221,1807745222,1807745224,1807745226...1807745231,1807745233,1807745234,1807745236...1807745244&date=latestMINUS4&variable=18,45,248,249,111,1487,1488,1537,290,720...722,344,84,72,74,1463,1464,1558,885...888,416,418,1349,602...605,434...437,197,202&measures=20599,21001,21002,21003&signature=NPK-be81606366125733ff591b:0xf38669505a2fa883628ec2471d9566bbd3dd3563"

df_survey = pd.read_csv(url)
df_survey = df_survey[
    [
        "DATE",
        "GEOGRAPHY_NAME",
        "GEOGRAPHY_CODE",
        "GEOGRAPHY_TYPE",
        "MEASURES_NAME",
        "VARIABLE_NAME",
        "OBS_VALUE",
    ]
]
df_survey = df_survey[df_survey["GEOGRAPHY_CODE"].str.contains("E")]
df_survey_pivot = df_survey.pivot_table(
    index=["GEOGRAPHY_CODE"],
    columns=["VARIABLE_NAME", "MEASURES_NAME"],
    values="OBS_VALUE",
).reset_index()
df_survey_pivot.columns = df_survey_pivot.columns.map("|".join).str.strip("|")

# NOMIS - annual survey of hours and earnings - workplace analysis
url = "/api/v01/dataset/NM_99_1.data.csv?geography=1807745025...1807745028,1807745030...1807745032,1807745034...1807745083,1807745085,1807745282,1807745283,1807745086...1807745155,1807745157...1807745164,1807745166...1807745170,1807745172...1807745177,1807745179...1807745194,1807745196,1807745197,1807745199,1807745201...1807745218,1807745221,1807745222,1807745224,1807745226...1807745231,1807745233,1807745234,1807745236...1807745244&date=latestMINUS1&sex=8,9&item=2&pay=1,7&measures=20100,20701&signature=NPK-be81606366125733ff591b:0xf6642f02ae17b8d9fb60ef7229a0b28010dbfb3b"

df_workplace = pd.read_csv(url)
df_workplace = df_workplace[
    [
        "DATE",
        "GEOGRAPHY_NAME",
        "GEOGRAPHY_CODE",
        "GEOGRAPHY_TYPE",
        "SEX_NAME",
        "PAY_NAME",
        "MEASURES_NAME",
        "OBS_VALUE",
    ]
]
df_workplace = df_workplace[df_workplace["GEOGRAPHY_CODE"].str.contains("E")]
df_workplace_pivot = df_workplace.pivot_table(
    index=["GEOGRAPHY_CODE"],
    columns=["SEX_NAME", "PAY_NAME", "MEASURES_NAME"],
    values="OBS_VALUE",
).reset_index()
df_workplace_pivot.columns = df_workplace_pivot.columns.map("|".join).str.strip("|")

# NOMIS - jobs density
url = "https://www.nomisweb.co.uk/api/v01/dataset/NM_57_1.data.csv?geography=1807745025...1807745028,1807745030...1807745032,1807745034...1807745083,1807745085,1807745282,1807745283,1807745086...1807745155,1807745157...1807745164,1807745166...1807745170,1807745172...1807745177,1807745179...1807745194,1807745196,1807745197,1807745199,1807745201...1807745218,1807745221,1807745222,1807745224,1807745226...1807745231,1807745233,1807745234,1807745236...1807745244,1807745271...1807745281&date=latest&item=1,3&measures=20100&signature=NPK-be81606366125733ff591b:0xc789ee7ace7b897a1eed8f6e2ca5e3ad42ac8540"

df_density = pd.read_csv(url)
df_density = df_density[
    [
        "DATE",
        "GEOGRAPHY_NAME",
        "GEOGRAPHY_CODE",
        "GEOGRAPHY_TYPE",
        "ITEM_NAME",
        "MEASURES_NAME",
        "OBS_VALUE",
    ]
]
df_density = df_density[df_density["GEOGRAPHY_CODE"].str.contains("E")]
df_density_pivot = df_density.pivot_table(
    index=["GEOGRAPHY_CODE"], columns=["ITEM_NAME", "MEASURES_NAME"], values="OBS_VALUE"
).reset_index()
df_density_pivot.columns = df_density_pivot.columns.map("|".join).str.strip("|")

# NOMIS - Claimant count
url = "https://www.nomisweb.co.uk/api/v01/dataset/NM_162_1.data.csv?geography=1807745025...1807745028,1807745030...1807745032,1807745034...1807745083,1807745085,1807745282,1807745283,1807745086...1807745155,1807745157...1807745164,1807745166...1807745170,1807745172...1807745177,1807745179...1807745194,1807745196,1807745197,1807745199,1807745201...1807745218,1807745221,1807745222,1807745224,1807745226...1807745231,1807745233,1807745234,1807745236...1807745244,1807745271...1807745281&date=latestMINUS24&gender=0&age=0&measure=1...4&measures=20100&signature=NPK-be81606366125733ff591b:0xb2f5e7659af9ab5b972c8eacf5e12aa1c7aef5bf"

df_claim = pd.read_csv(url)
df_claim = df_claim[
    [
        "DATE",
        "GEOGRAPHY_NAME",
        "GEOGRAPHY_CODE",
        "GEOGRAPHY_TYPE",
        "MEASURE_NAME",
        "OBS_VALUE",
    ]
]
df_claim = df_claim[df_claim["GEOGRAPHY_CODE"].str.contains("E")]
df_claim_pivot = df_claim.pivot_table(
    index=["GEOGRAPHY_CODE"], columns=["MEASURE_NAME"], values="OBS_VALUE"
).reset_index()

# London Min Wage
url = "https://opendata.arcgis.com/datasets/3ba3daf9278f47daba0f561889c3521a_0.csv"

df_london = pd.read_csv(url)
df_london["london_min_wage"] = np.where(df_london["RGN19NM"] == "London", True, False)
df_london.drop(list(df_london.filter(["FID", "LAD19NM"])), axis=1, inplace=True)
df_london.rename(columns={"LAD19CD": "GEOGRAPHY_CODE"}, inplace=True)

# Merge to master file
merged_master = pd.merge(
    df_population_pivot, df_survey_pivot, on=["GEOGRAPHY_CODE"], how="left"
)
merged_master = pd.merge(
    merged_master, df_density_pivot, on=["GEOGRAPHY_CODE"], how="left"
)
merged_master = pd.merge(
    merged_master, df_workplace_pivot, on=["GEOGRAPHY_CODE"], how="left"
)
merged_master = pd.merge(
    merged_master, df_claim_pivot, on=["GEOGRAPHY_CODE"], how="left"
)
merged_master = pd.merge(merged_master, df_london, on=["GEOGRAPHY_CODE"], how="left")
merged_master.reset_index().to_csv("data/master_file.csv", index=False)

col_list = list(merged_master.columns)
df = pd.DataFrame(col_list)

# saving the dataframe
df.to_csv("data/metrics.csv")
