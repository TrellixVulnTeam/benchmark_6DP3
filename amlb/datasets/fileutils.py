import logging
import os
import shutil
import tarfile
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen, urlretrieve
import zipfile

from ..utils import touch

log = logging.getLogger(__name__)

SUPPORTED_SCHEMES = ("http", "https")


def is_valid_url(url):
    return urlparse(url).scheme in SUPPORTED_SCHEMES


def url_exists(url):
    if not is_valid_url(url):
        return False
    head_req = Request(url, method='HEAD')
    try:
        with urlopen(head_req) as test:
            return test.status == 200
    except URLError as e:
        log.error(f"Cannot access url %s: %s", url, e)
        return False


def download_file(url, dest_path):
    touch(dest_path)
    # urlretrieve(url, filename=dest_path)
    with urlopen(url) as resp, open(dest_path, 'wb') as dest:
        shutil.copyfileobj(resp, dest)


def is_archive(path):
    return zipfile.is_zipfile(path) or tarfile.is_tarfile(path)


def unarchive_file(path, dest_folder=None):
    # dest = dest_folder if dest_folder else os.path.dirname(path)
    dest = dest_folder if dest_folder else os.path.splitext(path)
    touch(dest, as_dir=True)
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            zf.extractall(path=dest_folder)
    elif tarfile.is_tarfile(path):
        with tarfile.open(path) as tf:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tf, path=dest_folder)
    return dest

