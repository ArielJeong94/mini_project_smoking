import pandas as pd
import numpy as np

# 연령대 구분 함수
def age_section(age):
    if age < 30:
        return "30대 미만"
    elif age < 50:
        return "30~50대"
    elif age < 70:
        return "50~70대"
    else:
        return "70대 이상"

# 체중 상태 구분 함수
def bmi_level(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 25:
        return "정상"
    elif bmi < 30:
        return "과체중"
    else:
        return "비만"

# 공복 혈당 범주화 함수
def fbs_level(fasting_blood_sugar):
    if fasting_blood_sugar < 100:
        return "정상"
    elif fasting_blood_sugar < 126:
        return "공복혈당장애"
    else:
        return "당뇨병"

# 중성 지방 범주화 함수
def triglyceride_level(triglyceride):
    if triglyceride < 150:
        return "정상"
    elif triglyceride <= 199:
        return "주의"
    elif triglyceride <= 499:
        return "고중성지방혈증"
    else:
        return "췌장염위험"

# hdl 범주화 함수
def hdl_criteria(hdl):
    if hdl <= 40:
        return "수치 낮음"
    elif hdl < 60:
        return "정상"
    else:
        return "심혈관보호효과"

# ldl 범주화 함수(심혈관 질환자는 55mg/dl 미만이어야 함)
def ldl_criteria(ldl):
    if ldl < 130:
        return "정상"
    elif ldl < 159:
        return "경계"
    else:
        return "높음"

# cholesterol 정상 범위 판단
def cholesterol_check(cholesterol):
    if cholesterol < 200:
        return "정상"
    elif cholesterol < 240:
        return "경계"
    else:
        return "높음"

# creatinine 정상 범위 판단
def creatinine_check(creatinine):
    if 0.50 <= creatinine <= 1.4:
        return "정상"
    else:
        return "의사면담필요"

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    원본 df를 받아 파생변수를 추가한 df를 반환
    - df는 최소한 'age', 'bmi' 컬럼이 있다고 가정 (없으면 해당 부분은 생략/에러)
    """
    out = df.copy()

    # 1) 연령대
    if "age" in out.columns:
        out["age_section"] = out["age"].apply(age_section)

    # 2) BMI 레벨
    if "bmi" in out.columns:
        out["bmi_level"] = out["bmi"].apply(bmi_level)

    # 3) 공복 혈당
    if "fasting_blood_sugar" in out.columns:
        out["fbs_level"] = out["fasting_blood_sugar"].apply(fbs_level)

    # 4) 중성지방
    if "triglyceride" in out.columns:
        out["triglyceride_level"] = out["triglyceride"].apply(triglyceride_level)

    # 5) hdl
    if "hdl" in out.columns:
        out["hdl_criteria"] = out["hdl"].apply(hdl_criteria)

    # 6) ldl
    if "ldl" in out.columns:
        out["ldl_criteria"] = out["ldl"].apply(ldl_criteria)

    # 7) cholesterol
    if "cholesterol" in out.columns:
        out["cholesterol_check"] = out["cholesterol"].apply(cholesterol_check)

    # 8) creatinine
    if "creatinine" in out.columns:
        out["creatinine_check"] = out["creatinine"].apply(creatinine_check)


    return out
