def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """
    計算 BMI / Calculate BMI:
    BMI = 體重(kg) / 身高(m)^2 | weight(kg) / height(m)^2
    """
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_bmi_status(bmi: float) -> tuple[str, str]:
    """
    根據台灣衛福部與國際標準判斷體位狀態 (回傳 中文, 英文)
    Determine BMI status based on Taiwan MOHW / WHO standards (returns zh-TW, EN)
    """
    if bmi < 18.5:
        return ("體重過輕", "Underweight")
    elif 18.5 <= bmi < 24:
        return ("正常範圍", "Normal weight")
    elif 24 <= bmi < 27:
        return ("體重過重", "Overweight")
    elif 27 <= bmi < 30:
        return ("輕度肥胖", "Mild obesity (Class I)")
    elif 30 <= bmi < 35:
        return ("中度肥胖", "Moderate obesity (Class II)")
    else:
        return ("重度肥胖", "Severe obesity (Class III)")

def run_calculator():
    """執行單次 BMI 計算 (中英雙語) / Run single BMI calculation (Bilingual)"""
    print("=" * 50)
    print("    BMI 健康計算機 / BMI Health Calculator")
    print("=" * 50)
    
    try:
        height_raw = input("請輸入身高 (公分 cm) / Enter height (cm): ").strip()
        weight_raw = input("請輸入體重 (公斤 kg) / Enter weight (kg): ").strip()

        height_input = float(height_raw)
        weight_input = float(weight_raw)

        if height_input <= 0 or weight_input <= 0:
            print("\n【錯誤 / Error】")
            print("身高與體重必須大於 0！")
            print("Height and weight must be greater than 0!")
            return

        bmi = calculate_bmi(height_input, weight_input)
        status_zh, status_en = get_bmi_status(bmi)

        # 建議健康體重範圍 (BMI 18.5 ~ 24) / Ideal weight range
        height_m = height_input / 100
        ideal_weight_min = 18.5 * (height_m ** 2)
        ideal_weight_max = 24.0 * (height_m ** 2)

        print("-" * 50)
        print(f"您的 BMI 數值 / Your BMI:          {bmi:.2f}")
        print(f"體位判定 / Category:               {status_zh} ({status_en})")
        print(f"理想體重範圍 / Ideal Weight Range: {ideal_weight_min:.1f} kg ~ {ideal_weight_max:.1f} kg")
        print("=" * 50)

    except ValueError:
        print("\n【錯誤 / Error】")
        print("請輸入有效的數字！")
        print("Please enter valid numeric values!")

def main():
    while True:
        run_calculator()
        
        # 詢問是否繼續計算 / Ask to calculate again
        choice = input("\n是否繼續計算下一筆？/ Calculate another? (y/n, default y): ").strip().lower()
        if choice == 'n':
            break
        print("\n")

    # 防止視窗在雙擊執行時自動關閉 / Prevent window from closing immediately
    print("\n感謝使用！ / Thank you for using!")
    input("請按 Enter 鍵結束程式... / Press Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程式已中止 / Program terminated.")
