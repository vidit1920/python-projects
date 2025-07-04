import pandas as pd

class Area:
    def __init__(self, name, pincode, population=0):
        self.name = name
        self.pincode = pincode
        self.population = population

    def set_population(self, population):
        self.population = population

    def __repr__(self):
        return f"Area(name='{self.name}', pincode={self.pincode}, population={self.population})"

    def __eq__(self, other):
        return isinstance(other, Area) and self.name == other.name and self.pincode == other.pincode


class City:
    def __init__(self, name): 
        self.name = name
        self.areas = {}

    def _find_area_key(self, name):
        for key in self.areas:
            if key.lower() == name.lower():
                return key
        return None

    def set_area_population(self, area_name, population):
        key = self._find_area_key(area_name)
        if key:
            self.areas[key].set_population(population)
        else:
            raise ValueError(f"Area '{area_name}' not found in city '{self.name}'")

    def update_area_name(self, old_name, new_name):
        key = self._find_area_key(old_name)
        if key:
            area = self.areas.pop(key)
            area.name = new_name
            self.areas[new_name] = area
            self.export_to_csv()
        else:
            raise ValueError(f"Area '{old_name}' not found in city '{self.name}'")
        
    def add_area(self, name, pincode, population):
        if name in self.areas:
            raise ValueError(f"Area '{name}' already exists.")
        self.areas[name] = Area(name=name, pincode=pincode, population=population)
        self.export_to_csv()

    def delete_area(self, name):
        key = self._find_area_key(name)
        if key:
            del self.areas[key]
            self.export_to_csv()
        else:
            raise ValueError(f"Area '{name}' not found in city '{self.name}'")

    def display_areas(self):
        if not self.areas:
            print("No areas available.")
            return
        df = pd.DataFrame([
            {'Name': area.name, 'Pincode': area.pincode, 'Population': area.population}
            for area in self.areas.values()
        ])
        print("\nCurrent Areas in City:")
        print(df.sort_values(by='Population', ascending=False).to_string(index=False))

    def search_area(self, query):
        results = [area for name, area in self.areas.items() if query.lower() in name.lower()]
        if results:
            for a in results:
                print(a)
        else:
            print("No area found with that name.")

    def export_to_csv(self, path="data/areas.csv"):
        df = pd.DataFrame(
            [(area.name, area.pincode, area.population) for area in self.areas.values()],
            columns=["Area Name", "Pincode", "Population"]
        )
        df.to_csv(path, index=False)
        print(f"\nArea data saved to '{path}'")

    def load_from_csv(self, path="data/areas.csv"):
        try:
            df = pd.read_csv(path)
            for _, row in df.iterrows():
                self.areas[row['Area Name']] = Area(row['Area Name'], int(row['Pincode']), int(row['Population']))
            print("Area data loaded from CSV.")
        except FileNotFoundError:
            print("⚠ No saved area data found. Starting fresh.")

    def __repr__(self):
        if not self.areas:
            return f"City: {self.name} (No areas yet)"
        area_strings = [
            f"{i+1}. {area.name} | Pincode: {area.pincode} | Population: {area.population}"
            for i, area in enumerate(self.areas.values())
        ]
        return f"City: {self.name}\n" + "\n".join(area_strings)
