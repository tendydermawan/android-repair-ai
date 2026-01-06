def diagnose(symptom):
    symptom = symptom.lower()

    if "mati total" in symptom:
        return "Kemungkinan IC power / short Vbat / EMMC rusak."
    elif "bootloop" in symptom:
        return "Firmware corrupt atau data rusak."
    elif "tidak ada sinyal" in symptom:
        return "Periksa RF IC & IMEI."
    else:
        return "Gejala belum terdaftar. Tambahkan ke database."
