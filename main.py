import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def parse_time(time_str):
    """Convert time from MM,SS,ss format to total seconds"""
    try:
        parts = str(time_str).replace(',', '.').split('.')
        if len(parts) == 3:
            minutes = int(parts[0])
            seconds = int(parts[1])
            hundredths = int(parts[2])
            return minutes * 60 + seconds + hundredths / 100
        return None
    except:
        return None

def main():
    data_path = Path("data/competition_data.xlsx")
    
    if not data_path.exists():
        print("❌ Файл data/competition_data.xlsx не найден!")
        print("Создай папку data и положи туда Excel-файл с результатами.")
        return

    # Read data
    df = pd.read_excel(data_path, sheet_name="Результаты")
    
    # Convert time to seconds
    df["time_sec"] = df["time_seconds"].apply(parse_time)
    
    # Remove rows with invalid time
    df = df.dropna(subset=["time_sec"])
    
    print("=" * 50)
    print("🏊 SWIMMING RESULTS ANALYZER")
    print("=" * 50)
    
    # General statistics
    print("\n📊 ОБЩАЯ СТАТИСТИКА")
    print(f"Всего результатов: {len(df)}")
    print(f"Среднее время: {df['time_sec'].mean():.2f} сек")
    print(f"Лучшее время:  {df['time_sec'].min():.2f} сек")
    print(f"Худшее время:  {df['time_sec'].max():.2f} сек")
    
    # Statistics by event
    print("\n📋 СТАТИСТИКА ПО ДИСТАНЦИЯМ")
    stats = df.groupby("event_name")["time_sec"].agg(["count", "mean", "min", "max"]).round(2)
    stats.columns = ["Кол-во", "Среднее", "Лучшее", "Худшее"]
    print(stats)
    
    # Statistics by gender
    if "gender" in df.columns:
        print("\n👥 СТАТИСТИКА ПО ПОЛУ")
        gender_stats = df.groupby("gender")["time_sec"].agg(["count", "mean", "min"]).round(2)
        gender_stats.columns = ["Кол-во", "Среднее", "Лучшее"]
        print(gender_stats)
    
    # Create output folder
    output_path = Path("output")
    output_path.mkdir(exist_ok=True)
    
    # Save processed data
    df.to_excel(output_path / "processed_results.xlsx", index=False)
    print(f"\n✅ Обработанные данные сохранены: output/processed_results.xlsx")
    
    # Create visualizations
    try:
        plt.style.use("seaborn-v0_8-whitegrid")
        
        # Chart 1: Average time by event
        plt.figure(figsize=(10, 5))
        avg_by_event = df.groupby("event_name")["time_sec"].mean().sort_values()
        avg_by_event.plot(kind="barh", color="#3b82f6")
        plt.title("Среднее время по дистанциям", fontsize=14, pad=15)
        plt.xlabel("Секунды")
        plt.tight_layout()
        plt.savefig(output_path / "avg_time_by_event.png", dpi=150)
        plt.close()
        
        # Chart 2: Distribution of times
        plt.figure(figsize=(8, 5))
        plt.hist(df["time_sec"], bins=15, color="#60a5fa", edgecolor="white")
        plt.title("Распределение результатов", fontsize=14, pad=15)
        plt.xlabel("Время (секунды)")
        plt.ylabel("Количество")
        plt.tight_layout()
        plt.savefig(output_path / "time_distribution.png", dpi=150)
        plt.close()
        
        print("✅ Графики сохранены в папку output/")
        
    except Exception as e:
        print(f"⚠️ Не удалось создать графики: {e}")
        print("Установи matplotlib: pip install matplotlib")

if __name__ == "__main__":
    main()
