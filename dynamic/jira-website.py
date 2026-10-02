#!/usr/bin/env python3
import argparse
import requests
import json

# TODO: warn on inconsistency between Has Image fields and the repo

AUTHORISED_VALUES = ','.join(['"Yes: SIH and Client approve"',
                              '"Legacy: SIH approves, client may have approved"'])
PENDING_VALUES = ','.join(['EMPTY',
                           '"SIH manager approves, awaiting client approval"',
                           '"Client approves, awaiting SIH approval"'])
ap = argparse.ArgumentParser()
ap.add_argument('-u', '--user', help='Username or email', required=True)
ap.add_argument('-p', '--password', help='Password or API key', required=True)
meg = ap.add_mutually_exclusive_group()
kw = dict(action='store_const', dest='can_be_published_values')
meg.add_argument('--authorised', const=AUTHORISED_VALUES,
                 help='Only get authorised (default)', **kw)
meg.add_argument('--pending', const=PENDING_VALUES,
                 help='Only get pending', **kw)
meg.add_argument('--pending-also', const=AUTHORISED_VALUES + ',' + PENDING_VALUES,
                 help='Get pending and authorised', **kw)
meg.add_argument('--rejected', const='"No"',
                 help='Get disallowed', **kw)
ap.set_defaults(can_be_published_values='"Yes"')


args = ap.parse_args()
auth = (args.user, args.password)
headers = {'Content-Type': 'application/json'}
prefix = 'https://ctdshub.atlassian.net/rest/api/2/'


def get(path, **kwargs):
    return requests.get(prefix + path,
                        headers=headers,
                        auth=auth,
                        **kwargs)


fields = {'11500': 'Title',
          '11005': 'Start date',
          '11007': 'End date',
          '11502': 'Clients',
          '11503': 'SIH Team',
          '11507': 'SIH Staff',
          '10703': 'Contact first name',
          '10705': 'Contact last name',
          '10707': 'Contact role',
          '11100': 'Faculty',
          '11103': 'Centre',
          '11506': 'Cost',
          '11508': 'Techniques and Technologies',
          '11509': 'Has Thumbnail Image',
          '11510': 'Has Large Image',
          '11511': 'Youtube URL',
          '11512': 'Deliverables',
          '11513': 'Body',
          '11514': 'Classification Deliverables',
          '11515': 'Classification Dynamism',
          '11516': 'Classification Methodologies',
          '11517': 'Papers coauthored',
          '11518': 'Papers acknowledging',
          '11523': 'Software published',
          '11523': 'Software published',
          '11532': 'Testimonial',
          '11525': 'Public',  # is this project summary public?
          '11526': 'Reason not public',
          }
fields = {'customfield_' + k: v for k, v in fields.items()}
line_delimited = {'customfield_' + x
                  for x in {'11508', '11512', '11517', '11518', '11507',
                            '11502'}}

# Get PIPEs with a body that are marked as viewable on the web site
query = '''
"Website Body" is not null
AND "cf[11525]" in (%s)
AND project = PIPE
AND statusCategory = Done
ORDER BY resolutiondate DESC
''' % args.can_be_published_values
params = {'jql': query,
          'fields': ','.join(sorted(fields)),
          'maxResults': '50'}


def clean_value(value, line_sep=False):
    if line_sep:
        value = value.split('\n')
        value = [s.strip('\r') for s in value if s.strip()]
    elif isinstance(value, dict) and len(value) == 3 and 'value' in value:
        return value['value']
    elif isinstance(value, list):
        return list(map(clean_value, value))
    return value


def clean_issue(issue):
    issue['fields'] = {fields.get(k, k): clean_value(v, k in line_delimited)
                       for k, v in issue['fields'].items()
                       if v is not None}
    del issue['expand']
    return issue

issues = get('search', params=params).json()['issues']
print(json.dumps([clean_issue(issue)
                  for issue in issues],
                 indent=2, sort_keys=True))
