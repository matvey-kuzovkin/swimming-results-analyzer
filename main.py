```python
import pandas as pd
from pathlib import Path

def parse_time(time_str):
    """Convert time from MM,SS,ss format to seconds"""
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
        print("Файл data/competition_data.xlsx не найден!")
        print("Создай папку data и положи туда Excel-файл.")
        return

    df = pd.read_excel(data_path, sheet_name="Результаты")
    
    # Convert time
    df["time_sec"] = df["time_seconds"].apply(parse_time)
    
    # Basic statistics
    print("=== Общая статистика ===")
    print(f"Всего результатов: {len(df)}")
    print(f"Среднее время: {df['time_sec'].mean():.2f} сек")
    print(f"Лучшее время: {df['time_sec'].min():.2f} сек")
    print(f"Худшее время: {df['time_sec'].max():.2f} сек")
    
    print("\n=== По дистанциям ===")
    print(df.groupby("event_name")["time_sec"].agg(["count", "mean", "min", "max"]).round(2))
    
    # Save results
    output_path = Path("output/processed_results.xlsx")
    output_path.parent.mkdir(exist_ok=True)
    df.to_excel(output_path, index=False)
    print(f"\nРезультаты сохранены в {output_path}")

if __name__ == "__main__":
    main()
