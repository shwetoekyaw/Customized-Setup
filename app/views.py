import json
from django.shortcuts import render
# step 1.1 import HttpResponse 
from django.http import HttpResponse, JsonResponse

from app.dijkstra import Dijkstra

from .places import places
from .graph import graph
from .links import links

# step 1.2 create function with request parameter
# Function to find a dictionary by id using list comprehension
def find_dict_by_id(list_of_dicts, id):
    result = [item for item in list_of_dicts if item['id'] == id]
    return result[0] if result else None

# index is function name
def splash(request):
    # step 1.3 return content with HttpResponse
    # return HttpResponse("Hello World")
    return render(request, 'splash.html')
def static_home(request):
    context = {
        'places': places
    }
    return render(request, 'pages/static_ui/home_page.html', context)
def static_about(request):
    return render(request, 'pages/static_ui/about_page.html')
def static_places(request):
    context = {
        'places': places
    }
    return render(request, 'pages/static_ui/places_page.html', context)
def static_result(request):
    # need to find nearest 3 points 
    # pass center node and nearest 3 node
    # Find dictionary with id 2

    source_id = request.GET.get('id', 0)
    center_place = find_dict_by_id(places, source_id)

    dijkstra = Dijkstra(graph)
    nearest_three_points = dijkstra.nearest_three_points(source=source_id)
    nearest_three_places = []

    # translate places
    for id in nearest_three_points:
        place = find_dict_by_id(places, id)
        nearest_three_places.append(place)


    context = {
        'center_place': center_place,
        'nearest_three_places': nearest_three_places
    }

    return render(request, 'pages/static_ui/result_page.html', context)
def static_search(request):
    context = {
        'places': places
    }
    return render(request, 'pages/static_ui/search_page.html', context)

# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    # return HttpResponse("Hello World")
    return render(request, 'index.html')

def start_page(request):
    return render(request, 'pages/start_page.html')

def about_page(request):
    return render(request, 'pages/about_page.html')

def home_page(request):
    return render(request, 'pages/home_page.html')

def places_page(request):
    return render(request, 'pages/places_page.html')

def result_page(request):
    return render(request, 'pages/result_page.html')

def search_page(request):
    return render(request, 'pages/search_page.html')

def listing(request):
    data = {
        "status":"success", 
        "places" : places
    }
    """
        places = [
    {"id": "1", "name": "Governor's House", "cat_id": "1",
        "lat": "22.01872392062109", "long": "96.45711393689749", "image_url" : "test.png"},

    {"id": "2", "name": "Purcell Clock Tower", "cat_id": "8",
        "lat": "22.026959885709", "long": "96.46417970991676"},

    {"id": "3", "name": "Myoma Market", "cat_id": "2",
        "lat": "22.025588687828435", "long": "96.46520300806128"},

    {"id": "4", "name": "Pyin Oo Lwin Night Market", "cat_id": "6",
        "lat": "22.026071741293258", "long": "96.48056965224376"},

    {"id": "5", "name": " Chinese Vegetarian Temple", "cat_id": "7",
        "lat": "22.021865239667722", "long": "96.47863775038817"},

    {"id": "6", "name": "National Kandawgyi Botanical Gardens", "cat_id": "2",
        "lat": "21.994167004139996", "long": "96.46943243689662"},

    {"id": "7", "name": " Bamboo Cafe & Restaurant", "cat_id": "8",
     "lat": "21.994291180231247", "long": "96.46943273689668"},

    {"id": "8", "name": "National Landmarks Garden",
     "cat_id": "3", "lat": "21.996116681244256", "long": "96.47346266573322"},

    {"id": "9", "name": "Royal Rose Farm",
     "cat_id": "4", "lat": "21.98438649401161", "long": "96.5207270755123"},

    {"id": "10", "name": "Shwe Pyin Oo Lwin Grape Fruit Garden", "cat_id": "8",
     "lat": "21.956437245224727", "long": "96.49118050620335"},

    {"id": "11", "name": "Coniferous Forests မြိုရှောင်လမ်းထင်းရှူးတော", "cat_id": "8",
     "lat": "22.005234308287008", "long": "96.48811642155098"},

    {"id": "12", "name": "Ruby Mart", "cat_id": "2",
     "lat": "22.03820131899479", "long": "96.49007583875364"},

    {"id": "13", "name": "Maha EnthtookanTar Pagada & Garden", "cat_id": "5",
     "lat": "22.05961151693717", "long": "96.52665613875438"},

    {"id": "14", "name": "Pwe Kauk Falls (B.E. Falls)", "cat_id": "6",
     "lat": "22.065450526163218", "long": "96.53381486573561"},

    {"id": "15", "name": "Htoo Orange Farm",
     "cat_id": "7", "lat": "22.09367835933169", "long": "96.53365930991907"},

    {"id": "16", "name": "December Garden & Waterfall", "cat_id": "2",
     "lat": "22.0586365802124", "long": "96.55371113504336"},

    {"id": "17", "name": "Maha Nandamu Peik Chin Myaung Cave", "cat_id": "3",
     "lat": "22.096238178463086", "long": "96.62021013690016"},

    {"id": "18", "name": "Nhee Phaya", "cat_id": "4",
     "lat": "21.967755628479928", "long": "96.41749622340525"},

    {"id": "19", "name": "The View Resort & Restaurant",
        "cat_id": "4", "lat": "21.98484602060471", "long": "96.38827953689629"},

    {"id": "20", "name": "Dat Taw Gyaint Waterfall", "cat_id": "3",
     "lat": "21.98493241256396", "long": "96.38827050805986"}    
]}
    """
    return HttpResponse(json.dumps(data))
    # return JsonResponse(data)

def do_graph(request):
    data = {
        "status":"success",
        "misc":"{\"operation\":\"get_graph\"}",
        "places" : places,
        # နေရာတွေကို ဒီမှာ ထည့်ပါ 1
        "places": [
            {"id": "1", "name": "Governor's House", "cat_id": "1",
            "lat": "22.01872392062109", "long": "96.45711393689749", "image_url" : "test.png"},

            {"id": "2", "name": "Purcell Clock Tower", "cat_id": "8",
                "lat": "22.026959885709", "long": "96.46417970991676"},

            {"id": "3", "name": "Myoma Market", "cat_id": "2",
                "lat": "22.025588687828435", "long": "96.46520300806128"},

            {"id": "4", "name": "Pyin Oo Lwin Night Market", "cat_id": "6",
                "lat": "22.026071741293258", "long": "96.48056965224376"},

            {"id": "5", "name": " Chinese Vegetarian Temple", "cat_id": "7",
                "lat": "22.021865239667722", "long": "96.47863775038817"},

            {"id": "6", "name": "National Kandawgyi Botanical Gardens", "cat_id": "2",
                "lat": "21.994167004139996", "long": "96.46943243689662"},

            {"id": "7", "name": " Bamboo Cafe & Restaurant", "cat_id": "8",
            "lat": "21.994291180231247", "long": "96.46943273689668"},

            {"id": "8", "name": "National Landmarks Garden",
            "cat_id": "3", "lat": "21.996116681244256", "long": "96.47346266573322"},

            {"id": "9", "name": "Royal Rose Farm",
            "cat_id": "4", "lat": "21.98438649401161", "long": "96.5207270755123"},

            {"id": "10", "name": "Shwe Pyin Oo Lwin Grape Fruit Garden", "cat_id": "8",
            "lat": "21.956437245224727", "long": "96.49118050620335"},

            {"id": "11", "name": "Coniferous Forests မြိုရှောင်လမ်းထင်းရှူးတော", "cat_id": "8",
            "lat": "22.005234308287008", "long": "96.48811642155098"},

            {"id": "12", "name": "Ruby Mart", "cat_id": "2",
            "lat": "22.03820131899479", "long": "96.49007583875364"},

            {"id": "13", "name": "Maha EnthtookanTar Pagada & Garden", "cat_id": "5",
            "lat": "22.05961151693717", "long": "96.52665613875438"},

            {"id": "14", "name": "Pwe Kauk Falls (B.E. Falls)", "cat_id": "6",
            "lat": "22.065450526163218", "long": "96.53381486573561"},

            {"id": "15", "name": "Htoo Orange Farm",
            "cat_id": "7", "lat": "22.09367835933169", "long": "96.53365930991907"},

            {"id": "16", "name": "December Garden & Waterfall", "cat_id": "2",
            "lat": "22.0586365802124", "long": "96.55371113504336"},

            {"id": "17", "name": "Maha Nandamu Peik Chin Myaung Cave", "cat_id": "3",
            "lat": "22.096238178463086", "long": "96.62021013690016"},

            {"id": "18", "name": "Nhee Phaya", "cat_id": "4",
            "lat": "21.967755628479928", "long": "96.41749622340525"},

            {"id": "19", "name": "The View Resort & Restaurant",
                "cat_id": "4", "lat": "21.98484602060471", "long": "96.38827953689629"},

            {"id": "20", "name": "Dat Taw Gyaint Waterfall", "cat_id": "3",
            "lat": "21.98493241256396", "long": "96.38827050805986"}
            ],
            
        "links" : links,
        # Link တွေကို ဒီမှာ ထည့်ပါ 3 
        "links": [
            {"id": "1", "node1": "1", "node2": "2", "distance": "0.9"},
            {"id": "2", "node1": "1", "node2": "3", "distance": "0.8"},
            {"id": "3", "node1": "1", "node2": "5", "distance": "2.1"},
            {"id": "4", "node1": "1", "node2": "6", "distance": "2.9"},
            {"id": "5", "node1": "1", "node2": "8", "distance": "2.7"},
            {"id": "6", "node1": "1", "node2": "18", "distance": "5.4"},
            {"id": "7", "node1": "1", "node2": "19", "distance": "6.2"},
            {"id": "8", "node1": "2", "node2": "3", "distance": "0.3"},
            {"id": "9", "node1": "2", "node2": "12", "distance": "2"},
            {"id": "10", "node1": "3", "node2": "4", "distance": "1.2"},
            {"id": "11", "node1": "3", "node2": "5", "distance": "1.1"},
            {"id": "12", "node1": "3", "node2": "6", "distance": "2.7"},
            {"id": "13", "node1": "3", "node2": "8", "distance": "2.6"},
            {"id": "14", "node1": "4", "node2": "5", "distance": "0.4"},
            {"id": "15", "node1": "4", "node2": "9", "distance": "5.8"},
            {"id": "16", "node1": "4", "node2": "11", "distance": "4.3"},
            {"id": "17", "node1": "4", "node2": "12", "distance": "1.6"},
            {"id": "18", "node1": "5", "node2": "6", "distance": "2.5"},
            {"id": "19", "node1": "5", "node2": "8", "distance": "2.4"},
            {"id": "20", "node1": "5", "node2": "11", "distance": "3.6"},
            {"id": "21", "node1": "6", "node2": "7", "distance": "0.04"},
            {"id": "22", "node1": "6", "node2": "8", "distance": "0.1"},
            {"id": "23", "node1": "6", "node2": "9", "distance": "5.2"},
            {"id": "24", "node1": "6", "node2": "10", "distance": "3.5"},
            {"id": "25", "node1": "8", "node2": "11", "distance": "1.2"},
            {"id": "26", "node1": "9", "node2": "10", "distance": "4.2"},
            {"id": "27", "node1": "9", "node2": "11", "distance": "5.5"},
            {"id": "28", "node1": "12", "node2": "13", "distance": "3.2"},
            {"id": "29", "node1": "13", "node2": "14", "distance": "0.9"},
            {"id": "30", "node1": "13", "node2": "16", "distance": "2"},
            {"id": "31", "node1": "14", "node2": "15", "distance": "2.9"},
            {"id": "32", "node1": "16", "node2": "17", "distance": "7.8"},
            {"id": "33", "node1": "18", "node2": "19", "distance": "3"},
            {"id": "34", "node1": "18", "node2": "20", "distance": "3"},
            {"id": "35", "node1": "19", "node2": "20", "distance": "1.9"}
        ]    
    }
        
        
    return HttpResponse(json.dumps(data)) 

def calculate(request):
    # get source_id and destination id
    # Retrieve GET parameters with default values
    source_id = request.GET.get('source_id', 0)
    destination_id = request.GET.get('destination_id', 0)
    # return HttpResponse(destination_id)

    # Graph တွေကို ဒီမှာ ထည့်ပါ။
    """
    graph =  {
        "1": {"2": 0.9, "3": 0.8, "5": 2.1, "6": 2.9, "8": 2., "18": 5.4, "19": 6.2},
        "2": {"1": 0.9, "3": 0.3, "12": 2},
        "3": {"1": 0.8, "2": 0.3, "4": 1.2, "5": 1.1, "6": 2.7, "8": 2.6},
        "4": {"3": 1.2, "5": 0.4, "9": 5.8, "11": 4.3, "12": 1.6},
        "5": {"1": 2.1, "3": 1.1, "4": 0.4, "6": 2.5, "8": 2.4, "11": 3.6},
        "6": {"1": 2.9, "3": 2.7, "5": 2.5, "7": 0.04, "8": 0.1, "11": 1.1},
        "7": {"6": 0.04},
        "8": {"1": 2.7, "3": 2.6, "5": 2.4, "6": 0.1, "11": 1.2},
        "9": {"4": 5.8, "6": 5.2, "10": 4.2, "11": 5.5},
        "10": {"6": 3.5, "9": 4.2},
        "11": {"4": 4.3, "5": 3.6, "8": 1.2, "9": 5.5},
        "12": {"2": 2, "4": 1.6, "13": 3.2},
        "13": {"12": 3.2, "14": 0.9, "16": 2},
        "14": {"13": 0.9, "15": 2.9},
        "15": {"14": 2.9},
        "16": {"13": 2, "17": 7.8},
        "17": {"16": 7.8},
        "18": {"1": 5.4, "19": 3, "20": 3},
        "19": {"1": 6.2, "18": 3, "20": 1.9},
        "20": {"18": 3, "19": 1.9}
    }
    """
    dijkstra = Dijkstra(graph)
    result = dijkstra.shortest_path(source_id, destination_id)
    """
    {
        "status": "route",
        "distance": 3351,
        "solution_path": [
            "1",
            "2",
            "3",
            "4",
            "5",
            "10",
            "11",
            "16"
        ]
    }
    """

    # loop through solution_path
    # my_list = result['solution_path']
    # pairs = [(my_list[i], my_list[i + 1]) for i in range(len(my_list) - 1)]
    # return HttpResponse(pairs)


    # Translate result to readable format

    # calculate result

    data = {
        "status":"success",
        "misc":"{\"operation\":\"shortest_path\",\"source_id\":\"1\",\"destination_id\":\"15\"}",
        # link တွေကို ဒီမှာ ထည့်ပါ 2
        "links" : links,
         "links": [
            {"id": "1", "node1": "1", "node2": "2", "distance": "0.9"},
            {"id": "2", "node1": "1", "node2": "3", "distance": "0.8"},
            {"id": "3", "node1": "1", "node2": "5", "distance": "2.1"},
            {"id": "4", "node1": "1", "node2": "6", "distance": "2.9"},
            {"id": "5", "node1": "1", "node2": "8", "distance": "2.7"},
            {"id": "6", "node1": "1", "node2": "18", "distance": "5.4"},
            {"id": "7", "node1": "1", "node2": "19", "distance": "6.2"},
            {"id": "8", "node1": "2", "node2": "3", "distance": "0.3"},
            {"id": "9", "node1": "2", "node2": "12", "distance": "2"},
            {"id": "10", "node1": "3", "node2": "4", "distance": "1.2"},
            {"id": "11", "node1": "3", "node2": "5", "distance": "1.1"},
            {"id": "12", "node1": "3", "node2": "6", "distance": "2.7"},
            {"id": "13", "node1": "3", "node2": "8", "distance": "2.6"},
            {"id": "14", "node1": "4", "node2": "5", "distance": "0.4"},
            {"id": "15", "node1": "4", "node2": "9", "distance": "5.8"},
            {"id": "16", "node1": "4", "node2": "11", "distance": "4.3"},
            {"id": "17", "node1": "4", "node2": "12", "distance": "1.6"},
            {"id": "18", "node1": "5", "node2": "6", "distance": "2.5"},
            {"id": "19", "node1": "5", "node2": "8", "distance": "2.4"},
            {"id": "20", "node1": "5", "node2": "11", "distance": "3.6"},
            {"id": "21", "node1": "6", "node2": "7", "distance": "0.04"},
            {"id": "22", "node1": "6", "node2": "8", "distance": "0.1"},
            {"id": "23", "node1": "6", "node2": "9", "distance": "5.2"},
            {"id": "24", "node1": "6", "node2": "10", "distance": "3.5"},
            {"id": "25", "node1": "8", "node2": "11", "distance": "1.2"},
            {"id": "26", "node1": "9", "node2": "10", "distance": "4.2"},
            {"id": "27", "node1": "9", "node2": "11", "distance": "5.5"},
            {"id": "28", "node1": "12", "node2": "13", "distance": "3.2"},
            {"id": "29", "node1": "13", "node2": "14", "distance": "0.9"},
            {"id": "30", "node1": "13", "node2": "16", "distance": "2"},
            {"id": "31", "node1": "14", "node2": "15", "distance": "2.9"},
            {"id": "32", "node1": "16", "node2": "17", "distance": "7.8"},
            {"id": "33", "node1": "18", "node2": "19", "distance": "3"},
            {"id": "34", "node1": "18", "node2": "20", "distance": "3"},
            {"id": "35", "node1": "19", "node2": "20", "distance": "1.9"}
        ],
        "solution": result, # {"status":"route","distance":3041,"solution_path":["1",8,9,12,"15"]},
        "places" : places,
        # နေရာတွေကို ဒီမှာ ထည့်ပါ 2
        "places": [
            {"id": "1", "name": "Governor's House", "cat_id": "1",
            "lat": "22.01872392062109", "long": "96.45711393689749", "image_url" : "test.png"},

            {"id": "2", "name": "Purcell Clock Tower", "cat_id": "8",
                "lat": "22.026959885709", "long": "96.46417970991676"},

            {"id": "3", "name": "Myoma Market", "cat_id": "2",
                "lat": "22.025588687828435", "long": "96.46520300806128"},

            {"id": "4", "name": "Pyin Oo Lwin Night Market", "cat_id": "6",
                "lat": "22.026071741293258", "long": "96.48056965224376"},

            {"id": "5", "name": " Chinese Vegetarian Temple", "cat_id": "7",
                "lat": "22.021865239667722", "long": "96.47863775038817"},

            {"id": "6", "name": "National Kandawgyi Botanical Gardens", "cat_id": "2",
                "lat": "21.994167004139996", "long": "96.46943243689662"},

            {"id": "7", "name": " Bamboo Cafe & Restaurant", "cat_id": "8",
            "lat": "21.994291180231247", "long": "96.46943273689668"},

            {"id": "8", "name": "National Landmarks Garden",
            "cat_id": "3", "lat": "21.996116681244256", "long": "96.47346266573322"},

            {"id": "9", "name": "Royal Rose Farm",
            "cat_id": "4", "lat": "21.98438649401161", "long": "96.5207270755123"},

            {"id": "10", "name": "Shwe Pyin Oo Lwin Grape Fruit Garden", "cat_id": "8",
            "lat": "21.956437245224727", "long": "96.49118050620335"},

            {"id": "11", "name": "Coniferous Forests မြိုရှောင်လမ်းထင်းရှူးတော", "cat_id": "8",
            "lat": "22.005234308287008", "long": "96.48811642155098"},

            {"id": "12", "name": "Ruby Mart", "cat_id": "2",
            "lat": "22.03820131899479", "long": "96.49007583875364"},

            {"id": "13", "name": "Maha EnthtookanTar Pagada & Garden", "cat_id": "5",
            "lat": "22.05961151693717", "long": "96.52665613875438"},

            {"id": "14", "name": "Pwe Kauk Falls (B.E. Falls)", "cat_id": "6",
            "lat": "22.065450526163218", "long": "96.53381486573561"},

            {"id": "15", "name": "Htoo Orange Farm",
            "cat_id": "7", "lat": "22.09367835933169", "long": "96.53365930991907"},

            {"id": "16", "name": "December Garden & Waterfall", "cat_id": "2",
            "lat": "22.0586365802124", "long": "96.55371113504336"},

            {"id": "17", "name": "Maha Nandamu Peik Chin Myaung Cave", "cat_id": "3",
            "lat": "22.096238178463086", "long": "96.62021013690016"},

            {"id": "18", "name": "Nhee Phaya", "cat_id": "4",
            "lat": "21.967755628479928", "long": "96.41749622340525"},

            {"id": "19", "name": "The View Resort & Restaurant",
                "cat_id": "4", "lat": "21.98484602060471", "long": "96.38827953689629"},

            {"id": "20", "name": "Dat Taw Gyaint Waterfall", "cat_id": "3",
            "lat": "21.98493241256396", "long": "96.38827050805986"}
            ],
    }
        
    return HttpResponse(json.dumps(data)) 