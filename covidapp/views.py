from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "32c890df81msh53e451d5fcff9e6p195166jsn5cdfa2cde5b5",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# print(response.text)


def main(request):
    n = int(response['results'])
    countryList = []
    for x in response['response']:
        countryList.append(x['country'])
    if request.method == "POST":
        selectedCountry = request.POST['selectedcountry']
        for x in range(0, n):
            if selectedCountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)

        context = {
            'countryList': countryList,
            'selectedCountry': selectedCountry,
            'new': new,
            'active': active,
            'critical': critical,
            'recovered': recovered,
            'total': total,
            'deaths': deaths
        }

        return render(request, 'main.html', context)

    context = {
        'countryList': countryList
    }

    return render(request, 'main.html', context)
