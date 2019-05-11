# -*- coding: utf-8 -*-

"""Generate scripts for generating dockerfiles."""

common_modules = [
    'opencv',
    'onnx',
    'jupyterlab',
    'spacy',
    'keras',
    'xgboost'
]

candidate_modules = [
    'tensorflow==1.13.1',
    'tensorflow==2.0.0a0'
]

non_python_modules = [
]

pyvers = [
    '3.6',
]


def get_command(modules, postfix, cuda_ver, cudnn_ver):
    terms = postfix.split("==")
    if len(terms) > 1:
        postfix = '%s-%s' % (terms[0], terms[1])
    cuver = 'cpu' if cuda_ver is None else 'cu%d' % (float(cuda_ver) * 10)
    postfix += '-%s' % cuver
    return 'python ../generator/generate.py ../openbayes-docker/Dockerfile.%s %s%s%s\n' % (
        postfix,
        ' '.join(m for m in modules),
        '' if cuda_ver is None else ' --cuda-ver %s' % cuda_ver,
        '' if cudnn_ver is None else ' --cudnn-ver %s' % cudnn_ver,
    )


def generate(f, candidate_modules, cuda_ver=None, cudnn_ver=None):

        # single module
        for module in candidate_modules:
            if module in non_python_modules:
                modules = [module]
                f.write(get_command(modules, module, cuda_ver, cudnn_ver))
            else:
                for pyver in pyvers:
                    modules = [module, 'python==%s' % pyver, *common_modules]
                    postfix = '%s-py%s' % (
                        module, pyver.replace('.', ''))
                    f.write(get_command(modules, postfix, cuda_ver, cudnn_ver))

if __name__ == '__main__':
    with open('gen-docker-openbayes.sh', 'w') as f:
        generate(f, candidate_modules, '10.0', '7')
        generate(f, candidate_modules)
        # generate(f, ['1.12.0'], '10.0', '7')
