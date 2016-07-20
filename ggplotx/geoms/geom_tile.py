from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..utils import resolution
from ..utils.doctools import document
from .geom_rect import geom_rect


@document
class geom_tile(geom_rect):
    """
    Rectangles specified using a center points

    {documentation}
    """
    DEFAULT_AES = {'alpha': 1, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 0.1}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    def setup_data(self, data):
        try:
            width = data.pop('width')
        except KeyError:
            width = resolution(data['x'], False)

        try:
            height = data.pop('height')
        except KeyError:
            height = resolution(data['y'], False)

        data['xmin'] = data['x'] - width / 2
        data['xmax'] = data['x'] + width / 2
        data['ymin'] = data['y'] - height / 2
        data['ymax'] = data['y'] + height / 2
        return data