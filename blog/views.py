from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
blog_post = [
    {
        "title": "বাংলাদেশের পরিস্থিতির ওপর তিন মাস তীক্ষ্ণ নজর থাকবে যুক্তরাষ্ট্রের, বার্তা দিয়ে গেলেন আফরিন",
        "content": "বাংলাদেশ সফরে এসে যুক্তরাষ্ট্রের দক্ষিণ ও মধ্য এশিয়াবিষয়ক উপসহকারী পররাষ্ট্রমন্ত্রী আফরিন আক্তার ওয়াশিংটনের এমন অবস্থানের কথা জানিয়ে গেছেন। দুই দিনের সফর শেষে তিনি গতকাল মঙ্গলবার রাতে ঢাকা ছেড়ে যান। আফরিন আক্তার গত সোমবার সকালে ঢাকায় আসেন। সফরের প্রথম দিন তিনি পররাষ্ট্রসচিব মাসুদ বিন মোমেনের সঙ্গে রাষ্ট্রীয় অতিথি ভবন পদ্মায় দেখা করেন। এর আগে তিনি সেখানে পররাষ্ট্র মন্ত্রণালয়ের দুই মহাপরিচালক ফেরদৌসি শাহরিয়ার ও খন্দকার মাসুদুল আলমের সঙ্গে বৈঠক করেন।",
        "author": "আফরিন",
        "date_posted": " 18 OCT 2023"
    }
]


# def home(request):
#     return HttpResponse("<h1> Welcome to my Blog page</h1>")


def home(request):
    return render(request, template_name="blog/home.html", context={"blog_post": blog_post})

def about(request):
    return render(request, template_name="blog/about.html", context={"title": "About Page"})
