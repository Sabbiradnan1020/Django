from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={'name' :'autor','age' :29,'lst' : ['kicui','valo','lage na'],'value' :' ','birthday' : datetime.datetime.now(),'courses':[


        {
            'id':1,
            'course':'python',
            'fee':7000
        },

        {
            'id':2,
            'course':'django',
            'fee':5790
        },
        {
            'id':3,
            'course':'React',
            'fee':5000
        },

        # for loop


     
    ]}
    return render(request,'home.html',d)
