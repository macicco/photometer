from __future__ import print_function, division
import traitlets

class SourceDetection(traitlets.HasTraits):
    """
    Model for (automatic) source detection.
    """
    
    def __init__(self):
        super(SourceDetection, self).__init__(description='Source Detection')
        pass

class AperturePhotometry(traitlets.HasTraits):
    """
    Model that links to the GUI to perform the aperture
    photometry on a given set of sources.
    """

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
        super(AperturePhotometry, self).__init__(description='Photometry model')
        pass

    @traitlets.observe()
    def perform_photometry(self, change):
        pass

    def calc_typical_sky_pix(self):
        pass
