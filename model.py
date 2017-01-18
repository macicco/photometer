from __future__ import print_function, division
import traitlets

class AperturePhotometry(traitlets.HasTraits):

    aperture_radius = traitlets.Integer()
    annulus_inner_radius = traitlets.Integer()
    annulus_outer_radius = traitlets.Integer()
    aperture_net_counts = traitlets.Float()
    reject_outlying_pix = traitlets.Bool()

    '''
    snr = traitlets.Float()
    typical_sky_pix = traitlets.Integer()
    centroid_ra_dec = traitlets.Integer()
    centroid_pix_coords = traitlets.Integer()
    fwhm = ?
    '''

    def __init__(self):
        super(Photometry, self).__init__(description='Photometry model')
        pass

    @traitlets.observe()
    def perform_photometry(self, change):
        pass

    def calc_typical_sky_pix(self):
        pass
