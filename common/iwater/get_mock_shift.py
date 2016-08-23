# -*- coding:utf-8 -*-
from totest.models import mock_shift


def get_mock_shift():
    shift_object = mock_shift.objects.filter(id=1)
    for i in shift_object:
        shift = i.is_open
    return shift
