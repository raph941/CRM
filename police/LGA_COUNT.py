from Criminal.models import Crime

Barkin_Ladi_count = Crime.objects.all().filter(local_gov_area="Barkin Ladi L.G.A").count()
Barkin_Ladi_Town_Area_count = Crime.objects.all().filter(local_gov_area="Barkin Ladi Town Area").count()
Bassa_West_count = Crime.objects.all().filter(local_gov_area="Bassa West LGA").count()
Bokkos_count = Crime.objects.all().filter(local_gov_area="Bokkos L.G.A").count()
Jos_count= Crime.objects.all().filter(local_gov_area="Jos").count()
Jos_East_count= Crime.objects.all().filter(local_gov_area="Jos East L.G.A").count()
Jost_North_count= Crime.objects.all().filter(local_gov_area="Jost North L.G.A").count()
Jos_South_count= Crime.objects.all().filter(local_gov_area="Jos South L.G.A").count()
Kanam_count= Crime.objects.all().filter(local_gov_area="Kanam L.G.A").count()
Kanke_count= Crime.objects.all().filter(local_gov_area="Kanke L.G.A").count()
Langtang_South_count= Crime.objects.all().filter(local_gov_area="Langtang South L.G.A").count()
Mangu_Zip_count= Crime.objects.all().filter(local_gov_area="Mangu Zip L.G.A").count()
Mikang_count= Crime.objects.all().filter(local_gov_area="Mikang L.G.A").count()
Pankshin_count= Crime.objects.all().filter(local_gov_area="Pankshin L.G.A").count()
Qua_count= Crime.objects.all().filter(local_gov_area="Qua").count()
Riyom_count= Crime.objects.all().filter(local_gov_area="Riyom L.G.A").count()
Shendam_count= Crime.objects.all().filter(local_gov_area="Shendam L.G.A").count()
Wase_count= Crime.objects.all().filter(local_gov_area="Wase L.G.A").count()


context2 = {
    'Barkin_Ladi_count': Barkin_Ladi_count,
    "Barkin_Ladi_Town_Area_count": Barkin_Ladi_Town_Area_count,
    'Bassa_West_count': Bassa_West_count,
    'Bokkos_count': Bokkos_count,
    'Jos_count': Jos_count,
    'Jos_East_count': Jos_East_count,
    'Jost_North_count': Jost_North_count,
    'Jos_South_count': Jos_South_count,
    'Kanam_count': Kanam_count,
    'Kanke_count': Kanke_count,
    'Langtang_South_count': Langtang_South_count,
    'Mangu_Zip_count': Mangu_Zip_count,
    'Mikang_count': Mikang_count,
    'Pankshin_count': Pankshin_count,
    'Qua_count': Qua_count,
    'Riyom_count': Riyom_count,
    'Shendam_count': Shendam_count,
    'Wase_count': Wase_count,
}