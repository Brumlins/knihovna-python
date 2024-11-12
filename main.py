import csv
import json

SOUBOR = 'knihy.csv'

class KnihovniSystem:
    def __init__(self, soubor, novysoubor):
        self.file = soubor
        self.novysoubor = novysoubor
        self.knihy = self.cteni()

    def cteni(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return f'soubor {self.file} nenalezen'
        except:
            print(f'se souborem {self.file} nastala chyba')

    def ulozit(self):
        try:
            with open(self.novysoubor, 'w', encoding='utf-8') as f:
                json.dump(self.knihy, f, ensure_ascii=False, indent=4)
                print(f"Data byla úspěšně uložena do souboru {self.novysoubor}.")
        except Exception as e:
            print(f"Chyba při ukládání do souboru: {e}")

system = KnihovniSystem(SOUBOR,"vypsani.json")


if __name__ == '__main__':
    print(system.knihy[0]['nazev_knihy'])
    KnihovniSystem(SOUBOR, "vypsani.json").ulozit()