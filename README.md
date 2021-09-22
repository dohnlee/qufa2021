# qufa2021

- 수치형, 범주형 결측값 보간기
- 수치형 변수 기반 이상값 탐지기
- 입력 데이터 형식: csv
- python 3.7.6

## 1. 데이터 품질 검사

각 품질 지표에 대해 `print`

### 수치형 변수 결측률 검사

```
python get_numerical_missing_rate.py --input_fname bank_incomplete_test.csv
```

### 범주형 변수 결측률 검사

```
python get_categorical_missing_rate.py --input_fname bank_incomplete_test.csv
```

### 이상값 비율 검사

```
python get_outlier_rate.py --input_fname bank_test.csv
```

## 2. 데이터 품질 개선

### 결측값 보간

```
python data_imputation.py --input_fname bank_incomplete_test.csv --result_path result_imputation
```

- 보정 데이터 `./result_imputation/result.csv`
- 보정 결과 `./result_imputation/result.json`
```
{"result": {"age": 112, "job": 115, "marital": 112, "education": 109, "default": 95, "balance": 95, "housing": 100, "loan": 111, "contact": 97, "day": 107, "month": 104, "duration": 100, "campaign": 104, "pdays": 86, "previous": 102, "poutcome": 109, "deposit": 110}, "input_fname": "bank_incomplete_test.csv", "result_path": "result_imputation"}
```
  - "변수명": 결측 보간값 갯수(원래 결측값 갯수)

### 이상값 제거

```
python outlier_detection.py --input_fname bank_test.csv --result_path result_outlier
```

- 보정 데이터 `./result_outlier/result.csv`
- 보정 결과 `./result_outlier/result.json`

```
{"result": {"num_outliers": 9, "outlier_indices": [890, 891, 951, 952, 961, 968, 982, 985, 987]}}
```
  - `num_outliers`: 이상값 갯수
  - `outlier_indices`: 이상값 row index
