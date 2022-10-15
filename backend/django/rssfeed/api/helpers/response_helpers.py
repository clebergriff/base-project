def build_bulk_response(response):
    """
    Build a response for a bulk request in the format:
    {
        'created': 1,
        'updated': 2,
        'failed': [
            {
                'url': 'http://example.com',
                'error': 'Article already exists'
            }
        ]
    }
    """
    bulk_response = {
        'created': 0,
        'already_exists': 0,
        'failed': 0
    }
    for r in response:
        if r.status_code == 201:
            bulk_response['created'] += 1
        elif r.status_code == 200:
            bulk_response['already_exists'] += 1
        else:
            bulk_response['failed'] += 1
            # bulk_response['failed'].append({
            #     r.data['info'],
            # })
    return bulk_response
