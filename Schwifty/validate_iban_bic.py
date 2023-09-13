import schwifty

# Install module: pip install schwifty

ibans = [
    "FI5524759913532177",
    "FI9433136049675542",
    "FI6552813300354900",
    "FI6260517550827737",
    "FI6436518025915307",
]

# all_ibans = [schwifty.IBAN(iban) for iban in ibans]
# print(all_ibans)
# all_bics = [iban.bic for iban in all_ibans]
# print(all_bics)

with open("IBAN_checks.txt", "w", encoding="UTF-8") as iban_file:
    for iban in ibans:
        try:
            schwifty_iban = schwifty.IBAN(iban)
            iban_file.write(f"IBAN: {schwifty_iban} BIC: {schwifty_iban.bic}\n")
        except schwifty.exceptions.SchwiftyException:
            iban_file.write(f"Faulty IBAN: {schwifty_iban}\n")
