import logging
from concurrent.futures import as_completed
from craigslist.utils import import_class
from craigslist.io import requests_get
from craigslist._search import get_query_url
from craigslist._search.jsonsearch import parse_cluster_url_output
from craigslist.post import process_post_url_output

logger = logging.getLogger(__name__)

# move processing of posts into another generator that just downloads posts
# this will make the function cleaner
# remove the get_detailed_posts parameter from this function and keep it at the
# top level only
# get detailed posts code is same between regularsearch and jsonsearch

def jsonsearch(
    area,
    category,
    sort,
    get_detailed_posts,
    cache,
    cachedir,
    get=requests_get,
    executor_class='concurrent.futures.ThreadPoolExecutor',
    max_workers=None,
    **kwargs):

    if isinstance(executor_class, str):
        executor_class = import_class(executor_class)
    executor = executor_class(max_workers=max_workers)

    def process_post_url(url):
        logger.debug("downloading %s" % url)
        body = get(url)
        return process_post_url_output(body)

    def process_cluster_url(url):
        logger.debug("downloading %s" % url)
        body = get(url)
        return parse_cluster_url_output(body)

    def process_posts(posts, executor):
        futures = [executor.submit(
            process_post_url, post.url) for post in posts]
        for future in as_completed(futures):
            post = future.result()
            yield post

    def process_clusters(clusters, executor):
        futures = [executor.submit(
            process_cluster_url, cluster.url) for cluster in clusters]
        for future in as_completed(futures):
            posts, clusters = future.result()
            if get_detailed_posts:
                yield from process_posts(posts, executor)
            else:
                yield from posts
            process_clusters(clusters, executor)

    url = get_query_url(area, category, "jsonsearch", sort=sort, **kwargs)
    posts, clusters = process_cluster_url(url)
    if get_detailed_posts:
        yield from process_posts(posts, executor)
    else:
        yield from posts
    yield from process_clusters(clusters, executor)
