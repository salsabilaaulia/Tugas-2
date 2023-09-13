from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Mascara',
        'amount': 100,
        'description' : 'Mascara is a cosmetic commonly used to enhance the upper and lower eyelashes.',
        'price' : 100000,
        'category' : 'Makeup',
        'nama' : 'Salsabila Aulia',
        'kelas' : 'PBP C',

    }

    return render(request, "main.html", context)