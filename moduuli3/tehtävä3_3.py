sukupuoli = str(input("Sukupuoli: "))
if sukupuoli == "mies":
    hemoglobiini_m = float(input("Hemoglobiini: "))
elif sukupuoli == "nainen":
    hemoglobiini_n = float(input("Hemoglobiini: "))
else:
    print("Syötit sukupuolesi väärin")

if sukupuoli == "mies" and 134 <= hemoglobiini_m <= 195:
    print("Hemoglobiinisi on normaali")
elif sukupuoli == "mies" and hemoglobiini_m < 134:
    print("Hemoglobiinisi on alhainen")
elif sukupuoli == "mies" and hemoglobiini_m > 195:
    print("Hemoglobiinisi on korkea")

if sukupuoli == "nainen" and 117 <= hemoglobiini_n <= 175:
    print("Hemoglobiinisi on normaali")
elif sukupuoli == "nainen" and hemoglobiini_n < 117:
    print("Hemoglobiinisi on alhainen")
elif sukupuoli == "nainen" and hemoglobiini_n > 175:
    print("Hemoglobiinisi on korkea")
