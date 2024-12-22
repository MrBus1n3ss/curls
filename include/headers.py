def content_type(header_content_type, request):
    if header_content_type == 'application/json':
        return request.json()
    elif header_content_type == 'application/xml':
        pass
    elif header_content_type == 'application/x-www-form-urlencoded':
        pass
    elif header_content_type == 'application/pdf':
        pass
    elif header_content_type == 'text/html':
        pass
    elif header_content_type == 'text/css':
        pass
    else:
        return 'unknown'
# TODO: work on the headers, will move this to another file


