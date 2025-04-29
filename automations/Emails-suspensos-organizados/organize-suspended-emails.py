import xlwings as xw


wb = xw.Book("emails-suspensos.xlsx")

sheet_principal = wb.sheets["pg1"]

dados_pg1 = sheet_principal.used_range.value

sheet_names = ["2022", "2023", "2024", "2025"]

sheets_existentes = [sheet.name for sheet in wb.sheets]

for i in range(len(sheet_names)):
    sheet = wb.sheets[sheet_names[i]]

    if sheet_names[i] not in sheets_existentes:
        wb.sheets.add(name=sheet_names[i], before=None, after=sheet_principal)
    
    sheet_principal.range("A1:F1").api.Copy(sheet.range("A1:F1").api)
    

    



 
# wb.save()