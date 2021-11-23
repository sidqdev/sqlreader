BASE_DIR = ''
CACHED_QUERIES = dict()


def set_base_dir(directory_name: str):
    global BASE_DIR
    if not directory_name.endswith('/'):
        raise Exception('Directory name must end with "/"')
    BASE_DIR = directory_name


def read(query_name: str, file_extension: str = 'sql'):
    file_name = query_name + '.' + file_extension
    if file_name in CACHED_QUERIES:
        return CACHED_QUERIES[file_name]

    file = open(BASE_DIR + file_name, 'r')
    query = file.read()
    file.close()

    CACHED_QUERIES[file_name] = query

    return query


def clear_cache():
    global CACHED_QUERIES
    CACHED_QUERIES = dict()


