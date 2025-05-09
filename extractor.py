import re

def extract_fields(text):
    fields = {}
    amount_match = re.search(r"\$\s?([0-9]+(?:\.[0-9]{2})?)", text)
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", text)
    invoice_match = re.search(r"invoice\s+#?(\d+)", text, re.IGNORECASE)

    if amount_match:
        fields['amount'] = amount_match.group(1)
    if date_match:
        fields['date'] = date_match.group(1)
    if invoice_match:
        fields['invoice_number'] = invoice_match.group(1)

    return fields