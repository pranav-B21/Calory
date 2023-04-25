from django.shortcuts import render

#Lvah99V8UezSbLy1yB3ILA==DRGdEJzdwP1YBEHI

# Create your views here.

def home(request):
    import json
    import requests

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query, headers = {'X-Api-Key': 'Lvah99V8UezSbLy1yB3ILA==DRGdEJzdwP1YBEHI' })
        try:
            api = json.laods(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
            return render(request, 'home.html', {'api': api})
    else:
        return  render(request, 'home.html', {'query': 'Enter a valid query'})
        

    # query = '1lb brisket and fries'
    # api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    # response = requests.get(api_url, headers={'X-Api-Key': 'Lvah99V8UezSbLy1yB3ILA==DRGdEJzdwP1YBEHI'})
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)

    # return render(request, 'home.html')