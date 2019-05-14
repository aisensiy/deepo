# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .python import Python


@dependency(Python)
@source('pip')
class Pytorch(Module):
    def __init__(self, manager, **args):
        super(self.__class__, self).__init__(manager, **args)
        if self.version not in ('1.0.1', '1.1.0', 'latest'):
            raise NotImplementedError('unsupported pytorch version')

    def build(self):
        if self.version == 'latest':
            return self._nightly_build()
        else:
            return self._build_with_version(self.version)

    def _build_with_version(self, version):
        return r'''
            $PIP_INSTALL \
                future \
                numpy \
                protobuf \
                enum34 \
                pyyaml \
                typing \
            	torchvision \
                && \
            $PIP_INSTALL \
                torch==%s \
                && \
        ''' % version

    def _nightly_build(self):
        cuver = 'cpu' if self.composer.cuda_ver is None else 'cu%d' % (
            float(self.composer.cuda_ver) * 10)
        return r'''
            $PIP_INSTALL \
                future \
                numpy \
                protobuf \
                enum34 \
                pyyaml \
                typing \
            	torchvision_nightly \
                && \
            $PIP_INSTALL \
                torch_nightly -f \
                https://download.pytorch.org/whl/nightly/%s/torch_nightly.html \
                && \
        ''' % cuver
