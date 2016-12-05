from __future__ import print_function, division
import traitlets

class AperturePhotometry(traitlets.HasTraits):
    
    aperture_radius = traitlets.Integer()
    annulus_inner_radius = traitlets.Integer()
    annulus_outer_radius = traitlets.Integer()
    aperture_net_counts = traitlets.Float()
    
    def __init__(self):
        super(Photometry, self).__init__(description='Photometry model')
        pass

    @traitlets.observe()
    def perform_photometry(self, change):
        return 0
