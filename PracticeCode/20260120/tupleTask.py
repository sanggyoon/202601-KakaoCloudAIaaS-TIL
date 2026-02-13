# 주어진 데이터셋에서 튜플을 활용하여 다음 분석을 수행하세요
# 
# 연도별 판매량 계산
# 제품별 평균 가격 계산
# 최대 판매 지역 찾기
# 분기별 매출 분석

# 데이터: (연도, 분기, 제품, 가격, 판매량, 지역)
test_sales_data = [
    (2020, 1, "노트북", 1200, 100, "서울"),
    (2020, 1, "스마트폰", 800, 200, "부산"),
    (2020, 2, "노트북", 1200, 150, "서울"),
    (2020, 2, "스마트폰", 800, 250, "대구"),
    (2020, 3, "노트북", 1300, 120, "인천"),
    (2020, 3, "스마트폰", 850, 300, "서울"),
    (2020, 4, "노트북", 1300, 130, "부산"),
    (2020, 4, "스마트폰", 850, 350, "서울"),
    (2021, 1, "노트북", 1400, 110, "대구"),
    (2021, 1, "스마트폰", 900, 220, "서울"),
    (2021, 2, "노트북", 1400, 160, "인천"),
    (2021, 2, "스마트폰", 900, 270, "부산"),
    (2021, 3, "노트북", 1500, 130, "서울"),
    (2021, 3, "스마트폰", 950, 320, "대구"),
    (2021, 4, "노트북", 1500, 140, "부산"),
    (2021, 4, "스마트폰", 950, 370, "서울")
]

def sales_volume_by_year(sales_data):
  acc_sales = [0, 0]
  for data in sales_data:
    year, quarter, item, price, sales, region = data
    acc_sales[year-2020] += sales

  for i in range(len(acc_sales)):
    print(f"{i+2020}년도 판매량: {acc_sales[i]}")

def avg_price_by_item(sales_data):
  items = []
  for data in sales_data:
    year, quarter, item, price, sales, region = data
    if item not in items:
      items.append(item)

  for it in items:
    avg_price = 0
    count = 0
    for data in sales_data:
      year, quarter, item, price, sales, region = data
      if item == it:
        avg_price += price
        count += 1
    avg_price /= count
    print(f"{it}의 평균 가격: {avg_price}")

def max_sales_region(sales_data):
  regions = []
  for data in sales_data:
    year, quarter, item, price, sales, region = data
    if region not in regions :
      regions.append(region)

  max_acc_sales = 0
  max_region = ""
  for r in regions: 
    acc_sales = 0
    for data in sales_data:
      year, quarter, item, price, sales, region = data
      if region == r:
        acc_sales += sales
    if acc_sales > max_acc_sales:
      max_acc_sales = acc_sales
      max_region = r
  print(f"최대 판매지역은 {max_region}입니다")

def sales_report_by_quarter(sales_data):
  price_by_quarter = [0, 0, 0, 0]
  sales_by_quarter = [0, 0, 0, 0]
  count = [0, 0, 0, 0]
  for data in sales_data:
    year, quarter, item, price, sales, region = data
    price_by_quarter[quarter-1] += price
    sales_by_quarter[quarter-1] += sales
    count[quarter-1] += 1

  for i in range(4):
    print(f"{i+1}분기 누적 가격: {price_by_quarter[i]}" 
          f"누적 판매량: {sales_by_quarter[i]}"
          f"평균 가격: {price_by_quarter[i]/count[i]}"
          f"평균 판매량: {sales_by_quarter[i]/count[i]}")
    
print("=== 연도별 판매량 테스트 ===")
sales_volume_by_year(test_sales_data)
print()
print("=== 제품별 평균 가격 테스트 ===")
avg_price_by_item(test_sales_data)
print()
print("=== 최대 판매 지역 테스트 ===")
max_sales_region(test_sales_data)
print()
print("=== 분기별 매출 분석 테스트 ===")
sales_report_by_quarter(test_sales_data)
print()