from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def make_sorting_list(sort_params):
    sorting_list = []
    for sort in sort_params:
        sorting_list.append(sort)
        sorting_list.append("-" + sort)
    return sorting_list


def get_current_sort(current_query):
    current_sort = []
    if current_query.get('sort_by'):
        current_sort = current_query.get('sort_by').split("___")
    return current_sort


def is_other_sort(current_sort, sort_params):
    return current_sort and any(sort not in sort_params for sort in current_sort)


def filter_sorts(current_sort, sorting_list):
    return [sort for sort in current_sort if sort in sorting_list]


@register.simple_tag()
def build_tag(request, sort_field, tag_text):
    current_query = request.GET.copy()
    sort_params = sort_field.split("___")
    current_sort = get_current_sort(current_query)
    sorting_list = make_sorting_list(sort_params)
    icon = None

    if is_other_sort(current_sort, sort_params):
        current_query.pop('sort_by')

    filtered_sorts = filter_sorts(current_sort, sorting_list)
    if filtered_sorts:
        if all(not sort.startswith("-") for sort in filtered_sorts):
            icon = '&uarr;'
            current_query['sort_by'] = "___".join("-" + sort for sort in filtered_sorts)
        elif all(sort.startswith("-") for sort in filtered_sorts):
            icon = '&darr;'
            current_query['sort_by'] = "___".join(sort[1:] for sort in filtered_sorts)
    if not current_query.get('sort_by'):
        current_query['sort_by'] = "___".join(
            sort for sort in sorting_list if not sort.startswith("-")
        )
    built_query = current_query.urlencode()
    a_tag = f'<a href="?{built_query}">{tag_text} {icon or ""}</a>'
    return mark_safe(a_tag)
