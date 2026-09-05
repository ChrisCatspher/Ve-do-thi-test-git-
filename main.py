#Pandas
import pandas as pd
#Matplotlib
import matplotlib.pyplot as plt
#Seaborn
import seaborn as sns

data = {
    "Thang": ["Jan", "Feb", "Mar", "Apr"],
    "DoanhThu": [100, 150, 200, 180],
    "DonHang": [50, 70, 90, 80],
    "ChiPhiQuangCao" : [20, 30, 50, 15]
}

data2 = [100,150,200,180]
labels = ["Jan", "Feb", "Mar", "Apr"]
data3 = {"Tuoi" : [18,20,21,22,22,23,25,27,30,40,50]}

age = pd.DataFrame(data3)
df = pd.DataFrame(data)

print(plt.get_backend())

while True:
    print("""
    ============= Menu ==============
        1. Show data
        2. Show data that DoanhThu > 150
        3. Show line chart
        4. Show bar chart
        5. Show pie chart
        6. Scatter plot
        7. Du lieu tap trung o dau (tuoi)
        0. Shutdown
        Version 1.0
    """)

    choice = int(input("Input your choice: "))

    if choice == 1:
        print()
        print(df)

    elif choice == 2:
        print()
        print(df[df["DoanhThu"] > 150])

    elif choice == 3:
        plt.plot(df["Thang"], df["DoanhThu"])
        plt.title("Doanh thu theo thang")
        plt.xlabel("Thang")
        plt.ylabel("DoanhThu")
        plt.show()

    elif choice == 4:
        sns.barplot(
            data=df,
            x="Thang",
            y="DoanhThu"
        )
        plt.show()

    elif choice == 5:
        plt.pie(data2, labels = labels)
        plt.title("Ti trong doanh thu")
        plt.show()

    elif choice == 6:
        plt.scatter(
            df["ChiPhiQuangCao"],
            df["DoanhThu"]
        )

        plt.xlabel("Chi phí quảng cáo")
        plt.ylabel("Doanh thu")

        plt.show()

    elif choice == 7:
        sns.histplot(age["Tuoi"])
        plt.show()

    elif choice == 0:
        print()
        print("The proggram was shutdown")
        break

    else:
        print("Error!")
