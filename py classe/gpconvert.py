def convert_seconds(seconds):
    minute = 60
    heures= 60 * minute
    jours = 24 * heures
    mois = 30 * jours
    annees = 12 * mois

    years = seconds // annees
    seconds %= annees

    months = seconds // mois
    seconds %= mois

    days = seconds // jours
    seconds %= jours

    hours = seconds // heures
    seconds %= heures

    minutes = seconds // minute
    seconds %= minute

    return years, months, days, hours, minutes, seconds

total_seconds = int(input("saisir le nombre de secondes: "))
years, months, days, hours, minutes, seconds = convert_seconds(total_seconds)
print(f"{total_seconds} secondes correspond a:\n {years} ans\n {months} mois\n {days} jours\n {hours} heures\n {minutes} minutes \n {seconds} secondes.")
