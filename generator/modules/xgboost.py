# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source, version
from .python import Python


@dependency(Python)
@version('latest')
@source('pip')
class Xgboost(Module):

    def build(self):
        return r'''
            $PIP_INSTALL \
                xgboost \
                && \
        '''
