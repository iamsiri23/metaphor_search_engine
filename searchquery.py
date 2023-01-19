from elasticsearch import Elasticsearch

from query import basic_search, standard_analyzer
# from rules import process

INDEX = 'songs'
# client = Elasticsearch(HOST="https://localhost", PORT=9200,http_auth=('elastic', 'N*rb-0Pfb33UC_YbHqYt'))
# client = Elasticsearch("https://elastic:N*rb-0Pfb33UC_YbHqYt@localhost:9200",verify_certs=False)
client = Elasticsearch("http://localhost:9200", verify_certs=False,
                   http_auth=['elastic', 'DwIbcCE_g==ZZt939WlG'],)

def search(query):
    # result = client. (index=INDEX,body=standard_analyzer(query))
    # keywords = result ['tokens']['token']
    # print(keywords)

    # query_body= process(query)
    query_body = basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    print(res)
    return res

def basic_search_with_fields(fields):
    """
    example of query
    {
        "query": {
            "bool" : {
            "must" : [
                {"term" : { "Composer" : "அனிருத் ரவிச்சந்திரன்" }},
                {"term" : { "Lyricist" : "நா. முத்துக்குமார்" }},
                {"range" : {"Year" : { "gte" : 2000, "lte" : 2005 }}}
            ]
            }
        }
        }
    """
  
    q = {}
    q["query"] = {}
    q["query"]["bool"] = {}
    q["query"]["bool"]["must"] = []
    
    for field in fields:
        print(field)
        if field == 'Year':
            q["query"]["bool"]["must"].append({"range":{field:fields[field]}})
        else:
            q["query"]["bool"]["must"].append({"term":{field:fields[field]}})


    res = client.search(index=INDEX, body=q)
    return res


def search_advanced_query(query):
    q = {
       "query": {
            "wildcard": {
            "Metaphor": {
                "value": "*"+query+"*"
            }
            }
        }
    }
    res = client.search(index=INDEX, body=q)

    return res