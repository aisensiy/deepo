# -*- coding: utf-8 -*-

"""Generate dockerfiles & CI configuration."""

import os
import textwrap


def indent(n, s):
    prefix = ' ' * 4 * n
    return ''.join(prefix + l for l in s.splitlines(True))


def get_tags(postfix, py_split='-py', version=""):
    terms = postfix.split('-', 1)
    tags = ":".join(terms)
    if len(version) > 0:
        tags += '.' + version
    return [tags]


def get_job(filename, tags):
    job_name = '_'.join(tags)
    build_scripts = '''
# %s
docker build %s -f openbayes-docker/%s .\n''' % (
                    job_name,
                    ' '.join('-t $DOCKER_REPO/%s' % tag for tag in tags),
                    filename)
    for tag in tags:
        build_scripts += '''docker push $DOCKER_REPO/%s''' % tag
    build_scripts += '\n'
    return job_name, build_scripts


def generate(ci_fname, version=""):
    job_names = []
    results = "docker login -u $DOCKER_USER -p $DOCKER_PASS\n"
    for fn in os.listdir(os.path.join('..', 'openbayes-docker')):
        prefix = 'Dockerfile.'
        postfix = fn[len(prefix):]
        tags = get_tags(postfix, version=version)
        job_name, build_scripts = get_job(fn, tags)
        job_names.append(job_name)
        results += build_scripts

    with open(ci_fname, 'w') as f:
        f.write(results)

if __name__ == '__main__':
    import sys
    generate('../build_and_push.sh', len(sys.argv) >= 2 and sys.argv[1] or "")
