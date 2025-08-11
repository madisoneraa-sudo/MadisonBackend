from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "This is title",
        "text": "today's a good day!"
    }  # MUST BE A DICT
    return render(request, "home.html", context)

# 1. URL => The user enters the URL to the browser
# 2. URLS => our urls.py recieves and passes it to the func
# 3. VIEWS => The func recieves  the requst & answers back w/ responses(through render()) 
# 4. URLS => urls.py gets the response back & sends it back to the user who requested smth from out project
# =-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# EX: Our site is called https://www.express.com

# 1. User searches for our site & enters it
# 2. So we get the request to show them our first page
# 3. The urls.py gets that request & pases it to the func of views.py 
# 4. That func works  out the logic of what we should show the user & sends to urls.py in response form.
# 5. The urls.py sends that response to the user back as html file