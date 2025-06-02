# Webová aplikace pro správu softwaru
### Instalace
1. Naklonujte si repozitář s projektem na svůj disk
- `git clone https://github.com/PanVat/softwareova-webova-aplikace.git`
2. Přesun do adresáře webu
- `python -m venv .venv`
3. Vytvořte virtuálního prostředí do složky .venv
- `python -m venv .venv`
4. Aktivujte virtuální prostředí 
- `.venv\Scripts\activate` (ve Windows)
- `.venv/bin/activate` (v Linuxu)
5. Nainstalujte balíčky a závislosti
- `pip install -r requirements.txt`
6. Spusťte aplikaci
- `python manage.py runserver`

### Přístupové údaje do administrace
- superuživatel: `admin`
- heslo: `admin`