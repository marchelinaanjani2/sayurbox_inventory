from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'name': 'Mangga Harum Manis',
        'category': 'Buah-buahan',
        'price': '19.900',
        'amount': '30',
        'description': '''Tersedia dalam pilihan konvensional dan imperfect. Mangga imperfect memiliki bercak pada kulitnya, ukuran yang lebih kecil dan tekstur lembek di beberapa bagian sehingga disarankan agar dapat langsung dikonsumsi. Sementara Mangga konvensional perlu ditunggu 2-3 hari agar matang sempurna.

                            Mangga harum manis memiliki kulit yang mulus, rasanya manis, wanginya khas, dan tekstur juicy. Cocok dibuat jus, dimakan sebagai camilan sehat, dibuat selai, atau kreasi lainnya.

                            Terdapat potensi kelebihan/kekurangan gramasi +-10% per pack.'''
                                }

    return render(request, "main.html", context)
