import argparse
import os
import sys
from rgc.gitlab.clean import GitlabClean

def main():
    parser = argparse.ArgumentParser( description='Cleanup old tags from GitLab Docker Registry' )
    parser.add_argument( '--user',         '-u', metavar='RGC_USER',         default=os.environ.get('RGC_USER', None),         help='Username of the account used to make the request' )
    parser.add_argument( '--token',        '-t', metavar='RGC_TOKEN',        default=os.environ.get('RGC_TOKEN', None),        help='Token of the account used to make the request (requires : \'api\' and \'sudo\' privileges)' )
    parser.add_argument( '--gitlab_url',   '-g', metavar='RGC_GITLAB_URL',   default=os.environ.get('RGC_GITLAB_URL', None),   help='The GitLab URL that you want to access.' )
    parser.add_argument( '--registry_url', '-d', metavar='RGC_REGISTRY_URL', default=os.environ.get('RGC_REGISTRY_URL', None), help='The GitLab Registry URL that you want to access.' )
    parser.add_argument( '--retention',    '-r', metavar='RGC_RETENTION',    default=os.environ.get('RGC_RETENTION', '30'),    help='Remove tags older than this value (days) - defaults to 30' )
    parser.add_argument( '--exclude',      '-e', metavar='RGC_EXCLUDE',      default=os.environ.get('RGC_EXCLUDE', '^latest'), help='Regex to exclude from the cleanup - defaults to \'^latest\'' )
    parser.add_argument( '--minimum_tags', '-m', metavar='RGC_MINIMUM_TAGS', default=os.environ.get('RGC_MINIMUM_TAGS', '0'),  help='Minimum number of tags required before a registry is cleaned - defaults to 0' )
    parser.add_argument( '--check_run',    '-c', metavar='RGC_CHECK_RUN',    default=os.environ.get('RGC_CHECK_RUN', None),    help='If set only report on changes' )
    args = parser.parse_args()

    GitlabClean(
        user         = args.user,
        token        = args.token,
        gitlab_url   = args.gitlab_url,
        registry_url = args.registry_url,
        retention    = args.retention,
        exclude      = args.exclude,
        minimum_tags = args.minimum_tags,
        check_run    = args.check_run
    ).clean_projects()

    sys.exit(0)
