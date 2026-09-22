def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """計算 BMI：BMI = 體重(kg) / 身高(m)^2"""
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_bmi_status(bmi: float) -> str:
    """根據台灣衛福部國民健康署標準判斷 BMI 體位狀態"""
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 24:
        return "正常範圍"
    elif 24 <= bmi < 27:
        return "體重過重"
    elif 27 <= bmi < 30:
        return "輕度肥胖"
    elif 30 <= bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"

def main():
    print("=" * 30)
    print("         BMI 健康計算機")
    print("=" * 30)
    
    try:
        height_input = float(input("請輸入身高 (公分 cm)："))
        weight_input = float(input("請輸入體重 (公斤 kg)："))

        if height_input <= 0 or weight_input <= 0:
            print("【錯誤】身高與體重必須大於 0！")
            return

        bmi = calculate_bmi(height_input, weight_input)
        status = get_bmi_status(bmi)

        # 建議健康體重範圍 (BMI 18.5 ~ 24)
        height_m = height_input / 100
        ideal_weight_min = 18.5 * (height_m ** 2)
        ideal_weight_max = 24.0 * (height_m ** 2)

        print("-" * 30)
        print(f"您的 BMI 數值為：{bmi:.2f}")
        print(f"健康體位判定為：{status}")
        print(f"您的理想體重範圍：{ideal_weight_min:.1f} kg ~ {ideal_weight_max:.1f} kg")
        print("=" * 30)

    except ValueError:
        print("【錯誤】請輸入有效的數字！")

if __name__ == "__main__":
    main()
