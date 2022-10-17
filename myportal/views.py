import json

from django.shortcuts import render
from globus_portal_framework.gsearch import post_search, get_search_query, get_search_filters, get_template

def mysearch(request, index):
    print("*****")
    query = get_search_query(request)
    filters = get_search_filters(request)
    context = {'search': post_search(index, query, filters, request.user,
                                     request.GET.get('page', 1))}
    # return render(request, get_template(index, 'search.html'), context)
    print(json.dumps(context, indent=4, sort_keys=True, default=str))
    return render(request, get_template(index, 'schema-org-index/components/search-results.html'), context)
