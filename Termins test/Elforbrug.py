import pandas as pd
import matplotlib.pyplot as plt


class ElforbrugAnalyzer:
    def __init__(self, filename) -> None:
        try:
            self.df = pd.read_csv(filename, delimiter=';', decimal=',')  # Indlæs filen
            self.df['Fra_dato'] = pd.to_datetime(self.df['Fra_dato'], format='%d-%m-%Y %H:%M:%S')  # Konvertér dato
            self.df['date'] = self.df['Fra_dato'].dt.date  # Tilføj dato-kolonne
            self.df['month'] = self.df['Fra_dato'].dt.month  # Tilføj måned-kolonne
        except FileNotFoundError:
            print(f"Fejl: Kunne ikke finde filen '{filename}'. Tjek filnavn og sti!")
            raise
        except Exception as e:
            print(f"Fejl ved indlæsning af filen: {e}")
            raise

    def get_basic_dataset(self) -> pd.DataFrame:
        """Funktion til Opgave A: Returnerer dato/tid og forbrug."""

        # Tag kun kolonnerne 'Fra_dato' og 'Mængde' fra vores data
        return self.df[['Fra_dato', 'Mængde']]

    def calculate_daily_consumption(self, output_file='daily_consumption.csv') -> pd.DataFrame:
        """Funktion til Opgave B: Beregner dagligt forbrug og gemmer som CSV."""

        # Grupper data efter dato og sum forbrug
        # reset_index() bruges til at fjerne hierarkisk index
        daily_data = self.df.groupby('date')['Mængde'].sum().reset_index()

        # Gem data som CSV-fil og returnér
        daily_data.to_csv(output_file, index=False)
        return daily_data

    def plot_histogram(self, bins=10) -> None:
        """Funktion til Opgave C: Laver et histogram over forbruget."""
        plt.hist(self.df['Mængde'], 
                 bins=bins, color='blue', 
                 edgecolor='black')
        
        plt.title('Histogram over Elforbrug pr. Time')
        plt.xlabel('Elforbrug (kWh)')
        plt.ylabel('Antal Timer')
        plt.show()

    def calculate_monthly_consumption(self) -> pd.Series:
        """Funktion til Opgave D: Beregner månedligt forbrug."""
        return self.df.groupby('month')['Mængde'].sum()

    def plot_monthly_consumption(self) -> pd.Series:
        """Funktion til Opgave D: Laver et søjlediagram over månedligt forbrug."""
        monthly_data = self.calculate_monthly_consumption()

        monthly_data.plot(
            kind='bar', 
            color='green', 
            edgecolor='black'
            )
        plt.title('Elforbrug pr. Måned')
        plt.xlabel('Måned')
        plt.ylabel('Elforbrug (kWh)')
        plt.show()
        return monthly_data

# Hovedprogrammet
def main():
    # Opret en instans af klassen med filnavnet
    analyzer = ElforbrugAnalyzer('c:/Users/Shado/Downloads/MeterData.csv')

    """
    -   head() -> viser de første 5 rækker af datasættet
    -   bins = 10 -> betyder at der er 10 søjler i histogrammet
    -   float64 -> er en datatype, som er en 64-bit floating point
    """

    # Opgave A: Vis det basale datasæt
    print("Opgave A - Første 5 rækker af datasættet:")
    dataset_A = analyzer.get_basic_dataset()
    print(dataset_A.head())

    # Opgave B: Beregn og gem dagligt forbrug
    print("\nOpgave B - Dagligt forbrug gemt i 'daily_consumption.csv'")
    daily_data = analyzer.calculate_daily_consumption()
    print(daily_data.head())

    # Opgave C: Lav og vis histogram
    print("\nOpgave C - Histogram vist på skærmen")
    analyzer.plot_histogram(bins=10)

    # Opgave D (Bonus): Beregn og vis månedligt forbrug
    print("\nOpgave D - Elforbrug pr. måned (kWh):")
    monthly_data = analyzer.plot_monthly_consumption()
    print(monthly_data)


if __name__ == "__main__":
    main()