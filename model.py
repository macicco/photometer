from __future__ import print_function, division
import traitlets

class Photometry(traitlets.HasTraits):
    def __init__(self):
        super(Photometry, self).__init__(description='Photometry model')
        pass

    @traitlets.observe()
    def perform_photometry(self, change):
        return 0
