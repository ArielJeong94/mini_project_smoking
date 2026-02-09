# 🚬 Smoking Status Analysis Mini Project
> 흡연자 vs 비흡연자 간 건강지표 차이를 EDA + 통계 검정으로 비교 분석한 미니 프로젝트

---

## 1) Project Overview 🔍
- **목표**: 흡연 여부에 따라 건강 지표 분포/평균 차이가 존재하는지 확인
- **접근**: EDA(시각화) → 가설 검정(t-test / Mann–Whitney U) → 효과크기(Cohen’s d) → 시각화 개선(평균/중앙값/유의성 표시)
- **결과 요약**: BMI 그룹별로 여러 지표에서 흡연자/비흡연자 차이가 관찰됨(유의성 + 효과크기 함께 보고)

---

## 2) Key Questions (Hypotheses) 🧐
### Hypothesis 1
- 동일 BMI 그룹에서 흡연 여부에 따른 **(중성지방/HDL 비율)** 차이는 없다.
- 분석: BMI 그룹별 흡연자 vs 비흡연자 비교 (평균/분포 + p-value + Cohen’s d)

### Hypothesis 2
- 동일 BMI 그룹에서 흡연 여부에 따른 **(헤모글로빈/간효소 비율)** 분포 차이는 없다.
- 분석: 로그 변환 후 분포 비교(바이올린) + Mann–Whitney U + Cohen’s d

### Hypothesis 3
- ‘정상 BMI’ 범위(또는 동일 BMI 그룹)에서 흡연 여부에 따른 **크레아티닌** 차이는 없다.
- 분석: log1p 변환 + 그룹 비교 + p-value + Cohen’s d

---

## 3) Dataset 📊
- **형태**: 연습용 건강 데이터(개인정보/민감정보 없음)
- **주요 컬럼 예시**
  - `Smoker` (흡연자/비흡연자)
  - `bmi_level` (저체중/정상/과체중/비만)
  - `tgc_hdl_ratio`, `hemo_lel_ratio`, `creatinine` 등

> (구간 설정 범위 정의)

---

## 4) Methods 🛠️
- **Preprocessing**
  - 결측치 처리
  - 범주형 정렬(`order` 고정)
  - 분포 왜곡 완화: `log1p()` 변환(필요 변수)
- **Statistics**
  - Welch’s t-test (분산이 다를 수 있는 두 집단 평균 비교)
  - Mann–Whitney U test (비정규/분포 차이 중심 비교)
  - Effect size: Cohen’s d
- **Visualization**
  - 그룹별 히스토그램 + KDE + 평균/중앙값 라인
  - barplot(평균) + SD 오차막대(|-| 캡) + 유의성 별표 + 평균값 라벨
  - split violinplot + 중앙값 수치 표시

---

## 5) Results (Highlights) ⭐️

- **BMI별 (중성지방/HDL)**: 흡연자가 전반적으로 더 높은 경향 + 유의성/효과크기 확인
  <img width="989" height="689" alt="동일 BMI 그룹에서 (중성지방:hdl)ratio 흡연자 vs  비흡연자 비교" src="https://github.com/user-attachments/assets/08f539c6-322b-49de-8528-d9721f68aeb1" />
  <img width="1189" height="590" alt="동일 BMI에서 흡연자 vs  비흡연자 중성지방:HDL violinplot" src="https://github.com/user-attachments/assets/58450d1d-9fcc-49cc-aec2-1b8ac905feab" />

- **BMI별 (헤모글로빈/간효소)**: 로그 변환 후에도 흡연자 쪽 분포가 더 높은 경향
  <img width="989" height="689" alt="동일 BMI 그룹에서 (hemo:lel)ratio 흡연자 vs  비흡연자 비교" src="https://github.com/user-attachments/assets/5c673a55-275e-48f7-ada3-0a5a8700e9c5" />
  <img width="1189" height="590" alt="동일 BMI에서 흡연자 vs  비흡연자 헤모글로빈:간 효소율 비율(로그 변환 후)" src="https://github.com/user-attachments/assets/9eb795af-1472-4af4-bae8-39a35fa4db73" />

- **BMI별 크레아티닌(log)**: 흡연자 평균이 더 높은 경향 + 일부 구간에서 효과크기 중간 수준
  <img width="989" height="689" alt="동일 BMI 그룹에서 크레아티닌 흡연자 vs  비흡연자 비교" src="https://github.com/user-attachments/assets/28a25556-f420-444a-bbd0-e4ffbd91a9e1" />
  <img width="1189" height="590" alt="동일 BMI에서 흡연자 vs  비흡연자 크레아티닌 수치 비교(로그 변환 후)" src="https://github.com/user-attachments/assets/33ba4e83-6929-47ec-8c89-c6afbafd1ba2" />

---

## 6) Repo Structure
```txt
mini_project_smoking/
├── data/                 # raw/processed
├── notebooks/            # 분석 노트북
├── src/                  # 함수/모듈(시각화, 파생변수함수)
├── outputs/              # 결과 이미지 저장
├── requirements.txt      # 실행 환경
└── README.md
```

---

## 7) How to Run

### 1) (권장) 가상환경 생성
```
python -m venv .venv
source .venv/bin/activate  # mac/linux
# .venv\Scripts\activate   # windows
```

### 2) 패키지 설치
```
pip install -r requirements.txt
```

### 3) 노트북 실행
jupyter notebook

## 8) Tech Stack
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- SciPy (t-test, Mann–Whitney U)
- Jupyter Notebook

## 9) What I Learned
- “p-value만”이 아니라 **효과크기(Cohen’s d)**까지 함께 보며 해석을 강화
- 시각화에서 범주 순서(order) / hue 정렬 / 주석 매칭이 결과 신뢰도를 크게 좌우
- 데이터 분포에 따라 로그 변환 + 비모수 검정이 더 설득력 있는 선택이 될 수 있음

